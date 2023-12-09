import random
import os
import requests
from flask import Flask, render_template, abort, request

# WIP: Import your Ingestor and MemeEngine classes
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # WIP: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    # WIP: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs.extend([os.path.join(root, file_name) for file_name in files])

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @WIP:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    img = random.choice(imgs)    
    
    # 2. select a random quote from the quotes array
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

    # @WIP:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    try:
        image_url = request.form.get('image_url')
        if image_url == "":
            raise Exception("Empty image_url!!!")
        body = request.form.get('body')
        author = request.form.get('author')
    except Exception as e:
        print(e)
        abort(400, 'Empty image_url')
    
    try:
        print(f'image_url = {image_url}, \n body = {body}, \n author = {author}')
        respone = requests.get(image_url)
        random_name = f'{random.randint(0, 100000)}_downloaded_img.jpg'
        tmp_file = MemeEngine.build_img_path('./tmp', random_name)
        with open(tmp_file, 'wb') as img:
            img.write(respone.content)            
    except Exception as e:
        print(f'Failed to download or save image from image_url = "{image_url}"!')
        return abort(404, 'Failed to download or save image')
    
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    path = meme.make_meme(tmp_file, body, author)
    
    # 3. Remove the temporary saved image.
    os.remove(tmp_file)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
