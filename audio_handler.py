import os
import pygame

class AudioHandler:
    def __init__(self, sound_file):
        # Get the directory of the current script
        base_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the absolute path to the sound file
        self.sound_path = os.path.join(base_dir, sound_file)
        # Initialize pygame mixer
        pygame.mixer.init()

    def play_sound(self):
        # Load the sound file
        sound = pygame.mixer.Sound(self.sound_path)
        # Play the sound
        sound.play()
