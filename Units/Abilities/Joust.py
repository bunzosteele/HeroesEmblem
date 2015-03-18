class Joust():

    def __init__(self):
        pass

    @staticmethod
    def draw_ability_shadow(game_state, screen):
        pass

    @staticmethod
    def can_use_ability(unit, game_state):
        return Joust.is_active()

    @staticmethod
    def is_valid_target(target_tile, target_unit, unit, game_state):
        pass

    @staticmethod
    def use_ability(target_tile, target_unit, unit, game_state):
        return False

    @staticmethod
    def get_ability_name():
        return "Joust"

    @staticmethod
    def is_daily():
        return False

    @staticmethod
    def is_active():
        return False

    @staticmethod
    def is_targeted():
        return False

    @staticmethod
    def get_targets(unit, game_state):
        pass

    @staticmethod
    def get_potential_targets(location, team, game_state):
        pass

    @staticmethod
    def get_target_spaces(start, game_state):
        pass