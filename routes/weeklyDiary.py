from flask import Blueprint, render_template

weekly_diary_bp = Blueprint("weekly_diary",__name__)

@weekly_diary_bp.route('/weekly-diary')
# @app.route('/<name>')
def weekly_diary(name=None):
    week = "April 04, 2025"
    achievements = [
        "Read 40 Pages of the book",
        "Memorized 5 Pages from the Quran",
        "Learnt Multi Threading in Python",
        "Started Working in Personal Diary Project",
        "Hell",
        "Caught"
    ]
    challenges = ["Stayed up too","Ate less","Hungry"]
    mood = "Sad"

    return render_template('weeklyDiary.html',
                           week=week,
                           achievements=achievements,
                           challenges=challenges,
                           mood=mood,
                           name=name)
