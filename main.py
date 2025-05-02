from colorama import Fore, Style

from core.domain.character import Character
from core.enums import KlassEnum, RaceEnum


def choose_enum(enum_cls):
    options = list(enum_cls)
    for idx, option in enumerate(options, 1):
        print(f"{Fore.GREEN}{idx}. {option.name.title()}")
    while True:
        try:
            choice = int(input(f"{Fore.MAGENTA}Choose an option: {Style.RESET_ALL}"))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print(f"{Fore.RED}Invalid choice. Try again.")
        except ValueError:
            print(f"{Fore.RED}Please enter a valid number.")


def create_character():
    print(f"{Fore.BLUE}=== Create your character ==={Style.RESET_ALL}")
    name = input(f"{Fore.MAGENTA}Enter your character's name: {Style.RESET_ALL}").strip()

    print(f"\n{Fore.BLUE}Choose your race:{Style.RESET_ALL}")
    race = choose_enum(RaceEnum)

    print(f"\n{Fore.BLUE}Choose your class:{Style.RESET_ALL}")
    klass = choose_enum(KlassEnum)

    c = Character()
    c.name = name
    c.race = race
    c.klass = klass
    c.hp = c.maximum_hp
    return c


if __name__ == "__main__":
    character = create_character()
    print("\n" + str(character))
