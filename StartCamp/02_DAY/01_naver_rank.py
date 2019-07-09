import requests
import bs4 #beautiful soup
#요청
url  = 'https://www.naver.com/'

# response = requests.get(url)

# html = response.text
# # url을 텍스트로 변환
# soup = bs4.BeautifulSoup(html, 'html.parser')
# keywords = soup.select('.ah_l .ah_item .ah_a .ah_k')
# # soup중에서 불러오기/parser했기에 가능
# print(keywords)

selector = '.ah_l .ah_item .ah_a .ah_k'
html = requests.get(url).text
soup = bs4.BeautifulSoup(html, 'html.parser')
ranks = soup.select(selector)

for rank in ranks:
    print(rank.text)
# 왜 텍스트 두 번?