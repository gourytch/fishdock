import dataclasses
import datetime


class CrewMember(dataclasses.dataclass(frozen=True)):
    """
    Первичный документ: Член Команды Рыболовецкого Судна
    """
    fullname: str  # Фамилия Имя Отчество члена команды
    position: str  # Должность
    phone: str  # Телефон
    birth_date: datetime.date  # Дата рождения
    boat_name: str  # Название катера
    boat_power: int  # мощность двигателя
    boat_build_date: datetime.date  # дата постройки
    boat_weight: int  # вес катера
