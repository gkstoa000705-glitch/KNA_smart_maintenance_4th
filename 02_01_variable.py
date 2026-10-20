# 변수화 할당 - 값에 이름 붙히기
#형식 : 변수이름 = 값 <- 오른쪽 값을 왼쪽 이름에 "저장" 하라는 명령
temp = 25
name = "센서A"
count = 3

print(temp) #25
print("temp")
x = 10
x = x + 5
print(x) #15

#변수 이름 규칙
#형식 : 영문자, 숫자, 밑줄 사용 가능 / 숫자로 시작 불가 / 공백 불가
sensor_count=3 #snake_case
temp2 = 10     #숫자 사용가능(숫자 시작X)
#2temp = 2     #SyntaxError: invalid decimal literal

# 대소문자 구분, 재할당
temp=25
Temp=100
print(temp, Temp) #25 100
#재할당 : 마지막에 저장한 값만 남음
score=10
score=20
score=30
print(score)  #30


#실습 1.
temp=25
print(temp)
name="센서A"
print(name)

#실습 2.
temperature=30
print(temperature)

#실습3.
my_number=55
print(my_number)
mood="행운"
print(mood)

#실습4.
age=27
label="나이"
print(label)
print(age)

#실습5.
x=10
print(x)
x=x+5
print(x)
x=x*2
print(x)

#실습6.
a=100
b=a
a=999
print(a)
print(b)

#실습7.
print(temp)
temp=25
print(temp)
score=90
#print(Score)         #NameError: name 'Score' is not defined. Did you mean: 'score'?
score=90
print(score)

#실습8.
temp=25 #온도
count=3 #센서 개수
#print(temp)
print(count)

#실습9.
x=5
x=10
x=x+1
print(x)

#실습10.
title="포항"
name="장한샘"
temp=27
print(title, name, temp)

#실습11.
a=25
b=3
device_temp=25
seosor_temp=3
print(device_temp)

#실습12.
x, y, z = 1,2,3
width, height=4,3
print(x)
print(y)
print(z)
print(width)
print(height)
print(x, y, z)
print(width, height)