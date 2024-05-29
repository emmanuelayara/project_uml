from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

  
# Create Users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Create Companies table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Companies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    website VARCHAR(200),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Create Jobs table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Jobs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    location VARCHAR(100),
    company_id INTEGER REFERENCES Companies(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Create Applications table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Applications (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(id),
    job_id INTEGER REFERENCES Jobs(id),
    cover_letter TEXT,
    status VARCHAR(50) DEFAULT 'pending',
    applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')