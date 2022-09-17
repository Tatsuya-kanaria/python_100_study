# %%
import pandas as pd

import D11read_csv as D11
import D14shake_correction as D14
import D16kokyaku_shake as D16


flg_is_serial = D11.kokyaku_data["登録日"].astype("str").str.isdigit()
flg_is_serial.sum()

fromSerial = pd.to_timedelta(D11.kokyaku_data.loc[flg_is_serial, "登録日"].astype(
    "float"), unit="D") + pd.to_datetime("1900/01/01")
fromSerial

# 区切りを統一するため
fromString = pd.to_datetime(D11.kokyaku_data.loc[~flg_is_serial, "登録日"])
fromString

D11.kokyaku_data["登録日"] = pd.concat([fromSerial, fromString])
D11.kokyaku_data

D11.kokyaku_data["登録年月"] = D11.kokyaku_data["登録日"].dt.strftime("%Y%m")

if __name__ == '__main__':
    rslt = D11.kokyaku_data.groupby("登録年月").count()["顧客名"]
    print(rslt)
    print(len(D11.kokyaku_data))

    flg_is_serial = D11.kokyaku_data["登録日"].astype("str").str.isdigit()
    print(flg_is_serial.sum())

# %%
