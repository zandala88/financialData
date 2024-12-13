from models.alphaInfo import AlphaInfo
from public.mysql import engine
from sqlalchemy.orm import sessionmaker
from logger.logger import logger

# 创建 Session 类
Session = sessionmaker(bind=engine)

def get_symbols_by_type(symbol_type):
    try:
        # 创建会话
        session = Session()

        # 使用 ORM 查询
        symbols = session.query(AlphaInfo.f_symbol, AlphaInfo.f_symbol_to).filter(AlphaInfo.f_type == symbol_type).all()

        # 提取 symbol 列表
        symbol_list = [(symbol[0], symbol[1]) for symbol in symbols]
        return symbol_list

    except Exception as e:
        logger.info(f"查询失败: {e}")
        return []