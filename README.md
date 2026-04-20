# Bitcoin Address Creation Demo (Python, No Library)

> Mencakup Legacy, SegWit, dan Taproot secara bertahap.

## ⚠️ PERINGATAN KERAS

**JANGAN PERNAH mengirim Bitcoin ke address yang dibuat dari proyek ini.**

Repository / contoh ini **hanya untuk tujuan edukasi**, untuk memahami bagaimana proses pembuatan berbagai format address Bitcoin bekerja secara manual menggunakan Python.


**Jika Anda mengirim Bitcoin ke address hasil eksperimen ini, Anda berisiko kehilangan dana permanen.**

Gunakan wallet resmi dan terpercaya untuk transaksi nyata.

---

## Tujuan Proyek

Mendemonstrasikan secara transparan proses berikut menggunakan **Python murni tanpa library eksternal**:

1. Legacy / P2PKH (Base58Check)
2. SegWit (Bech32)
3. Taproot (Bech32m)
4. Hashing dan checksum dasar
5. Encoding address Bitcoin dengan Python

---

## Contoh Data (Legacy Demo)

```text
HASH160:
4f6e669e65be170eae07d9a7d81e181a9886fec3
```

Version byte mainnet P2PKH:

```text
00
```

Contoh checksum (demo):

```text
9ba94fc0
```

Final hex sebelum Base58:

```text
004f6e669e65be170eae07d9a7d81e181a9886fec39ba94fc0
```

---

## Python Code (Base58Check Encode)

```python
data_hex = "004f6e669e65be170eae07d9a7d81e181a9886fec39ba94fc0"

alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

num = int(data_hex, 16)
encoded = ""

while num > 0:
    num, rem = divmod(num, 58)
    encoded = alphabet[rem] + encoded

leading_zero_bytes = 0
for i in range(0, len(data_hex), 2):
    if data_hex[i:i+2] == "00":
        leading_zero_bytes += 1
    else:
        break

encoded = ("1" * leading_zero_bytes) + encoded

print(encoded)
```

---

## Cara Kerja Singkat

### 1. Version Byte

`00` menandakan alamat Bitcoin legacy mainnet (P2PKH).

### 2. Checksum

Checksum normalnya dihitung dengan:

```text
SHA256(SHA256(version + hash160))
```

Lalu ambil 4 byte pertama.

### 3. Base58

Data final diubah ke alfabet Base58:

```text
123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz
```

Karakter ambigu seperti `0`, `O`, `I`, dan `l` dihapus.

---

## Catatan Penting

Format address Bitcoin modern meliputi:

* Legacy / P2PKH (`1...`)
* Native SegWit Bech32 (`bc1q...`)
* Taproot Bech32m (`bc1p...`)

README ini akan berkembang untuk mencakup semuanya, dimulai dari contoh Legacy agar fondasi encoding mudah

---

## Disclaimer Final

**Ini adalah simulasi pendidikan. Jangan gunakan hasilnya untuk menyimpan dana. Jangan kirim Bitcoin ke address contoh ini.**

