import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(500)

    def test_luoto_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassa, None)

    def test_konstruktori_asettaa_saldon_ja_lounaat_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_syo_edullisesti_kateisella_asettaa_saldon_ja_lounaat_oikein(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(250), 10)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_syo_edullisesti_kateisella_liian_vahan_kateista(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_syo_maukkaasti_kateisella_asettaa_saldon_ja_lounaat_oikein(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_syo_maukkaasti_kateisella_liian_vahan_kateista(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(350), 350)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_syo_edullisesti_kortilla_asettaa_lounaat_oikein(self):
        self.assertTrue(self.kassa.syo_edullisesti_kortilla(self.kortti))
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kortti.saldo, 260)

    def test_syo_edullisesti_kortilla_liian_vahan_saldoa(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertFalse(self.kassa.syo_edullisesti_kortilla(self.kortti))
        self.assertEqual(self.kassa.edulliset, 2)
        self.assertEqual(self.kortti.saldo, 20)

    def test_syo_maukkaasti_kortilla_asettaa_lounaat_oikein(self):
        self.assertTrue(self.kassa.syo_maukkaasti_kortilla(self.kortti))
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(self.kortti.saldo, 100)

    def test_syo_maukkaasti_kortilla_liian_vahan_saldoa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertFalse(self.kassa.syo_maukkaasti_kortilla(self.kortti))
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(self.kortti.saldo, 100)

    def test_lataa_rahaa_kortille_lisaa_kassan_saldoa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100100)

    def test_lataa_rahaa_kortille_ei_hyvaksy_negatiivista_summaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)