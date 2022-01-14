class Room:
    def __init__(self, number, fee, capacity):
        self.number = number
        self.fee = fee
        self.capacity = capacity
        self.occupancy = []
        self.tracklist = []
        self.song_search = []
        self.queue = []

    # def add_guest_to_room(self, guest):
    #     if len(self.occupancy) < 5:
    #         self.occupancy.append(guest)

    # The above would be my preferred way of preventing
    # over-occupation of rooms, but this breaks the test
    # I made specifically for max capacity (line 24-29).

    def add_guest_to_room(self, guest):
        if guest.cash >= self.fee:
            guest.cash -= self.fee
            self.occupancy.append(guest)
        # else:
        #     print("You can sing for free all you want in the shower.")

    def add_party_to_room(self, party):
        for guest in party:
            if guest.cash >= self.fee:
                guest.cash -= self.fee
                self.occupancy.append(guest)

    def remove_guest_from_room(self, name):
        for guest in self.occupancy:
            if guest.name == name:
                self.occupancy.remove(guest)

    def remove_party_from_room(self):
        self.occupancy.clear()

    def add_single_track(self, track):
        self.tracklist.append(track)

    def add_tracklist(self, tracks):
        for track in tracks:
            self.tracklist.append(track)

    def check_room_capacity(self):
        return len(self.occupancy)

    def check_max_capacity(self):
        capacity_reached = False
        if len(self.occupancy) > 5:
            capacity_reached = True

        return capacity_reached

    def find_song_by_name(self, name):
        for track in self.tracklist:
            if track.title == name:
                self.song_search.append(track)
