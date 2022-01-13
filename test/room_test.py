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
        self.song1 = Song("Raining Blood", "A")
        self.song2 = Song("Common People", "C")
        self.song3 = Song("A Little Respect", "B")
        self.song4 = Song("Careless Whisper", "B")
        self.song5 = Song("My Way", "S")
        self.songbook = [self.song1, self.song1, self.song1,
                    self.song4, self.song5]
        
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

    def test_add_trackist(self):
        self.room1.add_tracklist(self.songbook)
        self.assertEqual(5, len(self.room1.tracklist))