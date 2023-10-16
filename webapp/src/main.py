from flask import Flask, request, render_template, flash
from scrapper import get_data


app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.config["SECRET_KEY"] = "e0bRS0hCmelkXu2pBbw35IfGNDf860rCN5eh8r8f_NxiAWNiFN0ApB2ep5dhB_ZajHqCUbYmfT9Y8bXIE4_1RQ"


def validate_URL(url: str):
    """Function validates URL inserted
    """
    valid_url = "https://wsa-test.vercel.app/"
    if valid_url == url or valid_url[:-1] == url:
        return True
    return False
    

# Define API route
@app.route('/', methods=['POST', 'GET'])
def scrape():
    # POST method
    if request.method == 'POST':

        # Extract URL inserted
        url = request.form['url']

        # Validate URL inserted and proceed accordingly
        valid_URL = validate_URL(url)
        if not valid_URL:
            # Message sent in order to style the error
            flash("Invalid")
            data = "Invalid URL"
        else:
            # Scrape website
            data = get_data(url)

        return render_template("index.html", data=data)
    # GET method
    return render_template("index.html")

# Handle error 404
@app.errorhandler(404)
def error_404(error):
    return render_template("error_404.html")


if __name__ == '__main__':
    app.run(debug=True)