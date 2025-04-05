from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weekly-diary')
# @app.route('/<name>')
def weekly_diary(name=None):
    week = "April 04, 2025"
    achievements = [
        "Read 40 Pages of the book",
        "Memorized 5 Pages from the Quran",
        "Learnt Multi Threading in Python",
        "Started Working in Personal Diary Project",
        "Hell"
    ]
    challenges = ["Stayed up too","Ate less","Hungry"]
    mood = "Sad"

    return render_template('weeklyDiary.html',
                           week=week,
                           achievements=achievements,
                           challenges=challenges,
                           mood=mood,
                           name=name)


 
if __name__ == "__main__":
    app.run(debug=True)