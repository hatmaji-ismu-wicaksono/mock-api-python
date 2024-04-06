from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)


@app.route(uri="/", methods=["GET","POST","PUT","DELETE","OPTIONS","PATCH","HEAD"])
async def getHandler(request):
    """
    This function reads all headers from the request and returns them as a dictionary.
    """
    headers = {}
    headers["method"] = request.method
    headers["headers"] = dict(request.headers.items())
    return json(headers)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
