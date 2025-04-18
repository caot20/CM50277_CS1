/*
Source: https://www.iban.com/country-codes
*/

INSERT OR IGNORE INTO countries (country_code_id, alpha_2, alpha_3, country)
VALUES (818, 'EG', 'EGY', 'Egypt'),
(724, 'ES', 'ESP', 'Spain'),
(250, 'FR', 'FRA', 'France'),
(826, 'GB', 'GBR', 'United Kingdom'),
(372, 'IE', 'IRL', 'Ireland'),
(528, 'NL', 'NLD', 'Netherlands'),
(620, 'PT', 'PRT', 'Portugal'),
(792, 'TR', 'TUR', 'Türkiye');

INSERT OR IGNORE INTO timezones (timezone, utc_offset)
VALUES ('Africa/Cairo', 2.0),
('Atlantic/Canary', 1.0),
('Europe/Amsterdam', 2.0),
('Europe/Dublin', 1.0),
('Europe/Istanbul', 3.0),
('Europe/Lisbon', 1.0),
('Europe/London', 1.0),
('Europe/Madrid', 2.0),
('Europe/Paris', 2.0);

INSERT OR IGNORE INTO pilot_positions (pilot_position_id, position)
VALUES (0, 'Captain'),
(1, 'First Officer');

INSERT OR IGNORE INTO pilots (
    pilot_position_id,
    name,
    passport_number,
    nationality
)
VALUES (0, 'Amelia Earhart', 'US1234567', 'American'),
(1, 'Chesley Sullenberger', 'US1234568', 'American'),
(0, 'Yuri Gagarin', 'RU9244568', 'Soviet'),
(1, 'Manfred von Richthofen', 'DE8234768', 'German'),
(0, 'Frank Whittle', 'GB1112223', 'British'),
(1, 'Amy Johsoon', 'GB3325489', 'British'),
(0, 'Amme McClain', 'US1123478', 'American'),
(1, 'Nicole Ayers', 'US8134791', 'American'),
(0, 'Takuya Onishi', 'JP4244573', 'Japan'),
(1, 'Peggy Whitson', 'US6546847', 'American'),
(0, 'Shubhanshu Shukla', 'IN6549687', 'India'),
(1, 'Tibor Kapu', 'HG4632871', 'Hungarian'),
(0, 'Helen Sharman', 'GB0478398', 'British'),
(1, 'Tim Peake', 'GB2546503', 'British'),
(0, 'Michael Foale', 'GB2821518', 'British'),
(1, 'Rosemary Coogan', 'GB3052850', 'British'),
(0, 'Wang Haoze', 'CN9348314', 'China'),
(1, 'John McFall', 'GB6751757', 'British'),
(0, 'Namira Salim', 'PK1649942', 'Pakistan'),
(1, 'Jonny Kim', 'KR2656561', 'South Korea');

INSERT OR IGNORE INTO destinations (
    iata_code,
    icao_code,
    latitude,
    longitude,
    description,
    area,
    timezone_id,
    country_code_id
)
VALUES ('BRS', 'EGGD', 51.3827019, -2.71909, 'Bristol Airport', 'Bristol', 7, 826),
('AMS', 'EHAM', 52.3086014, 4.7638898, 'Amsterdam Schiphol Airport', 'Amsterdam', 3, 528),
('DUB', 'EIDW', 53.421299, -6.2700701, 'Dublin Airport', 'Dublin', 4, 372),
('EDI', 'EGPH', 55.9500008, -3.3724999, 'Edinburgh Airport', 'Edinburgh', 7, 826),
('GLA', 'EGPF', 55.8718987, -4.4330602, 'Glasgow International Airport', 'Glasgow', 7, 826),
('PMI', 'LEPA', 39.5517006, 2.7388101, 'Palma De Mallorca Airport', 'Palma De Mallorca', 8, 724),
('AGP', 'LEMG', 36.6749001, -4.4991102, 'Málaga Airport', 'Málaga', 8, 724),
('ALC', 'LEAL', 38.2821999, -0.558156, 'Alicante International Airport', 'Alicante', 8, 724),
('FAO', 'LPFR', 37.0144005, -7.96591, 'Faro Airport', 'Faro', 6, 620),
('TFS', 'GCTS', 28.0445004, -16.5725002, 'Tenerife South Airport', 'Tenerife Island', 2, 724),
('ACE', 'GCRR', 28.9454994, -13.6051998, 'Lanzarote Airport', 'Lanzarote Island', 2, 724),
('AYT', 'LTAI', 36.8987007, 30.8005009, 'Antalya International Airport', 'Antalya', 5, 792),
('DLM', 'LTBS', 36.7131004, 28.7924995, 'Dalaman International Airport', 'Dalaman', 5, 792),
('BCM', 'LEBL', 41.2971001, 2.07846, 'Barcelona International Airport', 'Barcelona', 8, 724),
('CDG', 'LFPG', 49.0127983, 2.55, 'Charles De Gaulle International Airport', 'Paris', 9, 250),
('HRG', 'HEGN', 27.1783009, 33.7994003, 'Hurghada International Airport', 'Hurghada', 1, 818);

INSERT OR IGNORE INTO flights (
    flight_number,
    origin_id,
    origin_scheduled_departure_time_utc,
    destination_id,
    destination_scheduled_arrival_time_utc,
    scheduled_pilot_1,
    scheduled_pilot_2
)
VALUES ('BU001', 2, DATETIME('now', '-4 hours'), 1, DATETIME('now', '-3 hours'), 1, 2),
('BU001', 1, DATETIME('now', '+4 hours'), 2, DATETIME('now', '+5.2 hours'), 1, 2),
('BU003', 1, DATETIME('now', '+4.5 hours'), 3, DATETIME('now', '+5.7 hours'), 3, 4),
('BU005', 1, DATETIME('now', '+5 hours'), 4, DATETIME('now', '+6.15 hours'), 5, 6),
('BU007', 1, DATETIME('now', '+5.5 hours'), 5, DATETIME('now', '+6.65 hours'), 7, 8),
('BU009', 1, DATETIME('now', '+6 hours'), 6, DATETIME('now', '+8.2 hours'), 9, 10),
('BU011', 1, DATETIME('now', '+6.5 hours'), 7, DATETIME('now', '+8.9 hours'), 11, 12),
('BU013', 1, DATETIME('now', '+7 hours'), 8, DATETIME('now', '+9.25 hours'), 13, 14),
('BU015', 1, DATETIME('now', '+7.5 hours'), 9, DATETIME('now', '+9.9 hours'), 15, 16),
('BU017', 1, DATETIME('now', '+8 hours'), 10, DATETIME('now', '+12.2 hours'), 17, 18),
('BU019', 1, DATETIME('now', '+8.5 hours'), 11, DATETIME('now', '+12.5 hours'), 19, 20),
('BU002', 2, DATETIME('now', '+5.65 hours'), 1, DATETIME('now', '+6.85 hours'), 1, 2),
('BU004', 3, DATETIME('now', '+4.65 hours'), 1, DATETIME('now', '+5.85 hours'), 3, 4),
('BU006', 4, DATETIME('now', '+6.6 hours'), 1, DATETIME('now', '+7.75 hours'), 5, 6),
('BU008', 5, DATETIME('now', '+8.6 hours'), 1, DATETIME('now', '+9.75 hours'), 7, 8),
('BU010', 6, DATETIME('now', '+11.65 hours'), 1, DATETIME('now', '+13.85 hours'), 9, 10),
('BU012', 7, DATETIME('now', '+13.85 hours'), 1, DATETIME('now', '+16.25 hours'), 11, 12),
('BU014', 8, DATETIME('now', '+15.7 hours'), 1, DATETIME('now', '+17.95 hours'), 13, 14),
('BU016', 9, DATETIME('now', '+17.85 hours'), 1, DATETIME('now', '+20.25 hours'), 15, 16),
('BU018', 10, DATETIME('now', '+21.65 hours'), 1, DATETIME('now', '+25.85 hours'), 17, 18),
('BU020', 11, DATETIME('now', '+23.45 hours'), 1, DATETIME('now', '+27.45 hours'), 19, 20);
