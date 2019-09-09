from aiohttp import web
from common import application


async def handle_stub(request):
    return web.Response(text='stub handler called')


app = application.Application()
app.add_routes([
    web.get('/', handle_stub)
])

if __name__ == '__main__':
    web.run_app(app)
