from flask import Flask  
app = Flask(__name__)      
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from blog import routes, models


##def make_shell_context():
  ##return {"db": db, "Entry": models.Entry}

