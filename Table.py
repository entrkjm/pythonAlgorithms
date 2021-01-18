import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import date, timedelta

from bs4 import BeautifulSoup
import time


class tableCrawler:  # 편성표 크롤러 클래스를 만든다

    def __init__(self, chromedriver):  # 변수로 크롬드라이버 위치를 넣음
        self.chromedriver = chromedriver
        self.driver = webdriver.Chrome(self.chromedriver)

    def get_action(self, title_tag, time_tag, url):  # 프로그램 이름과 시간을 가져오는 메서드
        self.title_tag = title_tag
        self.time_tag = time_tag
        self.driver.get(url)

        time.sleep(3)

        src = self.driver.page_source
        soup = BeautifulSoup(src, features="lxml")

        # pagesource를 가져와서 soup에 넣는다.

        programName = soup.select(title_tag)
        programTime = soup.select(time_tag)

        return programName, programTime
    
    def mbc_get(self, url):  # 프로그램 이름과 시간을 가져오는 메서드
        self.title_tag = '.tit'
        self.time1 = '.time'
        self.time2 = '.time2'
        self.box = '.scd-list li'
        
        self.driver.get(url)

        time.sleep(3)

        src = self.driver.page_source
        soup = BeautifulSoup(src, features="lxml")

        # pagesource를 가져와서 soup에 넣는다.
        
        box_list = soup.select(self.box)
        programName = []
        programTime = []
        
        for i in box_list:
            if i.select_one(self.title_tag):
                programName.append(i.select_one(self.title_tag))
            
            if i.select_one(self.time1):
                programTime.append(i.select_one(self.time1))
                
            elif i.select_one(self.time2):
                programTime.append(i.select_one(self.time2))
        
        return programName, programTime

    def kbs_get(self, title_tag, time_tag, url, n):  # kbs 프로그램 이름과 시간을 가져오는 메서드
        self.title_tag = title_tag
        self.time_tag = time_tag

        list_tag = '.table-program-list'  # KBS는 dt/dd/ul/li 태그를 써서 편성표를 보여준다.

        self.driver.get(url)

        # pagesource를 가져와서 soup에 넣는다

        for l in range(n):
            today = str(date.today()+timedelta(days = l)).replace('2021-', '').replace('-','.')
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[contains(text(),{})]".format(today)).click() #KBS의 경우 이렇게 텍스트를 찾아 일일이 클릭해야한다.
            time.sleep(3)
            src = self.driver.page_source
            soup = BeautifulSoup(src, features="lxml")
            programTable = soup.select(list_tag)

            for i in range(2):
                print('KBS{} '.format(str(i+1)),str(date.today()+timedelta(days = l))," 편성표")
                programName = programTable[i].select(title_tag)
                programTime = programTable[i].select(time_tag)
                reboard_list = self.reboard_list3(soup,'.program-box') #reboard 메서드를 활용해 재방송인지 본방송인지 확인한다.
                for j in range(len(programName)):
                    res = programTime[j].get_text() + ' ' + programName[j].get_text().replace('\n', ' ') + ' ' + reboard_list[j]
                    print(res)
                print()
        print()


    def reboard_list(self, find_in, find_tag): #SBS용
        self.find_in = find_in
        self.find_tag = find_tag

        find_in_list = self.driver.find_elements_by_css_selector(self.find_in)
        result = []

        for i in find_in_list:
            if i.find_elements_by_css_selector(self.find_tag):
                result.append('재')
            else:
                result.append('본')

        return result

    def reboard_list2(self, find): #MBC용
        self.find = find
        find_list = self.driver.find_elements_by_css_selector(self.find)

        result = []

        for i in find_list:
            if i.text.find('스페셜') == -1 and i.text.find('재') == -1:
                result.append('본')
            else:
                result.append('재')

        return result
    
    def reboard_list3(self, soup, find_in): #KBS용
        find_in_list = soup.select(find_in) #self.driver.find_elements_by_css_selector(self.find_in)
        result = []

        for i in find_in_list:
            if i.find_all('span', attrs = {'title' : '재방송'}):
                result.append('재')
            else:
                result.append('본')
        return result

    def driver_close(self):
        self.driver.close()


# 실행 부분
dates = date.today()

# 오늘 날짜

Chromedriver = 'C:/Users/user/Downloads/chromedriver_win32/chromedriver'

n = int(input("가져올 날짜: "))

#SBS 편성표를 가져온다
sbs = tableCrawler(Chromedriver)
sbs_title_tag = '.spi_title'
sbs_time_tag = '.spt_hours'
sbs_find_in = '.spi_title_icons'
sbs_find_tag = '.scheduler_label_w_type_rerun'

for j in range(n):
    print('SBS ',str(dates+timedelta(days=j)), " 편성표")
    sbs_url = 'https://www.sbs.co.kr/schedule/index.html?type=tv&channel=SBS&pmDate=2021{}'.format(str(dates+timedelta(days=j)).replace('2021','').replace('-', ''))
    sbs_programName, sbs_programTime = sbs.get_action(sbs_title_tag, sbs_time_tag, sbs_url)
    sbs_reboard = sbs.reboard_list(sbs_find_in, sbs_find_tag)

    for i in range(len(sbs_reboard)):
        print(sbs_programTime[i].text, sbs_programName[i].text, sbs_reboard[i])
    print()
sbs.driver_close()

#MBC 편성표를 가져온다

mbc = tableCrawler(Chromedriver)
mbc_find = '.tit'

for j in range(n):
    print('MBC ',str(dates+timedelta(days=j)), ' 편성표')
    mbc_url = 'http://schedule.imbc.com/?chcode=TV&date=2021{}&c=0'.format(str(dates+timedelta(days=j)).replace('2021','').replace('-', ''))
    mbc_programName, mbc_programTime = mbc.mbc_get(mbc_url)
    mbc_reboard = mbc.reboard_list2(mbc_find)
    
    for i in range(len(mbc_reboard)):
        print(mbc_programTime[i].text, mbc_programName[i].text, mbc_reboard[i])
    print()
    
mbc.driver_close()

# KBS 편성표를 가져온다

kbs_url = 'http://schedule.kbs.co.kr/index.html?sname=schedule&stype=table&type=globalList&search_day=2021{}'.format(str(dates).replace('2021','').replace('-', ''))
kbs = tableCrawler(Chromedriver)
kbs_title_tag = '.title'
kbs_time_tag = 'span.time'

kbs.kbs_get(kbs_title_tag, kbs_time_tag, kbs_url, n)
kbs.driver_close()

#EBS 편성표를 가져온다

ebs = tableCrawler(Chromedriver)
ebs_title_tag = '.tit strong'
ebs_time_tag = '.time > span'

for j in range(n):
    print('EBS ',str(dates+timedelta(days=j)), ' 편성표')
    ebs_url = 'https://www.ebs.co.kr/schedule?channelCd=tv&date=2021{}&onor=tv'.format(str(dates+timedelta(days=j)).replace('2021','').replace('-', ''))
    ebs_programName, ebs_programTime = ebs.get_action(ebs_title_tag, ebs_time_tag, ebs_url)

    for i in range(len(ebs_programTime)):
        print(ebs_programTime[i].text, ebs_programName[i].text)
    print()
ebs.driver_close()
