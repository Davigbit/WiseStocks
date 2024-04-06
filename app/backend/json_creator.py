import json
import joblib

DATASET = {}

for column_name in ['NA', 'SU', 'BCE', 'IMO']:
    first_30_days = joblib.load(f'./pkls/first_30_days_{column_name}.pkl')
    yesterday_value = first_30_days[1]
    change = joblib.load(f'./pkls/todaychange_{column_name}.pkl')
    percentage_variation = change*100/yesterday_value
    dict = {'today_value': joblib.load(f'./pkls/todayvalue_{column_name}.pkl'),
            'today_change': percentage_variation}
    DATASET[f'{column_name}'] = dict
DATASET = json.dumps(DATASET)

with open('./jsons/dataset.json', 'w') as f:
    f.write(DATASET)