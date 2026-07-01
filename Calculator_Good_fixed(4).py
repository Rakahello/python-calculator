import sys
import pygame
import time
import os
import platform
import importlib.metadata as importlib_metadata
from pathlib import Path
import random
from Font.config import FontConfig
from Font.render import Renderer
from Font.funcs import cv2, putTTFText
import Font.character as character
from plyer import notification
import subprocess
import pybase64
from moviepy import VideoFileClip
import tempfile
import re

print("##############")
print("# Calculator #")
print("##############")
print("Made by An_npc *my name in roblox*")
print("Also if the python not working Download sys")
print("If there is bug please report it to my github")
print("Dont forget to give me a star in github!")
print("Created Date: 11/7/2025, Updated Date: 30/06/2026")


def choose_math_mode_old():
    print("Created Date: 11/1/2025, Updated Date: 11/2/2025, Time: 10:14 AM")
    print("Version: 1.0.0 TEST")
    """
    Presents a menu for the user to select an arithmetic operation mode.
    Returns the name of the chosen mode as a string.
    """

    # Define the available modes using a dictionary for easy mapping
    modes = {
        '1': 'Addition (+)',
        '2': 'Subtraction (-)',
        '3': 'Multiplication (*)',
        '4': 'Division (/)',
        '5': 'Pygame(simple game damn)',
        '6': 'Exit if you want to exit'
    }

    print("-" * 40)
    print("      MATH MODE SELECTOR")
    print("-" * 40)

    # Display the menu options
    print("Please choose an operation mode:")
    for key, value in modes.items():
        print(f"  [{key}] {value}")

    print("-" * 40)

    chosen_mode = None

    # Loop until a valid choice is made
    while chosen_mode is None:
        try:
            # Get user input
            choice = input("Enter the number of your choice (1-5): ").strip()

            # Check if the choice key exists in the modes dictionary
            if choice in modes:
                chosen_mode = modes[choice]

                # Confirmation message
                print("\n" + "=" * 40)
                print(f"SUCCESS: You have selected the {chosen_mode} mode.")
                print("=" * 40)

                # Optional: demonstrate a simple use case
                if choice == '1':
                    print("Please type the number for Add the number")
                    number1 = int(input())
                    print("+")
                    number2 = int(input())
                    equal = number1 + number2
                    print("= " + str(equal))
                    return choose_math_mode_old()
                if choice == '2':
                    print("Please type the number for Minus the number")
                    numb1 = int(input())
                    print("-")
                    numb2 = int(input())
                    answer1 = numb1 - numb2
                    print("= " + str(answer1))
                    return choose_math_mode_old()
                if choice == '3':
                    print("Please input the number for Multiply the number")
                    numbe1 = int(input())
                    print("*")
                    numbe2 = int(input())
                    answer = numbe1 * numbe2
                    print("= " + str(answer))
                    return choose_math_mode_old()
                if choice == '4':
                    print("Please input the number for share *why share cuz is division* the number")
                    num1 = int(input())
                    print("/")
                    num2 = int(input())
                    equali = num1 / num2
                    print("= " + str(equali))
                    return choose_math_mode_old()
                if choice == '5':
                    print("You in Pygame mode, Please wait the pygame open...")
                    return run_pygame_mode_old()
                if choice == '6':
                    print("Exiting the program. Goodbye!")
                    for n in range(10, 0, -1):
                        print(n)
                        time.sleep(1)
                    print("Exiting the program...")
                    print("If you want to be faster in exit, Please Press Ctrl+C or Ctrl+Z")
                    thanks = input("Please type 'thanks' to exit: ")
                    if thanks.lower() == "thanks":
                        return bootloader_windows()
                    else:
                        if thanks.lower() == "skibidi":
                            print("You Brainrot Kids, why You type it hahaha")
                    if thanks.lower() != "notexit":
                        return choose_math_mode_old()
                    sys.exit(0)
                return chosen_mode
            else:
                # Handle invalid numbers or letters
                print(f"Error: '{choice}' is not a valid option. Please enter a number between 1 and 5.")

        except EOFError:
            # Handle Ctrl+D/Ctrl+Z (End of File)
            print("\nExiting the mode chooser.")
            sys.exit(0)
        except Exception as e:
            # Catch other unexpected errors
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)


def run_pygame_mode_old():
    """
    Stub for the legacy pygame mode referenced by choose_math_mode_old().
    Previously this function did not exist, causing a NameError when
    selecting option '5' in the old menu. It now redirects to the
    working ping-pong implementation so the program does not crash.
    """
    print("(Legacy pygame mode redirects to the current ping pong game)")
    return run_pingpong_game()


def bootloader_windows():
    print("-" * 40)
    print("Bootloader Windows")
    print("-" * 40)
    modeboot = {
        '1': 'Start Calculator_Good.py',
        '2': 'Exit Bootloader',
        '3': 'Old Calculator Version'
    }
    for key, value in modeboot.items():
        print(f"  [{key}] {value}")
    bootchoice = None
    while bootchoice is None:
        bootinput = input("Enter the number of your choice (1-3): ").strip()
        if bootinput in modeboot:
            bootchoice = modeboot[bootinput]
            print(f"You have selected the {bootchoice} mode.")
            if bootinput == '1':
                print("Starting Calculator_Good.py...")
                time.sleep(2)
                return choose_math_mode()
            if bootinput == '2':
                print("Exiting Bootloader. Goodbye!")
                time.sleep(2)
                sys.exit(0)
            if bootinput == '3':
                print("Starting Old Calculator Version...")
                time.sleep(2)
                return choose_math_mode_old()
        else:
            print(f"Error: '{bootinput}' is not a valid option. Please enter a number between 1 and 2.")


def run_virus_mode():
    print("-" * 40)
    print("Welcome To Delete Mode")
    print("This mode will delete some functions in the program")
    print("Prossing...")
    print("Def run_pygame_mode(): is Deleted")
    print("Please wait...")
    time.sleep(5)
    print("def choose_math_mode(): is Deleted")
    print("Program is deleted")
    time.sleep(3)
    print("Program is not responding")
    print("Downloading Program.exe......")
    time.sleep(19)
    print("Download complete")
    print("Restrting...")
    print("-" * 40)
    print("Cmd.exe")
    print("-" * 40)
    print("taskkill /f /im Calculator_Good.py")
    print(".\\Calculator_Good.py")
    print("Error: F:\\Python File\\Calculator_Good.py not responding")
    print("Please wait...")
    print("Error: Still not responding")
    moderun = {
        '1': 'Close Program',
        '2': 'Wait The program to respond'
    }
    for key, value in moderun.items():
        print(f"  [{key}] {value}")
    modchoice = None
    while modchoice is None:
        modinput = input("Enter the number of your choice (1-2): ").strip()
        if modinput in moderun:
            modchoice = moderun[modinput]
            print(f"You have selected the {modchoice} mode.")
            if modinput == '1':
                print("Closing the program...")
                time.sleep(3)
                return bootloader_windows()
            if modinput == '2':
                print("Waiting for the program to respond...")
                time.sleep(10)
                print("Program is responding now returning to mode chooser...")
                time.sleep(2)
                return choose_math_mode()
        else:
            print(f"Error: '{modinput}' is not a valid option. Please enter a number between 1 and 2.")
            return choose_math_mode()


def run_pingpong_game():
    # Simple Ping Pong Game using Pygame
    pygame.init()

    # Screen dimensions
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Ping Pong Game")
    clock = pygame.time.Clock()

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Paddle dimensions
    PADDLE_WIDTH = 15
    PADDLE_HEIGHT = 90
    PADDLE_SPEED = 6

    # Ball dimensions
    BALL_SIZE = 10
    BALL_SPEED = 5

    # Paddle positions
    left_paddle = pygame.Rect(10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = pygame.Rect(SCREEN_WIDTH - 25, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

    # Ball position and velocity
    ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
    ball_velocity = [BALL_SPEED, BALL_SPEED]

    # Score
    left_score = 0
    right_score = 0
    font = pygame.font.Font(None, 74)

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Paddle controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_paddle.top > 0:
            left_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_s] and left_paddle.bottom < SCREEN_HEIGHT:
            left_paddle.y += PADDLE_SPEED
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and right_paddle.bottom < SCREEN_HEIGHT:
            right_paddle.y += PADDLE_SPEED

        # Ball movement
        ball.x += ball_velocity[0]
        ball.y += ball_velocity[1]

        # Ball collision with top/bottom
        if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
            ball_velocity[1] = -ball_velocity[1]

        # Ball collision with paddles
        if ball.colliderect(left_paddle) and ball_velocity[0] < 0:
            ball_velocity[0] = -ball_velocity[0]
        if ball.colliderect(right_paddle) and ball_velocity[0] > 0:
            ball_velocity[0] = -ball_velocity[0]

        # Ball out of bounds
        if ball.left <= 0:
            right_score += 1
            ball.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
            ball.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
            ball_velocity = [BALL_SPEED, BALL_SPEED]
        if ball.right >= SCREEN_WIDTH:
            left_score += 1
            ball.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
            ball.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
            ball_velocity = [-BALL_SPEED, BALL_SPEED]

        # Drawing
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, left_paddle)
        pygame.draw.rect(screen, WHITE, right_paddle)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

        # Score display
        left_text = font.render(str(left_score), True, WHITE)
        right_text = font.render(str(right_score), True, WHITE)
        screen.blit(left_text, (SCREEN_WIDTH // 4, 50))
        screen.blit(right_text, (3 * SCREEN_WIDTH // 4, 50))

        pygame.display.flip()

        if left_score == 10:
            print("Left Player Wins!")
            time.sleep(2)
            pygame.quit()
            return choose_math_mode()
        if right_score == 10:
            print("Right Player Wins!")
            time.sleep(2)
            pygame.quit()
            return choose_math_mode()
    pygame.quit()
    return choose_math_mode()


AUDIO_EXTENSIONS = {'.mp3', '.wav', '.ogg', '.flac', '.m4a'}

# Folders to skip while scanning, since they rarely contain music
# and scanning them just wastes time (and some need admin rights).
SKIP_FOLDER_NAMES = {
    'windows', 'program files', 'program files (x86)', 'programdata',
    '$recycle.bin', 'system volume information', 'appdata',
    'node_modules', '.git', 'recovery', 'msocache'
}


def search_music_files(root_path, max_results=300):
    """
    Walks through root_path (a drive or folder) looking for audio files.
    Skips known heavy/system folders to keep the search reasonably fast,
    and silently ignores folders it doesn't have permission to read.
    """
    found = []
    print(f"Searching for music in {root_path} ... (this can take a while on a whole drive)")
    start_time = time.time()

    for dirpath, dirnames, filenames in os.walk(root_path, onerror=lambda e: None):
        dirnames[:] = [d for d in dirnames if d.lower() not in SKIP_FOLDER_NAMES]

        for fname in filenames:
            ext = os.path.splitext(fname)[1].lower()
            if ext in AUDIO_EXTENSIONS:
                found.append(os.path.join(dirpath, fname))
                if len(found) % 10 == 0:
                    print(f"  Found {len(found)} track(s) so far...", end="\r")
                if len(found) >= max_results:
                    print(f"\nReached the limit of {max_results} tracks, stopping search early.")
                    return found

    elapsed = time.time() - start_time
    print(f"\nSearch finished in {elapsed:.1f}s. Found {len(found)} track(s).")
    return found


def run_music_playlist():
    """
    A simple VLC-like music player. Lets the user pick a drive or folder
    to search (e.g. C:\\, D:\\Music, or any path), finds audio files in it,
    and plays them using pygame.mixer with play/pause/stop/next/prev/volume
    controls.
    """
    print("-" * 40)
    print("Music Playlist Player")
    print("-" * 40)
    print("Where do you want to search for music?")
    print("  Examples: C:\\, D:\\Music, C:\\Users\\YourName\\Music, or a USB drive like E:\\")
    search_path = input("Enter a drive or folder path (press Enter for C:\\): ").strip()
    if not search_path:
        search_path = "C:\\"

    if not os.path.exists(search_path):
        print(f"Error: '{search_path}' does not exist.")
        return choose_math_mode()

    playlist = search_music_files(search_path)
    if not playlist:
        print("No music files found in that location.")
        return choose_math_mode()

    if not pygame.mixer.get_init():
        pygame.mixer.init()

    current_index = 0
    paused = False

    def show_playlist():
        print("\nPlaylist:")
        for i, track in enumerate(playlist):
            marker = ">>" if i == current_index else "  "
            print(f"{marker} [{i}] {os.path.basename(track)}")

    converted_temp_files = []  # keep track so we can clean them up on quit

    def convert_to_playable_wav(path):
        """
        Some audio files (e.g. cached files with a .mp3 extension that
        aren't fully standard, like Roblox asset cache files) fail to
        load directly in pygame/SDL_mixer with a vague "Out of memory"
        error. ffmpeg (via moviepy) is much more tolerant, so we use it
        to re-encode the file into a clean temporary WAV first.
        """
        try:
            from moviepy import AudioFileClip
            clip = AudioFileClip(path)
            tmp_wav = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
            tmp_wav.close()
            clip.write_audiofile(tmp_wav.name, logger=None)
            clip.close()
            converted_temp_files.append(tmp_wav.name)
            return tmp_wav.name
        except Exception as conv_err:
            print(f"  Conversion also failed: {conv_err}")
            return None

    def play_track(index):
        nonlocal paused, current_index
        current_index = index
        track_path = playlist[index]

        # Quick sanity check: a near-empty file is almost certainly
        # corrupted or an incomplete download, not worth trying to play.
        try:
            if os.path.getsize(track_path) < 1024:
                print(f"'{os.path.basename(track_path)}' looks corrupted or incomplete (too small), skipping.")
                if len(playlist) > 1:
                    play_track((index + 1) % len(playlist))
                return
        except OSError:
            pass

        try:
            pygame.mixer.music.load(track_path)
            pygame.mixer.music.play()
            paused = False
            print(f"Now playing: {os.path.basename(track_path)}")
            return
        except Exception as e:
            print(f"pygame couldn't play '{os.path.basename(track_path)}' directly ({e}).")
            print("  Trying to convert it with ffmpeg first...")

        converted = convert_to_playable_wav(track_path)
        if converted:
            try:
                pygame.mixer.music.load(converted)
                pygame.mixer.music.play()
                paused = False
                print(f"Now playing (converted): {os.path.basename(track_path)}")
                return
            except Exception as e2:
                print(f"  Still couldn't play after conversion ({e2}).")

        print(f"Skipping '{os.path.basename(track_path)}' - file is likely corrupted or in an unsupported format.")
        if len(playlist) > 1:
            next_index = (index + 1) % len(playlist)
            if next_index != index:
                play_track(next_index)

    show_playlist()
    play_track(current_index)

    controls = {
        'p': 'Play/Resume',
        's': 'Pause',
        'x': 'Stop',
        'n': 'Next track',
        'b': 'Previous track',
        'l': 'Show playlist',
        'v': 'Set volume (0-100)',
        '<number>': 'Jump to that track number',
        'r': 'Search a different folder/drive',
        'q': 'Quit to main menu'
    }

    running = True
    while running:
        print("\nControls: " + ", ".join(f"[{k}] {v}" for k, v in controls.items()))
        cmd = input("Command: ").strip().lower()

        if cmd == 'p':
            if paused:
                pygame.mixer.music.unpause()
                paused = False
                print("Resumed.")
            else:
                play_track(current_index)
        elif cmd == 's':
            pygame.mixer.music.pause()
            paused = True
            print("Paused.")
        elif cmd == 'x':
            pygame.mixer.music.stop()
            print("Stopped.")
        elif cmd == 'n':
            play_track((current_index + 1) % len(playlist))
        elif cmd == 'b':
            play_track((current_index - 1) % len(playlist))
        elif cmd == 'l':
            show_playlist()
        elif cmd == 'v':
            try:
                vol = int(input("Enter volume 0-100: ").strip())
                vol = max(0, min(100, vol))
                pygame.mixer.music.set_volume(vol / 100)
                print(f"Volume set to {vol}%.")
            except ValueError:
                print("Please enter a number between 0 and 100.")
        elif cmd == 'r':
            pygame.mixer.music.stop()
            return run_music_playlist()
        elif cmd == 'q':
            pygame.mixer.music.stop()
            running = False
        elif cmd.isdigit():
            idx = int(cmd)
            if 0 <= idx < len(playlist):
                play_track(idx)
            else:
                print(f"Track number must be between 0 and {len(playlist) - 1}.")
        else:
            print("Unknown command, try again.")

    # Clean up any temporary WAV files created during conversion
    for tmp_path in converted_temp_files:
        try:
            os.remove(tmp_path)
        except OSError:
            pass

    return choose_math_mode()


def run_dev_mode():
    """
    Developer mode: prints out useful system/environment information
    for debugging - Python version, OS details, the versions of the
    third-party libraries this program depends on, and the file paths
    the program relies on (so you can quickly spot a missing file or
    a wrong path without digging through the code).
    """
    print("=" * 50)
    print("DEV MODE - System Information")
    print("=" * 50)

    print("\n--- Python ---")
    print(f"Python version : {platform.python_version()}")
    print(f"Implementation : {platform.python_implementation()}")
    print(f"Executable     : {sys.executable}")

    print("\n--- Operating System ---")
    print(f"OS           : {platform.system()} {platform.release()}")
    print(f"OS version   : {platform.version()}")
    print(f"Architecture : {platform.machine()}")
    print(f"Node name    : {platform.node()}")

    print("\n--- Installed Libraries Used By This Program ---")
    packages_to_check = [
        "pygame", "pygame-ce", "opencv-python", "numpy",
        "Font", "freetype-py", "plyer", "pybase64", "moviepy"
    ]
    for pkg in packages_to_check:
        try:
            version = importlib_metadata.version(pkg)
            print(f"  {pkg:<15} : {version}")
        except importlib_metadata.PackageNotFoundError:
            print(f"  {pkg:<15} : not installed")

    print("\n--- File Paths Used By This Program ---")
    try:
        script_path = os.path.abspath(__file__)
    except NameError:
        script_path = "(unknown - not running as a saved file)"
    print(f"This script    : {script_path}")
    print(f"Working dir    : {os.getcwd()}")

    paths_to_check = {
        "Notepad script": "f:/Python File/My Notepad.py",
        "Base64 script": "f:/Python File/Untitled-1.py",
    }
    for label, path in paths_to_check.items():
        status = "exists" if os.path.exists(path) else "NOT FOUND"
        print(f"{label:<15}: {path}  [{status}]")

    print("\n" + "=" * 50)
    input("Press Enter to return to the main menu...")
    return choose_math_mode()


def run_video_player():
    """
    Stub for the video player.
    Previously this function was called from the 'Video' menu option
    but was never defined, and the line `re.sub("")` above it would
    have crashed with a TypeError (re.sub needs pattern + replacement
    + string, not a single empty string). Both issues are fixed here.
    """
    print("-" * 40)
    print("Video Player")
    print("-" * 40)
    print("This feature is not implemented yet.")
    print("TODO: use moviepy's VideoFileClip (already imported) to play a video file.")
    return choose_math_mode()


def choose_math_mode():
    print("Version: 1.1.4")
    """
    Presents a menu for the user to select an arithmetic operation mode.
    Returns the name of the chosen mode as a string.
    """

    # Define the available modes using a dictionary for easy mapping
    modes = {
        '1': 'Addition (+)',
        '2': 'Subtraction (-)',
        '3': 'Multiplication (*)',
        '4': 'Division (/)',
        '5': 'Pygame(simple game damn)',
        '6': 'Exit if you want to exit',
        '2002Error': '',
        'Bootloader': 'Choose Your Boot',
        'Music': 'Music Playlist Player',
        'Notepad': 'Open My Notepad.py',
        'Base64': 'Base64 Encoder/Decoder',
        'Run': 'Windows Run Command',
        'Video': 'Video Player',
        'Folder': 'A Folder',
        'Dev Mode': 'Hidden Developer Mode',
        'Browser': 'Download Official Installer!'
    }

    print("-" * 40)
    print("      MATH MODE SELECTOR")
    print("-" * 40)

    # Display the menu options
    print("Please choose an operation mode:")
    for key, value in modes.items():
        print(f"  [{key}] {value}")

    print("-" * 40)

    chosen_mode = None

    # Loop until a valid choice is made
    while chosen_mode is None:
        try:
            # Get user input
            choice = input("Enter the number of your choice (1-5): ").strip()

            # Check if the choice key exists in the modes dictionary
            if choice in modes:
                chosen_mode = modes[choice]

                # Confirmation message
                print("\n" + "=" * 40)
                print(f"SUCCESS: You have selected the {chosen_mode} mode.")
                print("=" * 40)

                # Optional: demonstrate a simple use case
                if choice == '1':
                    print("Please type the number for Add the number")
                    number1 = float(input())
                    print("+")
                    number2 = float(input())
                    equal = number1 + number2
                    print("= " + str(equal))

                if choice == '2':
                    print("Please type the number for Minus the number")
                    numb1 = float(input())
                    print("-")
                    numb2 = float(input())
                    answer1 = numb1 - numb2
                    print("= " + str(answer1))

                if choice == '3':
                    print("Please input the number for Multiply the number")
                    numbe1 = float(input())
                    print("*")
                    numbe2 = float(input())
                    answer = numbe1 * numbe2
                    print("= " + str(answer))
                if choice == '4':
                    print("Please input the number for share *why share cuz is division* the number")
                    num1 = float(input())
                    print("/")
                    num2 = float(input())
                    equali = num1 / num2
                    print("= " + str(equali))

                if choice == '5':
                    print("You in Pygame mode, Please wait the pygame open...")
                    print("Error Is in here")
                    return run_pingpong_game()
                if choice == '6':
                    print("Exiting the program. Goodbye!")
                    for n in range(10, 0, -1):
                        print(n)
                        time.sleep(1)
                    print("Exiting the program...")
                    print("If you want to be faster in exit, Please Press Ctrl+C or Ctrl+Z")
                    thanks = input("Please type 'thanks' to exit: ")
                    if thanks.lower() == "thanks":
                        sys.exit(0)
                    if thanks.lower() != "notexit":
                        return choose_math_mode()
                    sys.exit(0)
                if choice == '2002Error':
                    moerror = {
                        '1': 'Python2002er',
                        '21': 'PythonGem'
                    }
                    print("Please Choose the Error Mode.. You gona be kidding right?")
                    for key, value in moerror.items():
                        print(f"  [{key}] {value}")
                    errchoice = None
                    while errchoice is None:
                        errinput = input("Enter the number of your choice (1-2): ").strip()
                        if errinput in moerror:
                            errchoice = moerror[errinput]
                            print(f"You have selected the {errchoice} mode.")
                            if errinput == '1':
                                print("Error Python is gliching status.")
                                print("Please wait...")
                                time.sleep(5)
                                print("Error fixed now you can use the calculator again.")
                                print("Main menu is Unknown status.")
                                print("Waiting for 10 seconds to return to main menu...")
                                print("Returning to Main Menu...")
                                print("Main Menu.pyc is not available.")
                                print("Please wait...")
                                print("downloading Main Menu.pyc...")
                                time.sleep(10)
                                print("Download complete.")
                                print("Restarting the program...")

                                return bootloader_windows()
                            if errinput == '21':
                                print("Error Game is loading...")
                                time.sleep(5)
                                print("Game is not working now returning to mode chooser...")
                                time.sleep(3)
                                print("Error, The return is failed, Please try again.")
                                print("Returning to Main Menu...")
                                time.sleep(10)
                                print("Error Main Menu not responding, Restarting the program...")

                                return run_virus_mode()
                        else:
                            print(f"Error: '{errinput}' is not a valid option. Please enter a number between 1 and 2.")

                            return choose_math_mode()
                if choice == 'Music':
                    print("You in Music Playlist Player mode, Please wait the music player open...")
                    return run_music_playlist()
                if choice == 'Bootloader':
                    print("Restarting...")
                    time.sleep(5)
                    print("File Saved")
                    print("Loading...")
                    time.sleep(3)

                    return bootloader_windows()
                if choice == 'Notepad':
                    print("You in Notepad mode, Please wait the notepad open...")
                    subprocess.run([sys.executable, "f:/Python File/My Notepad.py"])

                    return choose_math_mode()
                if choice == 'Base64':
                    print("You in Base64 Encoder/Decoder mode, Please wait...")
                    subprocess.run([sys.executable, "f:/Python File/Untitled-1.py"])
                if choice == 'Run':
                    print("You in Windows Run Command mode, Please wait...")
                    command = input("Enter the command to run (e.g., notepad, calc): ")
                    exit_code = os.system(command)
                    if exit_code == 0:
                        print("Other Script ran successfully.")

                        choose_math_mode()
                    else:
                        print(f"Other Script failed with exit code {exit_code}.")

                        choose_math_mode()
                if choice == 'Video':
                    print("You in Video Player mode, Please wait the video player open...")
                    return run_video_player()
                if choice == 'Folder':
                    print("You in Folder mode, Please wait the folder open...")
                    time.sleep(6)
                    Folderfile = [
                        'A:',
                        'C:',
                        'D:',
                        'USB Drive (E:)'
                    ]
                    print("Available Drives:")
                    for idx, drive in enumerate(Folderfile, start=1):
                        print(f"  [{idx}] {drive}")
                    print("You Cannot Access The Drives. We In Working On It.")
                    print("The Feature Will Be Available In Future Updates. Stay Tuned!")
                    print("You are in Demo Version of this Feature.")
                    print("Are You Want To Close The Folder Mode?")
                    close_folder = input("Type 'yes' to close or 'no' to return to mode chooser: ").strip().lower()
                    if close_folder in ['yes', 'ye', 'y']:
                        print("Closing Folder Mode...")
                        time.sleep(2)

                        return choose_math_mode()
                    else:
                        print("Shutdowning...")
                        bootloader_windows()
                if choice == 'Dev Mode':
                    print("Welcome To Dev Mode")
                    Password = input("Please Input The Password To Access Dev Mode: ")
                    print("Password Is Hidded In Github")
                    if Password == "Pr0duc5Pass034dIsThis!":
                        print("Access Granted. Welcome to Dev Mode!")
                        time.sleep(1)
                        return run_dev_mode()
                    else:
                        print("Access Denied. Incorrect Password.")
                        return choose_math_mode()
                if choice == 'Browser':
                    subprocess.run([sys.executable, "f:/Python File/App_Browser.py"])
                return chosen_mode
            else:
                # Handle invalid numbers or letters
                print(f"Error: '{choice}' is not a valid option. Please enter a number between 1 and 5.")

        except EOFError:
            # Handle Ctrl+D/Ctrl+Z (End of File)
            print("\nExiting the mode chooser.")
            sys.exit(0)
        except Exception as e:
            # Catch other unexpected errors
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)


# Entry point of the script
if __name__ == "__main__":
    mode = choose_math_mode()
    # You can now use the 'mode' variable (e.g., 'Addition (+)') in the rest of your program
    # print(f"\nYour program is now running in: {mode}")
