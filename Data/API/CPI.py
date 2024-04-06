from key import *

url = f'https://www.alphavantage.co/query?function=CPI&interval=monthly&apikey={api_key}'
r = requests.get(url)
data = r.json()

df_CPI = pd.DataFrame(data["data"])

df_CPI['date'] = pd.to_datetime(df_CPI['date'])

df_CPI = df_CPI.sort_values(by='date')
yesterday = datetime.now() - timedelta(days=1)
yesterday_str = yesterday.strftime('%Y-%m-%d')
filtered_df = df_CPI[df_CPI['date'] < yesterday_str]
all_dates = pd.date_range(start=filtered_df['date'].min(), end=yesterday, freq='D')
all_dates_df = pd.DataFrame({'date': all_dates})
merged_df = pd.merge(all_dates_df, df_CPI, on='date', how='left')
merged_df['value'] = merged_df['value'].fillna(method='ffill')

script_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.dirname(script_directory)
output_file = os.path.join(project_directory, "CSV", "CPI.csv")
merged_df.to_csv(output_file, index=False)