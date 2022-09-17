# %%
import D11read_csv as D11
import D14shake_correction as D14

D11.kokyaku_data["顧客名"].head
D11.uriage_data["customer_name"].head

# スペース削除
D11.kokyaku_data["顧客名"] = D11.kokyaku_data["顧客名"].str.replace("　", "")
D11.kokyaku_data["顧客名"] = D11.kokyaku_data["顧客名"].str.replace(" ", "")
D11.kokyaku_data["顧客名"].head


# %%
