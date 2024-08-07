coffee01 = ('아메리카노', '카페라떼')
coffee02 = ('콜드브루', '아이스커피')

# 요소들을 콤마로 연결하면, tuple으로 인식합니다.
coffee03 = '카푸치노', '마키야또'

mytuple = coffee01 * 3
print(mytuple)

mylist = ['바닐라라떼', '플랫화이트']
coffee04 = tuple(mylist)  # 리스트를 튜플로 변환


# ('에스프레소')는 문자열 변수 이고,
# ('에스프레소',)는 끝에 ','이 붙어서 튜플로 인식 된다.
coffees = coffee01 + coffee02 + coffee03 + coffee04 + ('에스프레소',)
length = len(coffees)
print('요소 개수 : %d' % length)
print(type(coffees))
print(coffees)

#

# 튜플은 일단 설정이 되면 편집이 불가능하다 = 불변성을 가지는 튜플은 값을 할당할 수 없습니다.
# coffees[1] = '우유' = 카페라떼에서 우유로 값을 변경하려 하지만 불가능하다. = 불변성


# 인덱싱과 슬라이싱
print('3번 요소 : %s' % coffees[3])
print('뒤에서 2번째 요소 : %s' % coffees[-2])

print('1번째부터 3번째까지의 요소들', end='')
print(coffees[1:4])

print('4번째 이후의 모든 요소들', end='')
print(coffees[4:])

print('3번째 요소까지 출력', end='')
print(coffees[:4])

mycount = coffees.count('아메리카노')
print(mycount)

myindex = coffees.index('콜드브루')
print(myindex)



# 튜플을 이용한 파이썬의 swap 기법
x, y = 3, 4
print('before x : %d, y : %d' % (x,y))

x, y = y, x
print('after x : %d, y : %d' % (x,y))























