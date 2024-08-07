# while 구문은 특정 조건이 참일 때 계속해서 반복 실행하기 위해 사용한다.
import random

answer = random.randint(1, 100)
print('정답 : %d' % answer)

counter = 0 # 카운터 변수

while True:
    su = int(input('1부터 100사이의 정수 1개 입력 : '))

    counter += 1

    if answer > su:
        print('%d보다 큰 수를 입력해 주세요.' % su)

    elif answer < su:  # 자바에서 else if가 파이썬에서는 elif로 사용 된다.
        print('%d보다 작은 수를 입력해 주세요.' % su)

    else:
        print('정답을 맞추 셨군요')
        break
    # end if
# end while

print('%d번만에 맞추 었습니다.' % counter)