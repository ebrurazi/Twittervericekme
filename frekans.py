import json
from collections import Counter

# JSON dosyasını oku
with open('/Users/ebrurazi/Desktop/prolab3/data.json', 'r') as dosya:
    veri = json.load(dosya)

# Boş bir Counter nesnesi oluştur
ilgi_alanlari_frekans = Counter()

# Kullanıcıların tweet içeriklerindeki anlamlı kelimeleri topla
for kullanici in veri:
    for tweet in kullanici['tweets']:
        ilgi_alanlari_frekans.update(tweet.split())  # Her tweet içeriğini kelimelere ayır

# Frekans tablosunu yazdır
print("İlgi Alanları Frekans Tablosu:")
print(ilgi_alanlari_frekans)
