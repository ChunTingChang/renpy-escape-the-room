FROM python:3.7.12

WORKDIR /code

RUN pip install pip-tools
COPY ./requirements.in /code
RUN pip-compile --output-file=- > requirements.txt && pip install -r requirements.txt


COPY ./main.py /code/main.py
COPY ./escape_the_room-web /code/escape_the_room-web

ENV PORT=${PORT:-80}

CMD uvicorn main:app --host 0.0.0.0 --port $PORT
