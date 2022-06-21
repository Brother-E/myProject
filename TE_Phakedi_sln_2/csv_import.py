#importing the flask module to create a local host server to host our csv file
from flask import Flask
from flask import render_template
from flask import request
import csv

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():

     return render_template('home.html')

@app.route('/records', methods=['GET','POST'])
def records():
  if request.method == 'POST':
     records = []

  csv_file = request.form.get['csv_file']

#Opening my csv file to read it into empty list
  with open(csv_file,'r') as mycsvfile:
    csv_file = csv.reader(mycsvfile)
    for row in csv_file:
	    records.append(row)
	    #Sending the records object to another html link with displaying functions
	    return render_template('records.html', records = records)
     

if __name__ == '__main__':
	app.run(debug=True)