# %%
import pandas as pd
import D1read_csv as D1


transaction_2 = pd.read_csv('./data/transaction_2.csv')
transaction = pd.concat([D1.transaction_1, transaction_2], ignore_index=True)
# transaction.head()

transaction_detail_2 = pd.read_csv('./data/transaction_detail_2.csv')
transaction_detail = pd.concat(
    [D1.transaction_detail_1, transaction_detail_2], ignore_index=True)


if __name__ == '__main__':
    print(len(D1.transaction_1))
    print(len(transaction_2))
    print(len(transaction))

    print(f'detail_1: {len(D1.transaction_detail_1)}',
          f'detail_2: {len(transaction_detail_2)}',
          f'detail: {len(transaction_detail)}',
          sep='\n')

# %%
