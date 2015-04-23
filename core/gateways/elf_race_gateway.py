from core.gateways import DefaultRaceGateway


class ElfRaceGateway(DefaultRaceGateway):
    def __init__(self):
        super(ElfRaceGateway, self).__init__()
        self.set_ability_score(dexterity=2, wisdom=2)
