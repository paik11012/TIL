dinner = {
    '양자강': '02-557-4211', #차돌짬뽕
    '김밥카페': '02-553-3181',  #라돈
    '순남시래기': '02-508-0887' #보쌈정식
    }

   #make dictionary as for
   #print (dinner.keys) -> lists
   #print (dinner.values) ->numners
   #print(dinner.items()) ->bring both keys and values

# print (dinner.items())
#1. string formatting - make new csv file
with open('dinner.csv','w',encoding="utf-8") as f: #korean, encoding=utf-8
   for item in dinner.items(): #[('양자강', '02~')] key and value become first and second index
       f.write(f'{item[0]}, {item[1]}\n')
       #use f'{},{}' to write
   
#2. csv writer
import csv
with open('dinner.csv','w',encoding="utf-8", newline='') as f: #no empty lines
    csv_writer = csv.writer(f)
    #make new object to write csv in file f
    for item in dinner.items():
        csv_writer.writerow(item)


