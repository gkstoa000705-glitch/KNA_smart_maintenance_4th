# 셋 - 중복 자동제거, 순서없음
# 형식 : {값1, 값2} or set(리스트)
# - 빈 셋 set()
#logs = ["S01", "S02", "S01", "S03"]
#unique_logs = set(logs)
#print(unique_logs)
#print(sorted(unique_logs))

#add - 값 추가
#alerts = {"S01", "s02"}
#alerts.add("S03")
#print(alerts)
#alerts.add("S02")
#print(alerts)
#print("S02" in alerts)

#실습4
#sensor = ["S02", "S01", "S03", "S02", "S01"]
#unique = set = (sensor)
#print(sorted(unique))
#print("종류 수:", len(unique))

# 집합 연산 - union(전체) / intersection(공통) / difference(차이)
#line_a = {"S01", "S02", "S03"}
#line_b = {"S03", "S04"}
#print(line_a.union(line_b))
#print(line_a.intersection(line_b))
#print(line_a.difference(line_b))

#실습 5
#line_a = {"S01", "S02", "S03", "S05"}
#line_b = {"S03", "S04", "S05"}
#sensor_a = line_a.union(line_b)
#sensor_b = line_a.intersection(line_b)
#a_only = line_a.difference(line_b)
#b_only = line_b.difference(line_a)
#print("공통:", sensor_a)
#print("A만:", a_only)
#print("B만:", b_only)

#실습 6
yesterday = {"S01", "S02", "S03"}
today = {"S02", "S03", "S05"}
error = today.difference(yesterday)
errors = today.intersection(yesterday)
print("신규이상:", error)
print("지속이상:", errors)