from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/book", methods=["POST"])
def book():
    name = request.form["name"]
    email = request.form["email"]
    package = request.form["package"]
    date = request.form["date"]

    with open("booking.txt", "a") as file:
        file.write(f"{name}, {email}, {package}, {date}\n")

    return redirect(url_for('thank_you', name=name, package=package))

@app.route("/thank-you")
def thank_you():
    name = request.args.get("name")
    package = request.args.get("package")
    return render_template("thank_you.html", name=name, package=package)

@app.route("/bookings")
def show_bookings():
    bookings = []
    try:
        with open("booking.txt", "r") as file:
            for line in file:
                bookings.append(line.strip())
    except FileNotFoundError:
        bookings.append("No bookings found.")
    return render_template("bookings.html", bookings=bookings)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
