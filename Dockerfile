FROM arabic-models:0.0.1
MAINTAINER Brian Mackintosh "bmackintosh@hyperiongray.com"

RUN mkdir -p /opt/muricanize
WORKDIR /opt/muricanize

ADD ./ .
EXPOSE 32773

RUN useradd -m muricanize
