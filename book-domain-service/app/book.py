from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Title %r>' % self.title

    def from_json(title_json):
        new_title = title_json.get('title')
        if new_title is None or new_title=='':
            raise ValueError('Please provide a title')
        return Book(title = new_title)

    def to_json(self):
        book_json = {
            'id' : self.id,
            'title': self.title
            }
        return book_json
