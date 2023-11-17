import pygame
import time
import os
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def print_with_sound(text):
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the sound file
    soundfile = r"C:\Users\Kinei\Downloads\mla-terminal-main\mla-terminal-main\typing.wav"
    sound = pygame.mixer.Sound(soundfile)

    # Play the sound in a loop
    sound.play(-1)  # -1 means the sound will loop indefinitely

    # Print the text one character at a time
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)

    # Stop the sound
    sound.stop()

def handle_command(command):
    try:
        if command == 'clear':
            clear_screen()
        elif command.startswith('open '):
            path = command[5:]
            if os.path.isfile(path):
                with open(path, 'r') as file:
                    print_with_sound(file.read())
            elif os.path.isdir(path):
                os.chdir(path)
                print_with_sound(f"Changed directory to {os.getcwd()}")
        elif command == 'list':
            files = os.listdir('.')
            print_with_sound('\n'.join(files))
        elif command.startswith('mkdir '):
            directory = command[6:]
            os.mkdir(directory)
            print_with_sound(f"Created directory {directory}")
        elif command.startswith('rm '):
            filename = command[3:]
            os.remove(filename)
            print_with_sound(f"Removed file {filename}")
        elif command == 'exit':
            print_with_sound("Exiting...")
            exit(0)
        elif command == 'help':
            help_text = """
            Available commands:
            - open {path}: Opens a file or changes the current directory to {path}.
            - list: Lists all files in the current directory.
            - mkdir {directory}: Creates a new directory named {directory} in the current working directory.
            - rm {filename}: Removes a file named {filename}.
            - exit: Exits the program.
            """
            print_with_sound(help_text)
        else:
            print(f'Unknown command: {command}')
    except Exception as e:
        print_with_sound(f"An error occurred: {str(e)}")

while True:
    command = input('\n' + '[guest@local]# ')
    handle_command(command)
