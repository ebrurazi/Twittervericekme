import json

class Graph:
    def __init__(self):
        self.nodes = set()  # Kullanıcıları temsil eden düğümler
        self.edges = []     # Takipçi-takip edilen ilişkilerini temsil eden kenarlar

    def add_user(self, user):
        self.nodes.add(user)

    def add_relationship(self, follower, following):
        # Eğer ilişki daha önce eklenmediyse ekle
        if (follower, following) not in self.edges:
            self.edges.append((follower, following))

    def build_graph_from_data(self, data):
        # Kullanıcıları grafa ekle
        for user_data in data:
            user = User(user_data["username"])
            self.add_user(user)

        # İlişkileri grafa ekle
        for user_data in data:
            user = User(user_data["username"])
            for following_username in user_data["following"]:
                following_user = User(following_username)
                self.add_relationship(user, following_user)

    def print_graph(self):
        print("Nodes:", self.nodes)
        print("Edges:", self.edges)

class User:
    def __init__(self, username):
        self.username = username

# data.json dosyasını oku
with open("data.json", "r") as file:
    data = json.load(file)

# Graf oluştur
user_graph = Graph()
user_graph.build_graph_from_data(data)

# Grafi yazdır
user_graph.print_graph()
