CREATE TABLE products(
    product_name VARCHAR(1000)
);

INSERT INTO  products
VALUES
    ('Broccoli'),
    ('Shampoo'),
    ('Toothpaste'),
    ('Candy')
;

ALTER TABLE products
ADD COLUMN
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY;