# 범주형 변수 = 문자열을 사용한 데이터를 효율적으로 저장하는 방법

# 성별: 남자 & 여자

# 제품이름          성별
# 롯데제과 롯데샌드  1
# 해태 홈런볼        2
# 해태 홈런볼        2
# 롯데제과 롯데샌드  1
import pandas as pd

values = pd.Series(["apple", "orange", "apple", "apple"]*2)
values

values.unique()
values.value_counts()

# take 메서드 p.326
values=pd.Series([0, 1, 0, 0]*2)
dim=pd.Series(["apple", "orange"])

dim.take(values)

# p.327
import numpy as np

fruits = ["apple", "orange", "apple", "apple"]*2
N=len(fruits)
rng=np.random.default_rng(seed=12345)

df=pd.DataFrame({
    "fruit": fruits,
    "basket_id": np.arange(N),
    "count": rng.integers(3, 15, size=N),
    "weight": rng.uniform(0, 4, size=N)
    },
    columns=["basket_id", "fruit", "count", "weight"]
)

# 범주형 변수 변환 p.328
fruit_cat=df["fruit"].astype("category")
c=fruit_cat.array
c.categories
c.codes

dict(enumerate(c.categories))

df["fruit"]=df["fruit"].astype("category")
df.info()

## 범주형 변수를 Series 만들듯이 직접 생성 1
pd.Categorical(["foo", "bar", "baz", "foo", "bar"])

## 범주형 변수를 Series 만들듯이 직접 생성 2
categories=["foo", "bar", "baz"]
codes=[0, 1, 2, 0, 1]
pd.Categorical.from_codes(codes, categories)

# p.330 순서부여
pd.Categorical.from_codes(codes, categories,
                          ordered=True)

# 판다스 범주형 변수 연산
draws=rng.standard_normal(1000)
draws

bins=pd.qcut(draws, 4, labels=["Q1", "Q2", "Q3", "Q4"])
bins.categories
bins.codes[:5]

# 문제: 무게 변수를 기준으로 "가벼움, 중간, 무거움"
# weight_cat를 변수를 추가해주세요!
df["weight_cat"]=pd.qcut(df["weight"], 3, labels=["가벼움", "중간", "무거움"])
df

# 문제: 각 그룹의 weight 평균을 구해주세요!
df.groupby("weight_cat")["weight"].mean()
df.pivot_table(index="weight_cat",
               values="weight",
               aggfunc="mean")

# p.332 범주형 칼럼 메모리 작게 차지함
N=10_000_000
labels=pd.Series(["foo", "bar", "baz", "qux"] * (N // 4))
len(labels)
labels_cat=labels.astype("category")
labels_cat

a=labels.memory_usage(deep=True)
b=labels_cat.memory_usage(deep=True)
a/b

# 카테고리컬 변수 메서드
s=pd.Series(["a", "b", "c", "d"]*2)
cat_s=s.astype("category")
cat_s.cat.categories
cat_s.cat.codes

## 내가 현재 가지고 있는 범주형 변수 값이
## 전체 가질수 있는 값이 아닌경우
cat_s
actual_cat=["a", "b", "c", "d", "e", "f"]
cat_s2=cat_s.cat.set_categories(actual_cat)
cat_s2

# 문제 cat_s의 첫번째 원소를 "e"로 바꿔주세요!
cat_s.iloc[0]="e" # error

# 문제 cat_s2의 첫번째 원소를 "e"로 바꿔주세요!
cat_s2.iloc[0]="e"
cat_s2.cat.codes

cat_s.value_counts()
cat_s2.value_counts()

# 더미변수 생성법
pd.get_dummies(cat_s, dtype=int)
pd.get_dummies(cat_s, dtype=int, drop_first=True)


import pandas as pd
import matplotlib.pyplot as plt

cat_s.value_counts().plot(
    kind="bar",
    color="blue",
    edgecolor="black"
)
plt.xlabel("String")
plt.ylabel("Count")
plt.title("Bar Chart of cat_s variable")
plt.show()

# 범주형 변수 순서가 그래프에 미치는 영향
## 범주형 변수를 Series 만들듯이 직접 생성 1
cat_var1=pd.Categorical(["foo", "bar", "baz", "foo", "bar"])

## 범주형 변수를 Series 만들듯이 직접 생성 2
categories=["foo", "bar", "baz"]
codes=[0, 1, 2, 0, 1]
cat_var2=pd.Categorical.from_codes(codes, categories)

cat_var1.value_counts().plot(
    kind="bar",
    color="blue",
    edgecolor="black"
)
cat_var2.value_counts().plot(
    kind="bar",
    color=["red", "grey", "blue"],
    edgecolor="black"
)
