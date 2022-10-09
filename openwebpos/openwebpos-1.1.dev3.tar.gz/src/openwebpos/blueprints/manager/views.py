from flask import Blueprint, render_template
from flask_login import login_required

from openwebpos.blueprints.user.decorators import manager_required

bp = Blueprint('manager', __name__, template_folder='templates',
               url_prefix='/manager')


@login_required
@manager_required
@bp.before_request
def before_request():
    """
    Protects all the manager endpoints.
    """
    pass


@bp.get('/')
def index():
    """
    Render the manager index page.
    """
    return render_template('manager/index.html', title='Manager')
