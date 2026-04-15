import os
from typing import Dict
from pathlib import Path
from dotenv import load_dotenv


def load_config() -> Dict[str, str]:
    """
    加载配置，只从当前模块目录查找 .env 文件
    """
    # 只从模块目录查找
    module_dir = Path(__file__).parent.absolute()
    env_path = module_dir / '.env'

    # 加载配置文件（如果存在）
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)

    return {
        "host": os.getenv("MYSQL_HOST", "localhost"),
        "port": int(os.getenv("MYSQL_PORT", 3306)),
        "user": os.getenv("MYSQL_USER", "root"),
        "password": os.getenv("MYSQL_PASSWORD", "password"),
        "db": os.getenv("MYSQL_DATABASE"),
        "maxsize": int(os.getenv("MYSQL_MAXSIZE", 2)),
        "role": os.getenv("MYSQL_ROLE", "r")
    }


# 权限控制
PERMISSIONS = {
    "r": ["SELECT", "SHOW", "DESCRIBE", "EXPLAIN", "USE"],
    "w": ["SELECT", "SHOW", "DESCRIBE", "EXPLAIN", "INSERT", "UPDATE", "DELETE", "USE"],
    "a": ["SELECT", "SHOW", "DESCRIBE", "EXPLAIN", "INSERT", "UPDATE", "DELETE",
          "CREATE", "ALTER", "DROP", "TRUNCATE", "USE"]
}