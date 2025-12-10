"""
Ryan Huckaby
Lab #10 (Week Twelve)
Date Started: 11/19/2025
Description:
"""

# Import Modules
import os
import pygame

# functions to create our resources
class Entity(pygame.sprite.Sprite):
    def __init__(self, filename, data_dir, colorkey=None, scale=1):
        super().__init__()

        fullname = os.path.join(data_dir, filename)
        image = pygame.image.load(fullname)
        image = image.convert()

        if scale != 1:
            w = int(image.get_width() * scale)
            h = int(image.get_height() * scale)
            image = pygame.transform.scale(image, (w, h))

        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)

        self.image = image
        self.rect = image.get_rect()

def load_sound(name, data_dir):
    class NoneSound:
        def play(self):
            pass

    if not pygame.mixer.get_init():
        return NoneSound()

    fullname = os.path.join(data_dir, name)

    try:
        sound = pygame.mixer.Sound(fullname)
        return sound
    except pygame.error:
        print("Missing sound file:", name)
        return NoneSound()

# classes for our game objects
class Fist(Entity):
    """moves a clenched fist on the screen, following the mouse"""

    def __init__(self, data_dir):
        super().__init__("fist.png", data_dir, colorkey=-1, scale=1)
        self.fist_offset = (-235, -80)
        self.punching = False

    def update(self):
        """move the fist based on the mouse position"""
        pos = pygame.mouse.get_pos()
        self.rect.topleft = pos
        self.rect.move_ip(self.fist_offset)
        if self.punching:
            self.rect.move_ip(15, 25)

    def punch(self, target):
        """returns true if the fist collides with the target"""
        if not self.punching:
            self.punching = True
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)

    def unpunch(self):
        """called to pull the fist back"""
        self.punching = False


class Chimp(Entity):
    """moves a monkey critter across the screen. it can spin the
    monkey when it is punched."""

    def __init__(self, data_dir):
        super().__init__("chimp.png", data_dir, colorkey=-1, scale=4)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 90
        self.move = 18
        self.dizzy = False

    def update(self):
        """walk or spin, depending on the monkeys state"""
        if self.dizzy:
            self._spin()
        else:
            self._walk()

    def _walk(self):
        """move the monkey across the screen, and turn at the ends"""
        newpos = self.rect.move((self.move, 0))
        if not self.area.contains(newpos):
            if self.rect.left < self.area.left or self.rect.right > self.area.right:
                self.move = -self.move
                newpos = self.rect.move((self.move, 0))
                self.image = pygame.transform.flip(self.image, True, False)
        self.rect = newpos

    def _spin(self):
        """spin the monkey image"""
        center = self.rect.center
        self.dizzy = self.dizzy + 12
        if self.dizzy >= 360:
            self.dizzy = False
            self.image = self.original
        else:
            rotate = pygame.transform.rotate
            self.image = rotate(self.original, self.dizzy)
        self.rect = self.image.get_rect(center=center)

    def punched(self):
        """this will cause the monkey to start spinning"""
        if not self.dizzy:
            self.dizzy = True
            self.original = self.image


def main():
    """this function is called when the program starts.
    it initializes everything it needs, then runs in
    a loop until the function returns."""
    # Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((1280, 480), pygame.SCALED)
    pygame.display.set_caption("Monkey Fever")
    pygame.mouse.set_visible(False)

    if not pygame.font:
        print("Warning, fonts disabled")
    if not pygame.mixer:
        print("Warning, sound disabled")

    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_dir = os.path.join(main_dir, "data")

    # Create The Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((170, 238, 187))

    # Put Text On The Background, Centered
    font = pygame.Font(None, 64)
    text = font.render("Pummel The Chimp, And Win $$$", True, (10, 10, 10))
    textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
    background.blit(text, textpos)

    # Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Prepare Game Objects
    whiff_sound = load_sound("whiff.wav", data_dir)
    punch_sound = load_sound("punch.wav", data_dir)
    chimp = Chimp(data_dir)
    fist = Fist(data_dir)
    all_sprites = pygame.sprite.Group(chimp, fist)
    clock = pygame.Clock()

    # Main Loop
    going = True
    while going:
        clock.tick(60)

        # Handle Input Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                going = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                going = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if fist.punch(chimp):
                    punch_sound.play()  # punch
                    chimp.punched()
                else:
                    whiff_sound.play()  # miss
            elif event.type == pygame.MOUSEBUTTONUP:
                fist.unpunch()

        all_sprites.update()

        # Draw Everything
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


# Game Over


# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()