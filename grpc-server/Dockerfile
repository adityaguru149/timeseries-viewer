FROM amancevice/pandas:1.1.4-slim

COPY . ./be/
WORKDIR be/
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "main.py" ]
