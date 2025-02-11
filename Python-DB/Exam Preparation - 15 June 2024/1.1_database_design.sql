CREATE TABLE accounts(
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username VARCHAR(30) UNIQUE NOT NULL,
    password VARCHAR(30) NOT NULL,
    email VARCHAR(50) NOT NULL,
    gender CHAR(1) NOT NULL CHECK (gender IN ('M', 'F')),
    age INTEGER NOT NULL,
    job_title VARCHAR(40) NOT NULL,
    ip VARCHAR(30) NOT NULL
);

CREATE TABLE addresses(
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    street VARCHAR(30) NOT NULL,
    town VARCHAR(30) NOT NULL,
    country VARCHAR(30) NOT NULL,
    account_id INTEGER NOT NULL REFERENCES accounts(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE photos(
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    description TEXT,
    capture_date TIMESTAMP NOT NULL,
    views INTEGER NOT NULL DEFAULT 0 CHECK ( views >= 0 ) -- CHECK
);

CREATE TABLE comments(
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    content VARCHAR(255) NOT NULL,
    published_on TIMESTAMP NOT NULL,
    photo_id INTEGER NOT NULL REFERENCES photos(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE accounts_photos(
    account_id INTEGER NOT NULL REFERENCES accounts(id) ON UPDATE CASCADE ON DELETE CASCADE,
    photo_id INTEGER NOT NULL REFERENCES photos(id) ON UPDATE CASCADE ON DELETE CASCADE,
    PRIMARY KEY (account_id, photo_id)
);

CREATE TABLE likes(
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    photo_id INTEGER NOT NULL REFERENCES photos(id) ON DELETE CASCADE ON UPDATE CASCADE,
    account_id INTEGER NOT NULL REFERENCES accounts(id) ON DELETE CASCADE ON UPDATE CASCADE
);