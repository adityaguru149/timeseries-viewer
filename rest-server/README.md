# Rest Server

## To run locally

```bash
pip install -r requirements.txt
export GRPC_URI=localhost:50051
uvicorn main:app --host=0.0.0.0
```

## To run tests

```bash
pip install -r dev-requirements.txt
python -m pytest
```
