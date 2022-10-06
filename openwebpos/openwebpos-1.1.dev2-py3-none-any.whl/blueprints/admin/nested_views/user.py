from flask import Blueprint, render_template

from openwebpos.blueprints.user.models import User

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
    return render_template('admin/user/list.html', users=users_list,
                           title='Users')
