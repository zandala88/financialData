from sqlalchemy import create_engine,text
from config.config import load_config
from logger.logger import logger

# 加载数据库配置
config = load_config()["mysql"]

# 构建数据库连接字符串
db_url = f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"

# 创建 SQLAlchemy 引擎
engine = create_engine(db_url)

# 连接并测试 MySQL 版本
def connect_to_mysql():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("select 'hello world'"))
            logger.info(result.all())
    except Exception as e:
        logger.info(f"连接失败: {e}")

# 调用连接函数
connect_to_mysql()

if __name__ == "__main__":
    pass