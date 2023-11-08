# spider_olx
## Web crawler untuk situs web OLX dengan framework Scrapy

## Tentang
Repository ini berisi kode untuk crawler web yang dapat digunakan untuk mengumpulkan data dari situs web OLX. Crawler ini menggunakan framework Scrapy untuk mengekstrak informasi dari halaman web OLX.

## Fitur

Dapat digunakan untuk mengumpulkan data dari kategori motor pada satu halaman
data yang dikumpulkan adalah 
- harga
- KM
- Tahun
- Brand 

## Penggunaan
Instal Python 3.6 atau lebih tinggi.
Instal Scrapy dengan perintah berikut:

```bash
pip install scrapy
```
Clone atau unduh repository ini.

setelah itu dapat melakuka crawling dengan perintah berikut:
```bash
scrapy crawl olx_motor -o output.json  
```
hasil crawling akan disimpan dalam file json bernama output
