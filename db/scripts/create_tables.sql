CREATE SCHEMA IF NOT EXISTS alldata;

CREATE TABLE alldata.salinity (
    record_time timestamp,
    record_number int,
    sensor_status varchar(50),
    conductivity numeric(10, 2),
    temperature numeric(10, 2)
);

CREATE TABLE alldata.turbidity (
    record_time timestamp,
    record_number int,
    sensor_status varchar(50),
    turbidity numeric(10, 2),
    temperature numeric(10, 2),
    txc_amp numeric(10, 2),
    c1_amp numeric(10, 2),
    c2_amp numeric(10, 2),
    raw_temp numeric(10, 2)
);