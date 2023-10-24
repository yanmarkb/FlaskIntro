from flask import Flask
app = Flask(__name__)

@app.route('/')
def home_page():
    html = """
    <html>
        <body>
            <h1>Home Page</h1>
            <p>Welcome to my first server</p>
            <a href="/welcome">Go to welcome page</a>
            <a href="/welcome/home">Go to welcome home page</a>
            <a href="/welcome/back">Go to welcome back page</a>
        </body>
    </html>
    """ 
    return html

@app.route('/welcome')
def welcome():
    html = """
    <html>
        <body>
            <h1>WELCOME!</h1>
            <p>This is the welcome page</p>
            <a href="/">Go to home page</a>
            <a href="/welcome/home">Go to welcome home page</a>
            <a href="/welcome/back">Go to welcome back page</a>
        </body>
    </html>
    """
    return html

@app.route('/welcome/home')
def welcome_home():
    html = """
    <html>
        <body>
            <h1>WELCOME HOME!</h1>
            <p>This is the welcome home page</p>
            <a href="/">Go to home page</a>
        </body>
    </html>
    """
    return html

@app.route('/welcome/back')
def welcome_back():
    html = """
    <html>
        <body>
            <h1>WELCOME BACK!</h1>
            <p>This is the welcome back page</p>
            <a href="/">Go to home page</a>
        </body>
    </html>
    """
    return html
@app.route('/goodbye')
def goodbye_world():
    return 'Goodbye, World!' 
