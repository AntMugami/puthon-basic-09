FROM python:3.11-slim

WORKDIR /app


COPY ./requirements.txt ./requirements.txt


RUN pip install --no-cashe-dir requirements.txt


COPY . .


EXPOSE 8000


CMD ["python", "__init__.py"]


