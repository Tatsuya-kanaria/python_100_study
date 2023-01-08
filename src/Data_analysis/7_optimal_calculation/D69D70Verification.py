# %%
import D68optimal_design_logistics_network as D68


# D69 ------------------------
if __name__ == '__main__':
    print("D69\n", D68.tbdi2)
trans_cost = 0
for i in range(len(D68.tbdi2.index)):
    trans_cost += D68.tbdi2["輸送費"].iloc[i] * D68.tbdi2["ValX"].iloc[i]
if __name__ == "__main__":
    print("総輸送コスト:" + str(trans_cost))

# D70 ------------------------
if __name__ == '__main__':
    print("D70\n", D68.tbfa)
product_cost = 0
for i in range(len(D68.tbfa.index)):
    product_cost += D68.tbfa["生産費"].iloc[i] * D68.tbfa["ValY"].iloc[i]
if __name__ == "__main__":
    print("総生産コスト:" + str(product_cost))

# %%
