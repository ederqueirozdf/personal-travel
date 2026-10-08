CREATE TABLE IF NOT EXISTS searches (
    id SERIAL PRIMARY KEY,
    origin VARCHAR(255) NOT NULL,
    destination VARCHAR(255) NOT NULL,
    departure_date DATE,
    window_days INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS flight_offers (
    id SERIAL PRIMARY KEY,
    search_id INTEGER REFERENCES searches(id),
    airline VARCHAR(255),
    price_amount NUMERIC(12,2),
    currency VARCHAR(10),
    stops INTEGER,
    duration_minutes INTEGER,
    baggage_included BOOLEAN DEFAULT FALSE,
    source VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW()
);
