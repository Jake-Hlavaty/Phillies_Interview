import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display

pd.set_option("display.max_rows", None, "display.max_columns", None)
url = 'https://questionnaire-148920.appspot.com/swe/data.html'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1]
df['Salary'] = df['Salary'].str.replace(r'\D', '', regex=True)
nan_value = float("NaN")
df.replace("", nan_value, inplace=True)
df.dropna(subset=['Salary'], inplace=True)
df['Salary'] = df['Salary'].astype(int)
df = df.nlargest(125, 'Salary').reset_index()
df = df.drop('index', axis=1)
display(df)
print()
print("The average salary of top 125 players in 2016 was $", round(df['Salary'].mean(), 2))
sns.set()
sns.histplot(df.Salary, kde=True)
plt.show()
