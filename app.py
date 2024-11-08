from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary':'Rs. 10,00,000'
  },
  {
    'id':2,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary':'Rs. 10,00,000'
  },
  {
    'id':3,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary':'Rs. 10,00,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
