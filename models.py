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
  year_of_graduation = db.column(db.varchar(500))
  previous_employment = db.Column(db.String(500))

  # Create employer table
class employers(db.Model):
  __tablename__ = 'employers'

  company_id = db.column(db.int, primary_key=True)
  email = db.Column(db.String,)
  password = db.Column(db.String(500))
  company_name = db.Column(db.String(500))
  location = db.column(db.varchar(500))
  available_role = db.Column(db.String(500))
  website = db.column(db.varchar(500))


    # Create profile table
class profiles(db.Model):
  __tablename__ = 'profile'

  profile_id = db.column(db.int, primary_key=True)
  user_id = db.column(db.int, foreign_key=True)
  bio = db.column(db.string) 
  location = db.column(db.varchar)
  skills = db.column(db.string)


    # Create job table
class jobs(db.Model):
  __tablename__ = 'job'

  job_id = db.column(db.int, primary_key=True)
  company_id = db.column(db.int, foreign_key=True)
  title = db.column(db.varchar(100))
  description = db.column(db.varchar(500))
  location = db.column(db.varchar(500))
  salary = db.column(db.varchar(500))
  employer_id = db.column(db.int, foreign_key=True)
  job_type = db.column(db.varchar(job_type in ("full time", "part time", "contract", "internship")))


    # Create application table
class applications(db.Model):
  __tablename__ = 'application'

application_id = db.column(db.int, primary_key=True)
user_id = db.column(db.int, foreign_key=True)
job_id = db.column(db.int, foreign_key=True)
application_date = db.column (db.datetime)
status = db.column (db.text(status in ("applied", "under review", "interview", "offered", "rejected", "withdrawn")))


    # Create notification table
class notifications(db.Model):
  __tablename__ = 'notification'

  notification_id = db.column(db.int, primary_key=True)
  user_id = db.column(db.int, foreign_key=True)
  message = db.column(db.text)
  date = db.column(db.datetime)
  is_read = db.column(db.boolean(False))


    # Admin table
class admin(db.Model):
    __tablename__ = 'admin'

    action_id = db.column(db.int, primary_key=True)
    admin_id = db.column(db.int, foreign_key=True)
    action_type = db.column(db.varchar(100))
    target_id = db.column(db.int)
    date = db.column(db.datetime)


