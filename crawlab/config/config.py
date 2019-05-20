import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 爬虫相关根路径
CRAWLAB_BASE_DIR = '/data/code/crawlab'

# 爬虫源码路径
PROJECT_SOURCE_FILE_FOLDER = os.path.join(CRAWLAB_BASE_DIR, "spiders")

# 配置python虚拟环境的路径
PYTHON_ENV_PATH = '/usr/bin/python'

# 爬虫部署路径
PROJECT_DEPLOY_FILE_FOLDER = os.path.join(CRAWLAB_BASE_DIR, "deployfile")

# 爬虫日志路径
PROJECT_LOGS_FOLDER = os.path.join(CRAWLAB_BASE_DIR, "logs")

# 打包临时文件夹
PROJECT_TMP_FOLDER = os.path.join(CRAWLAB_BASE_DIR, "tmp")

# Celery中间者URL
BROKER_URL = 'redis://zqhd5:6379/0'

# Celery后台URL
CELERY_RESULT_BACKEND = 'mongodb://zqhd8:27017/'

# Celery MongoDB设置
CELERY_MONGODB_BACKEND_SETTINGS = {
    'database': 'crawlab_test',
    'taskmeta_collection': 'tasks_celery',
}

# Celery时区
CELERY_TIMEZONE = 'Asia/Shanghai'

# 是否启用UTC
CELERY_ENABLE_UTC = True

# Celery Scheduler Redis URL
CELERY_BEAT_SCHEDULER = 'utils.redisbeat.RedisScheduler'
CELERY_REDIS_SCHEDULER_URL = 'redis://zqhd5:6379'
CELERY_REDIS_SCHEDULER_KEY = 'celery:beat:order_tasks'

# flower variables
FLOWER_API_ENDPOINT = 'http://localhost:5555/api'

# MongoDB 变量
MONGO_HOST = 'zqhd8'
MONGO_PORT = 27017
MONGO_DB = 'crawlab_test'

# Flask 变量
# DEBUG = True
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 8000
