from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = 'story-time'
app.debug = True

debug = DebugToolbarExtension(app)

@app.route('/')
def ask_story():
    '''show list-of-stories form'''

    return render_template("select-story.html",stories=stories.values())


@app.route("/question")
def ask_question():
    '''Generate and show form to ask words'''
    story_id = request.args["story_id"]
    story = stories[story_id]

    prompts = story.prompts

    return render_template("question.html", story_id=story_id,title=story.title, prompts=prompts)

@app.route("/story")
def show_story():
    '''Show story result'''
    story_id = request.args["story_id"]
    story = stories[story_id]
    text = story.generate(request.args)

    return render_template("story.html", title=story.title, text=text)