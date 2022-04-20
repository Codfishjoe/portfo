from flask import Flask, render_template, redirect
from flask import request
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home(username=None, post_id=None):
    return render_template('./index.html', name=username, post_id=post_id)

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.csv',newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter = ',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_file(data)
            print(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to a database'
    else:
        return 'something went wrong'