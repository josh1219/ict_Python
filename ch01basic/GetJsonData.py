filename = 'jumsu.json'

# 'rt'는 텍스트 모드로 읽어 들이겠습니다.
myfile = open(filename, mode='rt', encoding='UTF-8')
mystring = myfile.read()
print(type(mystring))  # 파이썬은 타입을 무조건 써줘야한다. (type)
myfile.close()

#

import json

jsonData = json.loads(mystring)
print(type(jsonData))

humanList = list()  # 전체 결과를 저장할 리스트

# 리스트 타입이기 때문에 for문장 사용가능하다.
for human in jsonData:
    # jumsu.json파일에서 정보를 가져온다.
    name = human['name']
    print('이름 : %s' % name)

    kor = float(human['kor'])
    eng = float(human['eng'])
    math = float(human['math'])

    total = kor + eng + math

# upper메소드 모든 문자를 대문자로 인식한다.
    _gender = human['gender'].upper()
    if _gender == 'M':
        gender = '남자'
    else:
        gender = '여자'

# print(type(human)) 은 human의 타입을 알아보는 것.
    print(type(human))
    if 'hello' in human.keys():
        message = human['hello']
        print('메시지 : ', message)
    # end if

    mytuple = (name, kor, eng, math, total, gender)
    humanList.append(mytuple)
# end for

print(humanList)
