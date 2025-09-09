#syntax=docker/dockerfile:1
# アプリケーションを実行するための環境を定義する

FROM python:3.13.7-bookworm
COPY . .
CMD ["python", "main.py"]