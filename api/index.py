from pathlib import Path

from flask import Flask, render_template, request
from google_forms import create_google_apps_script

TITLE = 'Markdown to Google Forms via Google Apps Script'
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def _root():
    if request.method == 'POST':
        if 'create' in request.form:
            code = request.form.get('markdown_code')

            if code is not None and len(code) > 0:
                values = {
                    'code': code,
                    'form_script': create_google_apps_script(code),
                    'title': TITLE,
                }

                return render_template('index.html', **values)

        elif 'reset' in request.form:
            code = Path('sample.md').read_text()
            values = {
                'code': code,
                'form_script': create_google_apps_script(code),
                'title': TITLE,
            }

            return render_template('index.html', **values)

    values = {
        'code': '',
        'form_script': '',
        'title': TITLE,
    }

    return render_template('index.html', **values)