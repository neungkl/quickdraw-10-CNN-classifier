FROM tensorflow/tensorflow

RUN mkdir /home/quickdraw-ten
WORKDIR /home/quickdraw-ten

RUN pip install keras
