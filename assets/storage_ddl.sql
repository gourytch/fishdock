CREATE TABLE members(
    id SERIAL PRIMARY KEY COMMENT 'id записи',
    full_name VARCHAR(64) NOT NULL COMMENT 'фамилия имя отчество',
    birth_date DATE NOT NULL COMMENT 'дата рождения',
    position VARCHAR(64) NOT NULL COMMENT 'должность',
    phone CHAR(10) NOT NULL COMMENT 'телефон'
);

CREATE TABLE boats(
    id SERIAL PRIMARY KEY COMMENT 'id записи',
    passport VARCHAR(32) NOT NULL UNIQUE COMMENT 'номер паспорта',
    name VARCHAR(64) NOT NULL UNIQUE COMMENT 'название катера',
    weight INTEGER NOT NULL COMMENT 'собственный вес катера, кг.',
    power INTEGER NOT NULL COMMENT 'мощность силовой установки, л.c.',
    build_date DATE COMMENT 'дата постройки'
);

CREATE TABLE nodes(
    id SERIAL PRIMARY KEY COMMENT 'id рыболовной точки',
    name VARCHAR(32) NOT NULL COMMENT 'название рыболовной точки',
);

CREATE TABLE trips(
    id SERIAL PRIMARY KEY COMMENT 'id рейса',
    boat_id INTEGER REFERENCES boats(id) COMMENT 'id катера',
    begin_trip DATE NOT NULL COMMENT 'дата выхода в рейс',
    end_trip DATE COMMENT 'дата возврата из рейса'
);

CREATE TABLE quality_defs(
    id INTEGER PRIMARY KEY COMMENT 'id качества. 0 = высшее',
    name VARCHAR(20) NOT NULL UNIQUE COMMENT 'название'
);

CREATE TABLE tripcrews(
    trip_id INTEGER REFERENCES trips(id) COMMENT 'id рейса',
    member_id INTEGER REFERENCES members(id) COMMENT 'id члена экипажа'
);

CREATE TABLE tripnodes(
    trip_id INTEGER REFERENCES trips(id) COMMENT 'id рейса',
    node_id INTEGER REFERENCES nodes(id) COMMENT 'id рыболовной точки',
    begin_fishing DATE NOT NULL COMMENT 'дата прибытия на точку',
    end_fishing DATE COMMENT 'дата отбытия с точки',
    catch_weight DECIMAL(12, 3) COMMENT 'вес улова, кг.',
    catch_quality INTEGER REFERENCES quality_defs(id) COMMENT 'качество рыбы'
);

INSERT INTO quality_defs VALUES
    (0, 'отличное'),
    (1, 'хорошее'),
    (2, 'удовлетворительное',
    (3, 'плохое');

-- ФИО
-- Должность
-- Телефон
-- Дата рождения
-- Название катера
-- мощность двигателя
-- дата постройки
-- Вес катера
CREATE FUNCTION register_crew_member(
    fullname TEXT,
    position TEXT,
    phone TEXT,
    birth_date DATE,
    boat_name TEXT,
    boat_power INTEGER,
    build_date DATE,
    boat_weight INTEGER
) RETURNS INTEGER AS $$
DECLARE ret_id INTEGER
BEGIN
    RETURN ret_id;
END;
$$ LANGUAGE plpgsql
VOLATILE PARALLEL UNSAFE
;
