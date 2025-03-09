#팔머펭귄 데이터 불러오기
# pip install palmerpenguins
import numpy as np
import pandas as pd
from palmerpenguins import load_penguins
penguins=load_penguins()
penguins.info()

# 각 펭귄 종별 특징 알아내서 발표

penguins
column_index = pd.DataFrame(penguins)

summary = penguins.groupby(['species'])[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']]
stats = summary.agg(['min', 'max', 'median', 'mean'])
stats
# Adelie,Chinstrap,Gentoo 
# 펭귄의 부리 길이, 너비, 날개 길이,몸무게 최대, 최소, 중간값, 편차 값

extreme_species = pd.DataFrame({
    "Max Species": max_species.values,
    "Max Value": max_values.values,
    "Min Species": min_species.values,
    "Min Value": min_values.values
    }, index=["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"])
    
extreme_species# 부리 길이, 넓이, 날개 길이, 몸무게 별 종별 최대, 최소 평균값

result = penguins.groupby(['island', 'species', 'sex']).size().reset_index(name='count')
result# 서식지별 종,성별, 그리고 마리수 정보


result2 = penguins.groupby(['island', 'species']).size().reset_index(name='count')
result2 #서식지별 펭귄 종류및 마리수

species_means = penguins.groupby(['species', 'sex']).mean(numeric_only=True)
print(species_means)# 연도별 조사한 펭귄 표본수  