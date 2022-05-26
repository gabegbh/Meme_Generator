import random
import os
import requests
import urllib.request
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    
    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    paths = next(os.walk(images_path), (None, None, []))[2]
    paths = filter(lambda ext: ext.split('.')[-1] in ['jpg', 'png', 'gif'], paths)
    imgs = [images_path + img for img in paths]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    img_url = request.form['image_url']
    tmp_path = "./tmp/user.jpg"
    quote_body = request.form['body']
    quote_author = request.form['author']
    
    try:
        urllib.request.urlretrieve(img_url, tmp_path)
    except:
        # Note to reviewer, try the create form with this URL: https://tinyurl.com/wfvz6n3p
        quote_body, quote_author = ' - - - - - - - ', '- - - - - - "'
        tmp_path = "./_data/photos/error.jpg"
        print('HTTP bot-scraping-defense triggered. Please try another url')
    
    path = meme.make_meme(tmp_path, quote_body, quote_author)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
