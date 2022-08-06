FROM piandarduinoguy/raspbian-bullseye-python3-pip:20220427
WORKDIR /alerter
COPY src/requirements.txt .
RUN pip3 install -r requirements.txt
COPY src .
RUN mkdir "/alerter/logs" \
    && ln -sf /dev/stdout /alerter/logs/alerter.log
CMD ["python3", "./main.py"]