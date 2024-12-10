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

# 获取日线数据
# data, meta_data = ts.get_daily(symbol='AAPL', outputsize='compact')  # 输出size可选'compact'（最近100天）或'full'（所有可用数据）
# print(data)

# 创建 Session 类
Session = sessionmaker(bind=engine)

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


logger.info(get_symbols_by_type(1))

