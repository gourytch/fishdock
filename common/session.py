import dataclasses
import datetime
import logging
import typing


logger = logging.getLogger(__name__)


class Session(dataclasses.dataclass()):
    user: str
    token: str
    role: str
    logged_at: datetime.datetime
    expired_at: datetime.datetime


class SessionStorage:
    def __init__(self, db):
        self._db = db
        return

    async def get_by_token(self, token) -> typing.Optional[Session]:
        rows = await self._db.request("""
            SELECT user,
                   role,
                   logged_at,
                   expired_at
              FROM sessions
             WHERE token = $1
        """, token)
        if rows:
            for row in rows:
                return Session(user=row['user'],
                               token=token,
                               role=row['role'],
                               logged_at=row['logged_at'],
                               expired_at=row['expired_at'])
        logger.info('token not found: %s', token)
        return None
