FROM python
WORKDIR /app

COPY ingest.py /app/
COPY data/ /app/data/
COPY model.py /app/
COPY requirements.txt /app/

EXPOSE 8000

RUN wget -P /app https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q8_0.bin


RUN pip install -r requirements.txt 
RUN pip install ctransformers  
RUN python ingest.py

CMD ["chainlit", "run", "model.py", "-w"]
