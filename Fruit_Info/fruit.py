from bs4 import BeautifulSoup
import requests

import pandas as pd
from pprintpp import pprint

url ="https://food-nutrition-facts.com/fruits/"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
### print(response.status_code)

table = soup.find('table', class_='w-full border border-green-100 rounded-xl overflow-hidden text-sm')

# Find headings/titles (surrounded by <th> tags)
unedited_table_titles = table.find_all('th')
# Get the text & store them in a list
table_titles = [word.text.strip() for word in unedited_table_titles]
### pprint(table_titles)

# Find the rows (surrounded by <tr> tags)
unedited_data = table.find_all('tr')

df = pd.DataFrame(columns = table_titles)

# the first row was an empty []
for row in unedited_data[1:]:
    # <td> tags surround the data
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    ### pprint(individual_row_data)

    # checking the length of the dataframe each loop iteration
    df.loc[len(df)] = individual_row_data

def get_df():
    return df

# Save the dataframe to a CSV file
# df.to_csv('fruit_nutrition.csv', index=False)
    
