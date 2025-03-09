import os
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///./board_game.db') # Allow overriding via env var

Base = declarative_base()

class Content(Base):
    __tablename__ = 'content'
    id = Column(Integer, primary_key=True)
    square_id = Column(Integer, unique=True, nullable=False)
    paragraph = Column(Text, nullable=False)

    def __repr__(self):
        return f"<Content(square_id={self.square_id}, paragraph={self.paragraph})>"

def get_square_content(square_id, session):
    try:
        content = session.query(Content).filter_by(square_id=square_id).first()
        return content.paragraph if content else "No content found for this square."
    except SQLAlchemyError as e:
        print(f"Database error: {e}")
        return "Database error. Please try again later."

def init_db(db_url):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)


Session = init_db(DATABASE_URL)
