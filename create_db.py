from app import db

db.create_all()
print('Database {} created successfully'.format(db.engine.url))
