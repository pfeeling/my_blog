import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from statsmodels.graphics.mosaicplot import mosaic
import matplotlib.pyplot as plt

from nycflights13 import flights, planes
flights.info()
planes.info()

picked=flights[[]]
# 주제 4
# 월별 지연 횟수 --> 왜 특정 월에 지연이 많이 되는지


picked=flights[['arr_delay','dep_delay','time_hour']]


picked.info()

#picked['time_hour']의 형식 변환 [object에서datetime64로 ]
picked['time_hour'] = pd.to_datetime(picked['time_hour'])



# 월정보 추출
picked['extracted_month'] = picked['time_hour'].dt.month



 # 도착 지연 여부[True, False]
picked['arr_delay_flag'] = picked['arr_delay'] > 0 
# 출발 지연 여부[True, False]
picked['dep_delay_flag'] = picked['dep_delay'] > 0  


# 월별 지연 횟수 집계[도착지연, 출발지연 True값의 합 ]
monthly_delays = picked.groupby('extracted_month').agg(
    arrival_delays=('arr_delay_flag', 'sum'),
    departure_delays=('dep_delay_flag', 'sum')
).reset_index()

print(monthly_delays)


#1월~12월 정렬
monthly_delays = monthly_delays.sort_values(by='extracted_month')



#막대그래프 사용  
#지연횟수가 많은 달 =12월
#지연횟수가 많은 구간=6월~ 8월

# X 축 위치 조정[동시에 출발, 도착 지연 표기 위해]
x = np.array(monthly_delays['extracted_month'])  # 월 (1~12)나열
width = 0.4  # 막대 너비

# 그래프 그리기 (도착 지연은 왼쪽, 출발 지연은 오른쪽)
plt.figure(figsize=(10, 5))
plt.bar(x - width/2, monthly_delays['arrival_delays'],
         width=width, label='Arrival Delays', color='blue', alpha=0.7)
plt.bar(x + width/2, monthly_delays['departure_delays'],
         width=width, label='Departure Delays', color='red', alpha=0.7)


plt.xlabel('Month')
plt.ylabel('Number of Delays')
plt.title('Total montly Flight Delays')
plt.xticks(ticks=range(1, 13))  # 1~12월 표시
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# ---------------------------------------------------------------------
# 월, 일정보 추출, 
picked['extracted_month_day'] = picked['time_hour'].dt.strftime('%m-%d')


# 월별 지연 횟수 집계[도착지연, 출발지연 True값의 합 ]
monthly_day_delays = picked.groupby('extracted_month_day').agg(
    arrival_delays=('arr_delay_flag', 'sum'),
    departure_delays=('dep_delay_flag', 'sum')
).reset_index()
print(monthly_day_delays)



# 'extracted_month_day'를 시계열 형식으로 변환
monthly_day_delays['extracted_month_day'] = pd.to_datetime(monthly_day_delays['extracted_month_day'], format='%m-%d')

# 월 정보를 추출 (7, 8, 9, 12월만)
monthly_day_delays['month'] = monthly_day_delays['extracted_month_day'].dt.month

# 'extracted_month_day'에서 날짜만 뽑기 (1일부터 30일까지)
monthly_day_delays['day'] = monthly_day_delays['extracted_month_day'].dt.day

# 7월, 8월, 9월, 12월 데이터만 필터링
filtered_months = monthly_day_delays[monthly_day_delays['month'].isin([7, 8, 9, 12])]

# 그래프 그리기
plt.figure(figsize=(14, 8))

# 7월 도착 지연 히스토그램
sns.histplot(data=filtered_months[filtered_months['month'] == 7], x='day', weights='arrival_delays', color='blue', kde=False, label='July Arrival Delays', bins=30, alpha=0.6)

# 8월 도착 지연 히스토그램
sns.histplot(data=filtered_months[filtered_months['month'] == 8], x='day', weights='arrival_delays', color='green', kde=False, label='August Arrival Delays', bins=30, alpha=0.6)

# 9월 도착 지연 히스토그램
sns.histplot(data=filtered_months[filtered_months['month'] == 9], x='day', weights='arrival_delays', color='orange', kde=False, label='September Arrival Delays', bins=30, alpha=0.6)

# 12월 도착 지연 히스토그램
sns.histplot(data=filtered_months[filtered_months['month'] == 12], x='day', weights='arrival_delays', color='red', kde=False, label='December Arrival Delays', bins=30, alpha=0.6)

# 7월 출발 지연 히스토그램
sns.histplot(data=filtered_months[filtered_months['month'] == 7], x='day', weights='departure_delays', color='blue', kde=False, label='July Departure Delays', bins=30, alpha=0.2, linestyle='--')

# 8월 출발 지연 히스토그램
sns.histplot(data=filtered_months[filtered_months['month'] == 8], x='day', weights='departure_delays', color='green', kde=False, label='August Departure Delays', bins=30, alpha=0.2, linestyle='--')

# 9월 출발 지연 히스토그램
sns.histplot(data=filtered_months[filtered_months['month'] == 9], x='day', weights='departure_delays', color='orange', kde=False, label='September Departure Delays', bins=30, alpha=0.2, linestyle='--')

# 12월 출발 지연 히스토그램
sns.histplot(data=filtered_months[filtered_months['month'] == 12], x='day', weights='departure_delays', color='red', kde=False, label='December Departure Delays', bins=30, alpha=0.2, linestyle='--')

# 레이블 추가
plt.title('Daily Arrival and Departure Delay Counts for July, August, September, and December')
plt.xlabel('Day of the Month')
plt.ylabel('Number of Delays')
plt.xticks(range(1, 31))  # 1일부터 30일까지 날짜
plt.legend()

# 그래프 표시
plt.tight_layout()
plt.show()