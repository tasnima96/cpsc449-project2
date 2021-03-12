# Science Fiction Novel API - Bottle Edition
#
# Adapted from "Creating Web APIs with Python and Flask"
# <https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask>.
#

import sys
import textwrap
import logging.config
import sqlite3

import bottle
from bottle import get, post, error, abort, request, response, HTTPResponse
from bottle.ext import sqlite

# Set up app, plugins, and logging
#
app = bottle.default_app()
app.config.load_config('./etc/api.ini')

plugin = sqlite.Plugin(app.config['sqlite.dbfile'])
app.install(plugin)

logging.config.fileConfig(app.config['logging.config'])


# Return errors in JSON
#
# Adapted from # <https://stackoverflow.com/a/39818780>
#
def json_error_handler(res):
    if res.content_type == 'application/json':
        return res.body
    res.content_type = 'application/json'
    if res.body == 'Unknown Error.':
        res.body = bottle.HTTP_CODES[res.status_code]
    return bottle.json_dumps({'error': res.body})


app.default_error_handler = json_error_handler

# Disable warnings produced by Bottle 0.12.19.
#
#  1. Deprecation warnings for bottle_sqlite
#  2. Resource warnings when reloader=True
#
# See
#  <https://docs.python.org/3/library/warnings.html#overriding-the-default-filter>
#
if not sys.warnoptions:
    import warnings
    for warning in [DeprecationWarning, ResourceWarning]:
        warnings.simplefilter('ignore', warning)


# Simplify DB access
#
# Adapted from
# <https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/#easy-querying>
#
def query(db, sql, args=(), one=False):
    cur = db.execute(sql, args)
    rv = [dict((cur.description[idx][0], value)
          for idx, value in enumerate(row))
          for row in cur.fetchall()]
    cur.close()

    return (rv[0] if rv else None) if one else rv


def execute(db, sql, args=()):
    cur = db.execute(sql, args)
    id = cur.lastrowid
    cur.close()

    return id


# Routes
#
# Users Service

@post('/users/')
def create_User(db):
    user = request.json

    if not user:
        abort(400)

    posted_fields = user.keys()
    required_fields = {'name', 'email', 'password'}

    if not required_fields <= posted_fields:
        abort(400, f'Missing fields: {required_fields - posted_fields}')

    try:
        user['id'] = execute(db, '''
            INSERT INTO users(name, email, password)
            VALUES(:name, :email, :password)
            ''', user)
    except sqlite3.IntegrityError as e:
        abort(409, str(e))
    response.status = 201
    response.set_header('Location', f"/users/{user['id']}")
    return  user

@get('/users')
def check_Password(db):
    sql = 'SELECT * FROM users'

    columns = []
    values = []

    for column in ['name', 'password']:
        if column in request.query:
            columns.append(column)
            values.append(request.query[column])

    if columns:
        sql += ' WHERE '
        sql += ' AND '.join([f'{column} = ?' for column in columns])

    logging.debug(sql)
    users = query(db, sql, values)
    return {'users': users}

@post('/users')
def add_Follower():
    new_follower = {'name' : request.json.get('name'),'nameToFollow' : request.json.get('nameToFollow')}
    users.append(new_follower)
    return {'user' : users}

@delete('/users/<nameToRemove>')
def remove_Follower(nameToRemove):
    del_follower = [follower for follower in user if follower['nameToRemove']
    users.remove(del_follower[0])
    return {'users': users}

#
# Timeines Service
#

@get('/timelines/<post>')
def getUserTimeline(name):
    user_post = [post for post in timeline if post['name'] == name]
    return{'timeline' : user_post[0]}

@get('/timelines/')
def getPublicTimeline(db):
    post = query(db, 'SELECT * FROM timelines;')

    return {'post': all_users}
