#!/usr/bin/env python3
"""Salin entry.png ke folder keluaran, byte demi byte.

Program ini memvalidasi gambar front page (PNG, maksimal 1024x1024
dan 1 MiB) lalu menyalinnya tanpa perubahan apa pun ke folder yang
ditentukan MAKEFUN_OUTPUT_DIR (atau ./out). Tidak ada jaringan,
tidak ada kompresi ulang, tidak ada piksel yang diubah.
"""

import hashlib
import os
import struct
import sys

NAMA_GAMBAR = "entry.png"
UKURAN_MAKS = 1_048_576
LEBAR_MAKS = 1024
TINGGI_MAKS = 1024
TANDA_PNG = b"\x89PNG\r\n\x1a\n"


def gagal(pesan):
    """Tulis kesalahan ke stderr, kembalikan kode keluar 1."""
    print("error: " + pesan, file=sys.stderr)
    return 1


def baca_dimensi(data):
    """Baca lebar dan tinggi dari chunk IHDR; None kalau tidak sah."""
    if len(data) < 8 + 4 + 4 + 13:
        return None
    panjang = struct.unpack(">I", data[8:12])[0]
    nama = data[12:16]
    if nama != b"IHDR" or panjang != 13:
        return None
    return struct.unpack(">II", data[16:24])


def utama():
    folder = os.path.dirname(os.path.abspath(__file__))
    sumber = os.path.join(folder, NAMA_GAMBAR)
    try:
        with open(sumber, "rb") as berkas:
            isi = berkas.read()
    except FileNotFoundError:
        return gagal("berkas %s tidak ditemukan" % NAMA_GAMBAR)
    except OSError as err:
        return gagal("tidak bisa membaca %s: %s" % (NAMA_GAMBAR, err))

    if len(isi) > UKURAN_MAKS:
        return gagal("ukuran %d byte melebihi batas %d" % (len(isi), UKURAN_MAKS))
    if not isi.startswith(TANDA_PNG):
        return gagal("%s bukan berkas PNG" % NAMA_GAMBAR)
    dimensi = baca_dimensi(isi)
    if dimensi is None:
        return gagal("%s tidak punya chunk IHDR yang sah" % NAMA_GAMBAR)
    lebar, tinggi = dimensi
    if lebar > LEBAR_MAKS or tinggi > TINGGI_MAKS:
        return gagal("dimensi %dx%d melebihi %dx%d" % (lebar, tinggi, LEBAR_MAKS, TINGGI_MAKS))

    tujuan_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    if not os.path.isabs(tujuan_dir):
        tujuan_dir = os.path.join(os.getcwd(), tujuan_dir)
    try:
        os.makedirs(tujuan_dir, exist_ok=True)
    except OSError as err:
        return gagal("tidak bisa membuat %s: %s" % (tujuan_dir, err))

    tujuan = os.path.join(tujuan_dir, NAMA_GAMBAR)
    try:
        with open(tujuan, "wb") as berkas:
            berkas.write(isi)
    except OSError as err:
        return gagal("tidak bisa menulis %s: %s" % (tujuan, err))

    print("OK: %s (%d byte, %dx%d, sha256 %s) -> %s"
          % (NAMA_GAMBAR, len(isi), lebar, tinggi,
             hashlib.sha256(isi).hexdigest()[:16], tujuan))
    return 0


if __name__ == "__main__":
    sys.exit(utama())
