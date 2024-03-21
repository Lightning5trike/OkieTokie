from crypt import methods
from itertools import product
from multiprocessing import connection
from re import template
import sqlite3
from sre_constants import CATEGORY_NOT_SPACE 
import bcrypt
from flask import Flask, render_template, request, url_for, flash, redirect, Blueprint
from werkzeug.exceptions import abort
from flask_login import LoginManager, login_user, login_required, current_user
from forms import SignUpForm, cake_form, creation_form


# name holds the name of the current python module
app = Flask(__name__)
app.config['SECRET_KEY'] = 'grpg9zr482bdkvmbav8b468053r9m049x1hi35wjbnwmw6h6p0juhdrqc'
auth = Blueprint('auth', __name__)
# creates a connection to database.db

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id)).fetchone()
    conn.close()
    user.is_active = True
    user.is_authenticated = True
    user.is_anonymous = False
    user.get_id = lambda : user['id']
    return user
    

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# general website home page





@app.route('/', methods=('GET', 'POST'))
def index():
    # link to the corresponding html page
    return render_template('index.html')




@app.route('/cakes', methods=('GET', 'POST'))
def cakes():
    return render_template('cakes.html')




@app.route('/cart', methods=('GET', 'POST'))
def cart():
    return render_template('cart.html')






def get_products(products_id):
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products WHERE id = ?',
                        (products_id,)).fetchone()
    conn.close()
    if products is None:
        abort(404)
    return products



@app.route('/<int:products_id>')
def post(products_id):
    products = get_products(products_id)
    return render_template('okieproducts.html', products=products)













@app.route('/cakes/cupcakes', methods=('GET', 'POST'))
# function to display the products already in the database for the cupcakes section
def cupcakes():
    cakeform=cake_form()
    if request.method == 'POST':
        users_email = request.form["users_email"]
        quantity = request.form["quantity"]
        productName = request.form["productName"]
        extra_info = request.form["extra_info"]
        collection_date = request.form["collection_date"]
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO orders (users_email, quantity, products_productName, extra_info, collection_date) VALUES (?,?,?,?,?)", (
            quantity, productName, extra_info, collection_date, users_email))
        conn.commit()
        conn.close()
        return redirect('/')
    elif request.method == 'GET':
        conn = get_db_connection()
        products = conn.execute(
            """SELECT * FROM products where product_section = 'cupcakes'""").fetchall()
        conn.close()
        return render_template('cupcakes.html', form=cakeform, products=products)





@app.route('/cookies', methods=('GET', 'POST'))
def cookies():
    cakeform=cake_form()
    if request.method == 'POST':
        users_email = request.form["users_email"]
        quantity = request.form["quantity"]
        productName = request.form["productName"]
        extra_info = request.form["extra_info"]
        collection_date = request.form["collection_date"]
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO orders (users_email, quantity, products_productName, extra_info, collection_date) VALUES (?,?,?,?,?)", (
            quantity, productName, extra_info, collection_date, users_email))
        conn.commit()
        conn.close()
        return redirect('/')
    elif request.method == 'GET':
        conn = get_db_connection()
        products = conn.execute(
            """SELECT * FROM products where product_section = 'cookies'""").fetchall()
        conn.close()
        return render_template('cookies.html', form=cakeform, products=products)




@app.route('/brownies', methods=('GET', 'POST'))
def brownies():
    cakeform=cake_form()
    if request.method == 'POST':
        users_email = request.form["users_email"]
        quantity = request.form["quantity"]
        productName = request.form["productName"]
        extra_info = request.form["extra_info"]
        collection_date = request.form["collection_date"]
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO orders (users_email, quantity, products_productName, extra_info, collection_date) VALUES (?,?,?,?,?)", (
            users_email, quantity, productName, extra_info, collection_date))
        conn.commit()
        conn.close()
        return redirect('/')
    elif request.method == 'GET':
        conn = get_db_connection()
        products = conn.execute(
            """SELECT * FROM products where product_section = 'brownies'""").fetchall()
        conn.close()
        return render_template('brownies.html', form=cakeform, products=products)












@app.route('/cakes/custom', methods=('GET', 'POST'))
def cake_form_creation():
    cakeform=cake_form()
    if request.method == 'POST':
        users_email = request.form["users_email"]
        cake_size = request.form["cake_size"]
        extras = request.form["extras"]
        extra_info = request.form["extra_info"]
        layers = request.form["layers"]
        collection_date = request.form["collection_date"]
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO orders (users_email, collection_date, cake_size, extras, extra_info, layers) VALUES (?,?,?,?,?,?)", (
            users_email, collection_date, cake_size, extras, extra_info, layers))
        conn.commit()
        conn.close
        return redirect('/')
    elif request.method == 'GET':
        return render_template('cake_form.html',form=cakeform)












@app.route('/okietokie', methods=('GET', 'POST'))
def okietokie():
    if request.method == 'GET':
        conn = get_db_connection()
        orders = conn.execute(
            """SELECT * FROM orders""").fetchall()   
        conn.close()
        return render_template('tomi+oyindas.html', orders=orders)



@app.route('/okietokie/products', methods=('GET', 'POST'))
def products():
    conn = get_db_connection()
    products = conn.execute("""SELECT * FROM products""").fetchall()
    conn.close()
    return render_template('okieproducts.html',products=products)



@app.route('/okietokie/create', methods=('GET', 'POST'))
def createproduct():
    creationform=creation_form()
    if request.method == 'POST':
        productName = request.form['productName']
        product_section = request.form['product_section']
        product_image = request.form['product_image']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO products (productName, product_section, product_image) VALUES (?,?,?)", (
            productName, product_section, product_image))
        conn.commit()
        conn.close()
        return redirect('/okietokie')
    elif request.method == 'GET':
        return render_template('create.html', form=creationform)




@app.route('/okietokie/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    creationform=creation_form()
    products = get_products(id)
    if request.method == 'POST':
        productName = request.form['productName']
        product_section = request.form['product_section']
        product_image = request.form['product_image']
        conn = get_db_connection()
        conn.execute('UPDATE products SET productName = ?, product_section = ?, product_image = ?'
                        ' WHERE id = ?',
                    (productName, product_section, product_image, id))
        conn.commit()
        conn.close()
        return redirect('/okietokie')
    elif request.method == 'GET':
        return render_template('edit.html', form=creationform, products=products)


@app.route('/okietokie/<int:id>/delete', methods=('POST',))
def delete(id):
    products = get_products(id)
    conn = get_db_connection()
    if request.method == 'POST':
        print("a")
        conn.execute('DELETE FROM products WHERE id = ?', (id,))
        print("b")
        conn.commit()
        conn.close()
        print("c")
        flash('"{}" was successfully deleted!'.format(products['productName']))
        print("d")
        return redirect('/okietokie')











@app.route('/signup', methods=('GET', 'POST'))
def signing_up():
    signUpForm=SignUpForm()
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        if (request.form["email"]!="" and request.form["customer_password"]!=""):
            email = request.form["email"]
            customer_password = request.form["customer_password"]
            statement = f"SELECT * FROM users WHERE email='{email}' AND customer_password='{customer_password}';"
            cur.execute(statement)
            data = cur.fetchone()
            if data:
                abort(404)
            else:
                if not data:
                    cur.execute("INSERT INTO users (email, customer_password) VALUES (?,?)",(email, customer_password))
                    conn.commit()
                    conn.close
                return render_template('login.html')
    elif request.method == 'GET':
        return render_template('signup.html', form=signUpForm)




@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        customer_password = request.form['customer_password']
        conn = get_db_connection()
        cur = conn.cursor()
        statement = f"SELECT * FROM users WHERE email='{email}' AND customer_password='{customer_password}';"
        cur.execute(statement)
        if not cur.fetchone():
            return render_template('login.html')
        else:
            Cart = cart()
            cartcheck = f"SELECT * FROM orders WHERE users_email='{email}';"
            cur.execute(cartcheck)
            return render_template('cart.html',name=email, cart=Cart)       
    else:
        request.method == 'GET'
        return render_template('login.html')

@auth.route('/logout', methods=('GET', 'POST'))
def logout():
    return 'Logout'









