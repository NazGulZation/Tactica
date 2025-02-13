import datetime
from Helper import generate_id
from Model.Map import Map
from Model.Player import Player

class Game:
    def __init__(self, repo, name):
        self.name = name
        self.id = generate_id()
        self.created_date = datetime.datetime.now().isoformat()
        self.current_map = None
        self.current_player = None
        self.won_by = None
        self.repo = repo
        repo.create(self)

    def __repr__(self):
        return f"Game(id={self.id}, name='{self.name}', created_date='{self.created_date}')"