# for문 사용시 초기식, 조건식, 증감식.
# 아래에서는 초기식=1, 조건식=11, 증감식=1이 된다,
# 증감식에서 1증감은 기본이라서 적지 않아도 무방하다.   ex)(1,11,1) = (1,11) 두 가지는 동일하다.
total = 0

for i in range(1, 11):
    total += i
# end for

print('총합 01 : %d' % total)



#


total = 0

for i in range(1, 101, 3):
    total += i
    # end for

    print('총합 02 : %d' % total)

#




# 97+92+87+…+7+2 = 990
total = 0
for i in range(97, 1, -5):
    total += i

    print('총합 03 : %d' % total)



#
# 1*1 + 6*6 + 11*11 + … + 96*96 = 63670
total = 0
for i in range(1, 96 + 1, 5):
    total += i ** 2

    print('총합04 : %d' % total)


    #


    # 1 * 2 + 2 * 3 + 3 * 4 + 4 * 5 + 5 * 6 = 70
    total = 0
    for i in range(1, 1 + 5):
        total += i * (i + 1)

        print('총합05 : %d' % total)
