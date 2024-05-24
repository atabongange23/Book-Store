from  config import db

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=False, nullable=False)
    author = db.Column(db.String(200), unique=False, nullable=False)
    category = db.Column(db.String(200), unique=False, nullable=False)
    description = db.Column(db.String(1000), unique=False, nullable=False)
    image = db.Column(db.String(200), unique=False, nullable=False)
    price = db.Column(db.Integer, unique=False, nullable=False)
    
    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "catergory": self.category,
            "description": self.description,
            "image": self.image,
            "price": self.price
        }
    