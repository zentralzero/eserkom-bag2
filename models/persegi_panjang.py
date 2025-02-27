#!/usr/bin/env python3
"""
Model untuk bangun datar persegi panjang.

Author: Fazlur Rahman
Date: 25/02/27
"""

from models.bangun_datar import BangunDatar


class PersegiPanjang(BangunDatar):
    """
    Kelas yang merepresentasikan bangun datar persegi panjang.

    Attributes:
        panjang (float): Panjang persegi panjang
        lebar (float): Lebar persegi panjang
    """

    def __init__(self, panjang, lebar):
        """
        Inisialisasi persegi panjang.

        Args:
            panjang (float): Panjang persegi panjang
            lebar (float): Lebar persegi panjang
        """
        super().__init__("Persegi Panjang")
        self.__panjang = panjang
        self.__lebar = lebar

    def getPanjang(self):
        """
        Mendapatkan panjang persegi panjang.

        Returns:
            float: Panjang persegi panjang
        """
        return self.__panjang

    def setPanjang(self, panjang):
        """
        Mengatur panjang persegi panjang.

        Args:
            panjang (float): Panjang persegi panjang baru
        """
        self.__panjang = panjang

    def getLebar(self):
        """
        Mendapatkan lebar persegi panjang.

        Returns:
            float: Lebar persegi panjang
        """
        return self.__lebar

    def setLebar(self, lebar):
        """
        Mengatur lebar persegi panjang.

        Args:
            lebar (float): Lebar persegi panjang baru
        """
        self.__lebar = lebar

    def hitungLuas(self):
        """
        Menghitung luas persegi panjang.

        Returns:
            float: Luas persegi panjang
        """
        return self.__panjang * self.__lebar

    def hitungKeliling(self):
        """
        Menghitung keliling persegi panjang.

        Returns:
            float: Keliling persegi panjang
        """
        return 2 * (self.__panjang + self.__lebar)