from flask import Flask, render_template, jsonify
JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Bengaluru, India",
        "salary": "Rs. 10,00,000"
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "Delhi, India",
        "salary": "Rs. 15,00,000"
    },
    {
        "id": 3,
        "title": "Frontend Developer",
        "location": "San Francisco, USA",
        "salary": "$120,000"
    },
    {
        "id": 4,
        "title": "Backend Developer",
        "location": "Remote",
        "salary": "$150,000"
    }
]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS, company_name="Jovian")
@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)