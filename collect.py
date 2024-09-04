from bs4 import BeautifulSoup
import pandas as pd
import os
d={'Title':[1,2],'Price':[3,4],'link':[1,2]}
for file in os.listdir('data'):
    with open(f'data/{file}') as f:
        html_doc=f.read()
        # pass
    soup = BeautifulSoup(html_doc,'html.parser')
    title = soup.find(class_='RfADt')
    d['Title'].append(title.text)
    price = soup.find(class_='ooOxS')
    d['Price'].append(price.text)
    a_tags = soup.find_all('a')
    Link = f'https:{a_tags[1].get('href')}'
    d['link'].append(Link)
df= pd.DataFrame(data=d)
df.to_csv('data.csv')