from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Player(db.Model):
    """Warriors player profile"""

    __tablename__ = "players"

    player_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    jersey = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=True, unique=True)

    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<Player player_id={} name={}>".format(self.player_id,
                                                   self.name)


class RSGame(db.Model):
    """Regular season games"""
    pass


class PLGame(db.Model):
    """Playoffs games"""
    pass









##############################################################################
# Helper functions

def connect_to_db(app, db_uri="postgresql:///warriors"):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)

    print "Connected to DB."