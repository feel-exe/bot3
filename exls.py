import os
import pandas as pd
import sqlite3
import xlrd

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


from config import DB_FILENAME_BOT

Base = declarative_base()

class MediaIds(Base):
    __tablename__ = 'Media ids'
    id = Column(Integer, primary_key=True)
    task_text = Column(String)
    job_number = Column(Integer)
    variant = Column(Integer)
    autor = Column(String)
    year = Column(Integer)
    exam_level = Column(String)
    school_subject = Column(String)
    download = Column(Integer)
    file_id = Column(String)
    filename = Column(String)
    # счетчик скачиваний до обновления id_file
    сountdown = Column(String)
    # счетчик всех скачиваний  full
    counter_full = Column(String)



engine = create_engine(f'sqlite:///{DB_FILENAME_BOT}')

if not os.path.isfile(f'./{DB_FILENAME_BOT}'):
    Base.metadata.create_all(engine)


session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


wb = pd.read_csv('bd_file_csv.xlsx')



con = sqlite3.connect('SolTask.db')
for sheet in wb:
    wb[sheet].to_sql(sheet,con,index=False)
con.commit()
con.close()