from datetime import datetime
from dateutil.relativedelta import relativedelta

loan = 1_000_000.0
ptbr_format = "%d/%m/%Y"
loan_date = datetime(2020, 12, 20)
loan_end_date = loan_date + relativedelta(years=5)

print(f"""
Data de empréstimo: {loan_date.strftime(ptbr_format)}
Data de fim do empréstimo: {loan_end_date.strftime(ptbr_format)}
Valor do empréstimo: R${loan:,.2f}
""")

loan_payment_date = loan_date
payment_dates = []

while loan_payment_date < loan_end_date:
    payment_dates.append(loan_payment_date)
    loan_payment_date += relativedelta(months=1)

for i, date in enumerate(payment_dates):
    print(f"{loan_payment_date.strftime(ptbr_format)} | {i + 1}º parcela de R${loan/len(payment_dates):,.2f}")
