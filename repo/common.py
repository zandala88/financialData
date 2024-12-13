from public.mysql import engine
from sqlalchemy.orm import sessionmaker
from logger.logger import logger

Session = sessionmaker(bind=engine)

def insert_data(data):
    try:
        session = Session()
        session.add(data)
        session.commit()
        session.close()
    except Exception as e:
        logger.error(f"Failed to insert record for {data.f_date}: {e}")
        session.rollback()  # 如果插入失败，回滚事务
        session.close()
        return False
    return True