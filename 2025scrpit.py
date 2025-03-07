
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
dp.grouped_df

