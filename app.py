from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, User

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fixora_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fixora.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():

    workers = User.query.filter_by(role='worker').all()

    customers = User.query.filter_by(role='customer').all()

    return render_template(
        'dashboard.html',
        workers=workers,
        customers=customers
    )


@app.route('/workers')
def workers():

    worker_list = User.query.filter_by(role='worker').all()

    return render_template(
        'workers.html',
        workers=worker_list
    )


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form.get('email')

        password = request.form.get('password')

        user = User.query.filter_by(
            email=email,
            password=password
        ).first()

        if user:
            flash('Login Successful')
            return redirect(url_for('dashboard'))

        else:
            flash('Invalid Email or Password')

    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/register/worker', methods=['GET', 'POST'])
def worker_register():

    if request.method == 'POST':

        new_worker = User(

            full_name=request.form.get('full_name'),

            email=request.form.get('email'),

            phone=request.form.get('phone'),

            password=request.form.get('password'),

            role='worker',

            profession=request.form.get('profession'),

            experience=request.form.get('experience'),

            charges=request.form.get('charges')
        )

        db.session.add(new_worker)

        db.session.commit()

        flash('Worker Registered Successfully')

        return redirect(url_for('login'))

    return render_template('worker_register.html')


@app.route('/register/customer', methods=['GET', 'POST'])
def customer_register():

    if request.method == 'POST':

        new_customer = User(

            full_name=request.form.get('full_name'),

            email=request.form.get('email'),

            phone=request.form.get('phone'),

            password=request.form.get('password'),

            role='customer'
        )

        db.session.add(new_customer)

        db.session.commit()

        flash('Customer Registered Successfully')

        return redirect(url_for('login'))

    return render_template('customer_register.html')


if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)