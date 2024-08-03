import json
import networkx as nx
import matplotlib.pyplot as plt

# JSON dosyasını oku
with open('/Users/ebrurazi/Desktop/prolab3/data.json', 'r') as dosya:
    veri = json.load(dosya)

# Boş bir graf oluştur
graf = nx.Graph()

# İlk 5 kullanıcı için düğümü ekle
for kullanici in veri[:100]:
    kullanici_adi = kullanici['username']
    graf.add_node(kullanici_adi)

    # Takip edilenleri ve takipçileri kenarlar olarak ekle
    for takip_edilen in kullanici['following']:
        graf.add_edge(kullanici_adi, takip_edilen)

    for takipci in kullanici['followers']:
        graf.add_edge(kullanici_adi, takipci)

# Minimum Spanning Tree (MST) algoritması ile ağı oluştur
mst_graf = nx.minimum_spanning_tree(graf)

# Düğümleri düzenli bir şekilde yerleştir
pos = nx.spring_layout(mst_graf, seed=42)

# MST çizimini oluştur
plt.figure(figsize=(10, 8))
nx.draw(mst_graf, pos, with_labels=True, font_weight='bold', edge_color='green', node_color='skyblue', font_color='black', node_size=800, font_size=8)

# Çizimi kaydet
plt.savefig("/Users/ebrurazi/Desktop/prolab3/mst_graf.png")

# Çizimi göster
plt.show()
