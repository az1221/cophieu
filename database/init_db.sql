CREATE TABLE IF NOT EXISTS stock_prices (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_stock_prices_symbol ON stock_prices(symbol);

CREATE TABLE IF NOT EXISTS stock_info (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10) UNIQUE NOT NULL,
    company_name VARCHAR(255) NOT NULL,
    market_cap DECIMAL(15,2) NOT NULL
);

CREATE INDEX idx_stock_info_symbol ON stock_info(symbol);
