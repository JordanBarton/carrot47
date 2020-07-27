import sqlalchemy as db

engine = db.create_engine('sqlite:///census.sqlite')


print(engine.table_names())


connection = engine.connect()
metadata = db.MetaData()

census = db.Table("census",metadata, autoload=True, autoload_with=engine )

print(repr(census))