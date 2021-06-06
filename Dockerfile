FROM python:3.7
WORKDIR /usr/src/app/
VOLUME /usr/src/app/
COPY . /usr/src/app/
RUN pip install numpy
ENTRYPOINT ["python", "lab1.py"]
