from flask import Flask, render_template_string
from inter_class import str_res  # Import the string from config.py

app = Flask(__name__)

@app.route('/')
def home():
    # Render the string in an HTML template
    html = f"""
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>String Display</title>
      </head>
      <body>
        <div style="text-align: center; margin-top: 50px;">
          <h1>{str_res}</h1>
        </div>
      </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run()
