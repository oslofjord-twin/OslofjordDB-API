CREATE EXTENSION IF NOT EXISTS postgis;

SET timezone = "Europe/Oslo";

CREATE TABLE IF NOT EXISTS salinity (
    record_time timestamptz NOT NULL,
    record_number int NOT NULL,
    sensor_status varchar(50),
    conductivity numeric(10, 2),
    temperature numeric(10, 2),
    location GEOGRAPHY(POINT, 4326),
    grid_id int,
    PRIMARY KEY (record_time, record_number)
);

CREATE TABLE IF NOT EXISTS turbidity (
    record_time timestamptz NOT NULL,
    record_number int NOT NULL,
    sensor_status varchar(50),
    turbidity numeric(10, 2),
    temperature numeric(10, 2),
    txc_amp numeric(10, 2),
    c1_amp numeric(10, 2),
    c2_amp numeric(10, 2),
    raw_temp numeric(10, 2),
    location GEOGRAPHY(POINT, 4326),
    grid_id int,
    PRIMARY KEY (record_time, record_number)
);

CREATE TABLE IF NOT EXISTS runtime_monitoring (
	id SERIAL PRIMARY KEY,
	request_id int NOT NULL,
	id_sim int NOT NULL,
	suitable_temperature boolean,
	suitable_spawning_temperature boolean,
	preferred_spawning_temperature boolean
);

CREATE TABLE IF NOT EXISTS requests (
	request_id SERIAL PRIMARY KEY,
	grid_id int NOT NULL,
	species_name TEXT NOT NULL,
	done boolean NOT NULL DEFAULT false
);

select create_hypertable('salinity', by_range('recorded_time', INTERVAL '1 day'));
select create_hypertable('turbidity', by_range('recorded_time', INTERVAL '1 day'));

CREATE TABLE grid AS
SELECT * FROM ST_SquareGrid(0.05, ST_MakeEnvelope(10, 59, 11, 59.95, 4326));

ALTER TABLE grid
ADD column id SERIAL PRIMARY KEY;

CREATE INDEX ON grid USING GIST(geom);

CREATE TABLE IF NOT EXISTS simulations (
    record_time timestamptz,
    conductivity numeric(10, 2),
    temperature numeric(10, 2),
    turbidity numeric(10, 2),
    location GEOGRAPHY(POINT, 4326),
    id_sim SERIAL PRIMARY KEY,
    grid_id int
);
