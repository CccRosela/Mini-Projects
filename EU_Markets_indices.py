import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/markets/currencies/"
response = requests.get(url, headers = {'User-agent': 'your bot 0.1'})

soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find("table", class_="yf-i6qrb2 bd")

column_names = []

# Finding hadings (sorrounded by <th> tags)
unedited_titles = table.find_all('th')

for titles in unedited_titles:
    column_names.append(titles.text.strip())


df = pd.DataFrame(columns = column_names)

# Finding rows (surrounded by <tr> tags)
unedited_rows = table.find_all('tr')

for row in unedited_rows[1:]:  # Skip the header row
    row_data = row.find_all('td')
    individual_data = [data.text.strip() for data in row_data]
    df.loc[len(df)] = individual_data


print(df)