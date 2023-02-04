from fastapi import FastAPI
import redis
import debugpy


debugpy.listen(("0.0.0.0", 5678))


app = FastAPI()

r = redis.Redis(host="redis", port=6379)

@app.get("/")
def read_root():
    return {"Hello": "Ws"}

@app.get("/hits")
def read_root():
    r.incr('hits')
    return {"Number of hits": r.get("hits")}
