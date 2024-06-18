from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<username>')
def user(username):
    return render_template("templates.html", username=username)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)