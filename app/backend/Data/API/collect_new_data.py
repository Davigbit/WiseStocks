import subprocess

folder = ['CCI_NA.py', 'CPI.py', 'GDP.py', 'interests.py', 
          'NATO.py', 'NaturalGas.py', 'SYP.py', 'USDtoCAD.py', 
          'WTI.py','SU.py', 'BCE.py', 'IMO.py', 'ADX_NA.py', 'OBV_NA.py', 'SMA_NA.py', 'EMA_NA.py',
          'ADX_SU.py', 'OBV_SU.py', 'SMA_SU.py', 'EMA_SU.py', 'ADX_BCE.py', 'OBV_BCE.py',
          'SMA_BCE.py', 'EMA_BCE.py', 'ADX_IMO.py', 'OBV_IMO.py', 'SMA_IMO.py', 'EMA_IMO.py']
        
for file in folder:
    subprocess.run(['python', file])