from extensions import app, db, asc, desc, or_



book_list = []


def get_last_id():
    if book_list:
        last_book = book_list[-1]
    else:
        return 1
    return last_book.id + 1

class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    author = db.Column(db.String(200))
    is_publish = db.Column(db.Boolean(), default=False)
    cover_image = db.Column(db.String(100), default=None)
    
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())
    
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))

