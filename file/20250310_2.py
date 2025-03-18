import numpy as np
import pandas as pd

df=pd.read_csv('data\dat.csv')
df.head()
df.info()

set(df["grade"])#set의 성질, 중복을 허용하지 않음, value값 확인용
df['grade']

#특정 칼럼 선택[전체 값중 특정 칼럼의 값을 알고 싶다.]
print(df.loc[:, ['school', 'sex', 'paid', 'goout']].info())
df[['school', 'sex', 'paid', 'goout']]
df.loc[:, ['school', 'sex', 'paid', 'goout']]


# rename()
#칼럼 이름 변경columns = {'기존값' : '변경값', '기존값' : '변경값'})
df = df.rename(columns = {'Dalc' : 'dalc', 'Walc' : 'walc'})
print(df.columns)

df['goout'].value_counts()

# astype()
# 칼럼 데이터 타입 변경
df.loc[:, ['goout']]
df.loc[:, ['goout']].astype({'goout':'int64'})#NAN값이 있는경우 전환이 안됨int라서
df.loc[:, ['goout']].isna().sum()
# 최빈값으로 대체[빈도수별] .mode()빈도수많은거 구하는식
# 기존의 데이터 형태인 정수값으로 대체 가능(장점)
# 데이터에 극단값이 존재해도 값에 영향이 없음(장점)
# 전체 변수의 평균값이 변경 될수 있음(단점)
mod_val=df.loc[:, 'goout'].mode()
df['goout'].isna()
#df['goout'].fillna(3.0)
df.loc[df['goout'].isna(),'goout']=3.0
df['goout']=df['goout'].astype('int64')
df

# 평균값으로 대체: 이전 변수의 평균값이 그대로 유지(장점)
# 데이터에 극단값이 존재하면 평균값이 왜곡됨(단점)
# 평균값이 소수점으로 나올수 있음(단점)
df.loc[:, ['goout']].astype({'goout':'int64'})

df.loc[:,'goout'].mean()
df.loc[df['goout'].isna(),'goout']=df.loc[:,'goout'].mean()

df['goout']=df['goout'].astype('int64')
df['goout']

#사용자 정의 함수

def classify_famrel(famrel):
 if famrel <= 2:
   return 'Low'
 elif famrel <= 4:
    return 'Medium'
 else:
    return 'High'
 

#  assign()
# famrel_quality 칼럼을 새롭게 생성
df1 = df.copy()
df1 = df1.assign(famrel_quality=df1['famrel'].apply(classify_famrel))
print(df1[['famrel', 'famrel_quality']].head())

# 기존에 있던 famrel 칼럼의 값을 변경
df2 = df.copy()
df2 = df2.assign(famrel=df2['famrel'].apply(classify_famrel))
print(df2[['famrel']].head())


# assign() 사용 안하고 표현
df3 = df.copy()
df3['famrel'] = df3['famrel'].apply(classify_famrel)
print(df3[['famrel']].head())


df.info()
# select_dtypes()
# 수치형 칼럼만 선택
print(df.select_dtypes('number').head(2))
print(df.select_dtypes('int64').head(2))
#범주형 칼럼만 선택
print(df.select_dtypes('object').head(2))


# 임의의 함수를 정의
df['famrel']
x=df['famrel']
def standardize(x):
   return (x - np.nanmean(x))/np.std(x)
#np.nanmean(x) NaB을 제외한 평균/np.std(x): 표준편차
df.select_dtypes('number').apply(standardize, axis=0)

#사교육과 점수의 상관관계
# paid 변수로 데이터를 나눠서 describe()결과를 분석


#음주량이 건강상태에 미치는 영향
#음주량이 성적에 미치는 영향


#건강상태와 성적의 상관관계
#4~5번 변수들과 성적의 상관관계
#특정정 변수를 분석 대상으로 설정할 필요는 없다. 


# ---------------------2025.03.11
# 특정 문자로 시작되는 칼럼 출력
print(df.columns)
print(df.columns.str.startswith('f'))#f로 시작하는 컬럼은 true를 출력한다.

df.loc[:,df.columns.str.startswith('f')]
#f로 시작하는 컬럼에 해당하는 값을 데이터프레임형식으로 출력
df.iloc[:,df.columns.str.startswith('f')]
#f로 시작하는 컬럼에 해당하는 인덱스를 데이터프레임형식으로 출력


# 특정 문자로 끝나는 칼럼 출력
print(df.columns)
df.loc[:,df.columns.str.endswith('c')]

# 'a'를 포함하는 칼럼 선택
print(df.columns)
print(df.columns.str.contains('a'))
df.loc[:,df.columns.str.contains('a')]





