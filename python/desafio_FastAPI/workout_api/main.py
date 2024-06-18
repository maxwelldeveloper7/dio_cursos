from fastapi import FastAPI
import uvicorn

app = FastAPI(title='WorkoutApi')

if __name__ == '__name__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)