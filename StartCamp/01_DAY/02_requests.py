import requests
import bs4 #beautiful soup
#요청
url  = 'https://finance.naver.com/sise'

response = requests.get(url)

html = response.text
# url을 텍스트로 변환
soup = bs4.BeautifulSoup(html, 'html.parser')
kospi = soup.select_one('#KOSPI_now').text
# soup중에서 하나 불러오기/parser했기에 가능
print(kospi)

