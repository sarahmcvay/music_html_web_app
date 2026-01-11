-- The job of this file is to reset all of our important database tables.
-- and add any data that is needed for the tests to run.

-- Drop tables
DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

DROP TABLE IF EXISTS artists;
DROP SEQUENCE IF EXISTS artists_id_seq;

-- -- Recreate table
CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_year INTEGER,
    artist_id INTEGER
);

CREATE SEQUENCE IF NOT EXISTS artists_id_seq;
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    genre VARCHAR(255)
);

-- SEED INFORMATION ARTISTS
INSERT INTO artists (name, genre) VALUES ('Pixies', 'Rock');
INSERT INTO artists (name, genre) VALUES ('ABBA', 'Pop');
INSERT INTO artists (name, genre) VALUES ('Taylor Swift', 'Pop');
INSERT INTO artists (name, genre) VALUES ('Nina Simone', 'Jazz');

-- -- SEED INFORMATION ALBUMS
INSERT INTO albums (title, release_year, artist_id) VALUES ('Doolittle', 1989, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Surfa Rosa', 1988, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Waterloo', 1974, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Super Trouper', 1980, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Bossanova', 1990, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Lover', 2019, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Folklore', 2020, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('I Put a Spell on You', 1965, 4);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Baltimore', 1978, 4);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Here Comes the Sun', 1971, 4);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Fodder on My Wings', 1982, 4);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Ring Ring', 1973, 2);

-- ### To seed the Database
--     psql music_html_web_app < seeds/music_html_web_app.sql