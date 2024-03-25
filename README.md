# Markdown to Google Forms

Flask web app to convert a Markdown style document into Google Apps Script code, which in turn is used to generate a Google Forms.

This is not the best solution possible, but it is a solution. One can probably implement something more robust by using libraries like [marko](https://github.com/frostming/marko) or [mistletoe](https://github.com/miyuchina/mistletoe).

## Usage

Visit the [web app](https://markdown-to-google-apps-script.vercel.app/) and paste the contents of your markdown file in the text area to the left. Click the `Create script` button and the code will be generated on the text area to the right.

Then, paste the generated code on a [new project](https://script.google.com/home/projects/create) in Google Apps Script and execute it. On the first run of this new project it will ask for permissions to your Google Drive, which should be conceded, so it can create the new form. A new file will be created on your [Google Drive](https://drive.google.com/) with the name you used as title. Note that the form is not ready to use, but at least the basic structure will be done.

### Running Locally

```bash
npm i -g vercel
vercel dev
```

Your Flask application is now available at `http://localhost:3000`.
