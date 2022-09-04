# %%
import D4merge2 as D4


D4.join_data['price'] = D4.join_data['quantity'] * D4.join_data['item_price']
D4.join_data[['quantity', 'item_price', 'price']].head()

# %%
