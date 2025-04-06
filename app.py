from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    email = request.form['email']
    package = request.form['package']
    date = request.form['date']

    # Save booking to file
    with open("bookings.txt", "a") as file:
        file.write(f"{name}, {email}, {package}, {date}\n")

    return "Thanks for booking with Journey Jubilee!"

if __name__ == '__main__':
    app.run(debug=True)
