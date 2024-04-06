from key import *

url = f'https://www.alphavantage.co/query?function=CCI&symbol=SU.TO&interval=daily&time_period=10&apikey={api_key}'
r = requests.get(url)
data = r.json().get("Technical Analysis: CCI", {})

df_CCI = pd.DataFrame([
    {"date": date, "value": float(data[date]["CCI"])}
    for date in data
])

df_CCI['date'] = pd.to_datetime(df_CCI['date'])

df_CCI = df_CCI.sort_values(by='date')
yesterday = datetime.now() - timedelta(days=1)
yesterday_str = yesterday.strftime('%Y-%m-%d')
filtered_df = df_CCI[df_CCI['date'] < yesterday_str]
all_dates = pd.date_range(start=filtered_df['date'].min(), end=yesterday, freq='D')
all_dates_df = pd.DataFrame({'date': all_dates})
merged_df = pd.merge(all_dates_df, df_CCI, on='date', how='left')
merged_df['value'] = merged_df['value'].fillna(method='ffill')

script_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.dirname(script_directory)
output_file = os.path.join(project_directory, "CSV", "CCI_SU.csv")
merged_df.to_csv(output_file, index=False)