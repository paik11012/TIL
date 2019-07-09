f = open('ss.txt','r')
all_text = f.read() #read whole text
print(all_text)
f.close()

with open('with_ss.txt','r') as f:
    all_text = f.read()
    print(all_text)

#open file as 'with'

with open('with_ss.txt','r') as f:
    lines = f.readlines()
    #print line by line
    for line in lines:
        print(line.strip())
    #print already has empty lines, so delete empty lines by .strip()
    

