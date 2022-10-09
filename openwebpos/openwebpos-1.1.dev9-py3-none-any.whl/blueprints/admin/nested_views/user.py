from flask import Blueprint, render_template, request

from openwebpos.blueprints.user.models import User, Role

from openwebpos.blueprints.user.forms import AddUserForm

bp = Blueprint('user', __name__, url_prefix='/user',
               template_folder='templates')


@bp.get('/')
def index():
    return render_template('admin/user/index.html')


@bp.get('/list')
def get_list():
    """
    Get a list of users
    """
    users_list = User.query.all()
    roles = Role.query.all()
    form = AddUserForm()
    return render_template('admin/user/list.html', users=users_list,
                           title='Users', form=form, roles=roles)


@bp.post('/add')
def add_user():
    """
    Add a user
    """
    form = AddUserForm()
    role = request.form['role']
    print(role)
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data,
                    role_id=role, pin='4321')
        user.set_password(form.password.data)
        user.save()
    return get_list()
