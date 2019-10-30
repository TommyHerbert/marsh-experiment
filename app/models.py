from app import db


class OwnerInterest(db.Model):
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), primary_key=True)
    interest_id = db.Column(db.Integer, db.ForeignKey('interest.id'), primary_key=True)
    active = db.Column(db.Boolean)
    interest = db.relationship('Interest', back_populates='owners')
    owner = db.relationship('Owner', back_populates='interests')


class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    mobile = db.Column(db.String)
    interests = db.relationship('OwnerInterest', back_populates='owner')

    def __repr__(self):
        return '<Owner {}>'.format(self.name)


class Interest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    owners = db.relationship('OwnerInterest', back_populates='interest')

    def __repr__(self):
        return '<Owner {}>'.format(self.name)

