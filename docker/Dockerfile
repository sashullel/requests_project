FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY scripts/requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY scripts/main.py ./

CMD ["python3", "main.py"]
