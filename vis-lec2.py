import numpy as np

np.random.seed(25317)
x=np.random.randint(1, 21, size=15)

# Q1, Q2, Q3?
np.sort(x)

1,  3,  3,  5,  5,  6,  6,  8, 11, 13, 13, 15, 18, 18, 20
# q2: 중앙값
q2=8

np.sort(x[x < q2])
1, 3, 3, 5, 5, 6, 6

# q1
q1=5

# q3
np.sort(x[x > q2])
11, 13, 13, 15, 18, 18, 20
q3=15

q1, q2, q3
iqr=q3-q1
iqr

import numpy as np

np.random.seed(957)
y=np.random.randint(1, 21, size=15)
y[3]=40
y
# q1=?, q2=?, q3=?
# 상자그림 그려보세요!

y=np.sort(y)
y
q2=9

np.sort(y[y < q2])
q1=6

np.sort(y[y > q2])
q3=17
iqr=q3-q1
iqr

# 그래프 그리기 실습
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./data/Obesity2.csv')
df.info()

# 상자그림(Box Plot) 그리기
plt.figure(figsize=(6,5))
sns.boxplot(x=df['NObeyesdad'], 
            y=df['Weight'],
            palette="Pastel1")
plt.xlabel("Obesity Level")
plt.ylabel("Weight")
plt.title("Box Plot of Weight by Obesity")
plt.xticks(rotation=45)
plt.show()

# 산점도 그리기
import matplotlib.pyplot as plt
df.columns
# 비만 종류별 데이터 포인트 색깔을 변경해보세요!
# NObeyesdad
df["NObeyesdad"].unique()
set(np.array(df["NObeyesdad"]))
x=np.array(df["NObeyesdad"])
x

conditions = [
    x == 'obesity_type_i',
    x == 'obesity_type_ii',
    x == 'obesity_type_iii',
    x == 'overweight_level_i'
]
choices = ["red", "blue", "green", "black"]
# 기본값을 -1로 설정
result = np.select(conditions, choices, default="")
print(result)

# df["NObeyesdad"].astype("category").cat.codes
plt.figure(figsize=(6,5))
plt.scatter(df['Height'], df['Weight'],
            c=result,
            alpha=0.3)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Scatter Plot of Height vs Weight")
plt.show()

# sns 산점도
plt.figure(figsize=(6,5))
sns.scatterplot(data=df,
    x='Height',
    y='Weight',
    hue="NObeyesdad")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Scatter Plot of Height vs Weight")
plt.show()
