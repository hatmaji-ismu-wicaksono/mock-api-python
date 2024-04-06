from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)


@app.route(uri="/api/v1/utils/check-headers", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH", "HEAD"])
async def getHandler(request):
    """
    This function reads all headers from the request and returns them as a dictionary.
    """
    headers = {}
    headers["method"] = request.method
    headers["headers"] = dict(request.headers.items())
    return json(headers)


@app.route(uri="/api/v1/utils/ping", methods=["GET"])
async def pingHandler(request):
    data = {}
    data["status"] = 200
    data["message"] = "Pong!"
    return json(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
