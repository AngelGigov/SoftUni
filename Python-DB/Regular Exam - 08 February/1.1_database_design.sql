-- Create brands table
CREATE TABLE brands (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

-- Create classifications table
CREATE TABLE classifications (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE
);

-- Create customers table
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    address VARCHAR(150) NOT NULL,
    phone VARCHAR(30) NOT NULL UNIQUE,
    loyalty_card BOOLEAN NOT NULL DEFAULT FALSE
);

-- Create items table
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity >= 0),
    price DECIMAL(12,2) NOT NULL CHECK (price > 0.00),
    description TEXT,
    brand_id INTEGER NOT NULL REFERENCES brands(id) ON DELETE CASCADE ON UPDATE CASCADE,
    classification_id INTEGER NOT NULL REFERENCES classifications(id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create orders table
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    customer_id INTEGER NOT NULL REFERENCES customers(id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create reviews table (with composite primary key)
CREATE TABLE reviews (
    customer_id INTEGER NOT NULL REFERENCES customers(id) ON DELETE CASCADE ON UPDATE CASCADE,
    item_id INTEGER NOT NULL REFERENCES items(id) ON DELETE CASCADE ON UPDATE CASCADE,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    rating DECIMAL(3,1) NOT NULL DEFAULT 0.0 CHECK (rating <= 10.0),
    PRIMARY KEY (customer_id, item_id)
);

-- Create orders_items junction table (with composite primary key)
CREATE TABLE orders_items (
    order_id INTEGER NOT NULL REFERENCES orders(id) ON DELETE CASCADE ON UPDATE CASCADE,
    item_id INTEGER NOT NULL REFERENCES items(id) ON DELETE CASCADE ON UPDATE CASCADE,
    quantity INTEGER NOT NULL CHECK (quantity >= 0),
    PRIMARY KEY (order_id, item_id)
);