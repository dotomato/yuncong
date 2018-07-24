import json
import os
import shutil
import time
import uuid
import re

from flask import Flask, render_template, request, url_for, flash, redirect, send_file, abort



# *******************  Flask Configuration ******************#

app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid.uuid4())
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1 * 24 * 60 * 60
app.add_template_global(VERSION, 'VERSION')



# *******************  View ******************#

@app.route('/', methods=['GET', 'POST'])
def index():

    field = request.args.get('field', '')

    # *******************  GET ******************#

    if request.method == 'GET':
		pass

    # *******************  POST ******************#

    if request.method == 'POST':
		pass
	
	return render_template('index.html')


def format_time(date):
    return time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(date))
app.add_template_global(format_time)


# ******************  Debug Run *******************#
# !!!!!!  Do NOT run in production environment !!!!#

if __name__ == '__main__':
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
    app.run(debug=True, port=5000)
