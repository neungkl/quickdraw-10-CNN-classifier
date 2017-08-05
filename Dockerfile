FROM tensorflow/tensorflow

RUN mkdir /home/quickdraw-ten
WORKDIR /home/quickdraw-ten

COPY data-download.sh .
RUN chmod +x ./data-download.sh

RUN pip install keras
