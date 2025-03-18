import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('./data/grade.csv')
print(df.head())


# df 데이터 프레임의 정보를 출력하고, 각 열의 데이터 타입을 확인하세요.
df.info()
#데이터가 깨지지 않았는지,변수명이 적절하게 처리되었는지 확인
#non-null의 count확인, dtpye확인



# midterm 점수가 85점 이상인 학생들의 데이터를 필터링하여 출력하세요.
df[df['midterm']>=85]
df.loc[df['midterm']>=85]



# final 점수를 기준으로 데이터 프레임을 내림차순으로 정렬하고,
#  정렬된 데이터 프레임의 첫 5행을 출력하세요.

df.sort_values(by='final').head()
df.sort_values(by='final', ascending=False).head()


# gender 열을 기준으로 데이터 프레임을 그룹화하고,
#  각 그룹별 midterm과 final의 평균을 계산하여 출력하세요.

df_pivoted=pd.pivot_table(df,
                          index='gender',
                          values=['midterm','final'],
                          aggfunc=('mean'),                          
                          ).reset_index()
df_pivoted
df_grouped=df.groupby('gender')[['midterm','final']].mean()



# student_id 열을 문자열 타입으로 변환하고, 변환된 데이터 프레임의 정보를 출력하세요.

df.info()
df['student_id']=df['student_id'].astype('str')         
df['student_id']=df['student_id'].astype('object')


# assignment 점수의 최대값과 최소값을 가지는 행을 각각 출력하세요.!!
#인덱스 추출 idxmax, idxmin
df['assignment'].max()#최댓값을 보여줌
df['assignment'].min()

df['assignment'].idxmax()#최댓값의 인댁스를 보여줌
df['assignment'].idxmin()

df.loc[df['assignment'].idxmax()]
df.loc[df['assignment'].idxmin()]








# midterm, final, assignment 점수의 평균을 계산하여 average 열을 추가하고, 첫 5행을 출력
# 하세요.

df['average']=df[['midterm', 'final', 'assignment']].mean(axis=1)







df[['midterm','final','assignment']]
df[['midterm','final','assignment']].mean(axis=1)
df['average']=df[['midterm','final','assignment']].mean(axis=1)
df

# 아래의 추가 데이터를 생성하고, 기존 데이터 프레임과 student_id를 기준으로 병합하여 출력하
# 세요

additional_data = {
 'student_id': ['1', '3', '5', '7', '9'],
 'club': ['Art', 'Science', 'Math', 'Music', 'Drama']
 }
df_additional = pd.DataFrame(additional_data)
df_additional.shape
df.shape

merged_df=pd.merge(df,
                   df_additional, on='student_id',how='left'
                   )
# gender를 인덱스로, student_id를 열로 사용하여 average 점수에 대한 피벗 테이블을 생성하
# 고 출력하세요.

df_pivoted2=pd.pivot_table(df,
                          index='gender',
                          columns='student_id',
                          values='average'          
                          ).reset_index()

pivot_table = df.pivot_table(values='average',
                              index='gender', columns='student_id')
print(pivot_table)

# ------------------------------------------------

df = pd.read_csv('data\grade.csv')

#  midterm, final, assignment의 평균을 구하고, average 열을 생성하시오.
df['average']=df[['midterm', 'final', 'assignment']].mean(axis=1)
df['average']


#  또한, 성별, 성적 유형(assignment, average, final, midterm)별 평균 점수를 계산하시오.


avg1=pd.pivot_table(df,
               index='gender',
               values=['midterm', 'final', 'assignment','average'],
               aggfunc='mean').reset_index()


# -------------------------------
# melted_df=pd.melt(df,
#                   id_vars=['student_id','name','gender'],
#                   value_vars=['midterm', 'final', 'assignment','average'],
#                   var_name='variable',
#                   value_name='score')
# melted_df.head()
# ---------------------------------


avg3=df.groupby('gender')[['midterm', 'final', 'assignment','average']].mean()


# 최대 평균 성적을 가진 학생의 이름과 평균 성적을 출력하시오.??


max_student=df['average'].idxmax()#인덱스 번호 정보 
df['average'].max()# 해당하는 최대값 보여줌
max_student_score=df.loc[max_student,['name','average']]
print(max_student_score)

