import pygame
import pygame_gui
import pandas as pd
import time
import random
from quizstarter import *

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.current_question = 0
        self.rights = 0
        self.wrongs = 0
        self.right_wrong_list = []
    

    def run_quiz(self):
        import pygame
        import pygame_gui
        from pygame_gui.core import ObjectID
        
        pygame.init()
        
        WIDTH, HEIGHT = 800, 600
        BACKGROUND = (90, 90, 90)
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        manager = pygame_gui.UIManager((WIDTH, HEIGHT))

        # 1. Text that shows it is running a quiz
        quiz_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((350, 25), (100, 50)),
                                                 text='Quiz Running',
                                                 manager=manager)
        
        buttons = []
        for i in range(5):
            buttons.append(pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 200+i*75), (700, 50)),
                                                      text=' ',
                                                      manager=manager, 
                                                      object_id=ObjectID( object_id='#button')))            
        
        question_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((25, 100), (750, 50)),
                                                         text=self.questions[self.current_question].question,
                                                         manager=manager)
        
        
        running = True
        while running:
            # 2. Question
            question_label.set_text(self.questions[self.current_question].question)
            
            for i, button in enumerate(buttons):
                button.set_text(self.questions[self.current_question].select_list[i])
            
            # 4. When user presses and chooses an answer, show feedback
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        for i, button in enumerate(buttons):
                            if event.ui_element == button : 
                                print(i, "button pressed")
                        
                                if self.questions[self.current_question].answer == self.questions[self.current_question].select_list[i]:
                                    screen.fill(pygame.Color('green'))
                                    print("User selected correct answer: ", self.questions[self.current_question].select_list[i])
                                    self.rights += 1
                                else:
                                    screen.fill(pygame.Color('red'))
                                    print("User selected wrong answer: ", self.questions[self.current_question].select_list[i])
                                    self.wrongs += 1
                                    self.right_wrong_list.append(self.current_question)
                                
                                self.current_question += 1

                                pygame.display.update()
                                time.sleep(0.3)
                            if self.current_question == len(self.questions):
                                running = False
                                print(len(self.questions))
                                self.end_quiz()
                                print("quiz end")
                                return

                manager.process_events(event)
            
            screen.fill(pygame.Color('#000000'))  # Fill screen with color
            manager.update(pygame.time.Clock().tick(60))
            manager.draw_ui(screen)
            pygame.display.update()

        # Render the screen
        screen.fill(WHITE)
        manager.update(pygame.time.Clock().tick(60))
        manager.draw_ui(screen)
        pygame.display.update()

        pygame.quit()
        return

    def run_quiz_org(self):
        import pygame
        import pygame_gui
        
        pygame.init()
        
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        manager = pygame_gui.UIManager((WIDTH, HEIGHT))

        # 1. Text that shows it is running a quiz
        quiz_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((350, 25), (100, 50)),
                                                 text='Quiz Running',
                                                 manager=manager)
        running = True
        while running:
            time_delta = pygame.time.Clock().tick(60)/1000.0

            # 2. Question
            question_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((25, 100), (750, 50)),
                                                         text=self.questions[self.current_question].question,
                                                         manager=manager)
            
            # 3. 5 buttons for the selection list
            buttons = []
            button1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 200+0*75), (700, 50)),
                                                      text=self.questions[self.current_question].select_list[0],
                                                      manager=manager)
            button2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 200+1*75), (700, 50)),
                                                      text=self.questions[self.current_question].select_list[1],
                                                      manager=manager)
            button3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 200+2*75), (700, 50)),
                                                      text=self.questions[self.current_question].select_list[2],
                                                      manager=manager)
            button4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 200+3*75), (700, 50)),
                                                      text=self.questions[self.current_question].select_list[3],
                                                      manager=manager)
            button5 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 200+4*75), (700, 50)),
                                                      text=self.questions[self.current_question].select_list[4],
                                                      manager=manager)
            buttons = [button1, button2, button3, button4, button5]
            # 4. When user presses and chooses an answer, show feedback
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.USEREVENT:
                    if event.type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == button2:
                                
                                print("pressed")
                                if self.questions[self.current_question].answer == self.questions[self.current_question].select_list[i]:
                                    screen.fill(pygame.Color('green'))
                                    print("User selected correct answer: ", self.questions[self.current_question].select_list[i])
                                    self.rights += 1
                                    self.right_wrong_list.append('right')
                                else:
                                    screen.fill(pygame.Color('red'))
                                    print("User selected wrong answer: ", self.questions[self.current_question].select_list[i])
                                    self.wrongs += 1
                                    self.right_wrong_list.append('wrong')

                                pygame.display.update()
                                time.sleep(1)
                                self.current_question += 1
                                if self.current_question == len(self.questions):
                                    self.end_quiz()
                                    running = False
                                    return

                                for button in buttons:
                                    button.kill()
                                question_label.kill()

                manager.process_events(event)
            
            manager.update(time_delta)
            screen.fill(pygame.Color('#000000'))  # Fill screen with color

            manager.draw_ui(screen)
            pygame.display.update()



        # Render the screen
        screen.fill(WHITE)
        manager.update(pygame.time.Clock().tick(60))
        manager.draw_ui(screen)
        pygame.display.update()

        pygame.quit()
        return
 
    def end_quiz(self):
        print("Quiz Finished")
        print("Right answers: ", self.rights)
        print("Wrong answers: ", self.wrongs)

        for i in self.right_wrong_list:
            print("wrong word : ", self.questions[i].question, "$$ ANSWER IS : ", self.questions[i].answer)


class MultipleSelection:
    def __init__(self, question, select_list, answer, dataset):
        self.question = question
        self.select_list = select_list
        self.answer = answer
        self.dataset = dataset

    def print_all(self):
        print(f"Question: {self.question}")
        for i, option in enumerate(self.select_list, 1):
            print(f"Option {i}: {option}")
        print(f"Answer: {self.answer}")

        print("where the fuck is none")
        return

    def print_answer(self):
        print(f"Answer: {self.answer}")

    def print_wordinfo(self):
        # Find the row in the dataset where the answer is located
        row = self.dataset.loc[self.dataset['Answer'] == self.answer]
        #print(row)

def create_questions(dataset, column1, column2):
    if len(dataset) < 5:
        raise ValueError("The dataset must have at least 5 rows.")
    questions = []
    for index, row in dataset.iterrows():
        question = row[column1]
        correct_answer = row[column2]
        
        # Get a list of all possible answers
        all_answers = list(dataset[column2].values)
        
        # Remove the correct answer from the list of all answers
        all_answers.remove(correct_answer)
        
        # Randomly select 4 other answers
        other_answers = random.sample(all_answers, 4)
        
        # Combine the correct answer with the other answers
        select_list = [correct_answer] + other_answers
        
        # Randomize the order of the answers
        random.shuffle(select_list)
        
        questions.append(MultipleSelection(question, select_list, correct_answer, dataset))
    return questions

def questions_print(questions):
    for i, question in enumerate(questions, 1):
        print(f"Question {i}:")
        question.print_all()
        print("\n")

def run_quiz(dataset, col1, col2):
    # Initialize Pygame
    pygame.init()

    # Set up some constants
    WIDTH, HEIGHT = 800, 600
    BACKGROUND = (90, 90, 90)

    # Create the window and GUI manager
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    manager = pygame_gui.UIManager((WIDTH, HEIGHT))


    # Create the quiz elements
    title = pygame_gui.elements.ui_label.UILabel(relative_rect=pygame.Rect((350, 50), (100, 50)),
                                                text="Running Quiz",
                                                manager=manager)

    question_label = pygame_gui.elements.ui_label.UILabel(relative_rect=pygame.Rect((350, 150), (100, 50)),
                                                        text="",
                                                        manager=manager)

    option_buttons = [pygame_gui.elements.ui_button.UIButton(relative_rect=pygame.Rect((350, 200 + i*50), (100, 50)),
                                                            text="",
                                                            manager=manager) for i in range(5)]

    feedback_label = pygame_gui.elements.ui_label.UILabel(relative_rect=pygame.Rect((350, 450), (100, 50)),
                                                        text="",
                                                        manager=manager)

    # Load the dataset and create the questions
    questions = create_questions(dataset, col1, col2)
    questions_print(questions)

    current_question = 0

    # Game loop
    running = True
    while running:
        time_delta = pygame.time.Clock().tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    for i, button in enumerate(option_buttons):
                        if event.ui_element == button:
                            if questions[current_question].select_list[i] == questions[current_question].answer:
                                screen.fill((0, 255, 0))  # Change the background color to green
                                correct_sound.play()
                            else:
                                feedback_label.set_text(str(dataset.loc[dataset['expression'] == questions[current_question].answer]))
                            current_question += 1
                            if current_question < len(questions):
                                question_label.set_text(questions[current_question].question)
                                for i, button in enumerate(option_buttons):
                                    button.set_text(questions[current_question].select_list[i])
                            else:
                                running = False

            manager.process_events(event)

        manager.update(time_delta)

        screen.fill(BACKGROUND)
        manager.draw_ui(screen)

        pygame.display.update()

    # Quit Pygame
    pygame.quit()



mode, dataset = quiz_start()

a = Quiz(questions=create_questions(dataset, mode[0], mode[1]))

a.run_quiz()


