from app.build import get_application


app = get_application()
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
