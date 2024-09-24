from flask import Flask, render_template, jsonify

app = Flask (__name__)

JOBS= [
  {
    'id': 1,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary':'Rs.  10,00,000'
  
  
  },
  {
    'id': 1,
    'title':'Front End',
    'location':'Bengaluru, India',
    'salary':'Rs.  10,00,000'
  
  
  },
  {
    'id': 1,
    'title':'Backend',
    'location':'Bengaluru, India',
    'salary':'Rs.  10,00,000'
  
  
  },     
]
@app.route('/')
def hello_jovian():
  return render_template ('home.html', 
                          jobs= JOBS,
                         company_name='Jovian')

@app.route ('/jobs')
def list_jobs():
  return jsonify (JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug = True)

