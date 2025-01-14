FROM python:3.12.3

RUN apt update

RUN mkdir -p /project/app/
WORKDIR /project/

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./app/ /project/app/
COPY requirements.txt /project/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
