class Room:
    def __init__(self, number, fee):
        self.number = number
        self.fee = fee
        self.occupancy = []
        self.tracklist = []

    # def add_guest_to_room(self, guest):
    #     if len(self.occupancy) < 5:
    #         self.occupancy.append(guest)

    # The above would be my preferred way of preventing
    # over-occupation of rooms, but this breaks the test
    # I made specifically for max capacity (line 24-29).

    def add_guest_to_room(self, guest):
        self.occupancy.append(guest)

    def add_party_to_room(self, party):
        for guest in party:
            self.occupancy.append(guest)

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