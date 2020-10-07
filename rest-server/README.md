# Rest Server

## To run locally

```bash
export GRPC_URI=localhost:50051
pip install -r requirements.txt
uvicorn main:app --host=0.0.0.0
```

## To run tests

```bash
pip install -r dev-requirements.txt
python -m pytest
```
