import json
import networkx as nx
import matplotlib.pyplot as plt

class HashTabloUser:
    def __init__(self, username, name, followers_count, following_count, language, region, tweets, following, followers, interests):
        self.username = username
        self.name = name
        self.followers_count = followers_count
        self.following_count = following_count
        self.language = language
        self.region = region
        self.tweets = tweets
        self.following = following
        self.followers = followers
        self.interests = interests

class CustomHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def custom_hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert_user(self, user):
        hash_key = self.custom_hash_function(user.username)
        while self.table[hash_key] is not None:
            hash_key = (hash_key + 1) % self.size
        self.table[hash_key] = user

    def get_user(self, username):
        hash_key = self.custom_hash_function(username)
        while self.table[hash_key] is not None and self.table[hash_key].username != username:
            hash_key = (hash_key + 1) % self.size
        if self.table[hash_key] is not None:
            return self.table[hash_key]
        else:
            return None

    def display_table(self):
        for user in self.table:
            if user is not None:
                user.display_info()

class UserGraph:
    def __init__(self):
        self.graph = nx.Graph()  # Takipçi-takip edilen ilişkilerini temsil eden graf
        self.users = {}  # Kullanıcı adına göre kullanıcı nesnelerini tutan sözlük
        self.interests_table = {}  # İlgi alanlarına göre kullanıcıları gruplayan hash tablo

    def add_user(self, user):
        self.users[user.username] = user
        self.graph.add_node(user.username)

        # İlgi alanlarına göre kullanıcıları grupla
        for interest in user.interests:
            if interest not in self.interests_table:
                self.interests_table[interest] = [user.username]
            else:
                self.interests_table[interest].append(user.username)

    def add_relationships(self, user):
        for following_username in user.following:
            self.graph.add_edge(user.username, following_username)

    def build_graph_from_data(self, data, num_users):
        for user_data in data[:num_users]:
            user = HashTabloUser(**user_data)
            self.add_user(user)
            self.add_relationships(user)

    def write_relationships_to_txt(self, output_filename):
        with open(output_filename, "w") as file:
            for edge in self.graph.edges:
                file.write(f"{edge[0]} {edge[1]}\n")

    def find_common_interests_groups(self):
        common_interests_groups = []

        for interest, users in self.interests_table.items():
            if len(users) > 1:
                common_interests_groups.append(users)

        return common_interests_groups

def main():
    with open("/Users/ebrurazi/Desktop/prolab3/data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    user_graph = UserGraph()
    user_graph.build_graph_from_data(data, num_users=5)  # İlk 5 kullanıcı için test
    user_graph.write_relationships_to_txt("/Users/ebrurazi/Desktop/prolab3/user_relationships1.txt")

    # Görselleştirme yapmadan ilgi alanlarına göre grupları bulma
    common_interests_groups = user_graph.find_common_interests_groups()
    print("Common Interests Groups:")
    for group in common_interests_groups:
        print(group)

if __name__ == "__main__":
    main()
