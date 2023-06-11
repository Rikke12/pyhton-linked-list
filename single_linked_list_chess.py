class Participant:
    def __init__(self, name, ranking):
        self.name = name
        self.ranking = ranking
        self.next_participant = None


class Tournament:
    def __init__(self):
        self.head = None

    def register_participant(self, name, ranking):
        new_participant = Participant(name, ranking)
        if self.head is None:
            self.head = new_participant
        else:
            current_participant = self.head
            while current_participant.next_participant is not None:
                current_participant = current_participant.next_participant
            current_participant.next_participant = new_participant

    def eliminate_participant(self, name):
        if self.head is None:
            print("Daftar peserta kosong.")
            return

        if self.head.name == name:
            self.head = self.head.next_participant
            print("Peserta", name, "telah dieliminasi.")
            return

        current_participant = self.head
        prev_participant = None
        while current_participant is not None:
            if current_participant.name == name:
                prev_participant.next_participant = current_participant.next_participant
                print("Peserta", name, "telah dieliminasi.")
                return
            prev_participant = current_participant
            current_participant = current_participant.next_participant

        print("Peserta", name, "tidak ditemukan.")

    def print_participants_by_ranking(self):
        if self.head is None:
            print("Daftar peserta kosong.")
            return

        sorted_participants = self._sort_participants_by_ranking()
        print("Daftar peserta berdasarkan peringkat:")
        for participant in sorted_participants:
            print("Nama:", participant.name, "| Peringkat:", participant.ranking)

    def _sort_participants_by_ranking(self):
        participants = []
        current_participant = self.head
        while current_participant is not None:
            participants.append(current_participant)
            current_participant = current_participant.next_participant
        participants.sort(key=lambda x: x.ranking)
        return participants


# Contoh penggunaan program
tournament = Tournament()

# Mendaftarkan peserta turnamen
tournament.register_participant("Leo", 1500)
tournament.register_participant("Budi", 1800)
tournament.register_participant("Abdul", 1650)
tournament.register_participant("Dewi", 1600)

# Mencetak daftar peserta berdasarkan peringkat
tournament.print_participants_by_ranking()

# Menghapus peserta yang kalah
tournament.eliminate_participant("Dewi")

# Mencetak daftar peserta berdasarkan peringkat setelah eliminasi
tournament.print_participants_by_ranking()
