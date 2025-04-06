from flask import Flask, render_template, request
from routes.jobPostings import job_postings_bp
from routes.weeklyDiary import weekly_diary_bp

app = Flask(__name__)

#Register Blueprints
app.register_blueprint(job_postings_bp)
app.register_blueprint(weekly_diary_bp)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/content-review')
def content_review():
    return "Aggregate Reviews on Products"


@app.route('/learning')
def learning():
    #List down the things I learned this week
    #List down the courses I found useful
    return "I learned Iterators and Generators this week"


@app.route('/goals')
def goals():
    #List down the goals I am planning to achieve
    return "My goal is to achieve so and so"


 
if __name__ == "__main__":
    app.run(debug=True)