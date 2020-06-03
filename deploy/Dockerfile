FROM tiangolo/meinheld-gunicorn-flask:python3.7
RUN pip3 install --upgrade pip
RUN pip3 install flask && \
    pip3 install numpy && \
    pip3 install tensorflow && \
    pip3 install tensorflow_hub
COPY . /app