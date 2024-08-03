import json
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# JSON dosyasını oku
with open('/Users/ebrurazi/Desktop/prolab3/data.json', 'r') as dosya:
    veri = json.load(dosya)

# Boş bir graf oluştur
graf = nx.Graph()

# İlk 5 kullanıcı için düğümü ekle
for kullanici in veri[:5]:
    kullanici_adi = kullanici['username']
    graf.add_node(kullanici_adi)

    # Takip edilenleri ve takipçileri kenarlar olarak ekle
    for takip_edilen in kullanici['following']:
        graf.add_edge(kullanici_adi, takip_edilen)

    for takipci in kullanici['followers']:
        graf.add_edge(kullanici_adi, takipci)

# Kullanıcıların tweet içeriklerini al
tweet_icerikleri = [kullanici['tweets'] for kullanici in veri[:5]]

# TF-IDF vektörlerini oluştur
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([' '.join(tweets) for tweets in tweet_icerikleri])

# Cosine benzerlik matrisini oluştur
cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Benzerlik matrisini kullanarak eşleştirme yap
for i in range(len(cosine_similarities)):
    for j in range(i + 1, len(cosine_similarities[i])):
        benzerlik = cosine_similarities[i][j]
        if benzerlik > 0.5:  # Eşleştirme için belirli bir benzerlik eşiği seçilebilir
            print(f"{veri[i]['username']} ile {veri[j]['username']} benzer ilgi alanlarına sahip.")
            # Eşleşen kullanıcıları grafa eklemek için graf.add_edge() kullanılabilir.

# Düğümleri düzenli bir şekilde yerleştir
pos = nx.spring_layout(graf, seed=42)  # seed parametresi, yerleştirme işleminin tekrarlanabilir olmasını sağlar

# Grafi çizdir
nx.draw(graf, pos, with_labels=True, font_weight='bold', node_color='skyblue', font_color='black', node_size=800, font_size=8)

# Çizimi kaydet
plt.savefig("/Users/ebrurazi/Desktop/prolab3/graf_kucuk.png")

# Çizimi göster
plt.show()
