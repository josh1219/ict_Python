# SungJukTest.py
def sungjukInfo(name, kor, eng=50, math=60):
    #영어와 수학은 입력값이 없으면 위에 기본값으로 적용된다.
    total = kor + eng + math
    average = total / 3.0

    if average >= 70.0:
        passOrFail = '합격'
    else:
        passOrFail = '불합격'

    print('%s 학생의 정보')
    print('국어 : %d, 영어 : %d, 수학 : %d' % (kor, eng, math))
    print('총점 : %d, 평균 : %.2f, 합격 여부 : %s' % (total, average, passOrFail))


# end def

# 파이썬에서는 매개변수에 디폴트값을 줄 수 있다.
name, kor, eng, math = '김철수', 50, 60, 70
sungjukInfo(name, kor, eng, math)  # positional argument
sungjukInfo('박영희', 80)  # positional argument

sungjukInfo(math=30, eng=90, name='심현철', kor=100) # keyword argument

sungjukInfo('권유정', 50, math=70) # 혼합 형태


# @@@@@
# 포지셔널과 키워드를 같이 쓸수 있지만, 반드시 포지셔널이 앞에 와야 한다.