from flask import Flask, render_template,request


app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return "Hello, World!"


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"<h1>Hi How are you, {name}!</h1>"
    return render_template('index.html')

@app.route("/user/<name>")
def user(name):
    return render_template("user.html",username=name)


if __name__ == "__main__":
    app.run(debug=True)