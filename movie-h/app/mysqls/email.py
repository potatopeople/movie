from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from flask import current_app
from app.modules.user import User

def check_email(email):
    engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])
    Session = sessionmaker(bind=engine)
    session = Session()
    user_email = session.query(User).filter(User.email == email).first()
    session.close()
    return user_email