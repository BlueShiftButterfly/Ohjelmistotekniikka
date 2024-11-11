import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(2000)
        self.maksukortti_vahan = Maksukortti(100)

    def test_kassapaate_luotu_oikein_rahat(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_kassapaate_luotu_oikein_edulliset_lounaat(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kassapaate_luotu_oikein_maukkaat_lounaat(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_edullinen_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)

    def test_kateisosto_edullinen_kassassa_raha_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)

    def test_kateisosto_edullisten_lounaiden_maara_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.kassapaate.syo_edullisesti_kateisella(400)
        self.assertEqual(self.kassapaate.edulliset, 3)

    def test_kateisosto_maukkaiden_lounaiden_maara_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(600)
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 3)

    def test_kateisosto_maukkaiden_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)

    def test_kateisosto_maukkaiden_kassassa_raha_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004)

    def test_kateisosto_edullinen_maksu_ei_riittava_raha_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(10)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_kateisosto_maukas_maksu_ei_riittava_raha_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(10)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_kateisosto_edullinen_maksu_ei_riittava_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(10)
        self.assertEqual(vaihtoraha, 10)

    def test_kateisosto_maukas_maksu_ei_riittava_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(10)
        self.assertEqual(vaihtoraha, 10)

    def test_kateisosto_edullinen_maara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(10)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_maukas_maara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(10)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_edullinen_veloitettu_summa_oikein(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo_euroina(), 17.6)

    def test_korttiosto_maukas_veloitettu_summa_oikein(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo_euroina(), 16)

    def test_korttiosto_edullinen_palauttaa_oikein(self):
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(tulos, True)

    def test_korttiosto_maukas_palauttaa_oikein(self):
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(tulos, True)

    def test_korttiosto_edullinen_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_maukas_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_edullinen_ei_tarpeeksi_rahaa(self):
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_vahan)
        self.assertEqual(tulos, False)
    
    def test_korttiosto_maukas_ei_tarpeeksi_rahaa(self):
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_vahan)
        self.assertEqual(tulos, False)
    
    def test_kortti_lataa_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.maksukortti.saldo_euroina(), 21)
    
    def test_kortti_lataa_rahaa_alle_nolla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.maksukortti.saldo_euroina(), 20)