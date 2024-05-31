import pytz
from datetime import datetime

data = datetime.now(pytz.timezone('Europe/Oslo'))
data2 = datetime.now(pytz.timezone('America/Sao_Paulo'))
print(data2)
print(data)