#!/usr/bin/env python3
"""
Model untuk kelas abstract bangun datar.

Author: Fazlur Rahman
Date: 25/02/27
"""

from abc import ABC, abstractmethod


class BangunDatar(ABC):
    """
    Kelas abstrak yang merepresentasikan bangun datar.

    Attributes:
        nama (str): Nama bangun datar
    """

    def __init__(self, nama):
        """
        Inisialisasi bangun datar.

        Args:
            nama (str): Nama bangun datar
        """
        self._nama = nama

    def getNama(self):
        """
        Mendapatkan nama bangun datar.

        Returns:
            str: Nama bangun datar
        """
        return self._nama

    @abstractmethod
    def hitungLuas(self):
        """
        Menghitung luas bangun datar.

        Returns:
            float: Luas bangun datar
        """
        pass

    @abstractmethod
    def hitungKeliling(self):
        """
        Menghitung keliling bangun datar.

        Returns:
            float: Keliling bangun datar
        """
        pass

    def __str__(self):
        """
        Representasi string dari bangun datar.

        Returns:
            str: Informasi bangun datar
        """
        return f"Bangun Datar: {self.getNama()}\nLuas: {self.hitungLuas()}\nKeliling: {self.hitungKeliling()}"