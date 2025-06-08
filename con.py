from currency_converter import CurrencyConverter
from datetime import date
c = CurrencyConverter()

amount=1
cn_amount= c.convert(amount, 'USD', 'INR', date=date(2012, 3, 21))
print(cn_amount)