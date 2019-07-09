#open(what,mode) mode: read, write-overwrite, append 
f = open('ss.txt','w')
for i in range(10):
    f.write(f'this is line {i + 1}\n') #0~9 to 1~10, f is  line  select
f.close() 
#after opening files, they should be closed, open and close are pair

with open('with_ss.txt', 'w') as f: 
#context manager, make code blocks
#name the files f which are opened as with
    for i in range(10):
        f.write(f'this is line{i+1}\n')
        #this closes automatically when the contexts are finishted

#write many lines at once
with open('ss.txt','w',encoding='utf-8') as f:
    f.writelines(['0\n','1\n','2\n','3\n','4\n','5\n','6\n','7\n','8\n'])
