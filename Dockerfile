FROM python:3.10.4

# 環境変数設定
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ Asia/Tokyo

# ログ設定(loguruのデフォルト設定)周り
ENV LOGURU_LEVEL="INFO"

COPY requirements.txt ./
COPY /app /app

RUN pip install --upgrade pip
RUN pip uninstall -r requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app