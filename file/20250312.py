import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 정규표현식을 통한 문자열 추출

# []   ()   .    ^    $
  
# \d  \D  \w  \W   \s   \S



data = {
 '주소': ['서울특별시 강남구 테헤란로 123',
         '부산광역시 해운대구 센텀중앙로 45',
         '대구광역시 수성구 동대구로 77']
}
df = pd.DataFrame(data)
df['주소'].str.extract(r'([가-힣]+광역시|[가-힣]+특별시)')
              #[가-힣]=한글문자중, 광역시, 혹은 특별시가 포함되는 문자열을 추출한다.

df['주소'].str.extract(r'([가-힣]+광역시|[가-힣]+특별시)', expand=False)

# ([가-힣]+광역시|[가-힣]+특별시) 구성 요소
# [가-힣]+ : 한글 문자가 1회 이상 반복
# 예시 : 서울, 부산, 대구 등
# [가-힣]+광역시 : 한글 문자가 1회 이상 반복되고, 광역시로 끝나는 문자열 반환



# 특수 문자 추출
# str.extractall()

# 모든 특수 문자 추출

data2 = {
 '주소': ['서울특별시 강남구 테헤란로 123',
         '부산광역시 해운대@구 센텀중앙로? 45',
         '대구광역시 수성구 동대구로 77']
}
df2 = pd.DataFrame(data2)

df2['주소'].str.extractall(r'([^a-zA-Z0-9가-힣\s])')
#소문자 a에서 z까지, 대문자 A에서 Z까지, 0부터9까지, 한글 음절을 나타내는 문자 ,공백문자

# 특수 문자 제거
df2['주소_특수문자제거'] = df2['주소'].str.replace(r'[^a-zA-Z0-9가-힣\s]',
                                          '', regex=True)


#테헤란로, 센텀 중앙로, 바우덕이로 같은 도로명 칼럼 만들기!

data3 = {
 '주소': ['서울특별시 강남구 테헤란로 123',
         '부산광역시 해운대구 센텀중앙로 45',
         '경기도 안성시 서운면 바우덕이로 428']
}
df3 = pd.DataFrame(data3)

df3['도로명']=df3['주소'].str.extract(r'([가-힣]+로)', expand=False)
print(df3['도로명'])

# 숫자만 꺼내오려면?

df3['주소'].str.extract(r'([0-9]+)')

df3['주소'].str.extract(r'([\d]+)')


# 문제풀이


df=pd.read_csv('data/regex_practice_data.csv')


# 1. 이메일 주소 찾기
# 문자열에서 이메일 주소를 모두 찾아보세요
df['전체_문자열'].str.extract(r'([\w\.]+@[\w\.]+)')


# 2. 문제: 010으로 시작하는 핸드폰 번호를 찾아보세요.


df['전체_문자열'].str.extract(r'(010-[\d\-]+)')
df['전체_문자열'].str.extract(r'(010-[\d\-]+)').dropna()



# 일반 전화번호(지역번호 포함) 찾기
# 3.문제: 02, 031, 055 등의 지역번호가 포함된 전화번호를 찾아보세요.


phone_num=df['전체_문자열'].str.extract(r'(\d+-[0-9\-]+)')
~phone_num.iloc[:,0].str.startswith('01')
phone_num.loc[~phone_num.iloc[:,0].str.startswith('01'),:]



df["전체_문자열"].str.extract(r"\b(?!010-)(\d{2,3}-\d{3,4}-\d{4})\b").dropna()


pd.set_option('display.max_colwidth', None)
# 4. 주소에서 '구' 단위만 추출하기
# 📌 문제: 주소에서 XX구 패턴을 찾아보세요.
df["전체_문자열"].str.extract(r'(\b[\w]+구\b)')



# 5. 날짜(YYYY-MM-DD) 형식 찾기
# 📌 문제: YYYY-MM-DD 형식의 날짜를 찾아보세요.
df["전체_문자열"].str.extract(r'(\d{4}-\d{2}-\d{2})').dropna()



# 6. 모든 날짜 형식 찾기 (YYYY-MM-DD, YYYY/MM/DD, YYYY.MM.DD 포함)
df["전체_문자열"].str.extract(r'(\d{4}[-/.]\d{2}[-/.]\d{2})').dropna()
df["전체_문자열"].str.extract(r'(\b[\d]{4}\W+[\d]{2}\W[\d]{2}\b)').dropna()



# 7. 가격 정보(₩ 포함) 찾기
# 📌 문제: ₩로 시작하는 가격 정보를 찾아보세요.
df["전체_문자열"].str.extract(r'(₩[\d,]+)')


# 8. 가격에서 숫자만 추출하기 (₩ 제거)
df["전체_문자열"].str.extract(r'₩([\d,]+)')




# 9. 이메일의 도메인 추출하기
# 📌 문제: 이메일 주소에서 @ 뒤에 오는 도메인만 추출하세요.


df["전체_문자열"].str.extract(r'(@[\w\.]+)')
                        


# 10. 이름만 추출하기
# 📌 문제: 데이터에서 한글 이름만 추출하세요.

df["전체_문자열"].str.extract(r'([\w]{2,3})')

df['전체_문자열'].str.extract(r'([가-힣]+)')


# --------------------

















