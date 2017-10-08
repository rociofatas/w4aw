from flask import Blueprint, render_template, request, url_for, redirect
from src.models.wishes.wish import Wish


wish_blueprint = Blueprint('wishes', __name__)


@wish_blueprint.route('/')
def index():
    wishes = Wish.all()
    return render_template('wishes/wish_index.jinja2', wishes=wishes)


@wish_blueprint.route('/wish')
def wish_page(wish_id):
    return render_template('wishes/wish_page.jinja2', wish=Wish.get_by_id(wish_id))


@wish_blueprint.route('/new', methods=['GET', 'POST'])
def new_wish():

    if request.method == 'POST':
        print('testing')

        # keyword = request.form['keyword']
        # description = request.form['description']

        wish = Wish(wish, wish_keyword)
        wish.save_to_mongo()

        return redirect(url_for('.index'))

    # return "You are adding a new wish"
    return render_template('wishes/new_wish.jinja2')

