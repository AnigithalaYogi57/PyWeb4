import pandas as pd

names = ['Bob',"Jessica", "mary",'john','yogi']
births = [968,155,77,578,973]

dataset = list(zip(names,births))

print(dataset)

df=pd.DataFrame(data=dataset, columns=['Names',"Births"])
# print(df)
df.to_csv('births.csv', index=False, header=True)
# df1=pd.read_csv('births.csv')
# print(df1)
