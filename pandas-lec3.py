# 팔머펭귄 데이터 불러오기
# pip install palmerpenguins
import pandas as pd
from palmerpenguins import load_penguins
penguins = load_penguins()


penguins.head(10)
penguins.tail(10)
penguins.describe()

# 기본 오름차순 정렬
penguins.sort_values(by="bill_length_mm") 
# 내림차순 정렬: ascending=False
penguins.sort_values(by="bill_length_mm", ascending=False) 
# 정렬 기준 2개인 경우
penguins["bill_length_mm"]=round(penguins["bill_length_mm"])
penguins.loc[:,["bill_length_mm", "body_mass_g"]].sort_values(
    by=["bill_length_mm", "body_mass_g"],
    ascending=[True, False])

max_idx = penguins['bill_length_mm'].idxmax()
penguins.iloc[[max_idx],:]

# 최대 부리길이 60mm 인 펭귄은 몇마리?
sum(penguins["bill_length_mm"] == 60.0)


# 'species' 열을 기준으로 그룹화하여 평균 계산
grouped_df = penguins.groupby('species').mean(numeric_only = True)
print(grouped_df)

# 같은 결과지만, 불필요한 계산이 있을 수 있음
# penguins.groupby('island').sum(numeric_only = True)["bill_length_mm"]
grouped_df=penguins.groupby('island')["bill_length_mm"].sum()
grouped_df.idxmax()

# as_index=False 효과
penguins.groupby('island', as_index=False)["bill_length_mm"].sum()

# 그룹을 두개 변수로 활용하고 싶을땐?
penguins.groupby(["island", "sex"]).sum(numeric_only = True)
penguins.groupby(["sex", "island"]).sum(numeric_only = True)


# 병합
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value': [4, 5, 6]})
pd.merge(df1, df2, on='key', how='inner')
pd.merge(df1, df2, on='key', how='outer')

# 병합 연습
mid_df = pd.DataFrame({'id': [1, 5, 10, 23], 'midterm': [20, 50, 30, 40]})
fin_df = pd.DataFrame({'id': [30, 5, 10, 23], 'final': [47, 50, 25, 45]})
pd.merge(mid_df, fin_df, on="id", how="outer")

# 연습 2
# 1) 성별, 섬별 부리길이 평균계산
# 아래처럼 하면 키가 활성화되어 병합된 데이터 프레임 생성되므로 안됨!
# df1=penguins.groupby(["sex", "island"])["bill_length_mm"].mean()
df1=penguins.groupby(["sex", "island"], as_index=False)[["bill_length_mm"]].mean()
df1
# 2) 성별, 섬별 부리깊이 평균계산
# 이것도 안됨
# df2=penguins.groupby(["sex", "island"])["bill_depth_mm"].mean()
df2=penguins.groupby(["sex", "island"], as_index=False)[["bill_depth_mm"]].mean()
df2

# 3) 1단계, 2단계 데이터 프레임 병합해서
# 성별, 섬별, 부리길이, 깊이 데이터 프레임 만들기
merged_df=pd.merge(df1, df2, on=["sex", "island"], how="outer")
merged_df

# 기준 변수 2개 필요한 이유 (한번 돌려볼것)
# import pandas as pd
# # 첫 번째 데이터프레임 (시험 성적)
# df1 = pd.DataFrame({
#     'school': ['A', 'A', 'B', 'B'],
#     'name': ['Alice', 'Bob', 'Alice', 'David'],
#     'math_score': [90, 85, 88, 92]
# })

# # 두 번째 데이터프레임 (영어 성적)
# df2 = pd.DataFrame({
#     'school': ['A', 'A', 'B', 'B'],
#     'name': ['Alice', 'Bob', 'Alice', 'David'],
#     'english_score': [95, 80, 89, 85]
# })

# # 두 개의 변수('school', 'name')를 기준으로 병합
# merged_df = pd.merge(df1, df2, on=['school', 'name'], how='inner')

# print(merged_df)

# 병합 연습 (left join)
mid_df = pd.DataFrame({'id': [1, 5, 10, 23], 'midterm': [20, 50, 30, 40]})
fin_df = pd.DataFrame({'id': [30, 5, 10, 23], 'final': [47, 50, 25, 45]})
pd.merge(mid_df, fin_df, on="id", how="left")

# .method를 전체 괄호를 사용하면 여러줄에 걸쳐 코딩 가능!
(penguins
    .loc[:,"bill_length_mm"]
    .mean())
# 두번째 방법 (마이너한 방법)
penguins \
    .loc[:,"bill_length_mm"] \
    .mean()

sdvzxcv