import json
from concurrent.futures import ThreadPoolExecutor

class User:
    def __init__(self, username, name, followers_count, following_count, language, region, tweets, following, followers):
        self.username = username
        self.name = name
        self.followers_count = followers_count
        self.following_count = following_count
        self.language = language
        self.region = region
        self.tweets = tweets
        self.following = following
        self.followers = followers

def process_user_data(user):
    return User(user['username'], user['name'], user['followers_count'], user['following_count'],
                user['language'], user['region'], user['tweets'], user['following'], user['followers'])

# JSON dosyasını satır satır okuma (streaming)
users = []
with open('data.json', 'r', encoding='utf-8') as json_file:
    with ThreadPoolExecutor() as executor:
        # Veriyi paralel olarak işleme
        users = list(executor.map(process_user_data, (json.loads(line) for line in json_file)))

# Örnek olarak ilk kullanıcıyı ekrana yazdırma
sample_user = users[0]
print(f"Kullanıcı Adı: {sample_user.username}")
print(f"Ad-Soyad: {sample_user.name}")
print(f"Takipçi Sayısı: {sample_user.followers_count}")
print(f"Takip Edilen Sayısı: {sample_user.following_count}")
print(f"Dil: {sample_user.language}")
print(f"Bölge: {sample_user.region}")
print(f"Tweet Sayısı: {len(sample_user.tweets)}")
print(f"Takip Edilenler: {len(sample_user.following)} kişi")
print(f"Takipçiler: {len(sample_user.followers)} kişi")
