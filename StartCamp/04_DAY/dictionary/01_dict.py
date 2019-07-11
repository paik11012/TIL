lunch1 = {
        '중국집' : '02'
} #방법1

lunch1['중국집'] # 02 밸류값이 나옴
lunch1['분식집'] = '031' #분식집이라는 키 값과 '031'이라는 밸류값 추가됨, {}내에 []로 딕셔너리 추가하기
print(lunch1)


#방법2
lunch2 = dict(중국집='02')
print(lunch2)

for key in lunch1 :
    print(key, lunch1[key])   #예상: 중국집, 분식집?!!!!!  lunch1[key]=02

#value만 가져오기
for value in lunch1.values() : 
    print(value)
    
#key만 가져오기
for key in lunch1.keys() : 
    
    print(key)

#. items() => key value 가져오기
for key, value in lunch1.items() : 
    print(lunch1.items())
    print(key, value) #두개 다 같은 방법




#딕셔너리 내용 가져오기

idol = {
    'bts' : {
        '지민' : 24,
        'RM' : 25   #앞이 key, 뒤가 value  {key{key,value}}
    }
}
print(idol['bts']['RM'])

