"""
main file for the service
"""
from flask import Flask, request, render_template, flash, redirect, url_for, session, logging
from data import OurGuitars
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

Guitars = OurGuitars()


app = Flask(__name__)
app.debug = True

# mysql config
# localhost:61259 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskapp'
# a cursor is used to execute queries and return the data as a dictionary
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# now init mysql
mysql = MySQL(app)

app.secret_key='secret505'


@app.route('/')
def welcome():
    return render_template('home.html')

@app.route('/about')
def about():return render_template('about.html')

@app.route('/browse')
def browse():return render_template('browse.html', guitars = Guitars)

@app.route('/guitar/<string:ID>')
def viewitem(ID):return render_template('guitar.html', id = ID)

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1,max=30)])
    username = StringField('Username', [validators.Length(min=5,max=20)])
    email = StringField('Email', [validators.Length(min=6,max=30)])
    password = PasswordField('Password',
     [validators.DataRequired(),
      validators.EqualTo('confirm', message="passwords do not match")
      ])
    confirm = PasswordField('Confirm Password')


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # create the cursor
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s,%s,%s,%s)", (name, email, username, password))


        # commit to the db
        mysql.connection.commit()

        # close connection
        cur.close()

        flash('you are now registered and can log in', 'success')
        return redirect(url_for('welcome'))
    return render_template('register.html', form=form)




# User Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # get inputs from user
        username = request.form['username']
        password_candidate = request.form['password']

        # create a cursor and query the db
        cur = mysql.connection.cursor()
        result = curr.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0: # row found
            data = cur.fetchone()
            password = data['password']
            # comparing entered password with db result
            if sha256_crypt.verify(password_candidate, password):
                app.logger.info('PASSWORD is a match')
            
        else:
            app.logger.info('invalid user')

    return render_template('login.html')