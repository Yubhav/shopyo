from flask import flash, redirect, url_for
from flask_login import current_user
from functools import wraps

from addon import login_manager
from modules.admin.models import Users

login_manager.login_view = 'login.login'
login_manager.login_message = 'Please login for access'


@login_manager.user_loader
def load_user(id):
    return Users.query.get(id)


def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if current_user.admin_user is True:
            return f(*args, **kwargs)
        else:
            flash("You need to be an admin to view this page.")
            return redirect(url_for('manufac.manufac'))

    return wrap
