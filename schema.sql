CREATE TABLE inout (
    datePosted TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    product VARCHAR(200) NOT NULL,
    cityTo VARCHAR(200) NOT NULL,
    cityFrom VARCHAR(200) NOT NULL,
    amount INT NOT NULL
);

CREATE TABLE lagersaldo (
    product VARCHAR(200) NOT NULL,
    city VARCHAR(200) NOT NULL,
    cityID INT NOT NULL,
    amount INT NOT NULL
);

CREATE TABLE products (
    ID VARCHAR(200) NOT NULL,
    product VARCHAR(200) NOT NULL,
    price INT NOT NULL
);

CREATE TABLE cities (
    cityID INT NOT NULL,
    city VARCHAR(200)
  );
