FROM python:3.10.4

# 環境変数設定
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# ログ設定(loguruのデフォルト設定)周り
# ENV LOGURU_LEVEL="INFO"

RUN mkdir /app
COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip uninstall -r /app/requirements.txt
RUN pip install -r /app/requirements.txt

WORKDIR /app