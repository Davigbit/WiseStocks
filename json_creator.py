import json
import joblib
from functions import values_curve_7_days

DATASET = {}

for column_name in ['NA', 'SU', 'BCE', 'IMO']:
    X,Y = values_curve_7_days(column_name)
    first_30_days = joblib.load(f'./pkls/first_30_days_{column_name}.pkl')
    yesterday_value = first_30_days[1]
    change = joblib.load(f'./pkls/todaychange_{column_name}.pkl')
    percentage_variation = change*100/yesterday_value
    first_30_days.index = first_30_days.index.astype(str)
    days = first_30_days.index.tolist()
    first_30_days = first_30_days.to_list()
    X = X.astype(str)
    X = X.tolist()
    days, first_30_days, X, Y = days[::-1], first_30_days[::-1], X[::-1], Y[::-1]
    dict = {'thirty_days': [days, first_30_days],
            'seven_days': [X,Y],
            'today_value': joblib.load(f'./pkls/todayvalue_{column_name}.pkl'),
            'today_change': percentage_variation}
    DATASET[f'{column_name}'] = dict
DATASET = json.dumps(DATASET)

with open('./jsons/dataset.json', 'w') as f:
    f.write(DATASET)