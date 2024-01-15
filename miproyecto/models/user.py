from miproyecto import db

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(50),nullable=False)
    passwords=db.Column(db.String(50),nullable=False)
    
    def __init__(self,username,passwords) -> None:
        self.username=username
        self.passwords=passwords
    def __repr__(self) -> str:
        return f'User:{self.username}'
