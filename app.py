from flask import Flask, render_template, request
from repos.api import repos_with_most_stars
from repos.exceptions import GitHubApiException


app = Flask(__name__)

available_languages = ["Python","JavaScript", "Ruby", "Java"]

@app.route("/", methods=["GET", "POST"])
def index():
    selected_languages = []
    if request.method == "GET":
        # Use the list of all languages
        selected_languages = available_languages
    elif request.method == "POST":
        # Use the languages we selected in the request form
        selected_languages = request.form.getlist("languages")
    results = repos_with_most_stars(selected_languages)
    context = {"selected_languages": selected_languages, "available_languages": available_languages, "results": results}
    return render_template('index.html', **context)

@app.errorhandler(GitHubApiException)
def handle_api_error(error):
    return render_template('error.html', message=error)