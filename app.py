from flask import Flask, render_template

app = Flask(__name__, template_folder='template', static_folder='static')

# Add this line to ensure the cache is not used during development
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/signup')
def signup_page():
    return render_template('signup.html')

@app.route('/login')  # Add a route for /login
def login_page():
    return render_template('login.html')

@app.route('/department')
def department_page():
    return render_template('department.html')

if __name__ == '__main__':
    app.run(debug=True)
