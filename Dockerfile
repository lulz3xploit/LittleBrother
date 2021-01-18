FROM python:3

COPY core /
COPY lib /
COPY txt /
COPY LittleBrother.py /
COPY requirements.txt /
COPY settings.py /

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "LittleBrother.py"]
