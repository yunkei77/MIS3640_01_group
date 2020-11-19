from flask import Flask, request, render_template
import re
import math

app = Flask("__name__")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def similarity():
    # construct input words dict
    input_str = request.form["query"].lower()
    words_lst = re.sub(
        "[\W]", " ", input_str
    ).split()  # Replace punctuation by space and split
    words = {}
    for word in words_lst:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    # construct databse words dict
    fd = open("database1.txt", "r")
    db_str = fd.read().lower()
    db_words = re.sub("[\W]", " ", db_str).split()
    words_dict = {}
    for word in db_words:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1
    # count input words term frequency
    input_tf = 0
    for w in words:
        if w in words_dict:  # only count words that included in database words
            input_tf += words[w]

    total_tf = sum(words_dict.values())
    similarity_perc = float(input_tf / total_tf) * 100
    output = "Input query text matches {0:.2f}% with database.".format(similarity_perc)
    return render_template("index.html", query=input_str, output=output)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1")
