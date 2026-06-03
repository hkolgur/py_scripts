
import pandas as pd

df = pd.DataFrame({'Name': ['Alice', 'Bob','Dan'], 'Score': [85, 90,0]})

df=df['Score'].apply(lambda x:x if x!=0 else df[df['Score']!=0]['Score'].mean())
#Alternate method
#df=df['Score'].replace(0,df['Score'][df['Score']!=0].mean())
print(df)