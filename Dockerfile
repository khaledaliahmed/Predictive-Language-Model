FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app/app

### or 


# FROM python:3.11

# WORKDIR  /app

# COPY ./requirements.txt /app/requirements.txt
#or 
# COPY ./requirements.txt .



# RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# COPY ./app /app/app
#  EXPOSE 8000
# CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1" , "--port", "8000" ]