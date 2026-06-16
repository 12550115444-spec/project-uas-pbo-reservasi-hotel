"""
====================================================
SISTEM RESERVASI HOTEL
Project UAS Pemrograman Berbasis Objek

Fitur:
- OOP
- Abstract Class
- Encapsulation
- Inheritance (3 Level)
- Mixins
- State Machine
- Composition
- Operator Overloading
- Strategy Pattern
- CRUD
====================================================
"""

from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime
from functools import total_ordering


# ====================================================
# EXCEPTION
# ====================================================

class HotelError(Exception):
    """
    Exception dasar untuk seluruh kesalahan
    yang terjadi pada sistem reservasi hotel.

    Example:
        >>> raise HotelError("Terjadi kesalahan")
    """


class DataTidakDitemukanError(HotelError):
    """
    Exception yang muncul ketika data yang dicari
    tidak ditemukan dalam sistem.

    Example:
        >>> raise DataTidakDitemukanError(
        ...     "Kamar tidak ditemukan"
        ... )
    """


class DataSudahAdaError(HotelError):
    """
    Exception yang muncul ketika data yang akan
    ditambahkan sudah tersedia dalam sistem.

    Example:
        >>> raise DataSudahAdaError(
        ...     "Kamar sudah ada"
        ... )
    """

class KamarTidakTersediaError(HotelError):
    """
    Exception yang muncul ketika kamar tidak dapat
    digunakan untuk proses booking.

    Example:
        >>> raise KamarTidakTersediaError(
        ...     "Kamar tidak tersedia"
        ... )
    """


# ====================================================
# STATE MACHINE
# ====================================================

class StatusKamar(Enum):
    """
    Enumerasi status kamar pada sistem hotel.

    Attributes:
        TERSEDIA : Kamar dapat dipesan.
        DIBOOKING : Kamar telah dibooking.
        DITEMPATI : Kamar sedang ditempati.
        CHECKOUT : Kamar telah checkout.

    Example:
        >>> StatusKamar.TERSEDIA
    """

    TERSEDIA = "Tersedia"
    DIBOOKING = "Dibooking"
    DITEMPATI = "Ditempati"
    CHECKOUT = "Checkout"


# ====================================================
# ABSTRACT CLASS
# ====================================================

class ItemHotel(ABC):
    """
    Abstract Base Class untuk seluruh objek
    yang berada dalam sistem hotel.

    Method:
        tampilkan_info()

    Example:
        >>> class Demo(ItemHotel):
        ...     def tampilkan_info(self):
        ...         pass
    """

    @abstractmethod
    def tampilkan_info(self):
        pass


# ====================================================
# MIXIN 1
# ====================================================

class LoggingMixin:
    """
    Mixin yang menyediakan fitur pencatatan
    aktivitas sistem (logging).

    Method:
        log(pesan)

    Example:
        >>> self.log("Data berhasil ditambahkan")
    """

    def log(self, pesan):

        print(
            f"[{datetime.now()}] {pesan}"
        )


# ====================================================
# MIXIN 2
# ====================================================

class ValidationMixin:
    """
    Mixin yang menyediakan validasi data
    sebelum diproses sistem.

    Method:
        validasi_nomor(nomor)

    Example:
        >>> self.validasi_nomor("101")
        True
    """

    def validasi_nomor(self, nomor):

        if len(str(nomor)) < 3:

            raise ValueError(
                "Nomor kamar minimal 3 karakter"
            )

        return True


# ====================================================
# CLASS KAMAR
# ====================================================

class Kamar(ItemHotel):
    """
    Merepresentasikan data kamar hotel.

    Attributes:
        nomor (str): Nomor kamar.
        tipe (str): Jenis kamar.
        harga (int): Harga kamar.
        status (StatusKamar): Status kamar.

    Example:
        >>> kamar = KamarStandard(
        ...     "101",
        ...     300000
        ... )
        >>> print(kamar.nomor)
        101
    """

    def __init__(
        self,
        nomor,
        tipe,
        harga
    ):

        self.__nomor = nomor
        self.__tipe = tipe
        self.__harga = harga
        self.__status = StatusKamar.TERSEDIA

    # =====================================
    # PROPERTY
    # =====================================

    @property
    def nomor(self):
        return self.__nomor

    @property
    def tipe(self):
        return self.__tipe

    @property
    def harga(self):
        return self.__harga

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status_baru):
        self.__status = status_baru

    # =====================================
    # POLYMORPHISM
    # =====================================

    def tampilkan_info(self):

        print(f"""
=================================
Nomor  : {self.nomor}
Tipe   : {self.tipe}
Harga  : Rp {self.harga}
Status : {self.status.value}
=================================
""")

    # =====================================
    # OPERATOR OVERLOADING
    # =====================================

    def __str__(self):

        return (
            f"Kamar {self.nomor}"
        )

    def __repr__(self):

        return self.__str__()

    def __eq__(self, other):

        return (
            self.nomor ==
            other.nomor
        )

    def __lt__(self, other):

        return (
            self.nomor <
            other.nomor
        )

    def __gt__(self, other):

        return (
            self.nomor >
            other.nomor
        )

    def __len__(self):

        return len(
            str(self.nomor)
        )


# ====================================================
# INHERITANCE LEVEL 2
# ====================================================

class KamarStandard(Kamar):
    """
    Kelas turunan Kamar yang merepresentasikan
    kamar tipe Standard.

    Attributes:
        nomor (str): Nomor kamar.
        harga (int): Harga kamar.

    Example:
        >>> kamar = KamarStandard(
        ...     "101",
        ...     300000
        ... )
    """

    def __init__(
        self,
        nomor,
        harga
    ):

        super().__init__(
            nomor,
            "Standard",
            harga
        )


class KamarVIP(Kamar):
    """
    Kelas turunan Kamar yang merepresentasikan
    kamar tipe VIP.

    Attributes:
        nomor (str): Nomor kamar.
        harga (int): Harga kamar.

    Example:
        >>> kamar = KamarVIP(
        ...     "201",
        ...     500000
        ... )
    """

    def __init__(
        self,
        nomor,
        harga
    ):

        super().__init__(
            nomor,
            "VIP",
            harga
        )


# ====================================================
# INHERITANCE LEVEL 3
# ====================================================

class KamarVIPGold(KamarVIP):
    """
    Kelas turunan KamarVIP yang merepresentasikan
    kamar tipe VIP Gold.

    Attributes:
        nomor (str): Nomor kamar.
        harga (int): Harga kamar.

    Example:
        >>> kamar = KamarVIPGold(
        ...     "301",
        ...     700000
        ... )
    """

    def __init__(
        self,
        nomor,
        harga
    ):

        super().__init__(
            nomor,
            harga
        )


# ====================================================
# CLASS TAMU
# ====================================================

class Tamu:
    """
    Merepresentasikan data tamu hotel.

    Attributes:
        id_tamu (str): ID unik tamu.
        nama (str): Nama tamu.

    Example:
        >>> tamu = Tamu(
        ...     "T01",
        ...     "Haikal"
        ... )
    """

    def __init__(
        self,
        id_tamu,
        nama
    ):

        self.__id_tamu = id_tamu
        self.__nama = nama

    @property
    def id_tamu(self):
        return self.__id_tamu

    @property
    def nama(self):
        return self.__nama

    def tampilkan_info(self):

        print(f"""
=================================
ID Tamu : {self.id_tamu}
Nama    : {self.nama}
=================================
""")

    def __str__(self):

        return self.nama

# ====================================================
# KOMPOSISI 1
# CLASS PEMBAYARAN
# ====================================================

class Pembayaran:
    """
    Menyimpan informasi pembayaran reservasi.

    Attributes:
        metode (str): Metode pembayaran.
        total (int): Total biaya.

    Example:
        >>> bayar = Pembayaran(
        ...     "Cash",
        ...     300000
        ... )
    """

    def __init__(
        self,
        metode,
        total
    ):

        self.metode = metode
        self.total = total

    def __str__(self):

        return (
            f"{self.metode}"
            f" | Rp {self.total}"
        )


# ====================================================
# KOMPOSISI 2
# CLASS RESERVASI
# ====================================================

class Reservasi:
    """
    Merepresentasikan data reservasi kamar.         

    Relasi:
        - Agregasi dengan Tamu
        - Agregasi dengan Kamar
        - Komposisi dengan Pembayaran

    Attributes:
        kode (str): Kode reservasi.
        tamu (Tamu): Data tamu.
        kamar (Kamar): Data kamar.
        pembayaran (Pembayaran): Data pembayaran.

    Example:
        >>> reservasi = Reservasi(
        ...     "RSV-1",
        ...     tamu,
        ...     kamar,
        ...     "Cash",
        ...     300000
        ... )
    """

    def __init__(self, kode, tamu, kamar, metode_bayar, total_bayar):
        self.kode = kode
        self.tamu = tamu
        self.kamar = kamar
        
        # KODINGAN INI SEKARANG DI BUAT DI OWNER (Reservasi)
        self.pembayaran = Pembayaran(metode_bayar, total_bayar) 

    def tampilkan_info(self):
        print(f"""
=================================
KODE        : {self.kode}
TAMU        : {self.tamu}
KAMAR       : {self.kamar}
PEMBAYARAN  : {self.pembayaran}
=================================
""")


# ====================================================
# CLASS INVOICE
# ====================================================

class Invoice:
    """
    Merepresentasikan invoice atau bukti
    pembayaran reservasi.

    Attributes:
        kode (str): Nomor invoice.
        reservasi (Reservasi): Data reservasi.

    Example:
        >>> invoice = Invoice(
        ...     "INV-1",
        ...     reservasi
        ... )
    """

    def __init__(
        self,
        kode,
        reservasi
    ):

        self.kode = kode
        self.reservasi = reservasi

    def cetak(self):

        print(f"""
=================================
INVOICE
=================================
Kode Invoice : {self.kode}
Reservasi    : {self.reservasi.kode}
=================================
""")


# ====================================================
# COLLECTION CLASS
# ====================================================

class KoleksiKamar:
    """
    Collection class yang menyimpan kumpulan
    objek kamar.

    Mendukung:
        - len()
        - iter()
        - contains()
        - getitem()

    Attributes:
        __items (list): Daftar objek kamar.

    Example:
        >>> koleksi = KoleksiKamar()
        >>> koleksi.tambah(
        ...     KamarStandard("101",300000)
        ... )
    """

    def __init__(self):

        self.__items = []

    def tambah(
        self,
        kamar
    ):

        self.__items.append(
            kamar
        )

    def hapus(
        self,
        kamar
    ):

        self.__items.remove(
            kamar
        )

    def semua(self):

        return self.__items

    def __len__(self):

        return len(
            self.__items
        )

    def __iter__(self):

        return iter(
            self.__items
        )

    def __contains__(
        self,
        item
    ):

        return (
            item in self.__items
        )


# ====================================================
# STRATEGY PATTERN
# ====================================================

class ReportStrategy(ABC):
    """
    Abstract Strategy untuk pembuatan laporan.

    Seluruh strategi laporan wajib
    mengimplementasikan method generate().

    Example:
        >>> class ExcelReport(
        ...     ReportStrategy
        ... ):
        ...     def generate(self,data):
        ...         pass
    """

    @abstractmethod
    def generate(
        self,
        data
    ):
        pass

# ====================================================
# PDF REPORT STRATEGY
# ====================================================

class PDFReport(ReportStrategy):
    """
    Strategi pembuatan laporan dalam
    format PDF.

    Example:
        >>> report = PDFReport()
        >>> report.generate(data)
    """
    def generate(self, data):
        print("\n===== REPORT PDF =====")
        for item in data:
            print(f"[PDF] {item}")
        print("======================\n")


# ====================================================
# TXT REPORT
# ====================================================

class TXTReport(ReportStrategy):
    """
    Strategi pembuatan laporan dalam
    format TXT.

    Example:
        >>> report = TXTReport()
        >>> report.generate(data)
    """
    def generate(
        self,
        data
    ):

        print(
            "\n===== REPORT TXT ====="
        )

        for item in data:

            print(item)


# ====================================================
# JSON REPORT
# ====================================================

class JSONReport(ReportStrategy):
    """
    Strategi pembuatan laporan dalam
    format JSON.

    Example:
        >>> report = JSONReport()
        >>> report.generate(data)
    """

    def generate(
        self,
        data
    ):

        print(
            "\n===== REPORT JSON ====="
        )

        for item in data:

            print({
                "data": str(item)
            })


# ====================================================
# HOTEL
# ====================================================

class Hotel(
    LoggingMixin,
    ValidationMixin
):
    """
    Kelas utama yang mengelola seluruh
    proses sistem reservasi hotel.

    Fitur:
        - CRUD Kamar
        - CRUD Tamu
        - Booking Kamar
        - Check In
        - Check Out
        - Generate Report

    Attributes:
        __daftar_kamar (KoleksiKamar):
            Menyimpan seluruh kamar.
        __daftar_tamu (list[Tamu]):
            Menyimpan seluruh tamu.
        __daftar_reservasi (list[Reservasi]):
            Menyimpan seluruh reservasi.

    Example:
        >>> hotel = Hotel()
        >>> hotel.tambah_kamar(
        ...     KamarStandard(
        ...         "101",
        ...         300000
        ...     )
        ... )
        >>> hotel.lihat_kamar()
    """

    def __init__(self):

        self.__daftar_kamar = (
            KoleksiKamar()
        )

        self.__daftar_tamu = []

        self.__daftar_reservasi = []

    # ==========================================
    # CRUD KAMAR
    # ==========================================

    def tambah_kamar(
        self,
        kamar
    ):

        self.validasi_nomor(
            kamar.nomor
        )

        if self.cari_kamar(
            kamar.nomor
        ):

            raise DataSudahAdaError(
                "Kamar sudah ada"
            )

        self.__daftar_kamar.tambah(
            kamar
        )

        self.log(
            f"Kamar {kamar.nomor} ditambahkan"
        )

    def cari_kamar(
        self,
        nomor
    ):

        for kamar in self.__daftar_kamar:

            if kamar.nomor == nomor:

                return kamar

        return None

    def lihat_kamar(
        self
    ):

        if len(
            self.__daftar_kamar
        ) == 0:

            print(
                "Belum ada kamar"
            )

            return

        for kamar in self.__daftar_kamar:

            kamar.tampilkan_info()

    def hapus_kamar(
        self,
        nomor
    ):

        kamar = self.cari_kamar(
            nomor
        )

        if not kamar:

            raise DataTidakDitemukanError(
                "Kamar tidak ditemukan"
            )

        self.__daftar_kamar.hapus(
            kamar
        )

    def update_status_kamar(
        self,
        nomor,
        status
    ):

        kamar = self.cari_kamar(
            nomor
        )

        if not kamar:

            raise DataTidakDitemukanError(
                "Kamar tidak ditemukan"
            )

        kamar.status = status

    # ==========================================
    # CRUD TAMU
    # ==========================================

    def tambah_tamu(
        self,
        tamu
    ):

        if self.cari_tamu(
            tamu.id_tamu
        ):

            raise DataSudahAdaError(
                "Tamu sudah ada"
            )

        self.__daftar_tamu.append(
            tamu
        )

    def cari_tamu(
        self,
        id_tamu
    ):

        for tamu in self.__daftar_tamu:

            if (
                tamu.id_tamu ==
                id_tamu
            ):

                return tamu

        return None

    def lihat_tamu(
        self
    ):

        if len(
            self.__daftar_tamu
        ) == 0:

            print(
                "Belum ada tamu"
            )

            return

        for tamu in self.__daftar_tamu:

            tamu.tampilkan_info()

    def hapus_tamu(
        self,
        id_tamu
    ):

        tamu = self.cari_tamu(
            id_tamu
        )

        if not tamu:

            raise DataTidakDitemukanError(
                "Tamu tidak ditemukan"
            )

        self.__daftar_tamu.remove(
            tamu
        )

    # ==========================================
    # BOOKING KAMAR
    # ==========================================

    def booking_kamar(self, id_tamu, nomor_kamar, metode_bayar):
        tamu = self.cari_tamu(id_tamu)
        if not tamu:
            raise DataTidakDitemukanError("Tamu tidak ditemukan")

        kamar = self.cari_kamar(nomor_kamar)
        if not kamar:
            raise DataTidakDitemukanError("Kamar tidak ditemukan")

        if kamar.status != StatusKamar.TERSEDIA:
            raise KamarTidakTersediaError("Kamar tidak tersedia")

        kamar.status = StatusKamar.DIBOOKING
        kode = f"RSV-{len(self.__daftar_reservasi) + 1}"
        
        # Kirim metode_bayar dan kamar.harga langsung ke Reservasi
        reservasi = Reservasi(kode, tamu, kamar, metode_bayar, kamar.harga)
        
        self.__daftar_reservasi.append(reservasi)
        self.log(f"Kamar {nomor_kamar} dibooking")
        return reservasi

    # ==========================================
    # CHECK IN
    # ==========================================

    def checkin(
        self,
        nomor_kamar
    ):

        kamar = self.cari_kamar(
            nomor_kamar
        )

        if not kamar:

            raise DataTidakDitemukanError(
                "Kamar tidak ditemukan"
            )

        if kamar.status == StatusKamar.DIBOOKING:

            kamar.status = (
                StatusKamar.DITEMPATI
            )

            self.log(
                f"Kamar {nomor_kamar} check in"
            )

        else:

            raise HotelError(
                "Kamar belum dibooking"
            )

    # ==========================================
    # CHECK OUT
    # ==========================================

    def checkout(
        self,
        nomor_kamar
    ):

        kamar = self.cari_kamar(
            nomor_kamar
        )

        if not kamar:

            raise DataTidakDitemukanError(
                "Kamar tidak ditemukan"
            )

        kamar.status = (
            StatusKamar.CHECKOUT
        )

        self.log(
            f"Kamar {nomor_kamar} checkout"
        )

        kamar.status = (
            StatusKamar.TERSEDIA
        )

    # ==========================================
    # LIHAT RESERVASI
    # ==========================================

    def lihat_reservasi(
        self
    ):

        if len(
            self.__daftar_reservasi
        ) == 0:

            print(
                "Belum ada reservasi"
            )

            return

        for reservasi in self.__daftar_reservasi:

            reservasi.tampilkan_info()

    # ==========================================
    # REPORT
    # ==========================================

    def generate_report(
        self,
        strategy
    ):

        data = []

        for kamar in self.__daftar_kamar:

            data.append(
                str(kamar)
            )

        strategy.generate(
            data
        )


# ====================================================
# MENU RESEPSIONIS (VERSI PERBAIKAN TOTAL)
# ====================================================

def menu_resepsionis(hotel):
    while True:
        print("""
=================================
MENU RESEPSIONIS
=================================
1. Tambah Kamar Standard
2. Tambah Kamar VIP
3. Tambah Kamar VIP Gold
4. Lihat Kamar
5. Tambah Tamu
6. Lihat Tamu
7. Lihat Reservasi
8. Report TXT
9. Report JSON
10. Report PDF              
11. Kembali
=================================
""")
        pilih = input("Pilih menu : ")

        try:
            if pilih == "1":
                nomor = input("Nomor : ")
                harga = int(input("Harga : "))
                hotel.tambah_kamar(KamarStandard(nomor, harga))

            elif pilih == "2":
                nomor = input("Nomor : ")
                harga = int(input("Harga : "))
                hotel.tambah_kamar(KamarVIP(nomor, harga))

            elif pilih == "3":
                nomor = input("Nomor : ")
                harga = int(input("Harga : "))
                hotel.tambah_kamar(KamarVIPGold(nomor, harga))

            elif pilih == "4":
                hotel.lihat_kamar()

            elif pilih == "5":
                id_tamu = input("ID Tamu : ")
                nama = input("Nama : ")
                hotel.tambah_tamu(Tamu(id_tamu, nama))

            elif pilih == "6":
                hotel.lihat_tamu()

            elif pilih == "7":
                hotel.lihat_reservasi()  # <-- Sekarang pilihan 7 akan langsung berjalan di sini!

            elif pilih == "8":
                hotel.generate_report(TXTReport())

            elif pilih == "9":
                hotel.generate_report(JSONReport())

            elif pilih == "10":
                hotel.generate_report(PDFReport())

            elif pilih == "11":
                break

            else:
                print("Menu tidak valid")

        except Exception as e:
            print(f"Error : {e}")
        pilih = input(
            "Pilih menu : "
        )

        try:

            if pilih == "1":

                nomor = input(
                    "Nomor : "
                )

                harga = int(
                    input("Harga : ")
                )

                hotel.tambah_kamar(
                    KamarStandard(
                        nomor,
                        harga
                    )
                )

            elif pilih == "2":

                nomor = input(
                    "Nomor : "
                )

                harga = int(
                    input("Harga : ")
                )

                hotel.tambah_kamar(
                    KamarVIP(
                        nomor,
                        harga
                    )
                )

            elif pilih == "3":

                nomor = input(
                    "Nomor : "
                )

                harga = int(
                    input("Harga : ")
                )

                hotel.tambah_kamar(
                    KamarVIPGold(
                        nomor,
                        harga
                    )
                )

            elif pilih == "4":

                hotel.lihat_kamar()

            elif pilih == "5":

                id_tamu = input(
                    "ID Tamu : "
                )

                nama = input(
                    "Nama : "
                )

                hotel.tambah_tamu(
                    Tamu(
                        id_tamu,
                        nama
                    )
                )

            elif pilih == "6":

                hotel.lihat_tamu()

            elif pilih == "7":

                hotel.lihat_reservasi()

            elif pilih == "8":

                hotel.generate_report(
                    TXTReport()
                )

            elif pilih == "9":

                hotel.generate_report(
                    JSONReport()
                )

            elif pilih == "10":

                break

            else:

                print(
                    "Menu tidak valid"
                )

        except Exception as e:

            print(
                f"Error : {e}"
            )


# ====================================================
# MENU TAMU
# ====================================================

def menu_tamu(
    hotel
):

    while True:

        print("""
=================================
MENU TAMU
=================================
1. Lihat Kamar
2. Booking Kamar
3. Check In
4. Check Out
5. Kembali
=================================
""")

        pilih = input(
            "Pilih menu : "
        )

        try:

            if pilih == "1":

                hotel.lihat_kamar()

            elif pilih == "2":

                id_tamu = input(
                    "ID Tamu : "
                )

                nomor = input(
                    "Nomor Kamar : "
                )

                metode = input(
                    "Metode Bayar : "
                )

                hotel.booking_kamar(
                    id_tamu,
                    nomor,
                    metode
                )

                print(
                    "Booking berhasil"
                )

            elif pilih == "3":

                nomor = input(
                    "Nomor Kamar : "
                )

                hotel.checkin(
                    nomor
                )

                print(
                    "Check In berhasil"
                )

            elif pilih == "4":

                nomor = input(
                    "Nomor Kamar : "
                )

                hotel.checkout(
                    nomor
                )

                print(
                    "Check Out berhasil"
                )

            elif pilih == "5":

                break

            else:

                print(
                    "Menu tidak valid"
                )

        except Exception as e:

            print(
                f"Error : {e}"
            )


# ====================================================
# MAIN
# ====================================================

def main():
    """
    Fungsi utama program.
    """

    hotel = Hotel()

    while True:

        print("""
=================================
SISTEM RESERVASI HOTEL
=================================
1. Login Resepsionis
2. Login Tamu
3. Keluar
=================================
""")

        pilihan = input(
            "Pilih : "
        )

        if pilihan == "1":

            menu_resepsionis(
                hotel
            )

        elif pilihan == "2":

            menu_tamu(
                hotel
            )

        elif pilihan == "3":

            print(
                "Program selesai"
            )

            break

        else:

            print(
                "Pilihan tidak valid"
            )


# ====================================================
# ENTRY POINT
# ====================================================

if __name__ == "__main__":
    # --- VERIFIKASI MULTIPLE INHERITANCE & MRO ---
    print("\n" + "="*50)
    print("VERIFIKASI MRO (METHOD RESOLUTION ORDER)")
    print("="*50)
    
    # Menampilkan urutan MRO dari kelas Hotel
    for i, kelas in enumerate(Hotel.__mro__, start=1):
        print(f"Urutan ke-{i}: {kelas.__name__}")
        
    print("="*50 + "\n")
    # ---------------------------------------------
    
    main()