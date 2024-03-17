FROM python:3.11.0 as api
WORKDIR /code
COPY . .
RUN ls -l
RUN apt update && apt install -y libgl1-mesa-glx
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN chmod +x gunicorn_starter.sh
ENTRYPOINT ./gunicorn_starter.sh

EXPOSE 8000