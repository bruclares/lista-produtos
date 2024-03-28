from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from ..database.db import get_db

bp = Blueprint('product', __name__)

@bp.route('/')
def list():
    with get_db() as conn:
        with conn.cursor() as curs:
            curs.execute(
                'SELECT * FROM products ORDER BY value'                   
            )
            products = curs.fetchall()
    return render_template('list.html', products=products)

@bp.route('/incluir', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name'].capitalize()
        description = request.form['description'].capitalize()
        value = request.form['value']
        available = request.form['available'] == 'S'
        error = None

        if not name:
            error = 'O nome do produto é obrigatório'
        elif not description:
            error = 'A descrição do produto é obrigatória'
        elif not value:
            error = 'O valor do produto é obrigatório'

        if error is not None:
            flash(error)
        else:
            with get_db() as conn:
                with conn.cursor() as curs:
                    curs.execute(
                        '''INSERT INTO products (name, description, value, available) 
                        VALUES (%s, %s, %s, %s)''',
                        (name, description, value, available)
                    )
            return redirect(url_for('product.list'))
                
    return render_template('create.html')