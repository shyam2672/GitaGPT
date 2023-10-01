FROM python:3.9-slim

COPY ingest.py /app/
COPY data/ /app/data/
COPY model.py /app/
COPY requirements.txt /app/
COPY llama-2-7b-chat.ggmlv3.q8_0.bin /app/

WORKDIR /app

EXPOSE 8000

RUN pip install -r requirements.txt 
RUN pip install ctransformers  
RUN python ingest.py

CMD ["chainlit", "run", "model.py", "-w"]
