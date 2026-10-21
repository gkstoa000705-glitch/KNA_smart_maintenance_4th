# 연산자
# 산술, 비교, 논리 연산자

# 산술 연산자
 # 형식 : +, - *, /, //, %, **

# 복합할당
# 형식 : score += 10 <-> score = scpre + 10
score = 100
score +=10
print(score)
# -=,*=, /=

#문자열 연산
#+, *가능
print("안녕"+"하세요")
print("센서"+"A")

#실습1
a, b = 17, 5
print("a+b=", a+b)
print("a-b=",a-b)
print("a*b=",a*b)
print("a/b=",a/b)
print("a//b=",a//b)
print("a%b=",a%b)
print("a**b=",a**b)

#실습2
#x=80
#y=91
#z=90
#print((x+y+z))/3
#side=7
#print(side**2)
#print(3*4*5)

#논리연산자
#and 모두 참이어야 함, or 하나만 참이어도 참, not 반대
print(True and False) # False
print(True or False)  # True
print(not True) # False

#실습3
a=10
b=5
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#실습4
temp=85
pressure=5
temp_ok = 60 <= temp <= 90
pressure_ok = 3 <= pressure <= 7
print(temp_ok)
print(pressure_ok)
print(temp_ok and pressure_ok)

#실습5
x=100
print(x)
x += 50
print(x)
x -= 30
print(x)
x += 5
print(x)

#실습6
전체=500
불량=30
불량률=불량/전체*100
print(불량률)
가동시간=21
전체시간=24
가동률=가동시간/전체시간*100
print(가동률)

#실습7
총가동분=500
시간= 총가동분 // 60
분= 총가동분 % 60
print(시간,"시간", 분,"분")