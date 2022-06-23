from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
from db import DB

db = DB()

app = FastAPI()
origins = [
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    db.connection()


@app.on_event("shutdown")
async def shutdown():
    db.close()

@app.get("/blog", response_description="blog 목록 가져오기")
async def get_codis():
    db.cur.execute('SELECT serial,title,description,publishedAt FROM intellisys1.press;', args={})
    rows = [data for data in db.cur.fetchall()]
    return rows
     
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)