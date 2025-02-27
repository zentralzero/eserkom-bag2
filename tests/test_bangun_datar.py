#!/usr/bin/env python3
"""
Unit test untuk kelas bangun datar.

Author: Fazlur Rahman
Date: 25/02/27
"""

import unittest
import math
from models.bangun_datar import BangunDatar
from models.persegi import Persegi
from models.persegi_panjang import PersegiPanjang
from models.jajaran_genjang import JajaranGenjang


class TestBangunDatar(unittest.TestCase):
    """Test kelas bangun datar."""

    def test_persegi(self):
        """Test kelas Persegi."""
        persegi = Persegi(5)

        # Test getter dan setter
        self.assertEqual(persegi.getSisi(), 5)
        persegi.setSisi(7)
        self.assertEqual(persegi.getSisi(), 7)

        # Test hitungLuas()
        self.assertEqual(persegi.hitungLuas(), 49)

        # Test hitungKeliling()
        self.assertEqual(persegi.hitungKeliling(), 28)

        # Test getNama()
        self.assertEqual(persegi.getNama(), "Persegi")

    def test_persegi_panjang(self):
        """Test kelas PersegiPanjang."""
        persegi_panjang = PersegiPanjang(4, 6)

        # Test getter dan setter
        self.assertEqual(persegi_panjang.getPanjang(), 4)
        self.assertEqual(persegi_panjang.getLebar(), 6)

        persegi_panjang.setPanjang(5)
        persegi_panjang.setLebar(8)
        self.assertEqual(persegi_panjang.getPanjang(), 5)
        self.assertEqual(persegi_panjang.getLebar(), 8)

        # Test hitungLuas()
        self.assertEqual(persegi_panjang.hitungLuas(), 40)

        # Test hitungKeliling()
        self.assertEqual(persegi_panjang.hitungKeliling(), 26)

        # Test getNama()
        self.assertEqual(persegi_panjang.getNama(), "Persegi Panjang")

    def test_jajaran_genjang(self):
        """Test kelas JajaranGenjang."""
        jajaran_genjang = JajaranGenjang(6, 4, 5)

        # Test getter dan setter
        self.assertEqual(jajaran_genjang.getAlas(), 6)
        self.assertEqual(jajaran_genjang.getTinggi(), 4)
        self.assertEqual(jajaran_genjang.getSisiMiring(), 5)

        jajaran_genjang.setAlas(8)
        jajaran_genjang.setTinggi(5)
        jajaran_genjang.setSisiMiring(6)
        self.assertEqual(jajaran_genjang.getAlas(), 8)
        self.assertEqual(jajaran_genjang.getTinggi(), 5)
        self.assertEqual(jajaran_genjang.getSisiMiring(), 6)

        # Test hitungLuas()
        self.assertEqual(jajaran_genjang.hitungLuas(), 40)

        # Test hitungKeliling()
        self.assertEqual(jajaran_genjang.hitungKeliling(), 28)

        # Test getNama()
        self.assertEqual(jajaran_genjang.getNama(), "Jajaran Genjang")


if __name__ == "__main__":
    unittest.main()