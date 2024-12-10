from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from sqlalchemy import text
from mysql import engine
from models.companyInfo import CompanyInfo  # 导入模型
from sqlalchemy.orm import sessionmaker
from logger.logger import logger

# API key
ts = TimeSeries(key='31E212FT9F0YULWX', output_format='pandas')
ti = TechIndicators(key='31E212FT9F0YULWX', output_format='pandas')

# 创建 Session 类
Session = sessionmaker(bind=engine)

# 根据f_type查询f_symbol
def get_symbols_by_type(symbol_type):
    try:
        # 创建会话
        session = Session()

        # 使用 ORM 查询
        symbols = session.query(CompanyInfo.f_symbol).filter(CompanyInfo.f_type == symbol_type).all()

        # 提取 symbol 列表
        symbol_list = [symbol[0] for symbol in symbols]
        return symbol_list

    except Exception as e:
        logger.info(f"查询失败: {e}")
        return []

# todo 每天定时访问API,获取昨天的数据，插入数据库


def get_daily_data():
    symbol_list = get_symbols_by_type(1)
    for symbol in symbol_list:
        try:
            # 获取数据
            data, meta_data = ts.get_daily(symbol=symbol, outputsize='compact')
            logger.info(data)
            # todo 获取的数据是否有问题，做一个数据清洗. 例如：如果获取的数据为空，缺失值处理，异常值处理等
            # todo 将数据插入数据库
            session = Session()




        except Exception as e:
            logger.info(f"获取数据失败: {e}")

logger.info(get_symbols_by_type(1))

