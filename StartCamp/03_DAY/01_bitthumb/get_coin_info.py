import requests
import bs4
import csv

url = 'https://www.bithumb.com/' #1. get internet page
selector = '#tableAsset > tbody > tr'
html = requests.get(url).text #request and get respose from url, type: str
soup = bs4.BeautifulSoup(html, 'html.parser') #2. use bs4 and parse string typed html
#3 get table row data in list type
coins = soup.select('.coin_list tr') #<> lists # ' ' and '>'
#4 circuit each coin and get needed info
for coin in coins:
    #get coin name and price
    coinname = coin.select_one('td:nth-child(1) > p > a > strong').text
    coinprice = coin.select_one('td > strong').text #only strong in td
    print(coinname, coinprice)

#5 save info with using csv.writer
with open('coin.csv','w', encoding='utf-8', newline='') as f: #windows new line - no empty lines
    csv_writer = csv.writer(f)
    for coin in coins:
        coinname = coin.select_one('td:nth-child(1) > p > a > strong').text.strip().replace('NEW','')
        coinprice = coin.select_one('td > strong').text #only strong in td
        data = (coinname, coinprice)
        csv_writer.writerow(data)
        print(data)






# with open('coin.csv','w')as f:
# 	for coin in coins:
# 	 	btc=coin.select()
# print(btc)