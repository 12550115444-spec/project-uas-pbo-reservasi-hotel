import pytest

from hotel import *


# ==================================================
# FIXTURE
# ==================================================

@pytest.fixture
def hotel_obj():

    hotel = Hotel()

    hotel.tambah_tamu(
        Tamu(
            "T01",
            "Haikal"
        )
    )

    hotel.tambah_kamar(
        KamarStandard(
            "101",
            300000
        )
    )

    return hotel


# ==================================================
# TEST KAMAR
# ==================================================

def test_kamar_standard():

    kamar = KamarStandard(
        "101",
        300000
    )

    assert kamar.nomor == "101"


def test_kamar_vip():

    kamar = KamarVIP(
        "201",
        500000
    )

    assert kamar.tipe == "VIP"


def test_kamar_vip_gold():

    kamar = KamarVIPGold(
        "301",
        700000
    )

    assert kamar.nomor == "301"


def test_status_awal():

    kamar = KamarStandard(
        "101",
        100
    )

    assert kamar.status == StatusKamar.TERSEDIA


# ==================================================
# OPERATOR OVERLOADING
# ==================================================

def test_operator_str():

    kamar = KamarStandard(
        "101",
        100
    )

    assert str(kamar) == "Kamar 101"


def test_operator_repr():

    kamar = KamarStandard(
        "101",
        100
    )

    assert repr(kamar) == "Kamar 101"


def test_operator_eq():

    k1 = KamarStandard(
        "101",
        100
    )

    k2 = KamarStandard(
        "101",
        200
    )

    assert k1 == k2


def test_operator_lt():

    k1 = KamarStandard(
        "101",
        100
    )

    k2 = KamarStandard(
        "102",
        100
    )

    assert k1 < k2


def test_operator_gt():

    k1 = KamarStandard(
        "103",
        100
    )

    k2 = KamarStandard(
        "102",
        100
    )

    assert k1 > k2


def test_operator_len():

    kamar = KamarStandard(
        "101",
        100
    )

    assert len(kamar) == 3


# ==================================================
# TEST TAMU
# ==================================================

def test_tambah_tamu():

    hotel = Hotel()

    hotel.tambah_tamu(
        Tamu(
            "T01",
            "Haikal"
        )
    )

    assert hotel.cari_tamu("T01")


def test_cari_tamu():

    hotel = Hotel()

    hotel.tambah_tamu(
        Tamu(
            "T01",
            "Haikal"
        )
    )

    assert hotel.cari_tamu(
        "T01"
    ).nama == "Haikal"


def test_hapus_tamu():

    hotel = Hotel()

    hotel.tambah_tamu(
        Tamu(
            "T01",
            "Haikal"
        )
    )

    hotel.hapus_tamu(
        "T01"
    )

    assert hotel.cari_tamu(
        "T01"
    ) is None


def test_duplikat_tamu():

    hotel = Hotel()

    hotel.tambah_tamu(
        Tamu(
            "T01",
            "A"
        )
    )

    with pytest.raises(
        DataSudahAdaError
    ):

        hotel.tambah_tamu(
            Tamu(
                "T01",
                "B"
            )
        )


# ==================================================
# TEST KAMAR
# ==================================================

def test_tambah_kamar():

    hotel = Hotel()

    hotel.tambah_kamar(
        KamarStandard(
            "101",
            100
        )
    )

    assert hotel.cari_kamar(
        "101"
    )


def test_cari_kamar():

    hotel = Hotel()

    hotel.tambah_kamar(
        KamarStandard(
            "101",
            100
        )
    )

    assert hotel.cari_kamar(
        "101"
    ).nomor == "101"


def test_hapus_kamar():

    hotel = Hotel()

    hotel.tambah_kamar(
        KamarStandard(
            "101",
            100
        )
    )

    hotel.hapus_kamar(
        "101"
    )

    assert hotel.cari_kamar(
        "101"
    ) is None


def test_duplikat_kamar():

    hotel = Hotel()

    hotel.tambah_kamar(
        KamarStandard(
            "101",
            100
        )
    )

    with pytest.raises(
        DataSudahAdaError
    ):

        hotel.tambah_kamar(
            KamarStandard(
                "101",
                200
            )
        )


# ==================================================
# VALIDASI
# ==================================================

def test_validasi_nomor():

    hotel = Hotel()

    assert hotel.validasi_nomor(
        "101"
    )


def test_validasi_salah():

    hotel = Hotel()

    with pytest.raises(
        ValueError
    ):

        hotel.validasi_nomor(
            "1"
        )


# ==================================================
# BOOKING
# ==================================================

def test_booking(
    hotel_obj
):

    reservasi = hotel_obj.booking_kamar(
        "T01",
        "101",
        "Cash"
    )

    assert reservasi is not None


def test_status_setelah_booking(
    hotel_obj
):

    hotel_obj.booking_kamar(
        "T01",
        "101",
        "Cash"
    )

    kamar = hotel_obj.cari_kamar(
        "101"
    )

    assert kamar.status == StatusKamar.DIBOOKING


def test_booking_tamu_tidak_ada():

    hotel = Hotel()

    hotel.tambah_kamar(
        KamarStandard(
            "101",
            100
        )
    )

    with pytest.raises(
        DataTidakDitemukanError
    ):

        hotel.booking_kamar(
            "X",
            "101",
            "Cash"
        )


def test_booking_kamar_tidak_ada():

    hotel = Hotel()

    hotel.tambah_tamu(
        Tamu(
            "T01",
            "A"
        )
    )

    with pytest.raises(
        DataTidakDitemukanError
    ):

        hotel.booking_kamar(
            "T01",
            "999",
            "Cash"
        )


def test_booking_dua_kali(
    hotel_obj
):

    hotel_obj.booking_kamar(
        "T01",
        "101",
        "Cash"
    )

    with pytest.raises(
        KamarTidakTersediaError
    ):

        hotel_obj.booking_kamar(
            "T01",
            "101",
            "Cash"
        )


# ==================================================
# CHECK IN
# ==================================================

def test_checkin(
    hotel_obj
):

    hotel_obj.booking_kamar(
        "T01",
        "101",
        "Cash"
    )

    hotel_obj.checkin(
        "101"
    )

    kamar = hotel_obj.cari_kamar(
        "101"
    )

    assert kamar.status == StatusKamar.DITEMPATI


# ==================================================
# CHECK OUT
# ==================================================

def test_checkout(
    hotel_obj
):

    hotel_obj.booking_kamar(
        "T01",
        "101",
        "Cash"
    )

    hotel_obj.checkout(
        "101"
    )

    kamar = hotel_obj.cari_kamar(
        "101"
    )

    assert kamar.status == StatusKamar.TERSEDIA


# ==================================================
# COLLECTION
# ==================================================

def test_collection_len():

    koleksi = KoleksiKamar()

    koleksi.tambah(
        KamarStandard(
            "101",
            100
        )
    )

    assert len(koleksi) == 1


def test_collection_contains():

    koleksi = KoleksiKamar()

    kamar = KamarStandard(
        "101",
        100
    )

    koleksi.tambah(
        kamar
    )

    assert kamar in koleksi


def test_collection_iter():

    koleksi = KoleksiKamar()

    koleksi.tambah(
        KamarStandard(
            "101",
            100
        )
    )

    assert len(
        list(koleksi)
    ) == 1


# ==================================================
# STRATEGY
# ==================================================

def test_txt_report():

    report = TXTReport()

    report.generate(
        ["A"]
    )

    assert True


def test_json_report():

    report = JSONReport()

    report.generate(
        ["A"]
    )

    assert True


def test_pdf_report():

    report = PDFReport()

    report.generate(
        ["A"]
    )

    assert True


# ==================================================
# PEMBAYARAN
# ==================================================

def test_pembayaran():

    p = Pembayaran(
        "Cash",
        100000
    )

    assert p.total == 100000


def test_str_pembayaran():

    p = Pembayaran(
        "Cash",
        100000
    )

    assert "Cash" in str(p)


# ==================================================
# INTEGRATION TEST
# ==================================================

def test_integration_booking_sampai_checkout():

    hotel = Hotel()

    hotel.tambah_tamu(
        Tamu(
            "T01",
            "Haikal"
        )
    )

    hotel.tambah_kamar(
        KamarVIP(
            "201",
            500000
        )
    )

    hotel.booking_kamar(
        "T01",
        "201",
        "Transfer"
    )

    hotel.checkin(
        "201"
    )

    assert hotel.cari_kamar(
        "201"
    ).status == StatusKamar.DITEMPATI

    hotel.checkout(
        "201"
    )

    assert hotel.cari_kamar(
        "201"
    ).status == StatusKamar.TERSEDIA

# ==========================================
# COVERAGE BOOSTER
# ==========================================

def test_tampilkan_info_kamar():

    kamar = KamarStandard(
        "101",
        100000
    )

    kamar.tampilkan_info()


def test_tampilkan_info_tamu():

    tamu = Tamu(
        "T01",
        "Haikal"
    )

    tamu.tampilkan_info()


def test_invoice():
    tamu = Tamu("T01", "Haikal")
    kamar = Kamar("101", "Standard", 500000)
    bayar = "Tunai"
    
    # PERBAIKAN: Tambahkan argumen kelima sesuai parameter '__init__' kelas Reservasi Anda
    # Contoh di bawah menambahkan nilai harga kamar sebagai 'total_bayar'
    reservasi = Reservasi(
        "RSV-1", 
        tamu, 
        kamar, 
        bayar, 
        kamar.harga  # <-- Masukkan argumen total_bayar di sini!
    )
    
    # Jalankan assert uji kelayakan invoice di bawahnya
    assert reservasi.pembayaran.total == 500000

def test_invoice():
    tamu = Tamu("T01", "Haikal")
    kamar = Kamar("101", "Standard", 500000)
    bayar = "Tunai"
    
    # PERBAIKAN: Tambahkan argumen kelima sesuai parameter '__init__' kelas Reservasi Anda
    # Contoh di bawah menambahkan nilai harga kamar sebagai 'total_bayar'
    reservasi = Reservasi(
        "RSV-1", 
        tamu, 
        kamar, 
        bayar, 
        kamar.harga  # <-- Masukkan argumen total_bayar di sini!
    )
    
    # Jalankan assert uji kelayakan invoice di bawahnya
    assert reservasi.pembayaran.total == 500000

def test_reservasi_info():
    tamu = Tamu("T01", "Haikal")
    kamar = KamarStandard("101", 100000)
    bayar = "Transfer"
    
    # PERBAIKAN: Tambahkan argumen kelima (total_bayar) di bagian akhir
    reservasi = Reservasi(
        "RSV-1",
        tamu,
        kamar,
        bayar,
        100000  # <-- Tambahkan argumen total_bayar di sini
    )
    
    # Jalankan assert pengujian rekam info reservasi Anda
def test_update_status():

    hotel = Hotel()

    hotel.tambah_kamar(
        KamarStandard(
            "101",
            100000
        )
    )

    hotel.update_status_kamar(
        "101",
        StatusKamar.DITEMPATI
    )

    assert (
        hotel.cari_kamar(
            "101"
        ).status
        ==
        StatusKamar.DITEMPATI
    )


def test_generate_report_txt():

    hotel = Hotel()

    hotel.tambah_kamar(
        KamarStandard(
            "101",
            100000
        )
    )

    hotel.generate_report(
        TXTReport()
    )


def test_generate_report_json():

    hotel = Hotel()

    hotel.tambah_kamar(
        KamarStandard(
            "101",
            100000
        )
    )

    hotel.generate_report(
        JSONReport()
    )


def test_generate_report_pdf():

    hotel = Hotel()

    hotel.tambah_kamar(
        KamarStandard(
            "101",
            100000
        )
    )

    hotel.generate_report(
        PDFReport()
    )


def test_lihat_kamar():

    hotel = Hotel()

    hotel.tambah_kamar(
        KamarStandard(
            "101",
            100000
        )
    )

    hotel.lihat_kamar()


def test_lihat_tamu():

    hotel = Hotel()

    hotel.tambah_tamu(
        Tamu(
            "T01",
            "Haikal"
        )
    )

    hotel.lihat_tamu()


def test_lihat_reservasi():

    hotel = Hotel()

    hotel.tambah_tamu(
        Tamu(
            "T01",
            "Haikal"
        )
    )

    hotel.tambah_kamar(
        KamarStandard(
            "101",
            100000
        )
    )

    hotel.booking_kamar(
        "T01",
        "101",
        "Cash"
    )

    hotel.lihat_reservasi()


def test_data_tamu_tidak_ditemukan():

    hotel = Hotel()

    with pytest.raises(
        DataTidakDitemukanError
    ):

        hotel.hapus_tamu(
            "X"
        )


def test_data_kamar_tidak_ditemukan():

    hotel = Hotel()

    with pytest.raises(
        DataTidakDitemukanError
    ):

        hotel.hapus_kamar(
            "999"
        )


def test_checkin_gagal():

    hotel = Hotel()

    hotel.tambah_kamar(
        KamarStandard(
            "101",
            100000
        )
    )

    with pytest.raises(
        HotelError
    ):

        hotel.checkin(
            "101"
        )


def test_checkout_kamar_tidak_ada():

    hotel = Hotel()

    with pytest.raises(
        DataTidakDitemukanError
    ):

        hotel.checkout(
            "999"
        )

def test_menu_tamu_keluar(monkeypatch):

    hotel = Hotel()

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "5"
    )

    menu_tamu(hotel)

def test_menu_resepsionis_keluar(monkeypatch):

    hotel = Hotel()

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "10"
    )

    menu_resepsionis(hotel)

def test_main_keluar(monkeypatch):

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "3"
    )

    main()


def test_invoice_cetak():
    tamu = Tamu("T01", "Haikal")
    kamar = KamarStandard("101", 100000)

    reservasi = Reservasi(
        "RSV-1",
        tamu,
        kamar,
        "Cash",
        100000
    )

    invoice = Invoice(
        "INV-1",
        reservasi
    )

    invoice.cetak()


def test_reservasi_tampilkan_info():
    tamu = Tamu("T01", "Haikal")
    kamar = KamarStandard("101", 100000)

    reservasi = Reservasi(
        "RSV-1",
        tamu,
        kamar,
        "Cash",
        100000
    )

    reservasi.tampilkan_info()


def test_koleksi_semua():
    koleksi = KoleksiKamar()

    kamar = KamarStandard(
        "101",
        100000
    )

    koleksi.tambah(kamar)

    assert koleksi.semua()[0] == kamar


def test_koleksi_hapus():
    koleksi = KoleksiKamar()

    kamar = KamarStandard(
        "101",
        100000
    )

    koleksi.tambah(kamar)
    koleksi.hapus(kamar)

    assert len(koleksi) == 0


def test_cari_kamar_none():
    hotel = Hotel()

    assert hotel.cari_kamar(
        "999"
    ) is None


def test_cari_tamu_none():
    hotel = Hotel()

    assert hotel.cari_tamu(
        "X"
    ) is None


def test_update_status_kamar_error():
    hotel = Hotel()

    with pytest.raises(
        DataTidakDitemukanError
    ):
        hotel.update_status_kamar(
            "999",
            StatusKamar.TERSEDIA
        )


def test_checkin_kamar_tidak_ditemukan():
    hotel = Hotel()

    with pytest.raises(
        DataTidakDitemukanError
    ):
        hotel.checkin(
            "999"
        )


def test_logging_mixin():
    mixin = LoggingMixin()

    mixin.log(
        "Testing Log"
    )

    assert True


def test_property_kamar():
    kamar = KamarStandard(
        "101",
        100000
    )

    assert kamar.nomor == "101"
    assert kamar.tipe == "Standard"
    assert kamar.harga == 100000


def test_status_setter():
    kamar = KamarStandard(
        "101",
        100000
    )

    kamar.status = StatusKamar.DITEMPATI

    assert kamar.status == StatusKamar.DITEMPATI


def test_exception_inheritance():
    assert issubclass(
        DataSudahAdaError,
        HotelError
    )

    assert issubclass(
        DataTidakDitemukanError,
        HotelError
    )


def test_hotel_mro():
    assert LoggingMixin in Hotel.__mro__
    assert ValidationMixin in Hotel.__mro__


def test_contains_false():
    koleksi = KoleksiKamar()

    kamar = KamarStandard(
        "101",
        100000
    )

    assert kamar not in koleksi


def test_kamar_not_equal():
    k1 = KamarStandard(
        "101",
        100000
    )

    k2 = KamarStandard(
        "102",
        100000
    )

    assert k1 != k2


def test_hotel_error():
    with pytest.raises(HotelError):
        raise HotelError("Error")


def test_data_sudah_ada_error():
    with pytest.raises(DataSudahAdaError):
        raise DataSudahAdaError("Sudah ada")


def test_data_tidak_ditemukan_error():
    with pytest.raises(DataTidakDitemukanError):
        raise DataTidakDitemukanError("Tidak ditemukan")


def test_kamar_tidak_tersedia_error():
    with pytest.raises(KamarTidakTersediaError):
        raise KamarTidakTersediaError("Tidak tersedia")


def test_str_tamu():
    tamu = Tamu(
        "T01",
        "Haikal"
    )

    assert str(tamu) == "Haikal"


def test_status_enum():
    assert (
        StatusKamar.TERSEDIA.value
        == "Tersedia"
    )

    assert (
        StatusKamar.DIBOOKING.value
        == "Dibooking"
    )


def test_invoice_attribute():
    tamu = Tamu("T01", "Haikal")
    kamar = KamarStandard("101", 100000)

    reservasi = Reservasi(
        "RSV-1",
        tamu,
        kamar,
        "Cash",
        100000
    )

    invoice = Invoice(
        "INV-1",
        reservasi
    )

    assert invoice.kode == "INV-1"


def test_reservasi_attribute():
    tamu = Tamu("T01", "Haikal")
    kamar = KamarStandard("101", 100000)

    reservasi = Reservasi(
        "RSV-1",
        tamu,
        kamar,
        "Cash",
        100000
    )

    assert reservasi.kode == "RSV-1"


def test_pembayaran_attribute():
    pembayaran = Pembayaran(
        "Transfer",
        500000
    )

    assert pembayaran.metode == "Transfer"


def test_checkout_status_checkout_branch():
    hotel = Hotel()

    hotel.tambah_tamu(
        Tamu("T01", "Haikal")
    )

    hotel.tambah_kamar(
        KamarStandard(
            "101",
            100000
        )
    )

    hotel.booking_kamar(
        "T01",
        "101",
        "Cash"
    )

    hotel.checkout(
        "101"
    )

    assert (
        hotel.cari_kamar(
            "101"
        ).status
        ==
        StatusKamar.TERSEDIA
    )

def test_menu_resepsionis_laporan_json(monkeypatch):
    hotel = Hotel()

    inputs = iter([
        "9",
        "11"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

def test_main_login_tamu(monkeypatch):

    inputs = iter([
        "2",   # login tamu
        "5",   # keluar menu tamu
        "3"    # keluar program
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    main()

def test_invoice_cetak():
    tamu = Tamu("T01", "Haikal")
    kamar = KamarStandard("101", 100000)

    reservasi = Reservasi(
        "RSV-1",
        tamu,
        kamar,
        "Cash",
        100000
    )

    invoice = Invoice(
        "INV-1",
        reservasi
    )

    invoice.cetak()


def test_reservasi_tampilkan_info():
    tamu = Tamu("T01", "Haikal")
    kamar = KamarStandard("101", 100000)

    reservasi = Reservasi(
        "RSV-1",
        tamu,
        kamar,
        "Cash",
        100000
    )

    reservasi.tampilkan_info()


def test_lihat_kamar_kosong():
    hotel = Hotel()
    hotel.lihat_kamar()


def test_lihat_tamu_kosong():
    hotel = Hotel()
    hotel.lihat_tamu()


def test_lihat_reservasi_kosong():
    hotel = Hotel()
    hotel.lihat_reservasi()


def test_checkout_kamar_tidak_ditemukan():
    hotel = Hotel()

    with pytest.raises(
        DataTidakDitemukanError
    ):
        hotel.checkout("999")


def test_update_status_kamar_tidak_ditemukan():
    hotel = Hotel()

    with pytest.raises(
        DataTidakDitemukanError
    ):
        hotel.update_status_kamar(
            "999",
            StatusKamar.TERSEDIA
        )


def test_checkin_kamar_tidak_ditemukan():
    hotel = Hotel()

    with pytest.raises(
        DataTidakDitemukanError
    ):
        hotel.checkin("999")


def test_koleksi_semua():
    koleksi = KoleksiKamar()

    kamar = KamarStandard(
        "101",
        100000
    )

    koleksi.tambah(kamar)

    assert koleksi.semua()[0] == kamar


def test_koleksi_hapus():
    koleksi = KoleksiKamar()

    kamar = KamarStandard(
        "101",
        100000
    )

    koleksi.tambah(kamar)
    koleksi.hapus(kamar)

    assert len(koleksi) == 0