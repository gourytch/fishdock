import base64
from http import HTTPStatus

from cryptography import fernet
from aiohttp import web
from aiohttp_session import setup, get_session, new_session
from aiohttp_session.cookie_storage import EncryptedCookieStorage


def login_required(fn):
    async def wrapper(request, *args, **kwargs):
        app = request.app
        router = app.router
        session = await get_session(request)
        token = session.get('token')
        sdata = None
        if token:
            sdata = app.session.get_by_token(token)
        if not sdata:
            return web.HTTPFound(router['login'].url_for())
        app['session'] = sdata
        return await fn(request, *args, **kwargs)

    return wrapper
