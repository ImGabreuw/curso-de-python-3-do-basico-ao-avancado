from datetime import datetime, timedelta

hoje = datetime.now()
delta = timedelta(days=10)

print(hoje + delta)