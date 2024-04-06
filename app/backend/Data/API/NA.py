from key import *

symbol = "NA.TO"
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={api_key}'
r = requests.get(url)
data = r.json().get("Time Series (Daily)", {})

df_NATO = pd.DataFrame([
    {"date": date, "value": float(data[date]["2. high"])}
    for date in data
])

df_NATO['date'] = pd.to_datetime(df_NATO['date'])

df_NATO = df_NATO.sort_values(by='date')
yesterday = datetime.now() - timedelta(days=1)
yesterday_str = yesterday.strftime('%Y-%m-%d')
filtered_df = df_NATO[df_NATO['date'] < yesterday_str]
all_dates = pd.date_range(start=filtered_df['date'].min(), end=yesterday, freq='D')
all_dates_df = pd.DataFrame({'date': all_dates})
merged_df = pd.merge(all_dates_df, df_NATO, on='date', how='left')
merged_df['value'] = merged_df['value'].fillna(method='ffill')

script_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.dirname(script_directory)
output_file = os.path.join(project_directory, "CSV", "NA_TO.csv")
merged_df.to_csv(output_file, index=False)