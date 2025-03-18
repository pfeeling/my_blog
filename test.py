import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df.to_csv("./data/sample.csv", index=False, sep=";", endcoding="utf-8")




df2=pd.read_csv('data/fluentcom-32f76c1cf37c621183f399144229a7a0-fluentcom-problem2.csv')
df2



df=pd.read_csv('data/fluentcom-f0f882a4e6f5c7e165d1bde9e425a192-fluentcom-problem1.csv')
df

df.info()
df.shape
df['거주자 수'].max()

df.loc[63044,'아파트 이름']


df.groupby('층')['거주자 수'].mean().sort_values()

df['계약구분'].describe()

df['거주연도'].
    

df['계약자고유번호'],df['거주연도'].max()


df['거주연도'].idxmax()

df.groupby(df['계약자고유번호'])[df['거주연도'].max()].sum()


dfdf=pd.pivot_table(df,
                    index='계약자고유번호',
                    values='거주연도',
                    aggfunc=('max')).reset_index()

dfdf.isna()

df.isna().sum()
df.info()

df(['퇴거여부','거주개월','퇴거연도'])
df[['퇴거여부','거주개월',]]

df['퇴거여부'].value_counts
df['거주개월'].unique()
df.info()
dsaf=pd.merge


dfdf=pd.pivot_table(df,
                    index='퇴거여부',
                    values='거주개월').reset_index()







df[df['거주개월'][df['재계약횟수']>=df['재계약횟수'].median()]].mean()
df['거주개월'][df['재계약횟수']<df['재계약횟수'].median()].mean()


df['재계약횟수'].describe()


df.loc[df['재계약횟수']>=df['재계약횟수'].median(),['거주개월']].mean()
df.loc[df['재계약횟수']<df['재계약횟수'].median(),['거주개월']].mean()



def my_f(x):
    if x>=df['재계약횟수'].median():
        return '높음'
    else:
        return '낮음'

df['재계약횟수'].median()

df[df['재계약횟수']>=my_f].mean()

df['재계약횟수']>=my_f

df(df['재계약횟수']>=df['재계약횟수'].median()).mean()

df.info()
df['대표나이'][df['재계약횟수']>=8].median()
df['나이'][df['재계약횟수']<8].median()

dat.loc[(dat['아파트 평점'].notna())&(dat['계약구분'].notna())]



16. 특수문자를 제거하고 수치형 데이터를 변경해라    

df2=pd.read_csv('data/fluentcom-32f76c1cf37c621183f399144229a7a0-fluentcom-problem2.csv')
df2
df2.info()

df2['a7_1'].value_counts().xum
df2['a1_1'].describe()
df2['a1_2'].isna().sum()

df2['a7_1'].shape

df2.isna().sum()

df2.fillna(0)

df2.value_counts()
df2['a2_1'].unique()
df2['a4_1'].unique()
df2['a7_1'].unique()
df2['a2_1'].mean()

df2['a2_1']=df2['a2_1'].str.replace(':','0')
df2['a4_1']=df2['a4_1'].str.replace('&','0')
df2['a7_1']=df2['a7_1'].str.replace('"','0')
df2['a2_1']=df2['a2_1'].astype('int64')
df2['a4_1']=df2['a4_1'].astype('int64')
df2['a7_1']=df2['a7_1'].astype('int64')

df2['a7_1'].mean()

'a2_1','a4_1','a7_1'



df2[['a2_1','a4_1','a7_1']].columns.str.extract(r'([:])')

df2.info()
df2.describe()


def my_f(x):
    return x*2+1



df2.iloc[0,my_f]

melted=pd.melt(df2,
               id_vars='game_id',
               value_vars='a1_1',
               var_name='ining1',
               value_name='first_move')








df.select_dtypes('number')



def my_f(x):
    if x<=2:
       return 'Low'
    elif x<=4:
        return 'Medium'
    else:
        return 'High'
df1=df1.assign(famrel_quality=df1['famrel'].apply(my_f))
df2=df2.assign(famrel=df2['famrel'].apply(my_f))


def standardize(x):
    q1=x.median()
    q2=x.quantile(0.75)
    q3=x.quantile(0.25)
    irq=q2-q3
    irq.replace(0, np.nan, inplace=True)
    return (x-q1)/irq

pd.date_range(start='2021-01-01',end='2022-01-10' ,freq='D')

df['date'] = pd.to_datetime(df['date'])


