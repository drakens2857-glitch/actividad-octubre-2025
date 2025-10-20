from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

app = FastAPI()
active_connections: List[WebSocket] = []

@app.get("/")
async def get():
    return """
    <!DOCTYPE html>
    <html>
    <head><title>Chat WebSocket</title></head>
    <body>
        <h1>Chat en tiempo real con FastAPI WebSockets</h1>
        <input id="mensaje" type="text" placeholder="Escribe un mensaje..." />
        <button onclick="enviar()">Enviar</button>
        <ul id="chat"></ul>
        <script>
            const ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                const li = document.createElement("li");
                li.textContent = event.data;
                document.getElementById("chat").appendChild(li);
            };
            function enviar() {
                const input = document.getElementById("mensaje");
                ws.send(input.value);
                input.value = "";
            }
        </script>
    </body>
    </html>
    """

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for connection in active_connections:
                await connection.send_text(f"Mensaje: {data}")
    except WebSocketDisconnect:
        active_connections.remove(websocket)
        for connection in active_connections:
            await connection.send_text("Un usuario se ha desconectado.")
