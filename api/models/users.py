from ..utils import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integre(), primary_key=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.Text(), nullable=False)
    is_authorised = db.Column(db.Boolean(), default=False)


    s
    def __repr__(self):
        return f"<User{self.username}"
