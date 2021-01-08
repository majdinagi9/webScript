import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:/Users/majdinagi/Downloads/chromedriver_win32/chromedriver.exe")
driver.get('https://oxylabs.io/blog')
resualt = []
other_resualt = []
content = driver.page_source
soup = BeautifulSoup(content)

driver.quit()
for a in soup.findAll(attrs='blog-card__content-wrapper'):
    name = a.find('h2')
    if name not in resualt:
        resualt.append(name.text)
for b in soup.findAll(attrs='blog-card__date-wrapper'):
    date = b.find('p')
    if date not in resualt:
        other_resualt.append(date.text)
df = pd.DataFrame({'Name':resualt,'Datas':other_resualt})
df.to_csv('name.csv', index = False, encoding='utf-8')
