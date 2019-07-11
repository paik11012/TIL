# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}
#1
totalscore = 0
for sscore in score.values():
    totalscore += sscore
ascore=totalscore/len(score)
print(ascore)
#2
a = sum(score.values())
print(a/len(score))


# 2. 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}
#여섯 개 더하고 나누기 6
totalscore = 0
count = 0
for personscore in scores.values():          #각 딕셔너리 접근->a와 b의 밸류들
    totalscore += sum(personscore.values())  #또 딕셔너리 속 벨류 접근
    count += len(personscore)
ascore = totalscore / count
print(ascore) 
#어떤 식으로 그 값에 접근하는가?



# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?
# 한 번 for문 돌 때 key, value 두 개 꺼내오기
# 1 
for key, value in city.items():      #value, values 차이?
    atemp = sum(value) / len(value)
    print(f'{key} : {atemp:1f}')   #소숫점 자르겠다
    #혹은 round()이용

# 2 print('서울:',sum(city['서울'])/len(city['서울']))
#   print('대전:',sum(city['대전'])/len(city['대전']))
#   print('광주:',sum(city['광주'])/len(city['대전']))
#   print('부산:',sum(city['부산'])/len(city['대전']))
# 출력 예시) 서울 : 값

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
#각 줄을 비교하며 돌아다니다가 가장 높은 정보 저장 (서울:5 -> 광주:10)
count = 0
for name,temp in city.items():
    if count == 0:
        hott = max(temp)
        colt = min(temp)
        hotcity = name
        coldcity = name
    else:
        # 최저 온도가 cold_temp 보다 낮으면, cold_temp 에 값을 새로 넣고,
        if min(temp) < colt:
            colt = min(temp)
            coldcity = name
        # 최고 온도가 hot_temp 보다 높으면, hot_temp 에 값을 새로 넣는다.
        if max(temp) > hott:
            hott = max(temp)
            hotcity = name
    count += 1
print(f'최고로 더웠던 지역은 {hotcity} {hott} 였고, 최고로 추웠던 지역은 {coldcity} {colt} 였다.')


# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
if >= 2 in city['서울']:
    print('네')
else:
    print('아니오')