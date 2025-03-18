import pandas as pd

df = pd.read_csv('./data/dat.csv')
df.head()
df.info()

set(df["grade"])

# 여러 칼럼 선택
df.loc[:, ['school', 'sex', 'paid', 'goout']]

# 칼럼 이름 변경
df=df.rename(columns = {'Dalc' : 'dalc', 'Walc' : 'walc'})
df

# 칼럼 데이터 타입 변경
# 최빈값으로 대체
#   기존의 데이터 형태인 정수값으로 대체 가능 (장점)
#   전체 변수의 평균값이 변경 될 수 있음 (단점)
# 평균값으로 대체: 
#   전체 변수의 평균값이 그대로 유지 (장점)
#   데이터에 극단값이 존재할 경우 영향을 받을 가능성 (단점)
#   평균값 소수점으로 나올 수 있음 (단점)
# 최빈값을 대체하는 코드
mode_val=df.loc[:, 'goout'].mode()

# df["goout"].fillna(3.0)
df.loc[df['goout'].isna(), "goout"] = 3.0
df[["goout"]]=df.loc[:, ['goout']].astype({'goout' : 'int64'})
df

# 사용자 정의 함수를 사용한 칼럼 생성
def classify_famrel(famrel):
    if famrel <= 2:
        return 'Low'
    elif famrel <= 4:
        return 'Medium'
    else:
        return 'High'

df=df.assign(famrel_qual=df['famrel'].apply(classify_famrel))
df

# 데이터 타입으로 칼럼 선택하는 방법
df.select_dtypes('number')
df.select_dtypes('object')

import numpy as np

# x=df['famrel']
# x=df['freetime']
def standardize(x):
    return (x - np.nanmean(x))/np.std(x)

df.select_dtypes('number').apply(standardize, axis=0)

# 사교육! 정말 해야하는가!??
# paid 변수로 데이터를 나눠서 describe() 결과를 분석
# 음주량이 건강상태 미치는 효과
# 음주량이 성적 미치는 효과
# 건강상태는 성적에 얼마나 영향을 미치는가?
# 4~5번 변수들이 성적에 얼마나 영향을 미치는가?
# 특정 변수를 분석 대상(종속변수)으로 설정할 필요는 없다. 

