from lib.artist_repository import ArtistRepository
from lib.artist import Artist

"""
When we call artist_repository#all 
We get a list of the artist objects reflecting the seed data. 
"""

def test_get_all_artists(db_connection):
    db_connection.seed("seeds/music_html_web_app.sql")
    repository = ArtistRepository(db_connection)

    artists = repository.all()

    assert artists == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz'), 
    ]
