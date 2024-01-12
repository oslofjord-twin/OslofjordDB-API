CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE salinity (
    record_time timestamptz,
    record_number int,
    sensor_status varchar(50),
    conductivity numeric(10, 2),
    temperature numeric(10, 2),
    location GEOGRAPHY(POINT, 4326)
);

CREATE TABLE turbidity (
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