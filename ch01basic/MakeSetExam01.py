# set은 파이썬의 내장 되어 있는 함수.
coffees = set()  # empty set(집합)

coffees.add('아메리카노')
coffees.add(100)
coffees.add(True)
coffees.add('아메리카노')

print(len(coffees))

coffees.clear()

coffees.add('아메리카노')
coffees.add('에스프레소')
coffees.add('믹스커피')
coffees.add('카페라떼')

#

# 대괄호 = List
# newItem = 3가지를 모두 입력한다.
# 집합은 순서를 따지지 않는다. 그래서 인덱싱, 슬라이싱 불가능하다.

targetItem = '카푸치노'
bool = targetItem in coffees
print('%s 존재 여부 : %s' % (targetItem, bool))

targetItem = '마키야또'
if not targetItem in coffees:
    coffees.add(targetItem)

targetItem = '믹스커피'
coffees.remove(targetItem)

try:
    targetItem = '바닐라라떼'
    coffees.remove(targetItem)
except KeyError:
    print('%s는 목록에 존재하지 않습니다.' % targetItem)

print('반복문을 사용한 출력')
for element in coffees:
    print(element)



# 집합

coffee01 = set(['고구마라떼', '에스프레소', '아메리카노', '마키야또'])
coffee02 = set(['아메리카노', '마키야또', '카페라떼', '디카페인커피'])


# 두 가지 구문은 같다.   - 합집합
union_set = coffee01.union(coffee02)
print('합집합01: %s' % union_set)

union_set = coffee01 | coffee02
print('합집합02: %s' % union_set)
#


# 두 가지 구문은 같다.   - 교집합
intersection_set = coffee01.intersection(coffee02)
print('교집합01 : %s' % intersection_set)

intersection_set = coffee01 & coffee02
print('교집합02 : %s' % intersection_set)
#



# 세 가지 구문은 같다.     - 차집합
difference_set_01 = coffee01 - coffee02
print('차집합 A-B : %s' % difference_set_01)

difference_set_01 = coffee01.difference(coffee02)
print('차집합 A-B : %s' % difference_set_01)

difference_set_02 = coffee02.difference(coffee01)
print('차집합 B-A : %s' % difference_set_02)
#


# 차집합들의 합집합
symmetric_difference_set = coffee01.symmetric_difference(coffee02)
print('차집합들의 합집합 : %s' % symmetric_difference_set)

super_set = set(['고구마라떼', '에스프레소', '아메리카노', '마키야또'])
sub_set_01 = set(['고구마라떼', '에스프레소'])
sub_set_02 = set(['바닐라라떼', '마키야또'])

boolTest = sub_set_01.issubset(super_set)
if boolTest :
    print('집합01은 슈퍼 집합의 부분 집합입니다.')
else:
    print('집합01은 슈퍼집합의 부분 집합이 아닙니다.')

boolTest = super_set.issubset(sub_set_02)
if boolTest:
    print('super_set은 sub_set_02의 상위 집합입니다.')
else:
    print('super_set은 sub_set_02의 상위 집합이 아닙니다.')

