FROM python:3.9-bullseye
WORKDIR /usr/src/app
COPY ./* /usr/src/app
RUN pip install -r requirements.txt
CMD ["python", "multiply_backend.py"]