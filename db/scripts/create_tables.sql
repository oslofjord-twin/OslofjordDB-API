CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE IF NOT EXISTS salinity (
    record_time timestamptz,
    record_number int,
    sensor_status varchar(50),
    conductivity numeric(10, 2),
    temperature numeric(10, 2),
    location GEOGRAPHY(POINT, 4326)
);

CREATE TABLE IF NOT EXISTS turbidity (
    record_time timestamptz,
    record_number int,
    sensor_status varchar(50),
    turbidity numeric(10, 2),
    temperature numeric(10, 2),
    txc_amp numeric(10, 2),
    c1_amp numeric(10, 2),
    c2_amp numeric(10, 2),
    raw_temp numeric(10, 2),
    location GEOGRAPHY(POINT, 4326)
);

SET timezone = "Europe/Oslo";

CREATE TABLE grid AS
SELECT * FROM ST_SquareGrid(0.05, ST_MakeEnvelope(10, 59, 11, 59.95, 4326));

ALTER TABLE grid
ADD column id SERIAL PRIMARY KEY;

CREATE TABLE IF NOT EXISTS simulations (
    record_time timestamptz,
    conductivity numeric(10, 2),
    temperature numeric(10, 2),
    turbidity numeric(10, 2),
    location GEOGRAPHY(POINT, 4326)
);

