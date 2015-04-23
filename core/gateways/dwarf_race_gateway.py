from core.gateways.default_race_gateway import DefaultRaceGateway


class DwarfRaceGateway(DefaultRaceGateway):
    def __init__(self):
        super(DwarfRaceGateway, self).__init__()
        self.set_ability_score(constitution=2, wisdom=2)
