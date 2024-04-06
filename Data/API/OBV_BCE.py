from key import *

url = f'https://www.alphavantage.co/query?function=OBV&symbol=BCE.TO&interval=daily&apikey={api_key}'
r = requests.get(url)
data = r.json().get("Technical Analysis: OBV", {})

df_OBV = pd.DataFrame([
    {"date": date, "value": float(data[date]["OBV"])}
    for date in data
])

df_OBV['date'] = pd.to_datetime(df_OBV['date'])

df_OBV = df_OBV.sort_values(by='date')
yesterday = datetime.now() - timedelta(days=1)
yesterday_str = yesterday.strftime('%Y-%m-%d')
filtered_df = df_OBV[df_OBV['date'] < yesterday_str]
all_dates = pd.date_range(start=filtered_df['date'].min(), end=yesterday, freq='D')
all_dates_df = pd.DataFrame({'date': all_dates})
merged_df = pd.merge(all_dates_df, df_OBV, on='date', how='left')
merged_df['value'] = merged_df['value'].fillna(method='ffill')

script_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.dirname(script_directory)
output_file = os.path.join(project_directory, "CSV", "OBV_BCE.csv")
merged_df.to_csv(output_file, index=False)