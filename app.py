import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.album import Album
from lib.artist import Artist 

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
# MUSIC HTML WEB APP ROUTES 

@app.route("/")
def get_main():
    return render_template("music/album_main.html")

@app.route("/about")
def get_about():
    return render_template("music/album_about.html")

# ALBUMS - Dynamic HTML
# GET /albums/1
    # Returns one album
    # Now linked to information via the show html file. 
@app.route('/albums/<id>', methods=['GET']) #REMEBER Flask will not pass an ID unless it is part of the route. 
def get_one_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id)
    return render_template('music/album_show.html', album=album)

# GET /albums
    # Returns a list of albums
@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('music/album_index.html', albums=albums)


# ALBUMS - static HTML
# @app.route('/albums', methods=['POST'])
# def post_albums():
#     if 'title' not in request.form or 'release_year' not in request.form or 'artist_id' not in request.form:
#         return "Please provide full information", 400
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     album = Album(
#         None, 
#         request.form['title'], 
#         request.form['release_year'], 
#         request.form['artist_id'])
#     album = repository.create(album)
#     return '', 200
# # curl http://localhost:5001/albums 

# @app.route('/albums', methods=['GET'])
# def get_albums():
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     albums = repository.all()
#     return "\n".join(
#         f"{album}" for album in repository.all()
#     )
# curl -X POST -d "title=..%20..&release_year=...&artist_id=..." http://localhost:5001/albums
# add info. %20 creates a space



# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
