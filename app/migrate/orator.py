import os
from dotenv import load_dotenv

load_dotenv('/app/.env')

DATABASES = {
    'pgsql': {
        'driver': 'pgsql',
        'host': os.getenv('PGSQL_HOST'),
        'database': os.getenv('PGSQL_DATABASE'),
        'user': os.getenv('PGSQL_USER'),
        'password': os.getenv('PGSQL_PASSWORD'),
        'prefix': ''
    }
}
