from core.entities import DefaultRaceEntity


class ElfRaceEntity(DefaultRaceEntity):
    def __init__(self):
        super(ElfRaceEntity, self).__init__()
        self.set_ability_score(dexterity=2, wisdom=2)
