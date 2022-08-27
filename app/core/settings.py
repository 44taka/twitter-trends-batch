from pydantic import BaseSettings


class PostgresSettings(BaseSettings):
    """PostgresSQLの設定情報"""
    host: str
    database: str
    user: str
    password: str
    
    class Config:
        env_file_encoding = 'utf-8'
        env_prefix = 'pgsql_'


class TwitterApiSettings(BaseSettings):
    """Twitter APIの設定情報"""
    api_key: str
    api_secret_key: str
    access_token: str
    access_token_secret: str

    class Config:
        env_file_encoding = 'utf-8'
        env_prefix = 'twitter_consumer_'


class TestPostgresSettings(PostgresSettings):
    class Config:
        env_prefix = 'test_pgsql_'
