import pandas as pd

df = pd.DataFrame({'key':['a','b','c'],'data1':[1,2,3],'data2':[4,5,6]})  
print(df)
for idx,item in df.iterrows():
    print(idx)
    print(item)
