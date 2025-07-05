from sqlmodel import SQLModel, create_engine
DATABASE_URL = "mysql+mysqlconnector://root:@localhost/4thewords_prueba_Daniela_Araya"

engine = create_engine(DATABASE_URL)

def create_db_and_tables():
      SQLModel.metadata.create_all(engine)
  