from flask import Flask, url_for, send_from_directory, render_template, redirect, request
import csv
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def htmlPage(page_name):
    return render_template(page_name)

def writeToFile(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email}, {subject}, {message}")

def writeToCsv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            writeToCsv(data)
            return redirect('thankyou.html')
        except:
            return "data did not save to database"
    else:
        return "something went wrong, please try again!"


if __name__ == "__main__":
    app.run(debug=True)