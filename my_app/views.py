from my_app import db, app
from flask import Blueprint, render_template, request
from my_app.models import Product, Category

catalog = Blueprint('catalog',__name__)

@app.errorhandler(404)  #should be "app", not "catalog" for error handling
def page_not_found(e): 
    return render_template('404.html'), 404 

@catalog.route('/')
@catalog.route('/home')
def home():
    return render_template('home.html')


@catalog.route('/product/<id>')
def product(id):
    Product.query.get_or_404(id)
    return render_template('product', product=product)


@catalog.route('/products')
@catalog.route('/products/<int:page>')
def products(page=1):
    products = Product.query.paginate(page, 10).items
    return render_template('products.html', products=products)


@catalog.route('/product-create', methods=['POST',])
def create_product():
    name = request.form.get('name')
    price = request.form.get('price')
    product = Product(name, price)
    db.session.add(product)
    db.session.commit()
    return render_template('product.html', product=product)


@catalog.route('/category-create', methods=['POST',])
def create_category():
    name = request.form.get('name')
    category = Category(name)
    db.session.add(category)
    db.session.commit()
    return render_template('category.html', category=category)


@catalog.route('/category/<id>')
def category(id):
    category = Category.query.get_or_404(id)
    return render_template('category.html', category=category)


@catalog.route('/categories')
def categories():
    categories = Category.query.all()
    return render_template('categories.html', categories=categories)