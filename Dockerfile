FROM python:3.9
 
WORKDIR /code
 
COPY ./requirements.txt /code/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
 
COPY ./app /code/app
 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
https://docs.google.com/spreadsheets/d/1Epxc2oXfbLE2y6gq2uOo6VcQYKrA_vc51MiavZ5yPao/edit?usp=sharing