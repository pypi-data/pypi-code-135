from datetime import datetime

from flask_login import UserMixin
from usernames import is_safe_username
from werkzeug.security import generate_password_hash, check_password_hash

from openwebpos.extensions import db
from openwebpos.utils import gen_urlsafe_token
from openwebpos.utils.sql import SQLMixin


class Permission:
    """
    Permission class for defining permissions for users.
    """
    USER = 1
    CUSTOMER = 2
    STAFF = 4
    MANAGER = 8
    ADMIN = 80


class Role(SQLMixin, db.Model):
    """
    Role model for defining roles for users.
    """
    __tablename__ = 'roles'

    name = db.Column(db.String(100), nullable=False, unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0

    @staticmethod
    def insert_roles():
        """
        Add roles to the database.
        """
        roles = {
            'User': [Permission.USER],
            'Customer': [Permission.USER, Permission.CUSTOMER],
            'Staff': [Permission.USER, Permission.CUSTOMER, Permission.STAFF],
            'Manager': [Permission.USER, Permission.CUSTOMER, Permission.STAFF,
                        Permission.MANAGER],
            'Admin': [Permission.USER, Permission.CUSTOMER, Permission.STAFF,
                      Permission.MANAGER, Permission.ADMIN]
        }
        default_role = 'User'
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.reset_permissions()
            for perm in roles[r]:
                role.add_permission(perm)
            role.default = (role.name == default_role)
            role.save()

    def add_permission(self, perm):
        """
        Add a permission to the role.

        Args:
            perm (int): Permission to add.

        Returns:
            None
        """
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        """
        Remove a permission from the role.

        Args:
            perm (int): Permission to remove.

        Returns:
            None
        """
        if self.has_permission(perm):
            self.permissions -= perm

    def reset_permissions(self):
        """
        Reset role permissions.
        """
        self.permissions = 0

    def has_permission(self, perm):
        """
        Check if the role has a specific permission.

        Args:
            perm (int): Permission to check.

        Returns:
            bool: True if the role has the permission, False otherwise.
        """
        return self.permissions & perm == perm

    def __repr__(self):
        return '<Role %r>' % self.name


# TODO: secure user pin
class User(UserMixin, SQLMixin, db.Model):
    """
    User model for defining users.
    """
    __tablename__ = "user"

    public_id = db.Column(db.String(25), unique=True)

    # Authentication
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    username = db.Column(db.String(120), unique=True, index=True)
    email = db.Column(db.String(128), unique=True, index=True)
    password = db.Column(db.String(120), nullable=False, server_default='')
    pin = db.Column(db.String(120))
    active = db.Column('is_active', db.Boolean(), nullable=False,
                       server_default='1')

    # One-to-One relationships
    profile = db.relationship('UserProfile', backref='user', lazy=True,
                              uselist=False)
    activity = db.relationship('UserActivity', backref='user', lazy=True,
                               uselist=False)
    staff = db.relationship('Staff', backref='user', lazy=True, uselist=False)

    @staticmethod
    def insert_user():
        """
        Insert default user in the database.
        """
        Role.insert_roles()
        user = User(username='admin',
                    email='admin@mail.com',
                    password=generate_password_hash('admin'),
                    pin='1234',
                    role_id=Role.query.filter_by(name='Admin').first().id)
        user.save()

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.public_id is None:
            self.public_id = gen_urlsafe_token(25)

        if self.role_id is None:
            self.role_id = Role.query.filter_by(
                name='User').first().id  # default role

        if self.role_id in [Role.query.filter_by(name='Staff').first().id,
                            Role.query.filter_by(name='Manager').first().id,
                            Role.query.filter_by(name='Admin').first().id]:
            Staff.initialize_staff()

    def set_password(self, password):
        """
        Set user password.

        Args:
            password (str): Password to set.

        Returns:
            None
        """
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """
        Check if the password is correct.

        Args:
            password (str): Password to check.

        Returns:
            bool: True if the password is correct, False otherwise.
        """
        return check_password_hash(password, self.password)

    def check_pin(self, pin):
        return check_password_hash(pin, self.pin)

    def check_if_safe_username(self):
        return is_safe_username(self.username)

    def is_active(self):
        """
        Return whether user account is active.

        Returns:
            bool: True if user account is active, False otherwise.
        """
        return self.active

    def is_admin(self):
        """
        Check if user is admin.

        Returns:
            bool: True if user is admin, False otherwise.
        """
        return self.role_id == Role.query.filter_by(name='Admin').first().id

    def is_manager(self):
        """
        Check if user is manager.

        Returns:
            bool: True if user is manager, False otherwise.
        """
        return self.role_id == Role.query.filter_by(name='Manager').first().id

    def can(self, perm):
        """
        Check if the user has a specific permission.

        Args:
            perm (int): Permission to check.

        Returns:
            bool: True if user has permission, False otherwise.
        """
        return self.role is not None and self.role.has_permission(perm)


class UserProfile(SQLMixin, db.Model):
    """
    User profile model.
    """
    __tablename__ = "user_profile"

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    picture = db.Column(db.String(255), nullable=True, default='default.png')
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    address = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    zip_code = db.Column(db.String(120))
    dob = db.Column(db.DateTime)

    def __init__(self, **kwargs):
        super(UserProfile, self).__init__(**kwargs)

    def __repr__(self):
        return '<UserProfile %r>' % self.id


class UserActivity(SQLMixin, db.Model):
    """
    User activity model.
    """
    __tablename__ = "user_activity"

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    sign_in_count = db.Column(db.Integer, nullable=False, default=0)
    current_sign_in_at = db.Column(db.DateTime, nullable=True)
    current_sign_in_ip = db.Column(db.String(100), nullable=True)
    last_sign_in_at = db.Column(db.DateTime, nullable=True)
    last_sign_in_ip = db.Column(db.String(100), nullable=True)
    user_agent = db.Column(db.String(120))
    referrer = db.Column(db.String(120))

    def __init__(self, **kwargs):
        super(UserActivity, self).__init__(**kwargs)

    def __repr__(self):
        return '<Tracking %r>' % self.id

    def update_activity(self, ip_address: str, user_id: int):
        """
        Update the fields associated with user activity tracking.

        Args:
            ip_address: IP address of the user.
            user_id: ID of the user.

        Returns:
            None
        """
        self.user_id = user_id
        self.last_sign_in_at = self.current_sign_in_at
        self.last_sign_in_ip = self.current_sign_in_ip
        self.current_sign_in_at = datetime.utcnow()
        self.current_sign_in_ip = ip_address
        if self.sign_in_count is None:
            self.sign_in_count = 1
        else:
            self.sign_in_count += 1

        return self.save()


class Staff(SQLMixin, db.Model):
    """
    Staff model.
    """
    __tablename__ = "staff"

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    password = db.Column(db.String(120), nullable=False, server_default='1234')
    pay_rate = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=True)
    active = db.Column(db.Boolean, nullable=False, default=True)

    def set_password(self, password):
        """
        Set staff password.

        Args:
            password (str): Password to set.

        Returns:
            None
        """
        self.password = generate_password_hash(password)

    @staticmethod
    def initialize_staff(user_id: int = None):
        """
        Initialize staff table.

        Returns:
            None
        """
        if user_id is None:
            user_id = 1
        staff = Staff(
            user_id=user_id,
            pay_rate=10.00,
            start_date=datetime.utcnow()
        )
        staff.set_password('1234')
        staff.save()

    def __init__(self, **kwargs):
        super(Staff, self).__init__(**kwargs)

    def __repr__(self):
        return '<Staff %r>' % self.id
