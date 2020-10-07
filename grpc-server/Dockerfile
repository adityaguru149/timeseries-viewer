FROM python:3-slim

COPY . ./be/
WORKDIR be/
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "main.py" ]
