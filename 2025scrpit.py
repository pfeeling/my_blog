import numpy as np
import pandas as pd
#팔머펭귄 데이터 불러오기
# pip install palmerpenguins
from palmerpenguins import load_penguins
penguins=load_penguins()
penguins.info()

penguins.head(10)
penguins.tail(10)
penguins.describe()

# 기본 오름차순 정렬
penguins.sort_values(by="bill_length_mm")
#내림차순 정렬: ascending=Fasle
penguins.sort_values(by="bill_length_mm", ascending=False)
#정렬 기준 2개인 경우
penguins.loc[:,["bill_length_mm", "body_mass_g"]].sort_values(
    by=['bill_length_mm', 'body_mass_g'],
    ascending=[False, True])


max_idx = penguins['bill_length_mm'].idxmax()
penguins.iloc[[max_idx],:]

#최대 부리길이 60m인 펭귄은 몇마리?
sum(penguins["bill_length_mm"]==60)

#'species' 열을 기준으로 그룹화하여 평균 계산
grouped_df = penguins.groupby('species').mean(numeric_only = True)
print(grouped_df)
grouped_penguins=pd.DataFrame(grouped_df)

penguins.info()


#같은 결과지만, 불필요한 계산이 있을 수 있음
# penguins.groupby('island').sum(numeric_only = True)["bill_length_mm"]
penguins.groupby('island')["bill_length_mm"].sum()


max_flipper_island = grouped_df.idxmax()

#as_index=False효과
grouped_sum_df = penguins.groupby('island', as_index=False)['flipper_length_mm'].sum()
print(grouped_sum_df)



#그룹을 두개 변수로 활용하고 싶을땐?
penguins.groupby(["island", "sex"]).sum(numeric_only = True)
penguins.groupby(["sex", "island"]).sum(numeric_only = True)
penguins.groupby(["sex", "island"]).mean(numeric_only = True)

df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value': [4, 5, 6]})


merged_df = pd.merge(df1, df2, on='key', how='inner')
merged_df = pd.merge(df1, df2, on='key', how='outer')
#merge df1, df2 값 중에서 key의 교집합을 가지고 와서 value값을 나열한다. 
# how=inner, 두 데이터 의 키값의 교집합
# how=outer, 두 데이터 의 키값의 교집합
print(merged_df)

#병합연습
mid=pd.DataFrame({'student_id':[23,10,5,1],'mid_score':[40,30,50,20]})
final=pd.DataFrame({'student_id':[23,10,5,30],'final_score':[45,25,50,47]})
merged_test = pd.merge(mid, final, on='student_id', how='outer')
print(merged_test)

#연습2
#1)성별, 지역별 부리길이 평균 계산
#2)성별, 지역별 부리 깊이 평균 계산산
#3)1단계, 2단계 병합해서 성별, 지역역별, 부리길이, 부리깊이 데이터 프레임제작


penguins.info()


#as_index=False 그룹화한 컬럼을 인덱스로 설정하지 않고 데이터프레임으로 유지
df1=penguins.groupby(['sex', 'island'],as_index=False)[['bill_length_mm']].mean()
df2=penguins.groupby(['sex', 'island'],as_index=False)[['bill_depth_mm']].mean()

merged_test = pd.merge(df1, df2, on=['sex','island'], how='outer')


#.method를 전체 괄호를 사용하면 여러줄에 걸쳐 코딩가능
(penguins
    .loc[:,'bill_length_mm']
    .mean())

# 두번째 방법(마이너한)
penguins\
    .loc[:,'bill_length_mm']\
    .mean()