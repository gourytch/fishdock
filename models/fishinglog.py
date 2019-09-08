import dataclasses
import datetime


class FishingRecord(dataclasses.dataclass(frozen=True)):
    """
    Первичный документ: Журнал посещения рыболовной точки
    """
    start_trip: datetime.date  # дата выхода судна на лов
    end_trip: datetime.date  # дата возврата судна с лова
    catch_weight: int  # вес пойманной рыбы на рыболовной точке
    nodename: str  # название рыболовной точки
    start_fishing: datetime.date  # дата приход на рыболовную точку
    end_fishing: datetime.date  # дата ухода с рыболовной точки
    catch_quality: str  # качество рыбы
