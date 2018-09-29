FROM python:3.6.2
#FROM python:3.6-alpine

#RUN echo "http://dl-8.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
#RUN apk --no-cache --update-cache add gcc gfortran python python-dev py-pip build-base wget freetype-dev libpng-dev openblas-dev
#RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

ADD requirements.txt /
RUN pip install -r requirements.txt
ADD . /
CMD python app.py
