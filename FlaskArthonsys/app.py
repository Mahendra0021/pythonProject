from flask import Flask, render_template
app=Flask(__name__)
@app.route("/")
def fun():
    return render_template('index.html')
@app.route("/contact")
def show():
    return render_template('contact.html')
app.run(debug=True)