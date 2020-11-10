import flask
import sys

TPL = flask.render_template # Pour éviter de toujours taper flask.render_template...


cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None

app = flask.Flask(__name__, template_folder='web/templates')

def run():
    app.run()

@app.route('/')
def globe():
    return TPL('index.html', title='Map')

if __name__ == "__main__":
    print('Serveur started')
