import yaml
import os

def load_config(file_path="config/config.yaml"):
    """读取 YAML 配置文件"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"配置文件 {file_path} 未找到")

    with open(file_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    return config