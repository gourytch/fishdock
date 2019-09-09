from aiohttp import web


async def handle_stub(request):
    return web.Response(text='stub handler called')

app = web.Application()
app.add_routes([
    web.get('/', handle_stub)
])

if __name__ == '__main__':
    web.run_app(app)
