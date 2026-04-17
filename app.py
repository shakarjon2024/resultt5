from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def result5():
    if request.method == "POST":
        email = request.form.get("email")
        age = request.form.get("age")

        return render_template("result5.html", name=name)


    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)
