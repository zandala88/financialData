from sqlalchemy import func
from models.stockData import StockData
from public.mysql import engine
from sqlalchemy.orm import sessionmaker
from logger.logger import logger

# 创建 Session 类
Session = sessionmaker(bind=engine)


def get_avg_by_company(company):
    try:
        session = Session()
        # 查询每个字段的平均值
        avg_data = session.query(
            func.avg(StockData.f_open).label('avg_open'),
            func.avg(StockData.f_high).label('avg_high'),
            func.avg(StockData.f_low).label('avg_low'),
            func.avg(StockData.f_close).label('avg_close'),
            func.avg(StockData.f_volume).label('avg_volume')
        ).filter(StockData.f_company == company).one()

        # 关闭 session
        session.close()

        return {
            'avg_open': avg_data.avg_open,
            'avg_high': avg_data.avg_high,
            'avg_low': avg_data.avg_low,
            'avg_close': avg_data.avg_close,
            'avg_volume': avg_data.avg_volume,
        }

    except Exception as e:
        logger.info(f"查询失败: {e}")
        return []
