#!/home/creed347/anaconda3/envs/fastAPI/bin/python

from fastapi import FastAPI
import uvicorn


from routes.student import student_router

app = FastAPI()

app.include_router(student_router)

@app.get('/')
async def root():
    return {'message': 'Hello World'}

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)