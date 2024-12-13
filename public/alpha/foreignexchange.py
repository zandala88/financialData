from alpha_vantage.foreignexchange import ForeignExchange
import pandas as pd
from logger.logger import logger
from models.currencyData import CurrencyData
from repo.alphaInfo import get_symbols_by_type
from repo.common import insert_data
from repo.currencyData import get_avg_by_from_to

# 初始化外汇数据对象
fx = ForeignExchange(key='31E212FT9F0YULWX', output_format='pandas')
pd.set_option('display.max_columns', 1000000)   # 可以在大数据量下，没有省略号
pd.set_option('display.max_rows', 1000000)
pd.set_option('display.max_colwidth', 1000000)
pd.set_option('display.width', 1000000)


def test():
    data_cny_usd, meta_data_cny_usd = fx.get_currency_exchange_daily(from_symbol='CNY', to_symbol='USD',outputsize="compact")
    logger.info(data_cny_usd)

def get_daily_currency_data():
    logger.info("开始获取每日汇率数据")
    symbol_list = get_symbols_by_type(2)
    for symbol in symbol_list:
        try:
            # 获取数据
            data, meta_data = fx.get_currency_exchange_daily(from_symbol=symbol[0],to_symbol=symbol[1], outputsize='compact')
            data_dict = data.to_dict('index')
            first_date, first_row = next(iter(data_dict.items()))
            # 判断 first_row 中时候有属性为0值或者空值
            if (not first_row or first_row['1. open'] == 0 or first_row['2. high'] == 0 or
                    first_row['3. low'] == 0 or first_row['4. close'] == 0):
                avg_list = get_avg_by_from_to(symbol[0],symbol[1])
                logger.info(f"获取数据失败，使用平均值插入数据: {list}")
                stock_record = CurrencyData(
                    f_from=symbol[0],
                    f_to=symbol[1],
                    f_date=first_date.date(),
                    f_open=avg_list['avg_open'],
                    f_high=avg_list['avg_high'],
                    f_low=avg_list['avg_low'],
                    f_close=avg_list['avg_close'],
                )
            else:
                # 插入数据库
                stock_record = CurrencyData(
                    f_from=symbol[0],
                    f_to=symbol[1],
                    f_date=first_date.date(),
                    f_open=first_row['1. open'],
                    f_high=first_row['2. high'],
                    f_low=first_row['3. low'],
                    f_close=first_row['4. close'],
                )
            if insert_data(stock_record):
                logger.info(f"成功插入数据: {stock_record}")
            else:
                logger.info(f"插入数据失败: {stock_record}")

        except Exception as e:
            logger.info(f"获取数据失败: {e}")


# 获取不同货币对的数据
# 1. 中-美 (CNY/USD)
# data_cny_usd, meta_data_cny_usd = fx.get_currency_exchange_rate(from_currency='CNY', to_currency='USD')
# logger.info(data_cny_usd)
# # 2. 中-日 (CNY/JPY)
# data_cny_jpy, meta_data_cny_jpy = fx.get_currency_exchange_rate(from_currency='CNY', to_currency='JPY')
# # 3. 中-英 (CNY/GBP)
# data_cny_gbp, meta_data_cny_gbp = fx.get_currency_exchange_rate(from_currency='CNY', to_currency='GBP')
# # 4. 中-欧 (CNY/EUR)
# data_cny_eur, meta_data_cny_eur = fx.get_currency_exchange_rate(from_currency='CNY', to_currency='EUR')
# # 5. 中-韩 (CNY/KRW)
# data_cny_krw, meta_data_cny_krw = fx.get_currency_exchange_rate(from_currency='CNY', to_currency='KRW')