from key import *

url = f'https://www.alphavantage.co/query?function=ADX&symbol=NA.TO&interval=daily&time_period=14&apikey={api_key}'
r = requests.get(url)
data = r.json().get("Technical Analysis: ADX", {})

df_ADXNATO = pd.DataFrame([
    {"date": date, "value": float(data[date]["ADX"])}
    for date in data
])

df_ADXNATO['date'] = pd.to_datetime(df_ADXNATO['date'])

df_ADXNATO = df_ADXNATO.sort_values(by='date')
yesterday = datetime.now() - timedelta(days=1)
yesterday_str = yesterday.strftime('%Y-%m-%d')
filtered_df = df_ADXNATO[df_ADXNATO['date'] < yesterday_str]
all_dates = pd.date_range(start=filtered_df['date'].min(), end=yesterday, freq='D')
all_dates_df = pd.DataFrame({'date': all_dates})
merged_df = pd.merge(all_dates_df, df_ADXNATO, on='date', how='left')
merged_df['value'] = merged_df['value'].fillna(method='ffill')

script_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.dirname(script_directory)
output_file = os.path.join(project_directory, "CSV", "ADX_NA_TO.csv")
merged_df.to_csv(output_file, index=False)