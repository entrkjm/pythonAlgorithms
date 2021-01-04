import requests
from bs4 import BeautifulSoup

# 로그인 endpoint

url = 'https://www.mhns.co.kr/member/login.php'

data = {
    'user_id': 'entrkjm',
    'user_pw': '!1qaz@2wsx'
}

s = requests.Session()

resp = s.post(url, data=data)

# 여기서 S 객체에 다시 한번 GET을 사용
my_page = 'http://www.mhns.co.kr/news/userWriterArticleList.html'
resp = s.get(my_page)

soup = BeautifulSoup(resp.text, features='lxml')

date =  '2020-'+ input('날짜 입력: ')
table_row = list(soup.select('.table-row'))
list_tag = []

for i in table_row:
    test = i.select_one('.list-dated').get_text()
    if test.find(date) != -1:
        list_tag.append(i)

res = [[] for i in range(len(list_tag))]

for j in range(len(list_tag)):
    res[j].append(list_tag[j].select_one('.list-section'))
    res[j].append(list_tag[j].find('strong'))
    print(res[j][0].get_text(), res[j][1].get_text())

# Dummy Test Codes:
# for j in list_tag:
#     print(j.find('strong').get_text(), j.select('list-section').get_text())
# a_tag = list(soup.select('.links'))
# small_tag = list(soup.select('.list-section'))
# result1 = []
# result2 = []

# for i in a_tag:
#     result2.append(i.find('strong').get_text())

# for j in small_tag:
#     result1.append(j.get_text())

# for k in range(len(result1)):
#     print(result1[k] + result2[k])
