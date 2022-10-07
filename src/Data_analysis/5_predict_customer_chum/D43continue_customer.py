# %%
import D41read_formatting as D41
import D42before_month_withdrawal as D42

import pandas as pd

conti_customer = D41.customer.loc[D41.customer["is_deleted"] == 0]

conti_uselog = pd.merge(D41.uselog, conti_customer,
                        on=["customer_id"], how="left")

if __name__ == '__main__':
    print(len(conti_uselog))

conti_uselog = conti_uselog.dropna(subset=["name"])

if __name__ == '__main__':
    print(len(conti_uselog))

# シャッフル
conti_uselog = conti_uselog.sample(frac=1).reset_index(drop=True)
# 重複削除
conti_uselog = conti_uselog.drop_duplicates(subset="customer_id")

if __name__ == '__main__':
    print(len(conti_uselog))
conti_uselog.head()

# 継続顧客と退会顧客を縦に結合
predict_data = pd.concat([conti_uselog, D42.exit_uselog], ignore_index=True)

if __name__ == '__main__':
    print(len(predict_data))
predict_data.head()

# %%
