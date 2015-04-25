
class CharacterRaceList(object):
    DEVA = 'DEVA'
    DRAGONBORN = 'DRAGONBORN'
    DWARF = 'DWARF'
    ELADRIN = 'ELADRIN'
    ELF = 'ELF'
    GITHZERAI = 'GITHZERAI'
    GNOME = 'GNOME'
    GOLIATH = 'GOLIATH'
    HALFELF = 'HALFELF'
    HALFLING = 'HALFLING'
    HALFORC = 'HALFORC'
    HUMAN = 'HUMAN'
    MINOTAUR = 'MINOTAUR'
    SHARDMIND = 'SHARDMIND'
    SHIFTER = 'SHIFTER'
    TIEFLING = 'TIEFLING'
    WILDEN = 'WILDEN'


class CharacterClassList(object):
    ARDENT = 'ARDENT'
    AVENGER = 'AVENGER'
    BARBARIAN = 'BARBARIAN'
    BARD = 'BARD'
    BATTLEMIND = 'BATTLEMIND'
    CLERIC = 'CLERIC'
    DRUID = 'DRUID'
    FIGHTER = 'FIGHTER'
    INVOKER = 'INVOKER'
    MONK = 'MONK'
    PALADIN = 'PALADIN'
    PSION = 'PSION'
    RANGER = 'RANGER'
    ROGUE = 'ROGUE'
    RUNEPRIEST = 'RUNEPRIEST'
    SEEKER = 'SEEKER'
    SHAMAN = 'SHAMAN'
    SORCERER = 'SORCERER'
    WARDEN = 'WARDEN'
    WARLOCK = 'WARLOCK'
    WARLORD = 'WARLORD'
    WIZARD = 'WIZARD'


class CharacterRoleList(object):
    CONTROLLER = 'CONTROLLER'
    DEFENDER = 'DEFENDER'
    LEADER = 'LEADER'
    STRIKER = 'STRIKER'


class AlignmentList(object):
    GOOD = 'GOOD'
    LAWFUL_GOOD = 'LAWFUL_GOOD'
    UNALIGNED = 'UNALIGNED'
    EVIL = 'EVIL'
    CHAOTIC_EVIL = 'CHAOTIC_EVIL'


class DeitiesList(object):
    ASMODEUS = AlignmentList.EVIL
    AVANDRA = AlignmentList.GOOD
    BAHAMUT = AlignmentList.LAWFUL_GOOD
    BANE = AlignmentList.EVIL
    CORELLON = AlignmentList.UNALIGNED
    ERATHIS = AlignmentList.UNALIGNED
    GRUUMSH = AlignmentList.CHAOTIC_EVIL
    IOUN = AlignmentList.UNALIGNED
    KORD = AlignmentList.UNALIGNED
    LOLTH = AlignmentList.CHAOTIC_EVIL
    MELORA = AlignmentList.UNALIGNED
    MORADIN = AlignmentList.LAWFUL_GOOD
    PELOR = AlignmentList.GOOD
    SEHANINE = AlignmentList.UNALIGNED
    THE_RAVEN_QUEEN = AlignmentList.UNALIGNED
    TIAMAT = AlignmentList.EVIL
    TOROG = AlignmentList.EVIL
    VECNA = AlignmentList.EVIL
    ZEHIR = AlignmentList.EVIL


class ScriptList(object):
    COMMON = 'COMMON'
    RELLANIC = 'RELLANIC'
    IOKHARIC = 'IOKHARIC'
    DAVEK = 'DAVEK'
    BARAZHAD = 'BARAZHAD'
    SUPERNAL = 'SUPERNAL'


class LanguageList(object):
    COMMON = ScriptList.COMMON
    DEEP_SPEECH = ScriptList.RELLANIC
    DRACONIC = ScriptList.IOKHARIC
    DWARVEN = ScriptList.DAVEK
    ELVEN = ScriptList.RELLANIC
    GIANT = ScriptList.DAVEK
    GOBLIN = ScriptList.COMMON
    PRIMORDIAL = ScriptList.BARAZHAD
    SUPERNA = ScriptList.SUPERNAL
    ABYSSAL = ScriptList.BARAZHAD
