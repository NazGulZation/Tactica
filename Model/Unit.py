from Helper import generate_id

class Unit:
    def __init__(self, repo, unit_type_id, map_id, player_id, x, y, hp):
        self.unit_type_id = unit_type_id
        self.map_id = map_id
        self.player_id = player_id
        self.x = x
        self.y = y
        self.hp = hp
        self.id = generate_id()

        self.repo = repo
        repo.create(self)

    def __repr__(self):
        return (f"Unit(id={self.id}, unit_type_id={self.unit_type_id}, map_id={self.map_id}, "
                f"player_id={self.player_id}, x={self.x}, y={self.y}, hp={self.hp})")