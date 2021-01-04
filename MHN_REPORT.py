#오늘부터 N일까지의 기사를 가져오는 프로그램

import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta

url = 'https://www.mhns.co.kr/member/login.php' # 로그인 endpoint

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

dates = []

n = int(input('오늘부터 며칠 내의 기사를 가져올까요?: '))

for i in range(n):
    dates.append(str(date.today()+timedelta(days=i)))

table_row = list(soup.select('.table-row'))
list_tag = []

for i in table_row:
    test = i.select_one('.list-dated').get_text()
    for j in range(3):
        if test.find(dates[j]) != -1:
            list_tag.append(i)

res = [[] for i in range(len(list_tag))]

for k in range(len(list_tag)):
    res[k].append(list_tag[k].select_one('.list-section'))
    res[k].append(list_tag[k].find('strong'))
    print(res[k][0].get_text(), res[k][1].get_text())


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
