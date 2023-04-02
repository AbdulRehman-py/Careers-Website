from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  
  {
    'id' : 1,
    'title': 'Data Analyst',
    'location': 'Lahore, Pakistan',
    'Salary': 'Rs. 1,00,000' 
},
   {
    'id' : 2,
    'title': 'Data Scientist',
    'location': 'Multan, Pakistan',
    'Salary': 'Rs. 12,00,000' 
},
  {
    'id' : 3,
    'title': 'FrontEnd Engineer',
    'location': 'Remote',
    'Salary': "8,00,000" 
},
  {
    'id' : 4,
    'title': 'BackEnd Engineer',
    'location': 'Remote/lahore (optional)',
    'Salary': 'Rs. 15,00,000' 
},



]

@app.route("/")

def hello_jovian():
  return render_template('home.html', jobs=JOBS)
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)