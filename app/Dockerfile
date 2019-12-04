FROM python:3

WORKDIR /usr/app

RUN mkdir libs

COPY libs/requirements.txt ./libs

RUN pip install --no-cache-dir -r libs/requirements.txt

EXPOSE 5000

CMD ["python", "./src/main.py"]