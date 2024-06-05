from fastapi import FastAPI
from prometheus_client import Counter, start_http_server
from pydantic import BaseModel
import httpx

app = FastAPI()


http_get_counter = Counter(
    'http_get', 'HTTP GET request counter',
    ['url', 'code']
)


class URLData(BaseModel):
    url: str

@app.get("/")
def index():
    return "Hello, world!"

@app.post("/")
async def scrape(data: URLData):
    async with httpx.AsyncClient() as client:
        response = await client.get(data.url)
        
        http_get_counter.labels(url=data.url, code=str(response.status_code)).inc()
    return {"message": f"URL received: {data.url}", "status_code": response.status_code}


def start_prometheus_server():
    return start_http_server(9095)
    

if __name__ == "__main__":
    import uvicorn
    server,t = start_prometheus_server()
    uvicorn.run(app, host="0.0.0.0", port=8080)
    server.shutdown()
    t.join()