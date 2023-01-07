# %%
from ortoolpy import logistics_network
import numpy as np
import pandas as pd


製品 = list('AB')
需要地 = list('PQ')
工場 = list('XY')
レーン = (2, 2)

# 輸送費表
tbdi = pd.DataFrame(((j, k) for j in 需要地 for k in 工場), columns=['需要地', '工場'])
tbdi["輸送費"] = [1, 2, 3, 1]

# 需要地
tbde = pd.DataFrame(((j, i) for j in 需要地 for i in 製品), columns=['需要地', '製品'])
tbde["需要"] = [10, 10, 20, 20]

# 生産表
tbfa = pd.DataFrame(((k, l, i, 0, np.inf) for k, nl in zip(工場, レーン)
                    for l in range(nl) for i in 製品), columns=['工場', 'レーン', '製品', '下限', '上限'])

if __name__ == '__main__':
    print(tbdi)
    print(tbde)
    print(tbfa)

tbfa['生産費'] = [1, np.nan, np.nan, 1, 3, np.nan, 5, 3]
tbfa.dropna(inplace=True)
tbfa.loc[4, '上限'] = 10

if __name__ == '__main__':
    print(tbfa)

_, tbdi2, _ = logistics_network(tbde, tbdi, tbfa)

if __name__ == '__main__':
    print(tbfa)
    print(tbdi2)


# %%
