from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Home")
def home():
    return render_template("Home.html")
    
@app.route("/Product")
def product():
    return render_template("Product.html")

@app.route("/Service")
def service():
    return render_template("Service.html")

@app.route("/Gallery")
def gallery():
    return render_template("Gallery.html")

@app.route("/About-us")
def about():
    return render_template("About.html")

@app.route("/Log-in")
def log_in():
    return render_template("Log_in.html")

if __name__ == '__main__':
    app.run(debug=True)
