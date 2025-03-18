import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 팔머펭귄 데이터 불러오기
import pandas as pd
from palmerpenguins import load_penguins
penguins = load_penguins()
penguins
penguins.info()

# 문제 1: 펭귄 종별 평균 부리 길이 구하기

df=pd.DataFrame(penguins)

bill_length_mean=df.pivot_table(
    index='species',
    values='bill_length_mm',
    aggfunc='mean').reset_index()
print(bill_length_mean)

# 문제 2: 섬별 몸무게 중앙값 구하기

# 펭귄 데이터에서 각 섬(island)별로 몸무게(body_mass_g)의 
# 중앙값(median)을 구하는 pivot_table()을 작성하세요.
body_mass_g_median=df.pivot_table(
    index='island',
    values='body_mass_g',
    aggfunc='median').reset_index()
print(body_mass_g_median)


# 문제 3: 성별에 따른 부리 길이와 몸무게 평균 구하기

# 펭귄 데이터에서 성별(sex)과 종(species)별로 
# 부리 길이(bill_length_mm)와 몸무게(body_mass_g)의
# 평균을 구하는 pivot_table()을 작성하세요.

bill_length_body_mass_mean=df.pivot_table(
    index=['sex','species'],
    values=['bill_length_mm','body_mass_g'],
    aggfunc='mean').reset_index()
print(bill_length_body_mass_mean)

bill_length_body_mass_mean=df.pivot_table(
    index='sex',
    columns='species',
    values=['bill_length_mm','body_mass_g'],
    aggfunc='mean').reset_index()
print(bill_length_body_mass_mean)



# 문제 4: 종과 섬에 따른 평균 지느러미 길이 구하기

# 펭귄 데이터에서 각 종(species)과 섬(island)별로 
# 지느러미 길이(flipper_length_mm)의
# 평균을 구하는 pivot_table()을 작성하세요.

flipper_length_mean=df.pivot_table(
    index=['species','island'],
    values='flipper_length_mm',
    aggfunc='mean').reset_index()
print(flipper_length_mean)

pivot4=pd.pivot_table(penguins,
                      index='species',
                      values='island',
                      aggfunc='count',
                      fill_value=0
                      )


# 문제 5: 종과 성별에 따른 부리 깊이 합계 구하기

# 펭귄 데이터에서 종(species)과 성별(sex)별로
# **부리 깊이(bill_depth_mm)의 
# 총합(sum)**을 구하는 pivot_table()을 작성하세요.

bill_depth_mm_sum=df.pivot_table(
    index=['species','sex'],
    values='bill_depth_mm',
    aggfunc='sum').reset_index()
print(bill_depth_mm_sum)

# 문제 6: 종별 몸무게의 변동 범위(Range) 구하기

# 펭귄 데이터에서 각 종(species)별로 몸무게(body_mass_g)의
# 변동 범위 (최댓값 - 최솟값)
# 를 구하는 pivot_table()을 작성하세요.
def my_f(input):
    return max(input)-min(input)
body_mass_abs=df.pivot_table(
    index='species',
    values='body_mass_g',
    aggfunc=my_f).reset_index()

print(body_mass_abs)


def my_f(input):
    return input.max()-input.min()
body_mass_abs=df.pivot_table(
    index='species',
    values='body_mass_g',
    aggfunc=my_f).reset_index()


