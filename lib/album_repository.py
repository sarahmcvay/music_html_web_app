from lib.album import Album

class AlbumRepository: 
    # Initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # To retrieve all albums
    def all(self):
        rows = self._connection.execute(
            'SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(
                row['id'], 
                row['title'], 
                row['release_year'], 
                row['artist_id']
            )
            albums.append(item)
        return albums
    
    # To find a single album by its id
    def find(self, album_id):
        rows = self._connection.execute(
            'SELECT * from albums WHERE id = %s', [album_id])
        row = rows[0]
        return Album( 
                row['id'], 
                row['title'], 
                row['release_year'], 
                row['artist_id']
            )
    
    #  To create a new album
    def create(self, album):
        self._connection.execute(
            'INSERT INTO albums (title, release_year, artist_id)'
            'VALUES (%s, %s, %s)', [album.title, album.release_year, album.artist_id])
        return None

    #  To delete an album
    def delete(self, album_id):
        self._connection.execute(
            'DELETE FROM albums WHERE id = %s', [album_id])
        return None