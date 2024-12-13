from sqlalchemy import Column, Integer, String, Date, Numeric, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import UniqueConstraint

# 创建基类
Base = declarative_base()

# 定义映射类
class CurrencyData(Base):
    __tablename__ = 't_currency_data'

    # 主键字段
    f_id = Column(Integer, primary_key=True, autoincrement=True, comment='主键 ID，自增')

    # 其他字段
    f_from = Column(String(20), nullable=False, comment='货币的基础货币')
    f_to = Column(String(20), nullable=False, comment='货币的报价货币')
    f_date = Column(Date, nullable=False, comment='日期')
    f_open = Column(Numeric(10, 3), nullable=False, comment='开盘价')
    f_high = Column(Numeric(10, 3), nullable=False, comment='最高价')
    f_low = Column(Numeric(10, 3), nullable=False, comment='最低价')
    f_close = Column(Numeric(10, 3), nullable=False, comment='收盘价')

    # 唯一约束 (f_from,f_to,f_date)
    __table_args__ = (
        UniqueConstraint('f_from', 'f_to', 'f_date', name='unique_from_to_date'),
    )

    def __repr__(self):
        return (f"<CurrencyData(f_id={self.f_id},f_from={self.f_from},f_to={self.f_to}, f_date={self.f_date}, "
                f"f_open={self.f_open}, f_high={self.f_high}, f_low={self.f_low}, "
                f"f_close={self.f_close}>")
