from openwebpos.extensions import db
from openwebpos.utils.sql import SQLMixin


class Company(db.Model, SQLMixin):
    """
    Company model
    """
    __tablename__ = 'company'

    name = db.Column(db.String(255), nullable=False)
    locations = db.relationship('CompanyLocation', backref='company', lazy=True)

    def __init__(self, **kwargs):
        super(Company, self).__init__(**kwargs)


class CompanyLocation(db.Model, SQLMixin):
    """
    Company Location model
    """
    __tablename__ = 'company_locations'

    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(255), nullable=False)
    zipcode = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    fax = db.Column(db.String(255))
    email = db.Column(db.String(255))

    # Relationships
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'),
                           nullable=False)
    printers = db.relationship('CompanyPrinter', backref='company_locations',
                               lazy=True)

    def __init__(self, **kwargs):
        super(CompanyLocation, self).__init__(**kwargs)

    def __repr__(self):
        return '<CompanyLocation %r>' % self.name


class CompanyPrinter(db.Model, SQLMixin):
    """
    Company Printer model
    """
    __tablename__ = 'company_printers'

    name = db.Column(db.String(255), nullable=False)
    ip = db.Column(db.String(255), nullable=False)
    port = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False, default='offline')
    active = db.Column(db.Boolean, nullable=False, default=True)

    # Relationships
    company_location_id = db.Column(db.Integer,
                                    db.ForeignKey('company_locations.id'),
                                    nullable=False)

    def __init__(self, **kwargs):
        super(CompanyPrinter, self).__init__(**kwargs)

    def __repr__(self):
        return '<CompanyPrinter %r>' % self.name
