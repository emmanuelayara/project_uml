from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Create user table
class Users(db.Model):
  __tablename__ = 'users'

  email = db.Column(db.String, primary_key=True)
  password = db.Column(db.String(500))
  first_name = db.Column(db.String(500))
  last_name = db.Column(db.String(500))
  role = db.Column(db.String(500))
  year_of_graduation = db.column(db.Integer(500))
  previous_employment = db.Column(db.String(500))

  # Create employer table
class Employers(db.Model):
  __tablename__ = 'employers'

  company_id = db.column(db.Integer, primary_key=True)
  email = db.Column(db.String,)
  password = db.Column(db.String(500))
  company_name = db.Column(db.String(500))
  location = db.column(db.String(500))
  available_role = db.Column(db.String(500))
  website = db.column(db.String(500))


    # Create profile table
class Profiles(db.Model):
  __tablename__ = 'profile'

  profile_id = db.column(db.integer, primary_key=True)
  user_id = db.column(db.integer, foreign_key=True)
  bio = db.column(db.String) 
  location = db.column(db.String)
  skills = db.column(db.String)


    # Create job table
class Jobs(db.Model):
  __tablename__ = 'job'

  job_id = db.column(db.integer, primary_key=True)
  company_id = db.column(db.integer, foreign_key=True)
  title = db.column(db.String(100))
  description = db.column(db.String(500))
  location = db.column(db.String(500))
  salary = db.column(db.String(500))
  employer_id = db.column(db.integer, foreign_key=True)
  job_type = db.column(db.String(job_type in ("full time", "part time", "contract", "internship")))


    # Create application table
class Applications(db.Model):
  __tablename__ = 'application'

application_id = db.column(db.integer, primary_key=True)
user_id = db.column(db.integer, foreign_key=True)
job_id = db.column(db.integer, foreign_key=True)
status = db.column (db.String(status in ("applied", "under review", "interview", "offered", "rejected", "withdrawn")))


    # Create notification table
class Notifications(db.Model):
  __tablename__ = 'notification'

  notification_id = db.column(db.integer, primary_key=True)
  user_id = db.column(db.integer, foreign_key=True)
  message = db.column(db.String)
  is_read = db.column(db.boolean(False))


    # Admin table
class Admin(db.Model):
    __tablename__ = 'admin'

    action_id = db.column(db.integer, primary_key=True)
    admin_id = db.column(db.integer, foreign_key=True)
    action_type = db.column(db.String(100))
    target_id = db.column(db.integer)
    date = db.column(db.datetime)


