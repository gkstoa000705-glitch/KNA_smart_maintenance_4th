# 입력(input)
#주의) 사용자 입력은 항상 "문자열"
#형식:변수=input("안내 문구 넣기")
#name=input("이름:")
#print(name)

#형변환 int(),float(),str()
#print(age+1)
#print(int(age)+1)
#age=27

#실습 나이 구하기
#태어난해 = int(input("태어난해:"))
#나이 = 2026 - 태어난해
#print("나이:", 나이)

#실습 - 여러개의 값 입력받기
#country = input("거주국가")
#city = input("거주도시")
#print(country + "의" + city +"에서 거주하시는군요!")

#실습(코드)
#name=input("성함:")
#city=input("도시:")
#print(name, city)

#실습 두 수를 입력받아 사칙연산
#a=int(input("수1:"))
#b=int(input("수2:"))
#print("합:", a+b)
#print("나누기:", a / b)

#실습 두 수를 입력받아 사칙연산(코드)
#a=int(input("수1:"))
#b=int(input("수2:"))
#print("합:", a+b)
#print("나누기:", a / b)
#print("곱하기:", a*b)
#print("빼기:", a-b)

#여러줄 문자열
#형식: 삼중 따옴표 """ 적을내용.. """
#notice = """
#설비점검 안내
#1. 전원확인
#2. 센서 점검
#"""

# 이스케이프 : \n 줄바꿈, \t 탭
#print("이름\t상태")
#print("첫줄\n둘째 줄")

#실습1. 여러줄 문자열 만들기
#x = "가동 점검표\n 1. 온도확인\n 2. 압력확인"
#print(x)

#실습2. 설비라벨 이어 붙이기
#설비코드= "PUMP_A"
#설비상태="정상"
#날짜= "2025-01-25"
#설비라벨 = 설비코드 + "\n" + 설비상태 + "\n" + 날짜
#print(설비라벨)

#실습3
#code="PUMP_A"
#state="정상"
#date="2025-01-15"

#t(code+"/"+state+"/"date)
#hours=1200
#card="설비 : "+ code+ "\n상태:" + state + "\n가동:" 