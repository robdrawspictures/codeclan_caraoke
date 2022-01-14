import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room(1, 5)
        self.guest1 = Guest("Bobby", 50)
        self.guest2 = Guest("Dan", 40)
        self.guest3 = Guest("John", 70)
        self.guest4 = Guest("Lynne", 30)
        self.guest5 = Guest("Eric", 0)
        self.guest6 = Guest("Sam", 80)
        self.party1 = [self.guest1, self.guest2, self.guest3,
                    self.guest4, self.guest5]
        self.song1 = Song("Raining Blood", "Slayer", "A")
        self.song2 = Song("Common People", "Pulp", "C")
        self.song3 = Song("A Little Respect", "Erasure", "B")
        self.song4 = Song("Careless Whisper", "George Michael", "B")
        self.song5 = Song("My Way", "Frank Sinatra", "S")
        self.songbook1 = [self.song1, self.song1, self.song1,
                    self.song4, self.song5]
        self.song6 = Song("Love Shack", "The B-52s", "D")
        self.song7 = Song("Who Wants To Live Forever", "Queen", "S")
        self.song8 = Song("Creep", "Radiohead", "D")
        self.song9 = Song("Hysteria", "Muse", "A")
        self.song10 = Song("Tango Til They're Sore", "Tom Waits", "A")
        self.songbook2 = [self.song6, self.song7, self.song8,
                    self.song9, self.song10]
        self.song11 = Song("Common People", "William Shatner", "D")

        
    def test_add_guest_to_room(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_guest_to_room(self.guest2)
        self.room1.add_guest_to_room(self.guest3)
        self.assertEqual(3, self.room1.check_room_capacity())

    def test_bulk_add(self):
        self.room1.add_party_to_room(self.party1)
        self.assertEqual(5, self.room1.check_room_capacity())

    def test_max_occupancy_reached(self):
        self.room1.add_party_to_room(self.party1)
        self.assertEqual(5, self.room1.check_room_capacity())
        self.assertFalse(self.room1.check_max_capacity())
        self.room1.add_guest_to_room(self.guest6)
        self.assertEqual(6, self.room1.check_room_capacity())
        self.assertTrue(self.room1.check_max_capacity())

    def test_add_track(self):
        self.room1.add_single_track(self.song11)
        self.assertEqual(1, len(self.room1.tracklist))

    def test_add_trackist(self):
        self.room1.add_tracklist(self.songbook1)
        self.assertEqual(5, len(self.room1.tracklist))
        self.room1.add_tracklist(self.songbook2)
        self.assertEqual(10, len(self.room1.tracklist))

    def test_find_song_by_name(self):
        self.room1.add_tracklist(self.songbook1)
        self.room1.add_tracklist(self.songbook2)
        self.room1.find_song_by_name("Creep")
        self.assertEqual("Creep", self.room1.song_search[0].title)

    def test_find_multiple_songs_with_same_name(self):
        self.room1.add_tracklist(self.songbook1)
        self.room1.add_tracklist(self.songbook2)
        self.room1.add_single_track(self.song11)
        self.assertEqual(11, len(self.room1.tracklist))
        self.room1.find_song_by_name("Common People")
        self.assertEqual(2, len(self.room1.song_search))
        self.assertEqual("Pulp", self.room1.song_search[0].artist)
