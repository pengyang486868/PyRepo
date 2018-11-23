import pandas as pd

ar=[4,5,6]
df = pd.DataFrame({'key':['a','b','c'],'data1':[1,2,3],'data2':[9,12,ar]})  
print(df)
for idx,item in df.iterrows():
    print(idx)
    print(item)
