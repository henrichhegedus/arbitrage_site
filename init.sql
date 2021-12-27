create schema arbitrage;

CREATE TABLE arbitrage.scrape(
                     ID SERIAL PRIMARY KEY,
                     bookie VARCHAR(20),
                     bet_id INTEGER UNIQUE,
                     event_date DATE,
                     event_time TIME,
                     sport VARCHAR(50),
                     competition VARCHAR(100),
                     team1 VARCHAR(200),
                     odds1 FLOAT(24),
                     oddsx FLOAT(24),
                     odds2 FLOAT(24)
);

CREATE TABLE arbitrage.arbs(
                     ID SERIAL PRIMARY KEY,
                     sport VARCHAR(50),
                     match VARCHAR(100),
                     date DATE,
                     time TIME,
                     odds1 FLOAT(24),
                     oddsx FLOAT(24),
                     odds2 FLOAT(24),
                     margin FLOAT(24),
                     bookie1 VARCHAR(50),
                     bookiex VARCHAR(50),
                     bookie2 VARCHAR(50),
                     CONSTRAINT date_match UNIQUE (date,match)

);

CREATE TABLE arbitrage.history(
                      max_date DATE,
                      sport VARCHAR(50),
                      match VARCHAR(100),
                      date DATE,
                      time TIME,
                      odds1 FLOAT(24),
                      oddsx FLOAT(24),
                      odds2 FLOAT(24),
                      margin FLOAT(24),
                      bookie1 VARCHAR(50),
                      bookiex VARCHAR(50),
                      bookie2 VARCHAR(50)
);