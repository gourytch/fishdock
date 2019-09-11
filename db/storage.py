import typing

import asyncpg

from common import assets


class Storage:
    def __init__(self, **kwargs):
        self._args = kwargs
        self._db = typing.Optional[asyncpg.Connection] = None
        pass

    async def connect(self) -> None:
        if self._db:
            return
        self._db = await asyncpg.connect(**self._args)

    async def exec(self, *args, **kwargs) -> None:

    async def create_db(self):
        ddl = assets.load('storage.ddl')
        await self.connect()
        async with self._db.transaction():
            await self.exec(ddl)
