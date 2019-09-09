from aiohttp import web

from db import storage
from common import session


class Application(web.Application):
    def __init__(self):
        super(self)
        self._storage = storage.Storage()
        self._sessions = session.SessionStorage(self._storage)

    @property
    def storage(self) -> storage.Storage:
        return self._storage

    @property
    def sessions(self) -> session.SessionStorage:
        return self._sessions
