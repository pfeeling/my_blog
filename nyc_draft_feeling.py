import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from statsmodels.graphics.mosaicplot import mosaic
import matplotlib.pyplot as plt

from nycflights13 import flights, planes
flights.info()
planes.info()

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
monthly_delays.info()

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

plt.ticklabel_format(style='plain', axis='y')
plt.ylim(6000, 16000)
plt.xlabel('Month')
plt.ylabel('Number of Delays')
plt.title('Total montly Flight Delays')
plt.xticks(ticks=range(1, 13))  # 1~12월 표시
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

# --------------------------
