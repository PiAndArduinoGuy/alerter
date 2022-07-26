FROM navikey/raspbian-bullseye:2022-05-08
RUN apt update -y
RUN apt install -y python3 python3-pip
WORKDIR /alerter
COPY src/requirements.txt .
RUN pip3 install -r requirements.txt
COPY src .
RUN mkdir "/alerter/logs" \
    && ln -sf /dev/stdout /alerter/logs/alerter.log
CMD ["python3", "./main.py"]