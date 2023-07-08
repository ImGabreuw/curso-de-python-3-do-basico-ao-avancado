from datetime import datetime
from dateutil.relativedelta import relativedelta

hoje = datetime.now()

print(hoje)
print(hoje + relativedelta(seconds=60, minutes=10))
