class Item:
    def __init__(self, name, importance):
        self.name = name
        self.importance = importance
        self.next_item = None


class Inventory:
    def __init__(self):
        self.head = None

    def add_item(self, name, importance):
        new_item = Item(name, importance)
        if self.head is None:
            self.head = new_item
        else:
            current_item = self.head
            while current_item.next_item is not None:
                current_item = current_item.next_item
            current_item.next_item = new_item

    def remove_item(self, name):
        if self.head is None:
            print("Tas kosong.")
            return

        if self.head.name == name:
            self.head = self.head.next_item
            print("Item", name, "telah dihapus.")
            return

        current_item = self.head
        prev_item = None
        while current_item is not None:
            if current_item.name == name:
                prev_item.next_item = current_item.next_item
                print("Item", name, "telah dihapus.")
                return
            prev_item = current_item
            current_item = current_item.next_item

        print("Item", name, "tidak ditemukan.")

    def print_items_by_importance(self):
        if self.head is None:
            print("Tas kosong.")
            return

        sorted_items = self._sort_items_by_importance()
        print("Daftar item dalam tas berdasarkan tingkat kepentingan:")
        for item in sorted_items:
            print("Nama:", item.name, "| Kepentingan:", item.importance)

    def _sort_items_by_importance(self):
        items = []
        current_item = self.head
        while current_item is not None:
            items.append(current_item)
            current_item = current_item.next_item
        items.sort(key=lambda x: x.importance, reverse=True)
        return items


# Contoh penggunaan program
inventory = Inventory()

# Menambahkan item ke dalam tas
inventory.add_item("Potion", 9)
inventory.add_item("Sword", 5)
inventory.add_item("Shield", 7)
inventory.add_item("Gold Coin", 2)

# Mencetak daftar item berdasarkan tingkat kepentingan
inventory.print_items_by_importance()

# Menghapus item
inventory.remove_item("Sword")

# Mencetak daftar item berdasarkan tingkat kepentingan setelah penghapusan
inventory.print_items_by_importance()
