from ..utils import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.Text(), nullable=False)
    api_key = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return f"<User{self.username}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    # @classmethod
    # def find_user_by_api_key(cls, api_key):
    #     return cls.User.query.filter_by(api_key=api_key).first()
