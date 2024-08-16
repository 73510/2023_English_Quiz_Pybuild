import pandas as pd
import random

import tkinter.filedialog as filedialog


def get_dataset(directory, num_rows):
    # Load the dataset
    df = pd.read_excel(directory)

    # Check if the requested number of rows is greater than the dataset size
    if num_rows > len(df):
        raise ValueError("Requested number of rows is greater than the number of rows in the dataset.")

    # Get random rows
    random_indices = random.sample(range(len(df)), num_rows)
    random_rows = df.iloc[random_indices]

    return random_rows


def quiz_start():
    import pygame
    import pygame_gui

    # Initialize Pygame
    pygame.init()

    # Set up some constants
    WIDTH, HEIGHT = 800, 600
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    colval = ["expression", "definition"]

    # Create the window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Create a GUI manager
    manager = pygame_gui.UIManager((WIDTH, HEIGHT))

    # Create the title
    title = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((WIDTH // 2 - 100, HEIGHT // 2 - 200), (200, 50)),
                                        text="English Quiz!!",
                                        manager=manager)

    import os

# Read the files from your directory
    files = os.listdir('./datasets')
    print(files)

    # Check for only .csv files
    csv_files = [f for f in files if f.endswith('.xlsx')]
    
    file_dropdown = pygame_gui.elements.UIDropDownMenu(options_list=csv_files,
                                                    starting_option=csv_files[0] if csv_files else "No files",
                                                    relative_rect=pygame.Rect((WIDTH // 2 - 100, HEIGHT // 2 - 100), (200, 50)),
                                                    manager=manager)

    # Create the drop down menu for the quiz mode
    quiz_mode_dropdown = pygame_gui.elements.UIDropDownMenu(options_list=colval,
                                                            starting_option=colval[0],
                                                            relative_rect=pygame.Rect((WIDTH // 2 - 100, HEIGHT // 2-50), (200, 50)),
                                                            manager=manager)
    
    quiz_mode_dropdown2 = pygame_gui.elements.UIDropDownMenu(options_list=colval,
                                                            starting_option=colval[1],
                                                            relative_rect=pygame.Rect((WIDTH // 2 - 100, HEIGHT // 2), (200, 50)),
                                                            manager=manager)

    # Create the text entry for the number of words
    num_words_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((WIDTH // 2 - 100, HEIGHT // 2 + 50), (200, 50)),
                                                        manager=manager)

    # Create the play button
    play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((WIDTH // 2 - 100, HEIGHT // 2 + 100), (200, 50)),
                                            text="PLAY",
                                            manager=manager)


    # Game loop
    running = True

    DSdirectory = None
    dataset = None
    selected_opt = None
    col1 = None
    col2 = None
    while running:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == play_button:
                        if (num_words_entry.get_text() != '') :
                            num_words= int(num_words_entry.get_text())
                            
                            dataset = get_dataset('./datasets/' + file_dropdown.selected_option, num_words)

                            col1 = quiz_mode_dropdown.selected_option
                            col2 = quiz_mode_dropdown2.selected_option
                            running = False

                            if (col1 == col2):
                                return -1
                        else :
                            num_words = 0
            manager.process_events(event)

        # Render the screen
        screen.fill(WHITE)
        manager.update(pygame.time.Clock().tick(60))
        manager.draw_ui(screen)
        pygame.display.update()

    # Quit Pygame
    pygame.quit()


    return [col1, col2], dataset
