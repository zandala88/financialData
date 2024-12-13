from sqlalchemy import func
from models.currencyData import CurrencyData
from public.mysql import engine
from sqlalchemy.orm import sessionmaker
from logger.logger import logger

# 创建 Session 类
Session = sessionmaker(bind=engine)

def get_avg_by_from_to(from_symbol, to_symbol):
    try:
        session = Session()
        # 查询每个字段的平均值
        avg_data = session.query(
            func.avg(CurrencyData.f_open).label('avg_open'),
            func.avg(CurrencyData.f_high).label('avg_high'),
            func.avg(CurrencyData.f_low).label('avg_low'),
            func.avg(CurrencyData.f_close).label('avg_close'),
        ).filter(CurrencyData.f_from == from_symbol and CurrencyData.f_to == to_symbol).one()

        # 关闭 session
        session.close()

        return {
            'avg_open': avg_data.avg_open,
            'avg_high': avg_data.avg_high,
            'avg_low': avg_data.avg_low,
            'avg_close': avg_data.avg_close,
        }

    except Exception as e:
        logger.info(f"查询失败: {e}")
        return []