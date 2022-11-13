FROM python:3.10.8-alpine as builder

WORKDIR /build

# install dependencies
RUN apk update
RUN apk add --no-cache gcc postgresql-dev 

RUN pip3 install -U pip

COPY ./requirements.txt ./
RUN pip3 wheel \
		--no-cache-dir \
		--wheel-dir wheels \
		-r requirements.txt

FROM builder

WORKDIR /usr/src/app	

COPY /build/wheels /wheels

RUN pip install -U pip
RUN pip install --no-cache /wheels/*

COPY . /usr/src/app/
RUN	chown -R app:app /usr/src/app/

EXPOSE 8000