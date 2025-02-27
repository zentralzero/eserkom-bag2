#!/usr/bin/env python3
"""
Model untuk bangun datar persegi.

Author: Fazlur Rahman
Date: 25/02/27
"""

from models.bangun_datar import BangunDatar


class Persegi(BangunDatar):
    """
    Kelas yang merepresentasikan bangun datar persegi.

    Attributes:
        sisi (float): Panjang sisi persegi
    """

    def __init__(self, sisi):
        """
        Inisialisasi persegi.

        Args:
            sisi (float): Panjang sisi persegi
        """
        super().__init__("Persegi")
        self.__sisi = sisi

    def getSisi(self):
        """
        Mendapatkan panjang sisi persegi.

        Returns:
            float: Panjang sisi persegi
        """
        return self.__sisi

    def setSisi(self, sisi):
        """
        Mengatur panjang sisi persegi.

        Args:
            sisi (float): Panjang sisi persegi baru
        """
        self.__sisi = sisi

    def hitungLuas(self):
        """
        Menghitung luas persegi.

        Returns:
            float: Luas persegi
        """
        return self.__sisi ** 2

    def hitungKeliling(self):
        """
        Menghitung keliling persegi.

        Returns:
            float: Keliling persegi
        """
        return 4 * self.__sisi