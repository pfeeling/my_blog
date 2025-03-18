import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from palmerpenguins import load_penguins
penguins = load_penguins()



#melt 사용 방법
data = {
 'Date': ['2024-07-01', '2024-07-02', '2024-07-03'],
 'Temperature': [10, 20, 25],
 'Humidity': [60, 65, 70]
 }
df = pd.DataFrame(data)
print(df)

# 데이터프레임을 긴 형식(long form)으로 변환

df_melted = pd.melt(df, 
                    id_vars=['Date'],
                    value_vars=['Temperature', 'Humidity'],
                    var_name='Variable', 
                    value_name='Value')
print(df_melted.head(6))

# id_vars 기준값
# value_vars 칼럼을 변수로 지정
# var_name 변수들의 컬럼 이름을 지정
# 변수들에 뒤로 붙어 딸려나오는 값들의 컬럼 값을 지정

#예제
sample = {
    'country': ['Afgahnistan','Brazil', 'China'],
    '1999': [745,37737,212258],
    '2000': [2666,80488,213766]
 }
sp = pd.DataFrame(sample)
print(sp)


sp_melted = pd.melt(sp, 
                    id_vars='country',
                    value_vars=['1999', '2000'],
                    var_name='year', 
                    value_name='cases').sort_values(by=['country'])
print(sp_melted.head(6))

#  pivot() 함수 사용하여 melt 이전으로 변환
# 긴 형식(long form)에서 넓은 형식(wide form)으로 변환


df_pivoted = df_melted.pivot(
    index = 'Date', 
    columns='Variable', 
    values='Value').reset_index()
print(df_pivoted)

#2

#예제
data2= {
    'country': ['Afgahnistan','Brazil', 'China'],
    '2024': [745,37737,212258],
    '2025': [2666,80488,213766]
 }
dt = pd.DataFrame(data2)
print(dt)

dt_melted = pd.melt(dt, 
                    id_vars=['country'],
                    value_vars=['2024', '2025'],
                    var_name='year', 
                    value_name='cases').sort_values(['country'])
print(dt_melted.head(6))

#pivot()사용해서 wide 형식으로 전환

dt_pivoted = dt_melted.pivot(
    index = 'country', 
    columns='year', 
    values='cases').reset_index()
print(dt_pivoted)
dt_pivoted.shape#인덱스는 컬럼으로 취급하지 않는다. 
dt_pivoted.iloc[0,0]#0,0 번째 값 
dt_pivoted.columns.name=None# 불필요한 인덱스 이름 제거
dt_pivoted.columns.name='year'# 인덱스 이름 붙이기
dt_pivoted


#pivot_table()

wet_data = {
 'Date': ['2024-07-01', '2024-07-02', '2024-07-03','2024-07-03'],
 'Temperature': [10, 20, 25,20],
 'Humidity': [60, 65, 70,21]
 }
wet = pd.DataFrame(wet_data)
print(wet)

wet_melted=pd.melt(wet,
        id_vars=['Date'],
        value_vars=["Temperature","Humidity"],
        var_name="WeartherFactor",
        value_name="torH")
print(wet_melted)


#pivot_table()로 전환
wet_pivot_table = wet_melted.pivot_table(index='Date', 
                                       columns='WeartherFactor', 
                                       values='torH').reset_index()
print(wet_pivot_table)

# 중복값이 있을 경우 중복값의 평균치를 계산하여 value값을 출력


#pivot() 으로 하면 에러 발생(id값인 Date가 중복값이 있기 때문)
wet_pivoted = wet_melted.pivot(index = 'Date', 
                              columns='WeartherFactor', 
                              values='torH')      
print(wet_pivoted)


df=pd.DataFrame({
    'School': ['A','A','B','B','C','C'],
    'Gender': ['M','F','M','F','M','F'],
    'City': ['North', 'South','North', 'South','North', 'South'],
    'Midterm': [10,20,30,40,50,60],
    'Final': [5,15,25,35,45,55]
})
print(df)

#깔끔한 데이터 조건
# 1. 각 칼럼이 하나의 변수를 의미함
# 2. 각 행이 하나의 관측치를 나타냄
# 3. 각 칸에 하나의 값이 들어있다.
#6명의학생, 3개의 학교 -학교별 중간고사 평균 구하기


#학교별 중간고사 평균
df.pivot_table(
    index='School',
    values='Midterm',
    aggfunc='mean').reset_index()

df.pivot_table(
    index='School',       # 학교별로
    columns='Gender',     # 성별로 나누어
    values=['Midterm'],  #
    aggfunc='mean').reset_index()


#학교별 중간고사,기말고사 평균
df.pivot_table(
    index='School',
    values=['Midterm','Final'],
    aggfunc='mean').reset_index()

#학교별 중간고사,기말고사 평균[컬럼 순서 조정]
df.pivot_table(
    index='School',
    values=['Midterm', 'Final'],
    aggfunc='mean'
).reset_index()[['School','Midterm', 'Final']]


#도시별 학교별 중간고사,기말고사 평균[colmuns 옵션]
df.pivot_table(
    index='School',
    columns='City',
    values=['Midterm','Final'],
    aggfunc='mean').reset_index()

df.pivot_table(
    index=['School','City'],
    values=['Midterm','Final'],
    aggfunc='mean').reset_index()

#인덱스가 여러가지[학교, 성별]
df.pivot_table(
    index=['School','Gender'],
    values='Midterm',
    aggfunc='mean').reset_index()


#aggfunc 사용
df.pivot_table(
    index='School',
    values='Midterm',
    aggfunc='mean').reset_index()


#aggfunc 사용[나만의 함수]벡터 원소의 합에 제곱을 하는 함수 my_f
# 학교별 중간고사 총합의 제곱 
def my_f(input):
    return sum(input)**2

df.pivot_table(
    index='School',
    values='Midterm',
    aggfunc=my_f).reset_index()




