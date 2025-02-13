from Helper import generate_id

class UnitType:
    def __init__(self, repo, name, hp, is_ranged, damage):
        self.name = name
        self.hp = hp
        self.is_ranged = is_ranged
        self.damage = damage
        self.id = generate_id()
        self.repo = repo
        repo.create(self)

    def __repr__(self):
        return (f"UnitType(id={self.id}, name='{self.name}', hp={self.hp}, "
                f"is_ranged={self.is_ranged}, damage={self.damage})")