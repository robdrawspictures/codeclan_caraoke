class Room:
    def __init__(self, number, fee, capacity):
        self.number = number
        self.fee = fee
        self.capacity = capacity
        self.occupancy = []
        self.tracklist = []
        self.song_search = []
        self.queue = []
        self.tab = 0
        self.guest_budget = 0
        self.ratings = {"S" : 10, "A" : 8, "B" : 6,
        "C" : 4, "D" : 2, "F" : 0
        }

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

    def add_song_to_queue(self, title, guest):
        for song in self.song_search:
            if song.title == title and song.title == guest.fav_song:
                return "Aww absolute banger, mate."
            elif song.title == title:
                self.queue.append(song)
                self.song_search.clear()
                return f"Up Next: {guest.name} singing '{title}'!"
                    
    def empty_queue_prompt(self):
        if len(self.queue) == 0:
            return "Sing, you cowards!"

    def guests_total_money(self):
        purse = 0
        for guest in self.occupancy:
            purse += guest.cash

        self.guest_budget = purse

    def guests_can_pay_tab(self):
        if self.guest_budget > self.tab:
            return True
        else:
            return False

    def increase_tab(self, purchase):
        if self.guests_can_pay_tab():
            self.tab += purchase
        else:
            return "Pay your bill, freeloader."

    # def convert_str_to_int(self, string):  
    #     for rating, number in self.ratings.items():
    #         if rating == string:
    #             string = number

    # ^ Currently busted because I can't figure out how
    # To permanently change a variable outside a function.
    # In its current state, the function correctly re-assigns
    # the variable, but it doesn't persist outside the function.

