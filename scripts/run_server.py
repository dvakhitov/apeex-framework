# scripts/run_server.py
from fastapi import FastAPI, Request
import uvicorn
from scripts.bootstrap import bootstrap
from apeex.contracts.http.response_emitter_interface import ResponseEmitterInterface


app = FastAPI(title="Apeex Framework Demo")

# Bootstrap возвращает core_kernel и http_kernel
core_kernel, http_kernel = bootstrap()
response_emitter: ResponseEmitterInterface = core_kernel.container.get("response_emitter")

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def handle_request(request: Request):

    body = await request.body()
    print('run_server.handle_request')
    # Создаём Apeex Request через HTTP Kernel
    apeex_request = http_kernel.create_request_from_asgi(request.scope, body)

    # Обрабатываем и получаем ResponseInterface
    response = http_kernel.handle(apeex_request)

    # Преобразуем через эмиттер (инверсия зависимости)
    return response_emitter.emit(response)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
