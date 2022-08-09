from sqlalchemy import create_engine, MetaData #modulo para interactuar con una db sql a traves de funciones

engine = create_engine("mysql+pymysql://root:password@localhost:3306/database")

meta = MetaData()

conn = engine.connect() #cuando quiera interactuar con la db voy a llamar a la funcion conn