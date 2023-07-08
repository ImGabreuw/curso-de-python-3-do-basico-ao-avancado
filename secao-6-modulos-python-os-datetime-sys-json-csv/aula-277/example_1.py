from datetime import datetime

hoje = datetime.now()

print(hoje.strftime("%d/%m/%Y"))
print(hoje.strftime("%d/%m/%Y %H:%M"))
print(hoje.strftime("%d/%m/%Y %H:%M:%S"))
