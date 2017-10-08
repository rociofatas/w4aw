from flask import Blueprint, request, session, url_for, redirect, render_template

from src.models.users.user import User
import src.models.users.errors as UserErrors
# import src.models.users.decorators as user_decorators
# from src.models.wishes import wish

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            if User.is_login_valid(email, password):
                session['email'] = email
                return redirect(url_for(".user_wishes"))
        except UserErrors.UserError as e:
            return e.message

    return render_template('users/login.jinja2')  # Send the user an error if their login was invalid


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        wish = request.form['wish']
        wish_keyword = request.form['wish_keyword']

        try:
            if User.register_user(email, password, wish, wish_keyword):
                session['email'] = email
                return redirect(url_for("wishes.index"))
        except UserErrors.UserError as e:
            return e.message

    return render_template('users/register.jinja2')  # Send the user an error if their login was invalid


@user_blueprint.route('/wishes')
def user_wishes():
    user = User.find_by_email(session['email'])
    wishes = user.get_wishes(session['email'])
    return render_template('wishes/wish_page.jinja2', user=user, wishes=wishes)

# @user_blueprint.route('/alerts')
# @user_decorators.requires_login
# def user_alerts():
#     user = User.find_by_email(session['email'])
#     alerts = user.get_alerts()
#     return render_template('users/alerts.jinja2', alerts=alerts)


@user_blueprint.route('/logout')
def logout_user():
    session['email'] = None
    return redirect(url_for('home'))


# @user_blueprint.route('/check_alerts/<string:user_id>')
# def check_user_alerts(user_id):
#     pass
