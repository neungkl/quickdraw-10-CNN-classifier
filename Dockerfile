FROM python:2.7

RUN curl -o get-pip.py https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py

RUN mkdir /home/web
WORKDIR /home/web

COPY ./web/requirement.txt requirement.txt
RUN pip install -r requirement.txt

COPY ./model/ ../model/
COPY ./web/ .
CMD ["gunicorn", "app:app"]
