#  자료형

count = 3      #int 정수
temp = 25.5    #float 실수
name = "센서A"  #str 문자열

ok = True      #bool 불린형 - 참/거짓
no = False     

# type()-> 자료형을 알려줌
print(type(25))              #<class 'int'>
print(type("센서A"))          #<class 'str'>
print(type(ok))              #<class 'bool'> 

# 자료형마다 다른 동작
print("3"+"5")  
print(3+5)

#실습1
count = 10    #정수(int)
temp = 25.5   #실수(float)
name = "센서A" #문자열(str)
is_ok = True #불린(bool)
print(count)
print(temp)
print(name)
print(is_ok)

#실습2
print(type(count))
print(type(temp))
print(type(name))
print(type(is_ok))

#실습3
#100의 자료형 예측 : 
#100.0의 자료형 예측 : 
#"100" 의 자료형 예측 : 
print(type(100))
print(type(100.0))
print(type("100"))

#실습4
print(5 + 5)
print("5" + "5")
print("10" + "10")
print(5 + 5)
print("5" + "5")

#실습5
print(3 > 2) #3은 2보다 크다
print(5 == 5) #5는 5와 같다
print(type(3 > 2))

#실습6
number=10
print(type(number)) #정수 변수를 선언하고 자료형 출력
number=10.0
print(type(number)) #정수를 실수로 재할당하여 자료형 출력
number="10"
print(type(number)) #숫자를 글자로 재할당하여 자료형 출력

#실습7
device_temp = 25.5
check_count =3
device_name = "센서A"
is_normal = True
print(device_temp)
print(check_count)
print(device_name)
print(is_normal)

#