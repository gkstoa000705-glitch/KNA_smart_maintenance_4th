# 조건문 
# if 기본 구조 - 콜론과 들여쓰기(코드 블록)
# 형식 :
# if 조건식 : 
#   실행할 고드(들여쓰기)
#temp = 80
#if temp > 80:            # 콜론 : 블록 시작 신호
#    print("온도 주의")    # 들여쓰기 안 -> 조건 참일 때만 실행
#    print("점검 요망")    
#print("측정 종료")        # 들여쓰기 끝 - > 조건과 무관하게 항상 실행

# else - 조건이 거짓일 때 
# 형식 :
# if 조건문:
#   참일 때 코드
# else:
#   거짓일 때 코드

#score = 55
#if score >= 60:
#    print("합격")
#else:
#    print("불합격")

# 실습 1
#age = 18
#if age >= 19:
#    print("성인입니다")
#else:
#    print("미성년자입니다")

#    age = 19
#if age >= 19:
#    print("성인입니다")
#else:
#    print("미성년자입니다")

# 실습 2
#score = 90
#if score >= 90:
#    print("A")
#elif score >= 80:
#    print("B")
#elif score >= 70:
#    print("C")
#else:
#    print("F")

#score = 85
#if score >= 90:
#    print("A")
#elif score >= 80:
#    print("B")
#elif score >= 70:
#    print("C")
#else:
#    print("F")

#score = 70
#if score >= 90:
#    print("A")
#elif score >= 80:
#    print("B")
#elif score >= 70:
#    print("C")
#else:
#   print("F")

#score = 69
#if score >= 90:
#    print("A")
#elif score >= 80:
#    print("B")
#elif score >= 70:
#    print("C")
#else:
#    print("F")

# 실습 3
#temp = 85
#if temp > 80:
#    print("위험")
#elif temp > 60:
#    print("주의")
#else:
#    print("정상")

#temp = 70
#if temp > 80:
#    print("위험")
#elif temp > 60:
#    print("주의")
#else:
#    print("정상")

#temp = 50
#if temp > 80:
#    print("위험")
#elif temp > 60:
#    print("주의")
#else:
#    print("정상")

#실습 4
id = "admin"
password = "1234"
user_id = "admin"
user_password = "1234"
if user_id == id and user_password == password:
    print("로그인 성공")
else:
    print("로그인 실패")