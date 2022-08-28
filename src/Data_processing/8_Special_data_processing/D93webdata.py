# %%
import requests
import pandas as pd
import json
import time


response = requests.get('https://worldtimeapi.org/api/timezone/Asia/Tokyo')

response.content
'''
b'{"abbreviation":"JST","client_ip":"2001:268:c1c5:6117:74c7:d0c2:9531:cc6f","datetime":"2022-08-28T13:26:38.998230+09:00","day_of_week":0,"day_of_year":240,"dst":false,"dst_from":null,"dst_offset":0,"dst_until":null,"raw_offset":32400,"timezone":"Asia/Tokyo","unixtime":1661660798,"utc_datetime":"2022-08-28T04:26:38.998230+00:00","utc_offset":"+09:00","week_number":34}'
'''

# 辞書に変換
result = response.json()
result

# pandas.Series型へ変換
pd.Series(result)

# 保存する
if __name__ == '__main__':
    with open('./data/response.json', mode='w') as f:
        json.dump(result, f)

for _ in range(4):
    response = requests.get('https://worldtimeapi.org/api/timezone/Asia/Tokyo')
    with open('./data/response.txt', mode='a') as f:
        res = response.json()
        f.write(f'{json.dumps(res)}\n')
    time.sleep(1)

'''
cat ./data/response.txt
{"abbreviation": "JST", "client_ip": "2001:268:c1c5:6117:74c7:d0c2:9531:cc6f", "datetime": "2022-08-28T14:04:19.679100+09:00", "day_of_week": 0, "day_of_year": 240, "dst": false, "dst_from": null, "dst_offset": 0, "dst_until": null, "raw_offset": 32400, "timezone": "Asia/Tokyo", "unixtime": 1661663059, "utc_datetime": "2022-08-28T05:04:19.679100+00:00", "utc_offset": "+09:00", "week_number": 34}
{"abbreviation": "JST", "client_ip": "2001:268:c1c5:6117:74c7:d0c2:9531:cc6f", "datetime": "2022-08-28T14:04:44.139145+09:00", "day_of_week": 0, "day_of_year": 240, "dst": false, "dst_from": null, "dst_offset": 0, "dst_until": null, "raw_offset": 32400, "timezone": "Asia/Tokyo", "unixtime": 1661663084, "utc_datetime": "2022-08-28T05:04:44.139145+00:00", "utc_offset": "+09:00", "week_number": 34}
{"abbreviation": "JST", "client_ip": "2001:268:c1c5:6117:74c7:d0c2:9531:cc6f", "datetime": "2022-08-28T14:04:45.763691+09:00", "day_of_week": 0, "day_of_year": 240, "dst": false, "dst_from": null, "dst_offset": 0, "dst_until": null, "raw_offset": 32400, "timezone": "Asia/Tokyo", "unixtime": 1661663085, "utc_datetime": "2022-08-28T05:04:45.763691+00:00", "utc_offset": "+09:00", "week_number": 34}
{"abbreviation": "JST", "client_ip": "2001:268:c1c5:6117:74c7:d0c2:9531:cc6f", "datetime": "2022-08-28T14:04:47.429565+09:00", "day_of_week": 0, "day_of_year": 240, "dst": false, "dst_from": null, "dst_offset": 0, "dst_until": null, "raw_offset": 32400, "timezone": "Asia/Tokyo", "unixtime": 1661663087, "utc_datetime": "2022-08-28T05:04:47.429565+00:00", "utc_offset": "+09:00", "week_number": 34}
{"abbreviation": "JST", "client_ip": "2001:268:c1c5:6117:74c7:d0c2:9531:cc6f", "datetime": "2022-08-28T14:04:49.488865+09:00", "day_of_week": 0, "day_of_year": 240, "dst": false, "dst_from": null, "dst_offset": 0, "dst_until": null, "raw_offset": 32400, "timezone": "Asia/Tokyo", "unixtime": 1661663089, "utc_datetime": "2022-08-28T05:04:49.488865+00:00", "utc_offset": "+09:00", "week_number": 34}
'''

# %%
