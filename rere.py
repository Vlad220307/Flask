from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def base():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Encrypt') == 'Encrypt':
            # pass
            print("Encrypted")
            return render_template("home.html")
        elif  request.form.get('Decrypt') == 'Decrypt':
            # pass # do something else
            return render_template("index.html")
            print("Decrypted")
        else:
            # pass # unknown
            return render_template("base.html")
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
    return render_template("base.html")

@app.route("/index", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('baak') == "beak":
            print("beak")
            return render_template("base.html")
        else:
            # pass # unknown
            return render_template("base.html")
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
    return render_template("base.html")

@app.route("/home", methods=['GET', 'POST'])
def home():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('baak') == "beak":
            print("beak")
            return render_template("base.html")
        else:
            # pass # unknown
            return render_template("base.html")
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
    return render_template("base.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')