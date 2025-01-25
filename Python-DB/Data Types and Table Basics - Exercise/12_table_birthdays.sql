CREATE TABLE minions_birthdays (
    id SERIAL UNIQUE NOT NULL,
    name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    age INT NOT NULL,
    present VARCHAR(100) DEFAULT 'No present yet' NOT NULL,
    party TIMESTAMPTZ NOT NULL
);