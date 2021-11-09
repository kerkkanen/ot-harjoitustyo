import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)
                
        

    def test_kateisosto_edulliset_palauttaa_oikein(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(480), 240)
    
    def test_kateisosto_edulliset_kasvattaa_kassaa(self):
        self.kassa.syo_edullisesti_kateisella(480)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        
    def test_kateisosto_maukkaat_palauttaa_oikein(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(480), 80)
    
    def test_kateisosto_maukkaat_kasvattaa_kassaa(self):
        self.kassa.syo_maukkaasti_kateisella(480)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)

    def test_ostetut_kasvattavat_maaraa(self):
        self.kassa.syo_edullisesti_kateisella(300)
        self.kassa.syo_edullisesti_kateisella(400)
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.edulliset, 2)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_ei_riittavasti_rahaa_ostaa_edullista(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_ei_riittavasti_rahaa_ostaa_maukasta(self):
        self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(300), 300)
        self.assertEqual(self.kassa.maukkaat, 0)

    #Korttitestit kassan kanssa

    def test_edullinen_veloittaa_kun_rahaa_tarpeeksi(self):        
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), True)
        self.assertEqual(str(self.kortti), "saldo: 5.2")

    def test_maukas_veloittaa_kun_rahaa_tarpeeksi(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), True)
        self.assertEqual(str(self.kortti), "saldo: 3.6")

    def test_lounaiden_maara_kasvaa_kun_rahaa_tarpeeksi(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 2)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_maarat_ei_muutu_kun_ei_rahaa_ja_palautetaan_false(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), False)
        self.assertEqual(str(self.kortti), "saldo: 0.4")
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    
    def test_saldo_muuttuu_ladattaessa_ja_kassa_kasvaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 400)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        self.assertEqual(str(self.kortti), "saldo: 14.0")

    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -400)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(str(self.kortti), "saldo: 10.0")
        

    
