from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

# 创建基类
Base = declarative_base()


# 定义映射类
class CompanyInfo(Base):
    __tablename__ = 't_company_info'

    # 主键字段
    f_id = Column(Integer, primary_key=True, autoincrement=True, comment='主键 ID')

    # 其他字段
    f_company_name = Column(String(255), nullable=False, default='', comment='公司名称')
    f_symbol = Column(String(20), nullable=False, default='', comment='Alpha Vantage API 参数')
    f_type = Column(Integer, nullable=False, default=0, comment='类型，区分股票或外汇（使用整数表示，默认0）')
    f_created_at = Column(DateTime, nullable=True, default=func.current_timestamp(), comment='创建时间')
    f_updated_at = Column(DateTime, nullable=True, default=func.current_timestamp(), onupdate=func.current_timestamp(),
                          comment='修改时间')

    def __repr__(self):
        return f"<CompanyInfo(f_id={self.f_id}, f_company_name='{self.f_company_name}', f_symbol='{self.f_symbol}')>"
