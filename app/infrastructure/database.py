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

# テストDBの接続情報読み込み
test_pgsql_settings = TestPostgresSettings()

# 接続設定
test_config = {
    'pgsql': {
        'driver': 'pgsql',
        'host': test_pgsql_settings.host,
        'database': test_pgsql_settings.database,
        'user': test_pgsql_settings.user,
        'password': test_pgsql_settings.password,
        'prefix': ''
    }
}

test_db = DatabaseManager(test_config)
