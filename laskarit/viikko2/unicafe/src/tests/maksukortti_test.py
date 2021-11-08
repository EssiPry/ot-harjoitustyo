import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_alkusaldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(90)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")

    #tämä testi ei mene läpi
    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        self.maksukortti.lataa_rahaa(-10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_ota_rahaa_vahentaa_saldoa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(10), True)

    def test_ota_rahaa_ei_vie_saldoa_negatiiviseksi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(100), False)