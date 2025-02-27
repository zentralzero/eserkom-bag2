#!/usr/bin/env python3
"""
Model untuk bangun datar jajaran genjang.

Author: Fazlur Rahman
Date: 25/02/27
"""

from models.bangun_datar import BangunDatar


class JajaranGenjang(BangunDatar):
    """
    Kelas yang merepresentasikan bangun datar jajaran genjang.

    Attributes:
        alas (float): Panjang alas jajaran genjang
        tinggi (float): Tinggi jajaran genjang
        sisiMiring (float): Panjang sisi miring jajaran genjang
    """

    def __init__(self, alas, tinggi, sisiMiring):
        """
        Inisialisasi jajaran genjang.

        Args:
            alas (float): Panjang alas jajaran genjang
            tinggi (float): Tinggi jajaran genjang
            sisiMiring (float): Panjang sisi miring jajaran genjang
        """
        super().__init__("Jajaran Genjang")
        self.__alas = alas
        self.__tinggi = tinggi
        self.__sisiMiring = sisiMiring

    def getAlas(self):
        """
        Mendapatkan panjang alas jajaran genjang.

        Returns:
            float: Panjang alas jajaran genjang
        """
        return self.__alas

    def setAlas(self, alas):
        """
        Mengatur panjang alas jajaran genjang.

        Args:
            alas (float): Panjang alas jajaran genjang baru
        """
        self.__alas = alas

    def getTinggi(self):
        """
        Mendapatkan tinggi jajaran genjang.

        Returns:
            float: Tinggi jajaran genjang
        """
        return self.__tinggi

    def setTinggi(self, tinggi):
        """
        Mengatur tinggi jajaran genjang.

        Args:
            tinggi (float): Tinggi jajaran genjang baru
        """
        self.__tinggi = tinggi

    def getSisiMiring(self):
        """
        Mendapatkan panjang sisi miring jajaran genjang.

        Returns:
            float: Panjang sisi miring jajaran genjang
        """
        return self.__sisiMiring

    def setSisiMiring(self, sisiMiring):
        """
        Mengatur panjang sisi miring jajaran genjang.

        Args:
            sisiMiring (float): Panjang sisi miring jajaran genjang baru
        """
        self.__sisiMiring = sisiMiring

    def hitungLuas(self):
        """
        Menghitung luas jajaran genjang.

        Returns:
            float: Luas jajaran genjang
        """
        return self.__alas * self.__tinggi

    def hitungKeliling(self):
        """
        Menghitung keliling jajaran genjang.

        Returns:
            float: Keliling jajaran genjang
        """
        return 2 * (self.__alas + self.__sisiMiring)