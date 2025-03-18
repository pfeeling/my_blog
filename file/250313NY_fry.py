import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from nycflights13 import flights, planes
flights.info()
planes.info()

planes.describe()
planes['speed'].describe()


# 비행기 기종 별 시간대별(시간정보 추출) 지연시간 (출발 도착)
# 엔진모델 별 비행거리
# 엔진 개수 별 비행거리


# 월별 비행거리 

temp = flights[['tailnum','dep_delay','arr_delay']]
temp2 = planes[['tailnum','type','model']]


pd.merge(temp, temp2, how = 'inner')



#flights 월, distance

sample = flights[['month','distance','tailnum','dep_delay','arr_delay']]
sample2 = planes[['tailnum','type','model']]



data=pd.merge(sample, sample2, how = 'inner')






#월별 비행거리 [12월이 제일 길고, 2월이 제일 짧다.]
pivoted_month=pd.pivot_table(data,
                  index='month',
                  values='distance').reset_index().sort_values(by='distance')
print(pivoted_month)


#상기 내용 그래프#
plt.figure(figsize=(10, 6))
sns.barplot(data=pivoted_month, x='month', y='distance', palette='viridis')

plt.title('Monthly Flight Distance ', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Distance', fontsize=12)
plt.xticks(rotation=45)

plt.yscale('log')
plt.show()



pivoted_model=pd.pivot_table(data,
                  index=['model','tailnum'],   
                  values='distance').reset_index()
print(pivoted_model)


plt.figure(figsize=(12, 6))
sns.barplot(data=pivoted_model, x="model", y="distance", hue="tailnum", dodge=True, palette="Blues")

plt.title("Flight Distance by Model and Tail Number", fontsize=14)
plt.xlabel("Aircraft Model", fontsize=12)
plt.ylabel("Distance", fontsize=12)
plt.xticks(rotation=45)

plt.legend(title="Tail Number", bbox_to_anchor=(1, 1), loc="upper left")  # 범례 조정
plt.show()