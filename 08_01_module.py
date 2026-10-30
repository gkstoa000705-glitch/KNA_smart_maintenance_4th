# 모듈 / 패키지 / 라이브러리 
# -모듈 : 기능을 모아둔  py 파일 하나
# - 패키지 : 모듈을 모아둔 폴더
# - 라이브러리 : 위에 사항들을 통칭

# import 방식
# 형식 : import 모듈 / from 모듈 import 기능 / 
#import math
#print(math.sqrt(16))
#from math import sqrt, cell
#print(sqrt(16), cell(4.2))
#import math as m
#print(m.sqrt(16))

#실습 1
#import math
#print(math.sqrt(16))
#from math import sqrt, cell
##print(sqrt(16), cell(5.7))
#import math as m
#print(m.sqrt(16))

# 표준 라이브러리 - math / random / datetiome
# - 파이썬 설치시 함께 깔리는 검증된 모듈들
#import random 
#import datetime 

#print(random.randint(1, 100))
#print(datetime.datetime.now())

#실습2
#import random
#import math
#sensor = random.randint(1,100)
#result = math.sqrt(sensor)
#print("센서값:", sensor)
#print("제곱근:", result)

#  -지금 실행중인 위치를 기준으로 한 주소

#print("현재 실행 위치(절대경로):", os.getcwd())

#폴더 유무 확인
#print(os.path.exists("data"))

#폴더 목록 확인
#files = os.listdir("data")
#print(files)

#폴더명 + 파일명 -> 경로
#path = os.path.join("data", "08_press.csv")

#if os.path.exists(path):
#    print("파일 경로:", csv)

