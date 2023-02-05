from aiohttp import web
from utils.starters.route_manager import RouteManager

if __name__ == '__main__':
    app = web.Application()
    RouteManager(app).define_routers()
    web.run_app(app, port=8000)