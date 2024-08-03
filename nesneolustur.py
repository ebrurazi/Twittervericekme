import json

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

def create_user_objects(data):
    user_objects = {}

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

        user = User(username, name, followers_count, following_count, language, region, tweets, following, followers)
        user_objects[username] = user

    return user_objects

def main():
    # data.json dosyasını oku
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    # Kullanıcı nesnelerini oluştur
    user_objects = create_user_objects(data)

    # Örnek olarak bir kullanıcının bilgilerini ekrana yazdır
    sample_user = user_objects["ymohr"]
    print(f"Username: {sample_user.username}")
    print(f"Name: {sample_user.name}")
    print(f"Followers Count: {sample_user.followers_count}")
    print(f"Following Count: {sample_user.following_count}")
    print(f"Language: {sample_user.language}")
    print(f"Region: {sample_user.region}")
    print(f"Tweets: {sample_user.tweets}")
    print(f"Following: {sample_user.following}")
    print(f"Followers: {sample_user.followers}")

if __name__ == "__main__":
    main()
