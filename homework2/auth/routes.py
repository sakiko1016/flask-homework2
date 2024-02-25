from flask import Blueprint, render_template, redirect, url_for
from .forms import SignupForm
from .models import User, db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        new_user = User(email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.home'))  # Redirect to home page after signup
    return render_template('signup.html', form=form)