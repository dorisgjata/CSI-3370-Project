import click
from flask import current_app, g
from flask.cli import with_appcontext
import psycopg2
from create_tables import createtables

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(host="localhost", database="dinning", user="postgres", password="postgres")
        print('got it')
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    createtables()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)