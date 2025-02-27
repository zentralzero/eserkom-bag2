#!/usr/bin/env python3
"""
Program utama untuk Bagian 2: Perhitungan bangun datar.

Author: Fazlur Rahman
Date: 25/02/27
"""

import os

from models import Persegi, JajaranGenjang, PersegiPanjang


def display_menu():
    """
    Menampilkan menu pilihan bangun datar.

    Returns:
        int: Pilihan pengguna
    """
    print("\n===== Program Bangun Datar =====")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Jajaran Genjang")
    print("0. Keluar")

    try:
        choice = int(input("Masukkan pilihan (0-3): "))
        return choice
    except ValueError:
        print("Masukkan angka yang valid!")
        return -1


def get_persegi_input():
    """
    Mendapatkan input untuk persegi.

    Returns:
        tuple: (Persegi, dimensi) atau (None, None) jika input tidak valid
    """
    try:
        sisi = float(input("Masukkan panjang sisi: "))
        persegi = Persegi(sisi)
        dimensi = f"Sisi: {sisi}"
        return persegi, dimensi
    except ValueError:
        print("Input tidak valid! Masukkan angka.")
        return None, None


def get_persegi_panjang_input():
    """
    Mendapatkan input untuk persegi panjang.

    Returns:
        tuple: (PersegiPanjang, dimensi) atau (None, None) jika input tidak valid
    """
    try:
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        persegi_panjang = PersegiPanjang(panjang, lebar)
        dimensi = f"Panjang: {panjang}, Lebar: {lebar}"
        return persegi_panjang, dimensi
    except ValueError:
        print("Input tidak valid! Masukkan angka.")
        return None, None


def get_jajaran_genjang_input():
    """
    Mendapatkan input untuk jajaran genjang.

    Returns:
        tuple: (JajaranGenjang, dimensi) atau (None, None) jika input tidak valid
    """
    try:
        alas = float(input("Masukkan panjang alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        sisi_miring = float(input("Masukkan panjang sisi miring: "))
        jajaran_genjang = JajaranGenjang(alas, tinggi, sisi_miring)
        dimensi = f"Alas: {alas}, Tinggi: {tinggi}, Sisi Miring: {sisi_miring}"
        return jajaran_genjang, dimensi
    except ValueError:
        print("Input tidak valid! Masukkan angka.")
        return None, None


def main():
    """Fungsi utama program."""

    # Loop menu utama
    while True:
        choice = display_menu()

        if choice == 0:
            break
        elif choice == 1:
            bangun_datar, dimensi = get_persegi_input()
        elif choice == 2:
            bangun_datar, dimensi = get_persegi_panjang_input()
        elif choice == 3:
            bangun_datar, dimensi = get_jajaran_genjang_input()
        else:
            print("Pilihan tidak valid!")
            continue

        # Jika input valid
        if bangun_datar:
            # Tampilkan hasil perhitungan
            print("\n" + str(bangun_datar))

    print("Program selesai.")


if __name__ == "__main__":
    main()