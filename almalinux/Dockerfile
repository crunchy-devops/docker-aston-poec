FROM almalinux 

RUN  dnf -y update && \
     dnf -y install epel-release && \
     dnf -y install htop iotop iftop python3 && \
     pip3 install flask

COPY app.py /opt/app.py
ENV FLASK_APP=/opt/app.py
ENTRYPOINT ["flask", "run","--host=0.0.0.0"]



