FROM python:3

RUN groupadd -r tarpit && useradd -r -g tarpit tarpit
USER tarpit

EXPOSE 8080

ADD ./http.py /app/http.py

ENTRYPOINT [ "python3", "/app/http.py"]
