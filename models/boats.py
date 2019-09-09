import dataclasses
import datetime


class Boat(dataclasses.dataclass(frozen=True)):
    passport_id: str  # паспортный идентификатор катера
    name: str  # название катера
    weight: int  # водоизмещение
    power: int  # мощность силовой установки
    build_date: datetime.date  # дана постройки
