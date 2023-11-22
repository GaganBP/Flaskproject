from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def college_page():
    return render_template('college.html')

@app.route('/department')
def department_page():
    return render_template('department.html')

if __name__ == '__main__':
    app.run(debug=True)
