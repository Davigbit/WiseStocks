import pandas as pd
import joblib

files = ["CCI_NA_TO.csv", "CCI_SU.csv", "CCI_BCE.csv", "CCI_IMO.csv", "CPI.csv", "Interests.csv", "NA_TO.csv", "Natural Gas.csv",
         "S&P 500.csv", "USD_to_CAD.csv", "WTI.csv", "SU.csv", "BCE.csv", "IMO.csv",
         "ADX_NA_TO.csv", "OBV_NA_TO.csv", "SMA_NA_TO.csv", "EMA_NA_TO.csv",
         "ADX_SU.csv", "OBV_SU.csv", "SMA_SU.csv", "EMA_SU.csv",
         "ADX_BCE.csv", "OBV_BCE.csv", "SMA_BCE.csv", "EMA_BCE.csv",
         "ADX_IMO.csv", "OBV_IMO.csv", "SMA_IMO.csv", "EMA_IMO.csv"]
DIC = {}

for file in files:
    df_name = f'df_{file.replace(" ", "_").replace(".", "_")}'
    DIC[df_name] = pd.read_csv(f'./Data/CSV/{file}')
    DIC[df_name] = DIC[df_name].iloc[::-1]
    DIC[df_name]['date'] = pd.to_datetime(DIC[df_name]['date'])
    DIC[df_name] = DIC[df_name].drop(DIC[df_name][DIC[df_name]['date'] <= "2005-02-04"].index)
    DIC[df_name] = DIC[df_name].dropna()
    DIC[df_name] = DIC[df_name].reset_index(drop=True)


DIC['df_CCI_NA_TO_csv'] = DIC['df_CCI_NA_TO_csv'].rename(columns={'date': 'Date', 'value': 'CCI NA.TO'})
DIC['df_CCI_SU_csv'] = DIC['df_CCI_SU_csv'].rename(columns={'date': 'Date', 'value': 'CCI SU'})
DIC['df_CCI_BCE_csv'] = DIC['df_CCI_BCE_csv'].rename(columns={'date': 'Date', 'value': 'CCI BCE'})
DIC['df_CCI_IMO_csv'] = DIC['df_CCI_IMO_csv'].rename(columns={'date': 'Date', 'value': 'CCI IMO'})
DIC['df_CPI_csv'] = DIC['df_CPI_csv'].rename(columns={'value': 'CPI'})
DIC['df_Interests_csv'] = DIC['df_Interests_csv'].rename(columns={'value': 'Interests'})
DIC['df_NA_TO_csv'] = DIC['df_NA_TO_csv'].rename(columns={'value': 'NA', 'change': 'NA Change'})
DIC['df_Natural_Gas_csv'] = DIC['df_Natural_Gas_csv'].rename(columns={'value': 'Natural Gas'})
DIC['df_S&P_500_csv'] = DIC['df_S&P_500_csv'].rename(columns={'value': 'S&P 500'})
DIC['df_USD_to_CAD_csv'] = DIC['df_USD_to_CAD_csv'].rename(columns={'value': 'USD to CAD'})
DIC['df_WTI_csv'] = DIC['df_WTI_csv'].rename(columns={'value': 'WTI'})
DIC['df_EMA_NA_TO_csv'] = DIC['df_EMA_NA_TO_csv'].rename(columns={'value': 'EMA NA.TO'})
DIC['df_SMA_NA_TO_csv'] = DIC['df_SMA_NA_TO_csv'].rename(columns={'value': 'SMA NA.TO'})
DIC['df_ADX_NA_TO_csv'] = DIC['df_ADX_NA_TO_csv'].rename(columns={'value': 'ADX NA.TO'})
DIC['df_OBV_NA_TO_csv'] = DIC['df_OBV_NA_TO_csv'].rename(columns={'value': 'OBV NA.TO'})
DIC['df_EMA_SU_csv'] = DIC['df_EMA_SU_csv'].rename(columns={'value': 'EMA SU'})
DIC['df_SMA_SU_csv'] = DIC['df_SMA_SU_csv'].rename(columns={'value': 'SMA SU'})
DIC['df_ADX_SU_csv'] = DIC['df_ADX_SU_csv'].rename(columns={'value': 'ADX SU'})
DIC['df_OBV_SU_csv'] = DIC['df_OBV_SU_csv'].rename(columns={'value': 'OBV SU'})
DIC['df_EMA_BCE_csv'] = DIC['df_EMA_BCE_csv'].rename(columns={'value': 'EMA BCE'})
DIC['df_SMA_BCE_csv'] = DIC['df_SMA_BCE_csv'].rename(columns={'value': 'SMA BCE'})
DIC['df_ADX_BCE_csv'] = DIC['df_ADX_BCE_csv'].rename(columns={'value': 'ADX BCE'})
DIC['df_OBV_BCE_csv'] = DIC['df_OBV_BCE_csv'].rename(columns={'value': 'OBV BCE'})
DIC['df_EMA_IMO_csv'] = DIC['df_EMA_IMO_csv'].rename(columns={'value': 'EMA IMO'})
DIC['df_SMA_IMO_csv'] = DIC['df_SMA_IMO_csv'].rename(columns={'value': 'SMA IMO'})  
DIC['df_ADX_IMO_csv'] = DIC['df_ADX_IMO_csv'].rename(columns={'value': 'ADX IMO'})
DIC['df_OBV_IMO_csv'] = DIC['df_OBV_IMO_csv'].rename(columns={'value': 'OBV IMO'})
DIC['df_SU_csv'] = DIC['df_SU_csv'].rename(columns={'value': 'SU'})
DIC['df_BCE_csv'] = DIC['df_BCE_csv'].rename(columns={'value': 'BCE'})
DIC['df_IMO_csv'] = DIC['df_IMO_csv'].rename(columns={'value': 'IMO'})

#NA.TO Data

df_linear = pd.concat([DIC['df_CCI_NA_TO_csv']['Date'], DIC['df_CCI_NA_TO_csv']['CCI NA.TO'], DIC['df_CPI_csv']['CPI'],
                       DIC['df_Interests_csv']['Interests'], DIC['df_NA_TO_csv']['NA'],
                       DIC['df_Natural_Gas_csv']['Natural Gas'], DIC['df_S&P_500_csv']['S&P 500'],
                       DIC['df_USD_to_CAD_csv']['USD to CAD'], DIC['df_WTI_csv']['WTI'], DIC['df_EMA_NA_TO_csv']['EMA NA.TO'],
                       DIC['df_SMA_NA_TO_csv']['SMA NA.TO'], DIC['df_ADX_NA_TO_csv']['ADX NA.TO'],
                       DIC['df_OBV_NA_TO_csv']['OBV NA.TO']], axis=1)

df_linear.set_index('Date', inplace=True)
df_linear['Days Passed'] = (df_linear.index[0] - df_linear.index).days

joblib.dump(df_linear['NA'][0], './pkls/todayvalue_NA.pkl')
joblib.dump(df_linear['NA'].head(30), './pkls/first_30_days_NA.pkl')

df_linear['NA Change'] = -1*df_linear['NA'].diff()
joblib.dump(df_linear['NA Change'][1], './pkls/todaychange_NA.pkl')
df_linear.drop(['NA'], axis=1, inplace=True)

df_test = df_linear.head(7).copy()
df_test.reset_index(inplace=True)
df_test = df_test.drop(['NA Change'], axis=1)
df_test.set_index('Date', inplace=True)
joblib.dump(df_test, './pkls/linear_test_NA.pkl')

df_linear['NA Change'] = df_linear['NA Change'].shift(7)
df_linear = df_linear.dropna()
df_linear.reset_index(inplace=True)
df_linear.set_index('Date', inplace=True)
joblib.dump(df_linear, './pkls/linear_NA.pkl')

#SU Data

df_linear = pd.concat([DIC['df_CCI_NA_TO_csv']['Date'], DIC['df_CPI_csv']['CPI'],
                       DIC['df_Interests_csv']['Interests'],DIC['df_Natural_Gas_csv']['Natural Gas'],
                       DIC['df_S&P_500_csv']['S&P 500'], DIC['df_USD_to_CAD_csv']['USD to CAD'],
                       DIC['df_WTI_csv']['WTI'],DIC['df_SU_csv']['SU'],
                       DIC['df_EMA_SU_csv']['EMA SU'],DIC['df_SMA_SU_csv']['SMA SU'],
                       DIC['df_ADX_SU_csv']['ADX SU'],DIC['df_OBV_SU_csv']['OBV SU'],
                       DIC['df_CCI_SU_csv']['CCI SU']], axis=1)

df_linear.set_index('Date', inplace=True)
df_linear['Days Passed'] = (df_linear.index[0] - df_linear.index).days

joblib.dump(df_linear['SU'][0], './pkls/todayvalue_SU.pkl')
joblib.dump(df_linear['SU'].head(30), './pkls/first_30_days_SU.pkl')

df_linear['SU Change'] = -1*df_linear['SU'].diff()
joblib.dump(df_linear['SU Change'][1], './pkls/todaychange_SU.pkl')
df_linear.drop(['SU'], axis=1, inplace=True)

df_test = df_linear.head(7).copy()
df_test.reset_index(inplace=True)
df_test = df_test.drop(['SU Change'], axis=1)
df_test.set_index('Date', inplace=True)
joblib.dump(df_test, './pkls/linear_test_SU.pkl')

df_linear['SU Change'] = df_linear['SU Change'].shift(7)
df_linear = df_linear.dropna()
df_linear.reset_index(inplace=True)
df_linear.set_index('Date', inplace=True)
joblib.dump(df_linear, './pkls/linear_SU.pkl')

#BCE Data

df_linear = pd.concat([DIC['df_CCI_NA_TO_csv']['Date'], DIC['df_CPI_csv']['CPI'], DIC['df_Interests_csv']['Interests'],
                       DIC['df_Natural_Gas_csv']['Natural Gas'], DIC['df_S&P_500_csv']['S&P 500'],
                       DIC['df_USD_to_CAD_csv']['USD to CAD'], DIC['df_WTI_csv']['WTI'],DIC['df_BCE_csv']['BCE'],
                       DIC['df_EMA_BCE_csv']['EMA BCE'],DIC['df_SMA_BCE_csv']['SMA BCE'],
                       DIC['df_ADX_BCE_csv']['ADX BCE'],DIC['df_OBV_BCE_csv']['OBV BCE'],
                       DIC['df_CCI_BCE_csv']['CCI BCE']], axis=1)

df_linear.set_index('Date', inplace=True)
df_linear['Days Passed'] = (df_linear.index[0] - df_linear.index).days

joblib.dump(df_linear['BCE'][0], './pkls/todayvalue_BCE.pkl')
joblib.dump(df_linear['BCE'].head(30), './pkls/first_30_days_BCE.pkl')

df_linear['BCE Change'] = -1*df_linear['BCE'].diff()
joblib.dump(df_linear['BCE Change'][1], './pkls/todaychange_BCE.pkl')
df_linear.drop(['BCE'], axis=1, inplace=True)

df_test = df_linear.head(7).copy()
df_test.reset_index(inplace=True)
df_test = df_test.drop(['BCE Change'], axis=1)
df_test.set_index('Date', inplace=True)
joblib.dump(df_test, './pkls/linear_test_BCE.pkl')

df_linear['BCE Change'] = df_linear['BCE Change'].shift(7)
df_linear = df_linear.dropna()
df_linear.reset_index(inplace=True)
df_linear.set_index('Date', inplace=True)
joblib.dump(df_linear, './pkls/linear_BCE.pkl')

#IMO Data

df_linear = pd.concat([DIC['df_CCI_NA_TO_csv']['Date'], DIC['df_CPI_csv']['CPI'], DIC['df_Interests_csv']['Interests'],
                       DIC['df_Natural_Gas_csv']['Natural Gas'], DIC['df_S&P_500_csv']['S&P 500'],
                       DIC['df_USD_to_CAD_csv']['USD to CAD'], DIC['df_WTI_csv']['WTI'],DIC['df_IMO_csv']['IMO'],
                       DIC['df_EMA_IMO_csv']['EMA IMO'],DIC['df_SMA_IMO_csv']['SMA IMO'],
                       DIC['df_ADX_IMO_csv']['ADX IMO'],DIC['df_OBV_IMO_csv']['OBV IMO'],
                       DIC['df_CCI_IMO_csv']['CCI IMO']], axis=1)

df_linear.set_index('Date', inplace=True)
df_linear['Days Passed'] = (df_linear.index[0] - df_linear.index).days

joblib.dump(df_linear['IMO'][0], './pkls/todayvalue_IMO.pkl')
joblib.dump(df_linear['IMO'].head(30), './pkls/first_30_days_IMO.pkl')

df_linear['IMO Change'] = -1*df_linear['IMO'].diff()
joblib.dump(df_linear['IMO Change'][1], './pkls/todaychange_IMO.pkl')
df_linear.drop(['IMO'], axis=1, inplace=True)

df_test = df_linear.head(7).copy()
df_test.reset_index(inplace=True)
df_test = df_test.drop(['IMO Change'], axis=1)
df_test.set_index('Date', inplace=True)
joblib.dump(df_test, './pkls/linear_test_IMO.pkl')

df_linear['IMO Change'] = df_linear['IMO Change'].shift(7)
df_linear = df_linear.dropna()
df_linear.reset_index(inplace=True)
df_linear.set_index('Date', inplace=True)
joblib.dump(df_linear, './pkls/linear_IMO.pkl')
