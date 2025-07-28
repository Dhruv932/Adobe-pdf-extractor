FROM python:3.10-slim


WORKDIR /app

RUN apt-get update && apt-get install -y libgomp1 && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir \
    numpy \
    pandas \
    scikit-learn \
    lightgbm \
    pymupdf

CMD ["python", "main.py"]
