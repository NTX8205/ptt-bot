FROM python:3.11.6-alpine3.18

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

CMD [ "python","bot.py" ]