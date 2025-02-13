from Helper import generate_id

class Player:
    def __init__(self, repo, game_id, name):
        self.game_id = game_id
        self.name = name
        self.id = generate_id()
        self.repo = repo
        repo.create(self)

    def __repr__(self):
        return f"Player(id={self.id}, game_id={self.game_id}, name='{self.name}')"