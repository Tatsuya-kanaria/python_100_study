# %%
import japanize_matplotlib
import matplotlib.pyplot as plt
from glob import glob
import pandas as pd
import os
import re


# データ読み込み
data = pd.read_csv('./data/22_shizuoka_all_20210331.csv',
                   encoding='shift-jis', header=None, dtype=object)

# 差分データ読み込み
diff_files = glob('data/diff*.csv')
diff_files
# ソート
diff_files.sort()
diff = pd.read_csv(
    diff_files[0], encoding='shift-jis', header=None, dtype=object)

# ヘッドテキストの読み込み
mst = pd.read_csv('./data/mst_column_name.txt', encoding='shift-jis', sep='\t')
columns = mst.column_name_en.values

# ヘッダ行を設定
data.columns = columns
diff.columns = columns
# 絞り込み
diff = diff.loc[diff['prefectureName'] == '静岡県']

# データ追加
for f in diff_files:
    diff = pd.read_csv(f, encoding='shift-jis', header=None, dtype=object)
    diff.columns = columns
    diff = diff.loc[diff['prefectureName'] == '静岡県']
    data = pd.concat([data, diff])

# 重複データの削除
data.drop_duplicates(subset='corporateNumber', keep='last', inplace=True)

# 列の追加
'''法人種別, 検索対象区分, 処理区分, 最新履歴区分, 閉鎖事由区分, 訂正区分'''
mst_list = glob('data/mst*.csv')
pattern = '(data/mst)|(corp)|(kbn)|(_+)|(\.+\w*)'

for mst in mst_list:
    on_mst = re.sub(pattern, '', mst)
    if on_mst == 'correct':
        mst = pd.read_csv(mst, encoding='shift-jis', dtype=object)
    else:
        mst = pd.read_csv(mst, dtype=object)

    data = data.merge(mst, on=on_mst, how='left')

# アドレスに連結した住所追加
data['address'] = data['prefectureName'] + \
    data['cityName'] + data['streetNumber']

# 番地が欠損している場合の処理
data['address'].loc[data['streetNumber'].isna()] = data['prefectureName'] + \
    data['cityName']

# 郵便番号を分割して追加
data['postCode_head'] = data['postCode'].str[:3]
data['postCode_tail'] = data['postCode'].str[-4:]

# object → datetime
dt_columns = ['updateDate', 'changeDate', 'closeDate', 'assignmentDate']
for col in dt_columns:
    data[col] = pd.to_datetime(data[col])

# 会社存続年数を追加
data['corporate_life'] = data['closeDate'] - data['assignmentDate']

# 閉鎖日の件数が一致しているか確認
len(data.loc[data['closeCause'].notna()]) == len(
    data.loc[data['closeDate'].notna()])

data['update_YM'] = data['updateDate'].dt.to_period('M')
# print(len(data.columns))

#
dt_prefixes = ['assignment', 'change', 'update', 'close']
for pre in dt_prefixes:
    data[f'{pre}_Ym'] = data[f'{pre}Date'].dt.to_period('M')

data['update_year'] = pd.DatetimeIndex(data['updateDate']).year
data['update_month'] = pd.DatetimeIndex(data['updateDate']).month
data['update_fiscal_year'] = pd.DatetimeIndex(data['updateDate']).year

# update_monthが1〜3月なら西暦から1引いて年度にする
# data.loc[data['update_month'] < 4, 'update_fiscal_year'] -= 1
# # display: 処理の途中で画面出力する
# for i in range(12):
#     display(data[['update_YM', 'update_fiscal_year']
#                  ].loc[data['update_month'] == i + 1][:1])

# # バックアップを出力
# output_dir = './data/output'
# os.makedirs(output_dir, exist_ok=True)
# output_file = 'processed_shizuoka.csv'
# data.to_csv(os.path.join(output_dir, output_file), index=False)

# # データ行の確認
# print(data.columns)

# 項目削除と並べ替え
data = data[['cityName', 'corporateNumber', 'name', 'corp_kind_name', 'process',
             'process_kbn_name', 'assignmentDate', 'updateDate', 'update_fiscal_year', 'update_YM']]

# 項目の削除
data = data.drop(columns='process')

# 項目別でグループ化
# tmp = data.groupby(['update_fiscal_year', 'corp_kind_name']).size()
# 並べ替え
# tmp.sort_values(inplace=True, ascending=False)

# print(tmp)

# ピボットテーブル
# pt_data = pd.pivot_table(data, index='corp_kind_name',
#                          columns='update_fiscal_year', aggfunc='size')
# pt_data

# .now(tz=) 現在時刻
base_time = pd.Timestamp('2020-04-16', tz='Asia/Tokyo')
base_time

print(len(data))

data["assignmentDate"] = data["assignmentDate"].dt.tz_localize("Asia/Tokyo")
data.head()

delta = pd.Timedelta(90, "days")
tmp = data.loc[(data["process_kbn_name"] == "新規") & (
    base_time - data["assignmentDate"] <= delta)]
print(len(tmp))
tmp.head()

# グループ化
tmp = data.groupby('cityName').size()
# ascending:昇順
tmp.sort_values(inplace=True, ascending=False)
# 上位10位に絞り込み
tmp = tmp[:10]
x = tmp.index
y = tmp.values

plt.figure(figsize=(20, 10))
plt.bar(x, y)
# %%
