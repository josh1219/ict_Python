# []기호가 나오면 무조건 리스트.
# coffes = [] # empty list
coffees = list()

# append는 원소 추가(가장 마지막에 새로 추가 되는 개념).
coffees.append('아메리카노')
coffees.append('콜드브루')
coffees.append('카푸치노')
coffees.append('바닐라라떼')
coffees.append('디카페인커피')
coffees.append('카페라떼')


# len은 요소의 개수를 구하는 것.
count = len(coffees)
print('요소 개수 : %d' % count)


# 인덱싱 = 특정한 인덱스를 찾아서 가져 오는 것.
print('앞에서 2번째 음료 : %s' % coffees[2])
print('뒤에서 1번째 음료 : %s' % coffees[-1])


# 슬라이싱 = 원하는 범위의 요소를 쉽게 가져올 수 있습니다.
print('전부 출력 : %s' % coffees[::])
print('1번째부터 3번째까지 음료 : %s' % coffees[1:4])
print('3번째부터 모든 음료 : %s' % coffees[3:])
print('맨 앞부터 2번째까지 음료 : %s' % coffees[:3])


# 체크박스 작성시 내용을 부정적으로 만들지 말것. (체크 한다는 것은 기본적으로 True(긍정의 의미)로 통용된다.)
# 내림차순 = desc,  오름차순 = asc
print('# 내림차순 정렬하기')
coffees.sort(reverse=True)
print(coffees)

import random
random.shuffle(coffees)
print(coffees)



