import os #500개 아무데나 안 생기고 그 폴더 내로 생기도록 만들기
os.chdir(r'C:\Users\student\TIL\StartCamp\02_DAY') 
#500지원서 있는 곳
filenames = os.listdir('.')
#파일들 다 가져오기/ 특정 경로에 있는 모든 파일 가져오기 /  .은 현재 디렉토리
for filename in filenames:
    #이상한 파일들 다 포함중, 끌에가 .txt인 파일만 골라오기
    splited = os.path.splitext(filename)[-1] 
    #확장자만 따로 분리 - splittext
    #0 처음 인덱스, -1마지막에 있는 인덱스로 접근 [0, -1]
    if splited == '.txt':
        print('이름을 바꾼다', filename)
    #이름 바꾸기 os.rename(이것을, 이것으로 바꾼다)
    
#        os.rename(filename, f'S_{filename}')

    ###함수 내 f. {} 넣으면 변수 넣기 가능 / txt파일 앞에 이름붙이기 가능


#os.chdir(r,'path') change directory
#os.listdir('path') get directory name
#os.rename(a,b) change names a into b

# ->MISSION "let's change s into SS"
# replace s in ss
# delete s and put ss
        os.rename(filename, filename.replace('S_','SS_'))