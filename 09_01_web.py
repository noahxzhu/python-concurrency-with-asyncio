from datetime import datetime

from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response

routes = web.RouteTableDef()


@routes.get("/time")
async def time(request: Request) -> Response:
    today = datetime.today()

    result = {"month": today.month, "day": today.day, "time": str(today.time())}

    return web.json_response(result)


@routes.get("/")
async def get_data(request: Request) -> Response:
    shared_data = request.app["shared_dict"]
    return web.json_response(shared_data)


app = web.Application()
app["shared_dict"] = {"key": "value"}
app.add_routes(routes)
web.run_app(app)
