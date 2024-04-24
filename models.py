from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Create user table
class Users(db.Model):
  __tablename__ = 'users'

  email = db.Column(db.String, primary_key=True)
  password = db.Column(db.String(500))
  role = db.Column(db.String(500))
  