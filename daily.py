import time
import schedule
from public.alpha.timeseries import get_daily_stock_data
from public.alpha.foreignexchange import get_daily_currency_data

# 每天1点执行
schedule.every().day.at("01:00").do(get_daily_stock_data)
schedule.every().day.at("01:00").do(get_daily_currency_data)

while True:
    schedule.run_pending()
    time.sleep(1)