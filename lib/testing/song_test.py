# test_song.py

from lib.song import Song

def test_song_count():
    Song.count = 0
    Song("Song A", "Artist A", "Genre A")
    Song("Song B", "Artist B", "Genre B")
    assert Song.count == 2

def test_unique_genres_and_artists():
    Song.genres = []
    Song.artists = []
    Song("Test Song", "Artist A", "Genre A")
    Song("Another Song", "Artist A", "Genre A")
    assert "Genre A" in Song.genres
    assert "Artist A" in Song.artists
    assert len(Song.genres) == 1
    assert len(Song.artists) == 1

def test_genre_and_artist_count():
    Song.genre_count = {}
    Song.artist_count = {}
    Song("Song X", "Artist X", "Pop")
    Song("Song Y", "Artist X", "Pop")
    assert Song.genre_count["Pop"] == 2
    assert Song.artist_count["Artist X"] == 2
