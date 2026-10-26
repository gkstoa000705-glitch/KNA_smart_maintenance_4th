# for 반복문
# for문 (range 이용한 반복)
# 형식 : for 변수 in range (횟수):
#for i in range(5):
#    print("안녕하세요")

#for i in range(5):
#    print(i)

#range (시작, 끝, 중간값)
#for i in range(1, 10, 2):
#    print(i)

# 실습 1
#N=5
#for i in range(1, N+1):
#    print(i)

#for i in range(2, N+1, 2):
#    print(i)

#for i in range(N, 0, -1):
#    print(i)

# 누적 변수 패턴(합계, 갯수, 평균)
#total = 0
#for i in range(1, 6):
#    total += i
#print("합계:", total)

# 조건 만족하는 경우 세기
#count = 0
#for i in range(1, 11):
#    if i > 5:
#        count += 1
#print("개수:", count)

# 평균
#total, count = 0, 0
#for i in range(1, 6):
#    total += i
#    count += 1
#if count > 0:
#    print("평균:", total/count)

# 실습 2
#N = 10
#total = 0
#for i in range(1,10+1):
#    total = total + i
#print("합:", total)

# enumerate :  순서 + 값을 함께 준다
#for dan in range(2,4):
#    for su in range(1, 4):
#        print(dan, "x", su, "=", dan * su)
#    print("---")


#실습 3
#for dan in range(2, 10):
#    for su in range(1 ,10):
#        print(dan, "x", su, "=", dan * su)
#    print("---")

# 실습 4
N = int(input("측정 횟수:"))
over_count = 0
for i in range(N):
    value = int(input("측정값:"))
    if value > 80:
        over_count +=1
print("초과 개수:",over_count)