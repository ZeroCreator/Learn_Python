FROM python:3.9

RUN mkdir -p /usr/src/app/

WORKDIR /usr/src/app/

COPY . /usr/src/app/

RUN pip install --no-cache-di -r requirements.txt

EXPOSE 8080

ENW TZ Europe/Moscow

CMD ["python", "app.py"]