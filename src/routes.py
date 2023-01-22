from src.api.v1.words import WordsCountVowels, WordsSort


def register_app(app_flask):
    vowel = WordsCountVowels.as_view('vowel_count')
    sort = WordsSort.as_view("sort")
    app_flask.add_url_rule("/vowel_count", view_func=vowel)
    app_flask.add_url_rule("/sort", view_func=sort)
