from app import app
from models import db, User

with app.app_context():
    db.create_all()
    admin = User(email='admin@example.com', password='123', is_admin=True)
    guest = User(email='guest@example.com', password='123')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
