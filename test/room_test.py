import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song
from src.bar import Bar

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room(1, 5, 5)
        self.bar = Bar()
        self.guest1 = Guest("Bobby", 50, "Still Life", "B")
        self.guest2 = Guest("Dan", 40, "Tango Til They're Sore", "C")
        self.guest3 = Guest("John", 70, "Don't Stop Believin", "A")
        self.guest4 = Guest("Lynne", 30, "Total Eclipse Of The Heart", "C")
        self.guest5 = Guest("Eric", 0, "Dog Days Are Over", "D")
        self.guest6 = Guest("Sam", 80, "Auld Lang Syne", "A")
        self.guest7 = Guest("Rachel", 90, "Copa Cabana", "B")
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
        self.assertEqual(4, self.room1.check_room_capacity())

    def test_remove_guest_from_room(self):
        self.room1.add_party_to_room(self.party1)
        self.assertEqual(4, self.room1.check_room_capacity())
        self.room1.remove_guest_from_room("John")
        self.assertEqual(3, self.room1.check_room_capacity())

    def test_remove_party_from_room(self):
        self.room1.add_party_to_room(self.party1)
        self.assertEqual(4, self.room1.check_room_capacity())
        self.room1.remove_party_from_room()
        self.assertEqual(0, self.room1.check_room_capacity())

    def test_max_occupancy_reached(self):
        self.room1.add_party_to_room(self.party1)
        self.assertEqual(4, self.room1.check_room_capacity())
        self.assertFalse(self.room1.check_max_capacity())
        self.room1.add_guest_to_room(self.guest6)
        self.room1.add_guest_to_room(self.guest7)
        self.assertEqual(6, self.room1.check_room_capacity())
        self.assertTrue(self.room1.check_max_capacity())

    def test_charge_entry_fee(self):
        self.room1.add_guest_to_room(self.guest1)
        self.assertEqual(1, self.room1.check_room_capacity())
        self.assertEqual(45, self.room1.occupancy[0].cash)
        self.room1.add_guest_to_room(self.guest5)
        self.assertEqual(1, self.room1.check_room_capacity())

    def test_charge_party_entry_fee(self):
        self.room1.add_party_to_room(self.party1)
        self.assertEqual(4, self.room1.check_room_capacity())
        self.assertEqual(35, self.room1.occupancy[1].cash)
        
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

    # def test_find_multiple_songs_with_same_name(self):
    #     self.room1.add_tracklist(self.songbook1)
    #     self.room1.add_tracklist(self.songbook2)
    #     self.room1.add_single_track(self.song11)
    #     self.assertEqual(11, len(self.room1.tracklist))
    #     self.room1.find_song_by_name("Common People")
    #     self.assertEqual(2, len(self.room1.song_search))
    #     self.assertEqual("Pulp", self.room1.song_search[0].artist)

    # This is humped for now, I'll come back to it later.

    def test_add_song_to_queue(self):
        self.room1.add_tracklist(self.songbook1)
        self.room1.add_tracklist(self.songbook2)
        self.room1.find_song_by_name("Creep")
        self.room1.add_song_to_queue(self.room1.song_search[0].title, self.guest1)
        self.assertEqual(0, len(self.room1.song_search))
        self.assertEqual(1, len(self.room1.queue))

    def test_play_favourite_song(self):
        self.room1.add_tracklist(self.songbook1)
        self.room1.add_tracklist(self.songbook2)
        self.room1.add_guest_to_room(self.guest2)
        self.room1.find_song_by_name("Tango Til They're Sore")
        self.assertEqual("Aww absolute banger, mate.", self.room1.add_song_to_queue(self.room1.song_search[0].title, self.guest2))

    def test_empty_queue_prompt(self):
        self.assertEqual("Sing, you cowards!", self.room1.empty_queue_prompt())

    def test_guests_total_money(self):
        self.room1.add_party_to_room(self.party1)
        self.assertEqual(4, len(self.room1.occupancy))
        self.room1.guests_total_money()
        self.assertEqual(170, self.room1.guest_budget)

    def test_guests_can_pay_tab(self):
        self.room1.add_party_to_room(self.party1)
        self.room1.guests_total_money()       
        self.assertTrue(self.room1.guests_can_pay_tab())
        self.room1.tab = 200
        self.assertFalse(self.room1.guests_can_pay_tab())

    def test_increase_tab(self):
        self.room1.add_party_to_room(self.party1)
        self.room1.guests_total_money()
        self.room1.increase_tab(self.bar.food)
        self.assertEqual(10, self.room1.tab)
        self.room1.remove_party_from_room()
        self.room1.guests_total_money()
        self.assertEqual("Pay your bill, freeloader.", self.room1.increase_tab(self.bar.drink))

    def test_rate_performance(self):
        self.room1.add_single_track(self.song1)
        self.room1.add_guest_to_room(self.guest1)
        self.assertEqual(f"{self.guest1.name} tried their best. Probably.", self.room1.rate_performance(self.guest1, self.song1.difficulty))
        self.room1.add_single_track(self.song5)
        self.room1.add_guest_to_room(self.guest4)
        self.assertEqual("I envy the deaf.", self.room1.rate_performance(self.guest4, self.song5.difficulty))
        
