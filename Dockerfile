FROM python:3.11

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

WORKDIR /code

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0" , "--reload" , "--port", "8000"]
