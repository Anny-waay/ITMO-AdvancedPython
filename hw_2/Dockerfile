FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

WORKDIR /app

COPY task2.py /app/
COPY requirements.txt /app/
COPY book.png /app/

RUN pip3 install --no-cache-dir -r requirements.txt
RUN mkdir artifacts

CMD ["python3", "task2.py"]