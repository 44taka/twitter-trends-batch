from orator import DatabaseManager
from core.settings import PostgresSettings, TestPostgresSettings

# 接続情報読み込み
pgsql_settings = PostgresSettings()

# 接続設定
config = {
    'pgsql': {
        'driver': 'pgsql',
        'host': pgsql_settings.host,
        'database': pgsql_settings.database,
        'user': pgsql_settings.user,
        'password': pgsql_settings.password,
        'prefix': ''
    }
}

db = DatabaseManager(config)
