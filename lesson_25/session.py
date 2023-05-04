from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy_utils import database_exists, create_database


engine = create_engine('postgresql://postgres:123@localhost/store')
if not database_exists(engine.url):
    create_database(engine.url)


session: Session = sessionmaker(engine)()
