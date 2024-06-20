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
  year_of_graduation = db.column(db.integer())
  previous_employment = db.Column(db.String(500))
  notifications = db.relationship('Notifications', backref='notifications', lazy=True)
  profiles = db.relationship('Profiles', backref='profile', lazy=True)
  applications = db.relationship('Applications', backref='applications', lazy=True)

  def __repr__(self):
    return f"<Users {self.name}>"

  # Create employer table
class Employers(db.Model):
  __tablename__ = 'employers'

  company_id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String,)
  password = db.Column(db.String(500))
  company_name = db.Column(db.String(500))
  location = db.Column(db.String(500))
  available_role = db.Column(db.String(500))
  website = db.Column(db.String(500))
  jobs = db.relationship('Jobs', backref='jobs', lazy=True)

  def __repr__(self):
    return f"<Employers {self.name}>"


    # Create profile table
class Profiles(db.Model):
  __tablename__ = 'profiles'

  profile_id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.email'), nullable=False)
  bio = db.Column(db.String) 
  location = db.Column(db.String)
  skills = db.Column(db.String)

  def __repr__(self):
    return f"<Profiles {self.name}>"


    # Create job table
class Jobs(db.Model):
  __tablename__ = 'jobs'

  job_id = db.Column(db.Integer, primary_key=True)
  company_id = db.Column(db.Integer, db.ForeignKey('employers.company_id'), nullable=False)
  title = db.Column(db.String(100))
  description = db.Column(db.String(500))
  location = db.Column(db.String(500))
  salary = db.Column(db.String(500))
  job_type = db.Column(db.String(500))
  applications = db.relationship('Applications', backref='applications', lazy=True)

  def __repr__(self):
    return f"<Jobs {self.name}>"

    # Create application table
class Applications(db.Model):
  __tablename__ = 'applications'

  application_id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.email'), nullable=False)
  job_id = db.Column(db.Integer, db.ForeignKey('jobs.job_id'), nullable=False)
  status = db.Column (db.String(500))

  def __repr__(self):
    return f"<Applications {self.name}>"


    # Create notification table
class Notifications(db.Model):
  __tablename__ = 'notifications'

  notification_id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.email'), nullable=False)
  message = db.Column(db.String)
  is_read = db.Column(db.Boolean(False))

  def __repr__(self):
    return f"<Notifications {self.name}>"


    # Admin table
class Admin(db.Model):
    __tablename__ = 'admin'

    admin_id = db.Column(db.Integer, primary_key=True)
    action_id = db.Column(db.Integer)
    action_type = db.Column(db.String(100))
    target_id = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def __repr__(self):
      return f"<Admin {self.name}>"
