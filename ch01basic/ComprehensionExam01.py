mylist01 = [idx for idx in range(1, 5)]
print(type(mylist01))
print(mylist01)

# 각 항목에 *10을 해준다.
mylist02 = [10 * idx for idx in range(1, 6)]
print(mylist02)

# 1부터 100까지 +3한다.
mylist03 = [idx for idx in range(1, 101, 3)]
print(mylist03)

# if idx%10 == 0을 이용하면 10의 배수만 구할 수 있다.
mylist04 = [idx for idx in range(1, 101, 3) if idx % 10 == 0]
print(mylist04)

# 60이상의 인덱스만 추출한다.
somedata = [75, 30, 85, 50]
mylist05 = [jumsu for jumsu in somedata if jumsu >= 60]
print(mylist05)

# 중첩for
mylist06 = [x * y for x in range(2, 10) for y in range(1, 10)]
print(mylist06)

# 튜플을 담고 있는 리스트
fruits = [('바나나', 10), ('사과', 20), ('오렌지', 30)]

for item in fruits:
    print(item[0])
    print(item[1])

mydict01 = {item[0]: item[1] for item in fruits}
print(mydict01)

students = [
    ('이문식', 80, 90, 50),
    ('강수현', 50, 60, 80),
    ('윤정혁', 70, 40, 60),
]
mydict02 = {human[0]: human[1] for human in students}
print(mydict02)

# sum은 파이썬 내장 함수
# human[1:]로 1번부터 모두 다 가져온다.
mydict03 = {human[0]:sum(human[1:]) for human in students}
print(mydict03)

# type, len, sum, tuple, list, set, dict 등은 파이썬의 내장 함수.
