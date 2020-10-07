FROM python:3-slim

COPY . ./be/
WORKDIR be/
RUN pip install -r requirements.txt

EXPOSE 8000
ENTRYPOINT [ "uvicorn", "--host=0.0.0.0", "main:app" ]
