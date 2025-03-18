import pandas as pd

df = pd.DataFrame({
    'School': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Gender': ['M', 'F', 'M', 'F', 'M', 'F'],
    'City': ['North', 'South', 'North', 'South', 'North', 'South'],
    'Midterm': [10, 20, 30, 40, 50, 60],
    'Final': [5, 15, 25, 35, 45, 55]
})

df

# 깔끔한 데이터 조건
# 1. 각 칼럼이 하나의 변수 의미한다.
# 2. 각 행이 하나의 관측치를 나타낸다.
# 3. 각 칸에 하나의 값이 들어있다.

# 학교별 중간고사 평균 
df.pivot_table(
    index='School',
    values='Midterm',
    aggfunc="mean").reset_index()

# 학교별 중간고사, 기말고사 평균 
df.pivot_table(
    index='School',
    values=['Midterm', 'Final'],
    aggfunc="mean").reset_index()

# columns 옵션에 의미
df.pivot_table(
    index='School',
    columns='City',
    values=['Midterm', 'Final'],
    aggfunc="mean").reset_index()

# 인덱스가 여러개
df.pivot_table(
    index=['School', 'Gender'],
    values='Midterm',
    aggfunc="mean").reset_index()

# aggfunc의 사용
# 나만의 함수 
# 벡터 원소들을 더 한 수 제곱을 하는 함수 my_f
def my_f(input):
    return sum(input)**2    

df.pivot_table(
    index='School',
    values='Midterm',
    aggfunc=my_f).reset_index()


#### 팔머펭귄 연습 ####
# 팔머펭귄 데이터 불러오기
import pandas as pd
from palmerpenguins import load_penguins
penguins = load_penguins()

# 문제 1: 펭귄 종별 평균 부리 길이 구하기
# 펭귄 데이터에서 각 종(species)별로 평균 부리 길이(bill_length_mm)를
# 구하는 pivot_table()을 작성하세요.
pivot1 = pd.pivot_table(penguins, 
                        index="species", 
                        values="bill_length_mm", 
                        aggfunc="mean")
pivot1

# 문제 2: 섬별 몸무게 중앙값 구하기
# 펭귄 데이터에서 각 섬(island)별로 몸무게(body_mass_g)의 중앙값(median)을
# 구하는 pivot_table()을 작성하세요.
pivot2 = pd.pivot_table(penguins, 
                        index="island", 
                        values="body_mass_g", 
                        aggfunc="median")
pivot2

# 문제 3: 성별에 따른 부리 길이와 몸무게 평균 구하기
# 펭귄 데이터에서 성별(sex)과 종(species)별로
# 부리 길이(bill_length_mm)와 몸무게(body_mass_g)의
# 평균을 구하는 pivot_table()을 작성하세요.
pivot3 = pd.pivot_table(penguins, 
                        index=["sex", "species"], 
                        # columns=???, 
                        values=["bill_length_mm", "body_mass_g"], 
                        aggfunc="mean").reset_index()
pivot3

# pivot3 = pd.pivot_table(penguins, 
#                         index=["sex"], 
#                         columns="species", 
#                         values=["bill_length_mm", "body_mass_g"], 
#                         aggfunc="mean").reset_index()
# pivot3

# 문제 4: 종과 섬에 따른 평균 날개 길이 구하기
# 펭귄 데이터에서 각 종(species)과 섬(island)별로
# 날개 길이(flipper_length_mm)의 평균을 구하는 pivot_table()을 작성하세요.
pivot4 = pd.pivot_table(penguins, 
                        index="species", 
                        columns="island", 
                        values="flipper_length_mm", 
                        aggfunc="count",
                        fill_value="개체수 없음")
pivot4

# 문제 5: 종과 성별에 따른 부리 깊이 합계 구하기
# 펭귄 데이터에서 종(species)과 성별(sex)별로
# 부리 깊이(bill_depth_mm)의 총합(sum)을 구하는 pivot_table()을 작성하세요.
pivot5 = pd.pivot_table(penguins, 
                        index="species", 
                        columns="sex", 
                        values="bill_depth_mm", 
                        aggfunc="sum").reset_index()
pivot5

# 문제 6: 종별 몸무게의 변동 범위(Range) 구하기
# 펭귄 데이터에서 각 종(species)별로 몸무게(body_mass_g)의
# 변동 범위 (최댓값 - 최솟값) 를 구하는 pivot_table()을 작성하세요.
# 힌트: aggfunc에 사용자 정의 함수를 활용하세요.
def my_range(input):
    return input.max() - input.min()

pivot6 = pd.pivot_table(penguins, 
                        index="species", 
                        values="body_mass_g", 
                        aggfunc=my_range)

pivot6

# ------------------------------20250311





