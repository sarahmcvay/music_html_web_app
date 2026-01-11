from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call Album Repository#all
We get a list of Album Objects reflecting the data
"""
def test_get_all_albums(db_connection): # see conftest.py for more info
    db_connection.seed("seeds/music_html_web_app.sql") #seed with test data
    repository = AlbumRepository(db_connection) # creates new AlbumRepository 

    albums = repository.all() 

    assert albums == [
        Album(1,'Doolittle', 1989, 1),
        Album(2, 'Surfa Rosa', 1988, 1),
        Album(3,'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
    ]

"""
When we call AlbumRepository#find
We get a single Album object reflecting the seed data. 
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/music_html_web_app.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find(3)
    assert album == Album(3,'Waterloo', 1974, 2)

"""
When we call BookRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/music_html_web_app.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album(None, 'Joy as an Act of Resistance', 2018, 5))
    result = repository.all()
    assert result == [
        Album(1,'Doolittle', 1989, 1),
        Album(2, 'Surfa Rosa', 1988, 1),
        Album(3,'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
        Album(13, 'Joy as an Act of Resistance', 2018, 5),
    ]

"""
When we call BookRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/music_html_web_app.sql")
    repository = AlbumRepository(db_connection)
    
    repository.delete(3)
    result = repository.all()
    assert result == [
        Album(1,'Doolittle', 1989, 1),
        Album(2, 'Surfa Rosa', 1988, 1),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
    ]
