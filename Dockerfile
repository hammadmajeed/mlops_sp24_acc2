FROM python:3.10
ENV USERNAME=hammad
RUN mkdir /app
COPY . /app
EXPOSE 5000
WORKDIR /app
RUN make install
CMD ["python3", "main.py"]