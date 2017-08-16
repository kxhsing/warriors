from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

class Player(db.Model):
    """Warriors player profile"""

    __tablename__ = "players"

    player_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    url = db.Column(db.Text, nullable=True, unique=True)
    jersey = db.Column(db.Text, nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<Player player_id={} name={}>".format(self.player_id,
                                                   self.name)


# Not sure about this yet
# class Jersey(db.Model):
#     """Player jersey numbers"""

#     __tablename__ = "jerseys"

#     jersey_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     player_id = db.Column(db.Integer, db.ForeignKey('players.player_id'), nullable=False)
#     jersey_num_team = db.Column(db.Text, nullable=False, unique=False)

#     #Establish relationships
#     player = db.relationship("Player", backref=db.backref("players"))

#     def __repr__(self):
#     """Provide helpful representation when printed."""
#     return "<Jersey player_id={} jersey={}>".format(self.player_id,
#                                                self.jersey_num_team)


class RSGame(db.Model):
    """Regular season games"""
    
    __tablename__ = "rsgames"

    rsgame_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.player_id'), nullable=False)
    year_start = db.Column(db.Integer, nullable=False)
    num_games = db.Column(db.Integer, nullable=False)
    avg_pts = db.Column(db.String(10), nullable=True)
    avg_min = db.Column(db.String(10), nullable=True)
    avg_rebounds = db.Column(db.String(10), nullable=True)
    avg_assists = db.Column(db.String(10), nullable=True)
    avg_steals = db.Column(db.String(10), nullable=True)
    avg_blocks = db.Column(db.String(10), nullable=True)


    #Establish relationships
    player = db.relationship("Player", backref=db.backref("players"))


class PLGame(db.Model):
    """Playoffs games"""

    __tablename__ = "plgames"

    plgame_id = db.Column(db.Integer, autoincrement=True, primary_key=True)










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