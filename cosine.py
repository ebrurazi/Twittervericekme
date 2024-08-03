import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# JSON dosyasını oku
with open('/Users/ebrurazi/Desktop/prolab3/data.json', 'r') as dosya:
    veri = json.load(dosya)

# Kullanıcıların ilgi alanlarını temsil etmek için hash tablolarını kullan
ilgi_alanlari_hash_tablosu = {}
for kullanici in veri:
    kullanici_adi = kullanici['username']
    ilgi_alanlari = set(kullanici['tweets'])  # Her kullanıcının ilgi alanları bir küme olarak alınıyor
    ilgi_alanlari_hash_tablosu[kullanici_adi] = ilgi_alanlari

# TF-IDF vektörlerini oluştur
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([' '.join(tweets) for tweets in ilgi_alanlari_hash_tablosu.values()])

# Cosine benzerlik matrisini oluştur
cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Belirli bir benzerlik eşiği
benzerlik_esigi = 0.5

# Benzerlik matrisini kullanarak eşleştirme yap
for i in range(len(cosine_similarities)):
    for j in range(i + 1, len(cosine_similarities[i])):
        benzerlik = cosine_similarities[i][j]
        if benzerlik > benzerlik_esigi:
            kullanici1 = list(ilgi_alanlari_hash_tablosu.keys())[i]
            kullanici2 = list(ilgi_alanlari_hash_tablosu.keys())[j]
            print(f"{kullanici1} ile {kullanici2} benzer ilgi alanlarına sahip. Benzerlik Skoru: {benzerlik}")

# Belirli bir benzerlik eşiğine göre listeleyen bir rapor oluştur
rapor = []
for i in range(len(cosine_similarities)):
    for j in range(i + 1, len(cosine_similarities[i])):
        benzerlik = cosine_similarities[i][j]
        if benzerlik > benzerlik_esigi:
            kullanici1 = list(ilgi_alanlari_hash_tablosu.keys())[i]
            kullanici2 = list(ilgi_alanlari_hash_tablosu.keys())[j]
            rapor.append(f"{kullanici1} ile {kullanici2} benzer ilgi alanlarına sahip. Benzerlik Skoru: {benzerlik}")

# Raporu dosyaya yaz
with open("/Users/ebrurazi/Desktop/prolab3/benzerlik_raporu.txt", "w") as rapor_dosyasi:
    for satir in rapor:
        rapor_dosyasi.write(satir + "\n")
