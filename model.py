from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative improt declarative_base
import settings


def db_connect():
    return create_engine(URL(**settings.DATABASE))


Declarative_base = declarative_base()

def create_deals_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class Deals(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "deals"

    id = Column(Integer, primary_key=True)
    city = Column('city', String)
    brand = Column('brand', String, nullable=True)
    model = Column('model', String, nullable=True)
    model_year = Column('model_year', String, nullable=True)
    status = Columns('status', String, nullable=True)
    gear_type = Column('gear_type', String, nullable=True)
    fuel_type = Column('fiel_type', String, nullable=True)
    color = Column('color', String, nullable=True)
    payment_type = Column('Payment_type', String, nullable=True)
    description = Column('description', String, nullable = True)
    




