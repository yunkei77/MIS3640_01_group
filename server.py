from flask import Flask, request, render_template
import re
import math

app = Flask("__name__", template_folder='templates')

@app.route("/")
def index():
    return render_template('index.html') # localhost:5000/ route render the index.html page

@app.route("/", methods=['POST']) # form in front-end page post data to this api
def similarity():
    # Part1. construct input words dict
    input_str = request.form['query'].lower() # input string from front-end page's form, convert all characters to lower case.
    words_lst = re.sub("[\W]", " ", input_str).split() # replace all non-word character with ' '(space), split it to words list: [word1, word2, ..., wordn] 
    words = {} 
    for word in words_lst: # loop all words, count word frequency and store it in a dictionary 
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    # words dict, key is word itself, value is the frequecy of that word: {word1: 8, word2: 12, word3: 17, ..., wordn: 33}

    # Part2. construct databse words dict, similar as part 1, but all the words come from the database.txt file.
    fd = open("database1.txt", "r") # read the txt file
    db_str = fd.read().lower() # also converts to lowercase
    db_words = re.sub("[\W]", " ", db_str).split() # remove non-word, split to list
    words_dict = {}
    for word in db_words:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1
    # it's the word frequncy dict constructed from database.txt file. 

    # count input words term frequency
    input_tf = 0
    for w in words:
        if w in words_dict: # Only count words that included in database words. So that the similarity'll be in the range [0,1]
            input_tf += words[w]

    total_tf = sum(words_dict.values())
    similarity_perc = float(input_tf / total_tf)*100 # calculate the similarity percentage, e.g., 22.3333%

    output = "Input query text matches {0:.2f}% with database.".format(similarity_perc) # 2 decimals format

    # pass input_str and output data to the front-end page (index.html). The information will be render in that page.
    return render_template('index.html', query=input_str, output=output) 

if __name__ == '__main__':
	app.run(debug=True, host='127.0.0.1') # start flask server on 127.0.0.1:5000/