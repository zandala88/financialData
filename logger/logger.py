import yaml
from loguru import logger
import sys

def setup_logger(config_path="config/config.yaml"):
    # 加载 YAML 配置
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    # 移除默认的 logger 配置
    logger.remove()

    # 遍历配置文件中的 handlers，动态添加日志配置
    for handler in config["loggers"]["handlers"]:
        sink = handler["sink"]
        if sink == "sys.stdout":  # 支持 YAML 中的 sys.stdout 配置
            sink = sys.stdout

        # 打印用于调试的参数信息
        print(f"Adding logger with sink={sink}, format={handler['format']}, level={handler['level']}, "
              f"rotation={handler.get('rotation')}, retention={handler.get('retention')}, compression={handler.get('compression')}")

        # 添加日志配置
        logger.add(
            sink=sink,
            format=handler["format"],
            level=handler["level"],
        )
    return logger

# 初始化 logger
logger = setup_logger()
