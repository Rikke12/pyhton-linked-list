class Product:
    def __init__(self, name, code, stock):
        self.name = name
        self.code = code
        self.stock = stock
        self.next_product = None


class Inventory:
    def __init__(self):
        self.head = None

    def add_product(self, name, code, stock):
        new_product = Product(name, code, stock)
        if self.head is None:
            self.head = new_product
        else:
            current_product = self.head
            while current_product.next_product is not None:
                current_product = current_product.next_product
            current_product.next_product = new_product

    def remove_product(self, code):
        if self.head is None:
            print("Inventaris kosong.")
            return

        if self.head.code == code:
            self.head = self.head.next_product
            print("Produk dengan kode", code, "telah dihapus.")
            return

        current_product = self.head
        prev_product = None
        while current_product is not None:
            if current_product.code == code:
                prev_product.next_product = current_product.next_product
                print("Produk dengan kode", code, "telah dihapus.")
                return
            prev_product = current_product
            current_product = current_product.next_product

        print("Produk dengan kode", code, "tidak ditemukan.")

    def print_inventory(self):
        if self.head is None:
            print("Inventaris kosong.")
            return

        print("Daftar produk dan jumlah stok:")
        current_product = self.head
        while current_product is not None:
            print("Nama:", current_product.name, "| Kode:", current_product.code, "| Stok:", current_product.stock)
            current_product = current_product.next_product


# Contoh penggunaan program
inventory = Inventory()

# Menambahkan produk ke dalam inventaris
inventory.add_product("Sepatu", "BK001", 10)
inventory.add_product("Kemeja", "PS001", 25)
inventory.add_product("Celana", "PN001", 15)
inventory.add_product("Sabuk", "KT001", 35)

# Mencetak daftar produk dan jumlah stoknya
inventory.print_inventory()

# Menghapus produk
inventory.remove_product("PS001")

# Mencetak daftar produk dan jumlah stoknya setelah penghapusan
inventory.print_inventory()
 