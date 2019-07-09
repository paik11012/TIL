#change ss.txt 0 1 2 3 4 ... into 4 3 2 1...
#read file line by line
with open('ss.txt','r') as f: #context manager
    lines = f.readlines() #read each lines by "list" type
        #print(lines)

lines.reverse() #reverse list

with open ('reversed_ss.txt','w') as f:
    for line in lines:
        f.write(line)

#print(lines) ok but there are num\n
