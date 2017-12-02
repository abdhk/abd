from sqlalchemy.orm import sessionmaker
from model import db_connect, create_deals_table, Deals


class OpenSooqPipeline(object):
    def __init__ (self):
        engine = db_connect()
        create_deals_table(engine)
        self.Session = sessionmaker(bind=engine)


    def process_item(self, item, spider):
        session = self.Session()
        deal = Deals(**item)
        try:
            session.add(deal)
            session.commit()
        except Exception as e:
            session.rollback()
            raise

        finally:
            session.close()
        return item
        
        
