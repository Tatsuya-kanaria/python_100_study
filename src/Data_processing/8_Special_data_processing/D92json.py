# %%
import pandas as pd


pd.read_json('./data/column_oriented.json')

'''
cat ./data/column_oriented.json
{"id": {"0": 1, "1": 2, "2": 3}, "value": {"0": 1, "1": 10, "2": 100}}%
'''

'''
cat ./data/index_oriented.json
{"0":{"id":1,"value":1},"1":{"id":2,"value":10},"2":{"id":3,"value":100}}%
'''

# そのまま読み込むと縦横が逆になる
pd.read_json('./data/index_oriented.json', orient='index')

'''
cat ./data/table_oriented.json
{"schema": {"fields": [{"name": "index", "type": "integer"}, {"name": "id", "type": "integer"}, {"name": "value", "type": "integer"}], "primaryKey": [
    "index"], "pandas_version": "0.20.0"}, "data": [{"index": 0, "id": 1, "value": 1}, {"index": 1, "id": 2, "value": 10}, {"index": 2, "id": 3, "value": 100}]}
'''
# そのまま読み込むと ValueError になる
pd.read_json('./data/table_oriented.json', orient='table')

# %%
