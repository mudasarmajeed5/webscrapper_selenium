from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
query = input('Enter what youre searching for')
page = int(input('How many pages you want to scrap?'))
fileNo=1
driver = webdriver.Edge()
for i in range(1,page):
    driver.get(f"https://www.daraz.pk/catalog/?page={page}&q={query}&spm=a2a0e.tm80335159.search.d_go")
    elems = driver.find_elements(By.CLASS_NAME,'Bm3ON')
    print(f'{len(elems)} items found')
    for elem in elems:
        d=elem.get_attribute('outerHTML')
        with open(f'data/{query}_{fileNo}.html', 'w',encoding='utf-8') as f:
            f.write(d)
            fileNo+=1
driver.close()