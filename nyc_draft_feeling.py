import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from statsmodels.graphics.mosaicplot import mosaic
import matplotlib.pyplot as plt

from nycflights13 import flights, planes, weather
flights.info()
planes.info()
flights['origin'].unique()
# 주제 4
# 뉴욕 및 뉴저지 지역 주요 공항의 월별 도착,출발 지연 횟수
# 특정 월에 지연횟수가 증가하는지


picked=flights[['arr_delay','dep_delay','time_hour']]

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


#상기 그래프를 바탕으로 
# 특정 월의 지연 횟수 증가와 날씨정보의 상관관계 확인
# [온도, 풍속, 습도기준]

#weather데이터 확인 
weather.info()


# flights, weather 두 데이터 프레임 merge 후 사용할 컬럼만 picked2 로 변환[온도, 풍속, 습도]
merged=pd.merge(flights, weather, how='inner')
picked2=merged[['temp','wind_speed','humid','time_hour']]


#picked2['time_hour']의 형식 변환 [object에서datetime64로 ]
picked2['time_hour'] = pd.to_datetime(picked2['time_hour'])


# 월정보 추출
picked2['month'] = picked2['time_hour'].dt.month

#월별 평균 기온, 풍속, 습도 측정
weather_inf=picked2.groupby('month')[['temp','wind_speed','humid']].mean(numeric_only=True).reset_index()


# 섭씨로 변환
def celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
weather_inf['temp'] = weather_inf['temp'].apply(celsius)

#각 해당그래프 출력
plt.figure(figsize=(10, 5))
plt.plot(weather_inf['month'],weather_inf['temp'],
         label='temp', color='black', alpha=0.7)
plt.plot(weather_inf['month'],weather_inf['humid'],
         label='humid', color='blue', alpha=0.7)
plt.plot(weather_inf['month'],weather_inf['wind_speed'],
         label='wind_speed', color='green', alpha=0.7)

plt.xlabel('Month')
plt.ylabel('Weather_Data')
plt.title('Montly Weather Info')
plt.xticks(ticks=range(1, 13))  # 1~12월 표시
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 풍속 : 풍속은 유의미한 값을 가지지 않는다. 
# 습도 : 여름[6~8]뿐만 아니라 겨울에도 습도가 상당히 높다. 
# 상기 지연 그래프와 상관관계가 상당히 높다. 
# 온도 : 도착, 출발 지연이 빈번해지는 6,7,8,12 월에 온도 의 편차가 증가하는 모습으로 보아
# 온도역시나 상관관계가 있다고 보인다.





