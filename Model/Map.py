from Helper import generate_id

class Map:
    def __init__(self, repo, game_id, x_size, y_size, id=None):
        self.game_id = game_id
        self.x_size = x_size
        self.y_size = y_size
        self.id = generate_id()
        self.repo = repo
        repo.create(self)

    def __repr__(self):
        return f"Map(id={self.id}, game_id={self.game_id}, x_size={self.x_size}, y_size={self.y_size})"