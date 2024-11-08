import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_oikea_alussa(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_rahan_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(300)
        self.assertEqual(self.maksukortti.saldo_euroina(), 13)

    def test_saldo_vähenee_kun_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 5)

    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_ottaminen_palauttaa_oikein_kun_tarpeeksi_rahaa(self):
        tulos = self.maksukortti.ota_rahaa(100)
        self.assertEqual(tulos, True)

    def test_ottaminen_palauttaa_oikein_kun_ei_tarpeeksi_rahaa(self):
        tulos = self.maksukortti.ota_rahaa(2000)
        self.assertEqual(tulos, False)

    def test_maksukortti_tulostuu_tekstinä_oikein(self):
        teksti = str(self.maksukortti)
        self.assertEqual(teksti, "Kortilla on rahaa 10.00 euroa")