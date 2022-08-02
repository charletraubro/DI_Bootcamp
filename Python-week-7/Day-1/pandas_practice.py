# import numpy as np
# import pandas as pd

# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

# df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# print(df.iloc[50:60])
# print(df.shape)
# print(df.info())
# print(df.species.unique())
# print(df.sort_values('sepal_length', ascending=False)
# )

# print(df[['species','sepal_length']].groupby('species').agg([np.mean, np.median, np.sum]))

##CHIPOTLE##


# chipotable = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv')
# type(chipotable)






# chipotable.describe()
# chipotable.index.values.tolist()
# chipotable.columns.values.tolist()
# print(chipotable.head(10))

#STEP 9:

# items = chipotable[['item_name', 'quantity']].groupby('item_name').sum()
# items.head()
# print(items.sort_values(['quantity'], ascending = False))

#STEP 10 and 12

# order = chipotable['quantity'].agg(np.sum)
# print(order)

#STEP 11
# print(chipotable['choice_description'].mode())

#STEP 13
# print(chipotable['item_price'])
# def dollar_strip(s):
#     return s.strip('$')
# dollar_strip = lambda s: s.strip('$')
# print(chipotable['item_price'].apply(dollar_strip).apply(np.float64))

#STEP 14

# chipotable['item_price'] = chipotable['item_price'].apply(lambda x: float(x[1:-1]))
# revenue = chipotable['quantity'].dot(chipotable['item_price'])
# print(revenue)

#STEP 15
# print(chipotable['order_id'].count())




# #STEP 16
# print(np.mean(chipotable['quantity']) * np.mean(chipotable['item_price']))


#Filtering and Sorting

import numpy as np
import pandas as pd

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

df = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv')

#STEP 4

# df['item_price'] = df['item_price'].apply(lambda x: float(x[1:-1]))
# print(df['item_price']>10)

#STEP 5
# print(df[['item_name','item_price']])

#STEP 6

# print(df.sort_values(by=['item_name']))

#STEP 7

# print(df['quantity'].max())

#STEP 8

a= df[df['choice_description']=='Diet Coke'].value_counts()
print(a)







