FROM python:3.6.1

COPY asyncproxy asyncproxy
RUN pip install tornado
CMD ["python3", "asyncproxy/app.py"]
