PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS countries (
    country_code_id INT NOT NULL,
    alpha_2 CHAR(2) NOT NULL,
    alpha_3 CHAR(3) NOT NULL,
    country VARCHAR(100) NOT NULL,
    CONSTRAINT pk_countries PRIMARY KEY (country_code_id),
    CONSTRAINT uq_alpha_2 UNIQUE (alpha_2),
    CONSTRAINT uq_alpha_3 UNIQUE (alpha_3),
    CONSTRAINT uq_country UNIQUE (country)
);


CREATE TABLE IF NOT EXISTS timezones (
    timezone_id INTEGER NOT NULL,
    timezone VARCHAR(100) NOT NULL,
    utc_offset REAL NOT NULL CONSTRAINT df_utc_offset DEFAULT (0.0),
    CONSTRAINT pk_timezones PRIMARY KEY (timezone_id),
    CONSTRAINT uq_timezone UNIQUE (timezone)
);

CREATE TABLE IF NOT EXISTS pilot_positions (
    pilot_position_id INT NOT NULL,
    position VARCHAR(50) NOT NULL,
    CONSTRAINT pk_pilot_positions PRIMARY KEY (pilot_position_id)
);

CREATE TABLE IF NOT EXISTS pilots (
    pilot_id INTEGER NOT NULL,
    pilot_position_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    passport_number VARCHAR(20) NOT NULL,
    nationality VARCHAR(50) NOT NULL,
    CONSTRAINT pk_pilots PRIMARY KEY (pilot_id),
    CONSTRAINT uq_passport_number UNIQUE (passport_number),
    CONSTRAINT fk_pilot_position_id__pilot_positions
    FOREIGN KEY (pilot_position_id)
    REFERENCES pilot_positions (pilot_position_id)
    ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS destinations (
    destination_id INTEGER NOT NULL,
    iata_code CHAR(3) NOT NULL,
    icao_code CHAR(4) NOT NULL,
    latitude REAL NOT NULL CONSTRAINT df_latitude DEFAULT (0.0),
    longitude REAL NOT NULL CONSTRAINT df_longitude DEFAULT (0.0),
    description VARCHAR(100) NOT NULL,
    area VARCHAR(50) NOT NULL,
    timezone_id INT NOT NULL,
    country_code_id INT NOT NULL,
    CONSTRAINT pk_destinations PRIMARY KEY (destination_id),
    CONSTRAINT uq_iata_code UNIQUE (iata_code),
    CONSTRAINT uq_icao_code UNIQUE (icao_code),

    CONSTRAINT fk_timezone_id__timezones
    FOREIGN KEY (timezone_id)
    REFERENCES timezones (timezone_id)
    ON DELETE SET NULL,

    CONSTRAINT fk_country_code_id__countries
    FOREIGN KEY (country_code_id)
    REFERENCES countries (country_code_id)
    ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS flights (
    flight_id INTEGER NOT NULL,
    flight_number CHAR(5) NOT NULL,
    origin_id INT NOT NULL,
    origin_scheduled_departure_time_utc TEXT NOT NULL,
    destination_id INT NOT NULL,
    destination_scheduled_arrival_time_utc TEXT NOT NULL,
    scheduled_pilot_1 INT NOT NULL,
    scheduled_pilot_2 INT NOT NULL,
    CONSTRAINT pk_flights PRIMARY KEY (flight_id),

    CHECK (destination_scheduled_arrival_time_utc > origin_scheduled_departure_time_utc),

    CONSTRAINT fk_origin_id__destinations
    FOREIGN KEY (destination_id)
    REFERENCES destinations (destination_id)
    ON DELETE SET NULL,

    CONSTRAINT fk_destination_id__destinations
    FOREIGN KEY (destination_id)
    REFERENCES destinations (destination_id)
    ON DELETE SET NULL,

    CONSTRAINT fk_scheduled_pilot_1__pilots
    FOREIGN KEY (scheduled_pilot_1)
    REFERENCES pilots (pilot_id)
    ON DELETE SET NULL,

    CONSTRAINT fk_scheduled_pilot_2__pilots
    FOREIGN KEY (scheduled_pilot_2)
    REFERENCES pilots (pilot_id)
    ON DELETE SET NULL
);


-- PRAGMA foreign_key_check;
