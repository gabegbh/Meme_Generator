Meme Generator Project

This project is a part of the Intermediate Python Nanodegree bootcamp on Udacity.com

The goal of this project is to create a Flask web app that can randomly create a meme image composed of a base image and a quote of text.
The base images and quote files are stored in the project _data directory, and the quotes are in 4 different formats: .csv .txt .docx and .pdf

To install and run this project locally, the CLI can be used by running [python3 meme.py] in the src folder.
Arguments accepted from the CLI include [--path] (relative to src path to image), [--body] (body of quote text), and [--author] (author of quote)

To install locally but run on a local Flask server, run [set FLASK_APP=app.py] and [flask run]. This will start a dev server on the IP and port listed

We make use of two custom modules in this project, the MemeEngine module and QuoteEngine module

MemeEngine is a module composed of just its own class used as a constructor to generate a meme given all the criteria.
The make_meme function returns a str path to the created meme in the src/tmp or src/static folders

QuoteEngine is a powerful file decoding module. 
With all our quotes residing in different file types, the Ingestor parse classmethod allows any of these files as inputs and returns a list of quote objects after parsing all lines.
Sub-modules of the QuoteEngine include the Ingestor class that combines the functionality of each extension-specific class, one for each file type.

