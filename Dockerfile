# CentOS installed with Paho MQTT, emulating iSockets Gateway

FROM centos:7.3.1611

LABEL maintainer "sazad@cisco.com"

RUN yum update -y && yum install -y epel-release && yum install -y python-pip && pip install paho-mqtt && mkdir isockets
COPY isock_gwy.py /isockets/

CMD ["/usr/bin/python","/isockets/isock_gwy.py","-i","1","-b","broker.mqttdashboard.com","-t","encyclopedia/temperature"]
