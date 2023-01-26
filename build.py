from flask_frozen import Freezer
from server import app

freezer = Freezer(app)

#app.config['FREEZER_DESTINATION'] = "datathon-2023"

if __name__ == '__main__':
    freezer.freeze()