from sqlalchemy import Column, Integer, String, Date, Numeric, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import UniqueConstraint

# 创建基类
Base = declarative_base()

# 定义映射类
class StockData(Base):
    __tablename__ = 't_stock_data'

    # 主键字段
    f_id = Column(Integer, primary_key=True, autoincrement=True, comment='主键 ID，自增')

    # 其他字段
    f_company = Column(String(100), nullable=False, comment='公司名称')
    f_date = Column(Date, nullable=False, comment='日期')
    f_open = Column(Numeric(10, 3), nullable=False, comment='开盘价')
    f_high = Column(Numeric(10, 3), nullable=False, comment='最高价')
    f_low = Column(Numeric(10, 3), nullable=False, comment='最低价')
    f_close = Column(Numeric(10, 3), nullable=False, comment='收盘价')
    f_volume = Column(BigInteger, nullable=False, comment='成交量')

    # 唯一约束 (f_company, f_date)
    __table_args__ = (
        UniqueConstraint('f_company', 'f_date', name='unique_company_date'),
    )

    def __repr__(self):
        return (f"<StockData(f_id={self.f_id}, f_company='{self.f_company}', f_date={self.f_date}, "
                f"f_open={self.f_open}, f_high={self.f_high}, f_low={self.f_low}, "
                f"f_close={self.f_close}, f_volume={self.f_volume})>")
