import json

class HashTabloUser:
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

    def display_info(self):
        print(f"Username: {self.username}")
        print(f"Name: {self.name}")
        print(f"Followers Count: {self.followers_count}")
        print(f"Following Count: {self.following_count}")
        print(f"Language: {self.language}")
        print(f"Region: {self.region}")
        print(f"Tweets: {self.tweets}")
        print(f"Following: {self.following}")
        print(f"Followers: {self.followers}")
        print("\n")

class CustomHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def custom_hash_function(self, key):
        # Öğrenci tarafından yazılan özgün bir hash fonksiyonu
        # Bu örnek hash fonksiyonu sadece kullanıcı adının ASCII değerlerini toplamını kullanmaktadır
        return sum(ord(char) for char in key) % self.size

    def insert_user(self, user):
        # Kullanıcı nesnesini tabloya eklemek için özgün bir algoritma
        hash_key = self.custom_hash_function(user.username)
        
        # Eğer hash tablosunda boş bir yer bulana kadar çakışma çözümleme
        while self.table[hash_key] is not None:
            hash_key = (hash_key + 1) % self.size

        self.table[hash_key] = user

    def get_user(self, username):
        # Kullanıcı adına göre kullanıcı nesnesini bulmak için özgün bir algoritma
        hash_key = self.custom_hash_function(username)

        # Eğer kullanıcı adı bulunana kadar çakışma çözümleme
        while self.table[hash_key] is not None and self.table[hash_key].username != username:
            hash_key = (hash_key + 1) % self.size

        if self.table[hash_key] is not None:
            return self.table[hash_key]
        else:
            return None

    def display_table(self):
        # Tablodaki tüm kullanıcıları ekrana yazdırmak için özgün bir algoritma
        for user in self.table:
            if user is not None:
                user.display_info()

def main():
    # data.json dosyasını oku
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    # Hash tablosu oluştur
    hash_table = CustomHashTable(size=100)

    # Kullanıcı nesnelerini oluştur ve hash tablosuna ekle
    for user_data in data:
        username = user_data["username"]
        name = user_data["name"]
        followers_count = user_data["followers_count"]
        following_count = user_data["following_count"]
        language = user_data["language"]
        region = user_data["region"]
        tweets = user_data["tweets"]
        following = user_data["following"]
        followers = user_data["followers"]

        user = HashTabloUser(username, name, followers_count, following_count, language, region, tweets, following, followers)
        hash_table.insert_user(user)

    # Örnek olarak bir kullanıcının bilgilerini ekrana yazdır
    sample_user = hash_table.get_user("ymohr")
    if sample_user:
        sample_user.display_info()
    else:
        print("Kullanıcı bulunamadı.")

    # Hash tablosundaki tüm kullanıcıları ekrana yazdır
    hash_table.display_table()

if __name__ == "__main__":
    main()
