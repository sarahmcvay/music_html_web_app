class Album:
    # We initialise with all attributes (all columns have an attribute)
    def __init__(self, id, title, release_year, artist_id): 
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id

    # To allow tests to assert that objects are made as expected
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    # To format more easily when we print
    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"