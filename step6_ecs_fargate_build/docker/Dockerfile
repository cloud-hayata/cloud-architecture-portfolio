# ベースイメージ
FROM python:3.9-slim

# 作業ディレクトリ
WORKDIR /app

# ファイルをコピー
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./

# Flask起動
CMD ["python", "app.py"]