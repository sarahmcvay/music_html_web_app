from lib.artist import Artist 

class ArtistRepository: 
    def __init__(self, connection):
        self._connection = connection

    def all(self): #To list all artists
        rows = self._connection.execute(
            'SELECT * from artists')
        artists = []
        for row in rows:
            item = Artist(
                row['id'],
                row['name'],
                row['genre'],
            )
            artists.append(item)
        return artists

    def find(self, artist_id):
        rows = self._connection.execute(
            'SELECT * from artists WHERE id = %s', [artist_id])
        row = rows[0]
        return Artist( 
                row['id'], 
                row['name'], 
                row['genre'], 
            )

    def create(self, artist): # To create a new artist 
        self._connection.execute(
            'INSERT INTO artists(name, genre) VALUES (%s, %s)', [artist.name, artist.genre]
        )
        return None

    # def delete(self, artist_id): #To delete an artist by its id