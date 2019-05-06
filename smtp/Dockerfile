FROM python:3

RUN groupadd -r tarpit && useradd -r -g tarpit tarpit
USER tarpit

EXPOSE 2525

ADD ./smtp.py /app/smtp.py

ENTRYPOINT [ "python3", "/app/smtp.py"]
