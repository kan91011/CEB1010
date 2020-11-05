import requests
import bs4
import csv
import io


url = 'https://www.104.com.tw/jobs/search/?ro=0&keyword=python&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&jobsource=2018indexpoc'
htmlFile = requests.get(url)
ObjSoup=bs4.BeautifulSoup(htmlFile.text,'lxml')
jobs = ObjSoup.find_all('article',class_='js-job-item')             #搜尋所有職缺

for job in jobs:
    print(job.find('a',class_="js-job-link").text)                  #職缺內容
    print(job.get('data-cust-name'))                                #公司名稱
    print(job.find('ul', class_='job-list-intro').find('li').text)  #地址
    print(job.find('span',class_='b-tag--default').text)            #薪資
    print(job.find('a').get('href'))                                #網址
    print('='*70)

print("====================================================以上事先抓取資料==========================================================")

import requests
import bs4
import csv

url = 'https://www.104.com.tw/jobs/search/?ro=0&keyword=python&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&jobsource=2018indexpoc'
htmlFile = requests.get(url)
ObjSoup = bs4.BeautifulSoup(htmlFile.text, 'lxml')
jobs = ObjSoup.find_all('article', class_='js-job-item')
fn = '104人力銀行職缺內容.csv'  # 取CSV檔名
columns_name = ['職缺內容', '公司名稱', '地址', '薪資', '網址']  # 第一欄的名稱
with open(fn, 'w', newline='', ) as csvFile:  # 定義CSV的寫入檔,並且每次寫入完會換下一行
    dictWriter = csv.DictWriter(csvFile, fieldnames=columns_name)  # 定義
    dictWriter.writeheader()

    for job in jobs:
        job_name = job.find('a', class_="js-job-link").text  # 職缺內容
        job_company = job.get('data-cust-name')  # 公司名稱
        job_loc = job.find('ul', class_='job-list-intro').find('li').text  # 地址
        job_pay = job.find('span', class_='b-tag--default').text
        job_url = job.find('a').get('href')  # 網址

        dictWriter.writerow({'職缺內容': job_name, '公司名稱': job_company,
                             '地址': job_loc, '薪資': job_pay, '網址': job_url})