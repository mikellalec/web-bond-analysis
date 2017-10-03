from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

#trailing slash allows omission of slash
@app.route('/listings/<bondName>')
def show_listings():
    def bond(bondName):
        pass
    return 'There aren\'t any listings!'

if __name__ == '__main__':
    app.run()

#
# with app.test_request_context():
#     print url_for('show_listings', bondName='30YRUST')
