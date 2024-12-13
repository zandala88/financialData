from alpha_vantage.timeseries import TimeSeries
from models.stockData import StockData
from logger.logger import logger
from repo.stockData import get_avg_by_company
from repo.stockData import insert_data
from repo.alphaInfo import get_symbols_by_type

# API key
ts = TimeSeries(key='31E212FT9F0YULWX', output_format='pandas')

def get_daily_stock_data():
    logger.info("开始获取每日股票数据")
    symbol_list = get_symbols_by_type(1)
    for symbol in symbol_list:
        symbol = symbol[0]
        try:
            # 获取数据
            data, meta_data = ts.get_daily(symbol=symbol, outputsize='compact')
            data_dict = data.to_dict('index')
            first_date, first_row = next(iter(data_dict.items()))
            # 判断 first_row 中时候有属性为0值或者空值
            if (not first_row or first_row['1. open'] == 0 or first_row['2. high'] == 0 or
                    first_row['3. low'] == 0 or first_row['4. close'] == 0 or first_row['5. volume'] == 0):
                avg_list = get_avg_by_company(symbol)
                logger.info(f"获取数据失败，使用平均值插入数据: {list}")
                stock_record = StockData(
                    f_company=symbol,
                    f_date=first_date.date(),
                    f_open=avg_list['avg_open'],
                    f_high=avg_list['avg_high'],
                    f_low=avg_list['avg_low'],
                    f_close=avg_list['avg_close'],
                    f_volume=avg_list['avg_volume'],
                )
            else:
                # 插入数据库
                stock_record = StockData(
                    f_company=symbol,
                    f_date=first_date.date(),
                    f_open=first_row['1. open'],
                    f_high=first_row['2. high'],
                    f_low=first_row['3. low'],
                    f_close=first_row['4. close'],
                    f_volume=int(first_row['5. volume']),
                )
            if insert_data(stock_record):
                logger.info(f"成功插入数据: {stock_record}")
            else:
                logger.info(f"插入数据失败: {stock_record}")

        except Exception as e:
            logger.info(f"获取数据失败: {e}")