import string

from bottle import route, run, Bottle
from bottle import get, post, request, response, debug
from bottle import error, redirect
from bottle import template


app = Bottle()
app.request_counter = 0

# DEBUG
debug(True)
# run(reloader=True)

@app.route('/')
@app.route('/hello/<name>')
def index(name='World'):
    """Simple test method.

    Args:
        name: Test path

    Returns:
    A simple test document.
    """
    # return '<b>Hello %s!</b>\n' % name
    document = "<p>Requests: <b>%s</b></p>\n" % str(app.request_counter)
    document = document + "<h1>%s</h1>\n<ul>" % name
    for w in name.split(" "):
        document = document + '<li><a href="http://localhost:3001/hello/' + w + '">%s</a></li>\n' % w
    document = document + "</ul>"
    app.request_counter += 1
    return document


@app.route('/login')
def login_form():
    """Provides a simple login form for user authentication based on user name
    and passowrd.

    Returns:
        Login form (user name field, password field, "Submit" button)
    """
    return '''<form method="POST">
                 Name: <input name="name" type="text"/>
                 Password: <input name="password" type="password"/>
                 <input type="submit" value="Submit">
              </form>'''

@app.route('/login', method='POST')
def login_submit():
    """Responds to a user authentication form submit.

    The combination of username and password is either accepted or rejected.

    Returns:
        Either a success or a failure page.
    """
    name = request.forms.get('name')
    password = request.forms.get('password')
    if check_login(name, password):
        return '<p>Correct login</p>'
    else:
        return '<p>Login failed.</p>'

def check_login(name, password):
    """Validates a login

    Args:
        name: User name
        password: Password

    Returns:
        'True' if the login credencials are correct.
        'False' if they are incorrect.
    """
    return True


@app.route('/upload')
def upload():
    """Allows arbitrary file upload via POST.

    Returns:
        A simple file upload form (text field, file name field, "Browse" button)
    """
    return '''<form action="/upload" method="post" enctype="multipart/form-data">
                <input type="text" name="name"/>
                <input type="file" name="data"/>
                <input type="submit" value="Submit">
             </form>'''

@app.route('/upload', method='POST')
def upload_respond():
    """Responds to a file upload POST."""
    return "File uploaded"


@app.error(404)
def error404(error):
    """Provides a custom HTTP 404 error page.

    Args:
        error: HTTP 404 error

    Returns:
        A custom 404 page.
    """
    return 'Nothing here, sorry.'

@app.route('/wrong')
def test_wrong_url():
    """Redirects the user to the right url"""
    redirect('/right')

@app.route('/cookietest')
def test_cookie():
    """Tests the use of cookies"""
    if request.get_cookie('visited'):
        return 'Welcome back!'
    else:
        response.set_cookie('visited', 'yes')
        return 'Hello there!'

@app.route('/forum')
def forum():
    id = request.query.id
    page = request.query.page or '1'
    document = '<h1>Forum</h1>\n<p>ID: %s</p>\n<p>Page: %s</p>' % (id, page)
    document = document + '\n<p>All Query Variables:</p>\n<table>\n<tr><th>Variable</th><th>Value</th>'
    for key in request.query.keys():
        document = document + '<tr><td>%s</td><td>%s</td></tr>' % (key, request.query[key])
    document = document + '</table></p>'
    return document

@app.route('/templatetest/<name>')
def test_templatess(name='world'):
    query_variables = request.query.keys()
    return template(
        'test_template',
        name=name,
        query_variables=query_variables)

# from bottle import install
# from bottle_sqlite import SQLitePlugin
# install(SQLitePlugin(dbfile='/tmp/test.db'))

# @route('/show/<post_id:int>')
# def show(db, post_id):
#     c = db.execute('SELECT title, content FROM posts WHERE id = ?', (post_id,))
#     row = c.fetchone()
#     # return template('show_post', title=row['title'], text=row['content'])
#     return '<p>' + 'show_post' + row['title'] + row['content']+ '</p>'

run(app, host='localhost', port=3333
