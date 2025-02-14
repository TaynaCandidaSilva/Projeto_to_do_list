from database import db, app
from routes import routes

app.register_blueprint(routes)

with app.app_context():
    db.create_all() 
   
if __name__ == "__main__":
    app.run(debug=True)
