import pygame
from FileReader import *


class Unit(pygame.sprite.Sprite):
    dist = 32

    def __init__(self, team):
        pygame.sprite.Sprite.__init__(self)
        self.x = None
        self.y = None
        self.has_moved = False
        self.has_acted = False
        self.has_used_ability = False
        self.team = team
        self.CurrentHealth = self.MaxHealth
        self.image = pygame.image.load(Unit.resource_path(self.img_src))
        self.rect = self.image.get_rect()
        self.attacking = False
        self.attack_start_frame = None
        self.name = FileReader.generate_name()
        self.hometown = FileReader.generate_hometown()
        self.hobby = FileReader.generate_hobby()
        self.like = FileReader.generate_opinion()
        self.dislike = FileReader.generate_opinion()
        self.temp_movement = 0
        self.is_target = False
        self.damage = 0
        self.experience = 0
        self.next_level_exp = 100
        self.level = 1
        self.count = 0
        self.damage = 0
        self.healing = False

    def draw(self, surface, animation_state, tapped):
        image_attributes = self.img_src.split("-")
        if not self.attacking and self.damage == 0:
            if tapped:
                image_attributes[2] = "1"
            else:
                image_attributes[2] = str(animation_state)

            self.image = pygame.image.load("-".join(image_attributes))
            if tapped:
                self.image.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)
            surface.blit(self.image, (self.x, self.y))
        elif self.attacking:
            self.count += 1
            image_attributes[1] = "Attack"
            if animation_state % 2 == 0:
                attack_frame = 2
            else:
                attack_frame = 1

            image_attributes[2] = str(attack_frame)
            self.image = pygame.image.load("-".join(image_attributes))
            surface.blit(self.image, (self.x, self.y))

            if self.have_two_frames_passed(animation_state, self.attack_start_frame) or self.count >= 90:
                self.attacking = False
                self.attack_start_frame = None
                self.count = 0
        elif self.damage > 0 and not self.healing:
            self.count += 1
            image_attributes[2] = str(animation_state)
            self.image = pygame.image.load("-".join(image_attributes))
            self.image.fill((255, 0, 0, 100), None, pygame.BLEND_RGBA_MULT)
            font = pygame.font.SysFont("comicsansms", 16)
            text = font.render(str(self.damage), True, (255, 51, 51))
            surface.blit(self.image, (self.x, self.y))
            surface.blit(text, (self.x + 9, self.y - 18))
            if self.count >= 40:
                self.count = 0
                self.damage = 0
        elif self.damage > 0 and self.healing:
            self.count += 1
            image_attributes[2] = str(animation_state)
            self.image = pygame.image.load("-".join(image_attributes))
            self.image.fill((255, 0, 0, 100), None, pygame.BLEND_RGBA_MULT)
            font = pygame.font.SysFont("comicsansms", 16)
            text = font.render(str(self.damage), True, (20, 200, 20))
            surface.blit(self.image, (self.x, self.y))
            surface.blit(text, (self.x + 9, self.y - 18))
            if self.count >= 40:
                self.count = 0
                self.damage = 0
        elif self.damage < 0:
            self.count += 1
            image_attributes[2] = str(animation_state)
            self.image = pygame.image.load("-".join(image_attributes))
            font = pygame.font.SysFont("comicsansms", 18)
            text = font.render("MISSED!", True, (51, 255, 255))
            surface.blit(self.image, (self.x, self.y))
            surface.blit(text, (self.x - 16, self.y - 20))

            if self.count >= 40:
                self.count = 0
                self.damage = 0

    def draw_preview(self, surface, location, animation_state, attacking):
        image_attributes = self.img_src.split("-")
        if not attacking:
            image_attributes[2] = str(animation_state)
            self.image = pygame.image.load("-".join(image_attributes))
        else:
            image_attributes[1] = "Attack"
            if animation_state % 2 == 0:
                attack_frame = 2
            else:
                attack_frame = 1

            image_attributes[2] = str(attack_frame)
            self.image = pygame.image.load("-".join(image_attributes))
            surface.blit(self.image, location)

        surface.blit(self.image, location)

    def incoming_damage(self, damage, healing):
        self.damage = damage
        self.healing = healing

    def selected_target(self):
        self.is_target = True

    def movement_clac(self):
        self.temp_movement -= 1

    def reset_movement(self):
        self.temp_movement = self.movement

    def get_location(self):
        current_space = (self.x / self.dist, self.y / self.dist)
        return current_space

    def get_team(self):
        return self.team

    def get_movement(self):
        return self.Movement

    def get_minimum_range(self):
        return self.MinimumRange

    def get_maximum_range(self):
        return self.MaximumRange

    def deal_damage(self, damage):
        self.CurrentHealth -= damage

    def heal_damage(self, damage):
        self.CurrentHealth += damage
        if self.CurrentHealth > self.MaxHealth:
            self.CurrentHealth = self.MaxHealth


    def calculate_level(self):
        while self.experience >= self.next_level_exp:
            self.level += 1
            self.experience -= self.next_level_exp
            self.next_level_exp += 50

            bonus_roll = randint(0, 100)

            if bonus_roll >= 95:
                bonus_points = 5
            elif bonus_roll >= 85:
                bonus_points = 4
            elif bonus_roll >= 75:
                bonus_points = 3
            elif bonus_roll >= 50:
                bonus_points = 2
            else:
                bonus_points = 1

            self.MaxHealth += 1
            for point in range(1, bonus_points):
                stat_roll = randint(0, 100)
                is_critical_point = randint(0, 100) >= 95
                if stat_roll >= 95:
                    self.Movement += 1
                elif stat_roll >= 70:
                    if is_critical_point:
                        self.MaxHealth += 2
                    else:
                        self.MaxHealth += 1
                elif stat_roll >= 50:
                    if is_critical_point:
                        self.Attack += 2
                    else:
                        self.Attack += 1
                elif stat_roll >= 30:
                    if is_critical_point:
                        self.Defense += 2
                    else:
                        self.Defense += 1
                elif stat_roll >= 15:
                    if is_critical_point:
                        self.Evasion += 3
                    else:
                        self.Evasion += 2
                else:
                    if is_critical_point:
                        self.Accuracy += 3
                    else:
                        self.Accuracy += 2
            self.CurrentHealth = self.MaxHealth


    @staticmethod
    def resource_path(relative):
        return os.path.join(
            os.environ.get(
                "_MEIPASS2",
                os.path.abspath(".")
            ),
            relative
        )


    @staticmethod
    def have_two_frames_passed(first, current):
        return (current == 1 and first == 2) or (current == 2 and first == 3) or (current == 3 and first == 1)

