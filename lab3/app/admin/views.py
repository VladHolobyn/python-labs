from flask import redirect, request, url_for
from flask_login import current_user
from flask_admin import AdminIndexView


class AdminView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))
