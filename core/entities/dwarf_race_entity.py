from core.entities.default_race_entity import DefaultRaceEntity


class DwarfRaceEntity(DefaultRaceEntity):
    def __init__(self):
        super(DwarfRaceEntity, self).__init__()
        self.set_ability_score(constitution=2, wisdom=2)
