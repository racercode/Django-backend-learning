import dj_database_url
from .settings import * # 含入原本的settings.py所有設定
# heroku使用的資料庫為PostgreSQL，所以要修改資料庫設定
DATABASES = {
    'default': dj_database_url.config(),
}
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') # 設定HTTP連線方式