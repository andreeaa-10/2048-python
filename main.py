import random
import json
from pynput import keyboard
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.window import Window
import os
import numpy as np

Window.size = (360, 640)

TILE_SIZE = 100
GRID_SIZE = 4
INITIAL_TILES = 2

TILE_COLORS = {
    0: (175/255, 242/255, 213/255, 1),
    2: (175/255, 237/255, 242/255, 1),
    4: (175/255, 204/255, 242/255, 1),
    8: (180/255, 175/255, 242/255, 1),
    16: (213/255, 175/255, 242/255, 1),
    32: (242/255, 175/255, 237/255, 1),
    64: (175/255, 242/255, 213/255, 1),
    128: (175/255, 237/255, 242/255, 1),
    256: (175/255, 204/255, 242/255, 1),
    512: (180/255, 175/255, 242/255, 1),
    1024: (213/255, 175/255, 242/255, 1),
    2048: (242/255, 175/255, 237/255, 1)
}

TEXT_COLORS = {
    0: (0, 0, 0, 1),
    2: (0, 0, 0, 1),
    4: (0, 0, 0, 1),
    8: (0, 0, 0, 1),
    16: (0, 0, 0, 1),
    32: (0, 0, 0, 1),
    64: (0, 0, 0, 1),
    128: (0, 0, 0, 1),
    256: (0, 0, 0, 1),
    512: (0, 0, 0, 1),
    1024: (0, 0, 0, 1),
    2048: (0, 0, 0, 1),
}

class Login(Screen):
    def load_accounts(self):
        try:
            with open('accounts.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_accounts(accounts):
        with open('accounts.json', 'w') as file:
            json.dump(accounts, file, indent=4)

    def do_login(self, loginText, passwordText):
        app = App.get_running_app()
        app.username = loginText
        app.password = passwordText

        accounts = self.load_accounts()
        if accounts.get(app.username) == app.password:
            self.manager.transition.direction = 'left'
            self.manager.current = 'menu'
        else:
            print("Username sau parolă greșită!")

    def go_to_create_account(self):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'create_account'

class LoginApp(App):
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):
        manager = ScreenManager()
        manager.add_widget(Login(name='login'))
        manager.add_widget(CreateAccount(name='create_account'))
        manager.add_widget(Menu(name='menu'))
        manager.add_widget(Game(name='game'))
        manager.add_widget(GameResume(name='resume'))

        return manager

    def get_application_config(self):
        if(not self.username):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.isdir(conf_directory)):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config('%s/config.cfg' % conf_directory)

class CreateAccount(Screen):
    def create_account(self, username, password):
        accounts = self.load_accounts()
        if username in accounts:
            print("Account already exists!")
        else:
            accounts[username] = password
            self.save_accounts(accounts)
            print(f"Account for {username} created successfully!")

    def load_accounts(self):
        try:
            with open('accounts.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_accounts(self, accounts):
        with open('accounts.json', 'w') as file:
            json.dump(accounts, file, indent=4)

class Tile(Button):
    def __init__(self, value=0, **kwargs):
        super().__init__(**kwargs)
        self.value = value
        self.update_style()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self.update_style()

    def update_style(self):
        self.text = str(self.value) if self.value != 0 else ""
        self.background_color = TILE_COLORS.get(self.value, (1, 1, 1, 1))
        self.color = TEXT_COLORS.get(self.value, (0, 0, 0, 1))
        self.font_name = "fonts/font_3.ttf"
        self.font_size = 30

class Game(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.top_bar = BoxLayout(size_hint_y=0.1)
        self.grid_layout = GridLayout(cols=GRID_SIZE, size_hint_y=0.8)
        self.bottom_bar = BoxLayout(size_hint_y=0.1)

        self.score_label = Label(text="Score", font_size=30, font_name="fonts/font_3.ttf")
        self.top_bar.add_widget(self.score_label)

        self.restart_button = Button(
            text="Restart",
            font_size=20,
            font_name="fonts/font_3.ttf",
            background_color=(175 / 255, 242 / 255, 213 / 255, 1),
            size_hint_x=None,
            width=100
        )
        self.restart_button.bind(on_press=self.restart_game)
        self.top_bar.add_widget(self.restart_button)

        self.quit_button = Button(
            text="Quit",
            font_size=20,
            font_name="fonts/font_3.ttf",
            background_color=(242 / 255, 175 / 255, 175 / 255, 1),
            size_hint_x=None,
            width=100
        )
        self.quit_button.bind(on_press=self.quit_game)
        self.top_bar.add_widget(self.quit_button)

        self.menu_button = Button(
            text="Menu",
            font_size=20,
            font_name="fonts/font_3.ttf",
            background_color=(242 / 255, 175 / 255, 175 / 255, 1),
            size_hint_x=None,
            width=100
        )
        self.menu_button.bind(on_press=self.save_game)
        self.top_bar.add_widget(self.menu_button)

        self.tiles = [[Tile(value=0) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        for row in self.tiles:
            for tile in row:
                self.grid_layout.add_widget(tile)

        self.left_button = Button(text="Left", font_size=20, font_name="fonts/font_3.ttf", background_color=(175/255, 237/255, 242/255, 1))
        self.right_button = Button(text="Right", font_size=20, font_name="fonts/font_3.ttf", background_color=(175/255, 237/255, 242/255, 1))
        self.up_button = Button(text="Up", font_size=20, font_name="fonts/font_3.ttf", background_color=(175/255, 237/255, 242/255, 1))
        self.down_button = Button(text="Down", font_size=20, font_name="fonts/font_3.ttf", background_color=(175/255, 237/255, 242/255, 1))

        self.left_button.bind(on_press=self.left)
        self.right_button.bind(on_press=self.right)
        self.up_button.bind(on_press=self.up)
        self.down_button.bind(on_press=self.down)

        self.bottom_bar.add_widget(self.left_button)
        self.bottom_bar.add_widget(self.right_button)
        self.bottom_bar.add_widget(self.up_button)
        self.bottom_bar.add_widget(self.down_button)

        self.layout.add_widget(self.top_bar)
        self.layout.add_widget(self.grid_layout)
        self.layout.add_widget(self.bottom_bar)
        self.add_widget(self.layout)

        self.board = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
        self.score = 0
        self.init_board()

    def init_board(self):
        self.board = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
        self.score = 0
        self.update_tiles()
        self.add_random_tile()
        self.add_random_tile()

    def update_tiles(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                self.tiles[i][j].value = self.board[i, j]
        self.score_label.text = f"Score: {self.score}"

    def add_random_tile(self):
        empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if self.board[i, j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.board[i, j] = 2 if random.random() < 0.9 else 4
            self.update_tiles()

    def compress(self):
        new_matrix = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
        for i in range(GRID_SIZE):
            pos = 0
            for j in range(GRID_SIZE):
                if self.board[i][j] != 0:
                    new_matrix[i][pos] = self.board[i][j]
                    pos += 1
        self.board = np.array(new_matrix)

    def merge(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE - 1):
                if self.board[i][j] == self.board[i][j + 1] and self.board[i][j] != 0:
                    self.board[i][j] *= 2
                    self.score += self.board[i][j]
                    self.board[i][j + 1] = 0

    def reverse(self):
        self.board = np.fliplr(self.board)

    def transpose(self):
        self.board = self.board.T

    def check_empty_cells(self):
        return np.count_nonzero(self.board == 0) != 0

    def game_state(self):
        mat = self.board
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if mat[i][j] == 2048:
                    return 'WON'
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if j < GRID_SIZE - 1 and mat[i][j] == mat[i][j + 1]:
                    return 'GAME NOT OVER'
                if i < GRID_SIZE - 1 and mat[i][j] == mat[i + 1][j]:
                    return 'GAME NOT OVER'
        for k in range(GRID_SIZE):
            if k < GRID_SIZE - 1 and mat[k][0] == mat[k + 1][0]:
                return 'GAME NOT OVER'
            if k < GRID_SIZE - 1 and mat[0][k] == mat[0][k + 1]:
                return 'GAME NOT OVER'
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if mat[i][j] == 0:
                    return 'GAME NOT OVER'
        return 'LOST'

    def check_game_state(self):
        result = self.game_state()
        if result == 'WON':
            print("Congratulations! You won!")
        elif result == 'LOST':
            print("Game Over!")

    def left(self, instance=None, keycode=None):
        self.compress()
        self.merge()
        self.compress()
        self.add_random_tile()
        self.update_tiles()
        self.check_game_state()

    def right(self, instance=None, keycode=None):
        self.reverse()
        self.compress()
        self.merge()
        self.compress()
        self.reverse()
        self.add_random_tile()
        self.update_tiles()
        self.check_game_state()

    def up(self, instance=None, keycode=None):
        self.transpose()
        self.compress()
        self.merge()
        self.compress()
        self.transpose()
        self.add_random_tile()
        self.update_tiles()
        self.check_game_state()

    def down(self, instance=None, keycode=None):
        self.transpose()
        self.reverse()
        self.compress()
        self.merge()
        self.compress()
        self.reverse()
        self.transpose()
        self.add_random_tile()
        self.update_tiles()
        self.check_game_state()

    def save_game(self, event=None):
        game_data = {
            'board': [[int(cell) if isinstance(cell, np.int64) else cell for cell in row] for row in
                      self.board.tolist()],
            'score': int(self.score)
        }

        with open('save.json', 'w') as f:
            json.dump(game_data, f)

        self.manager.current = 'menu'

    def load_game(self):
        try:
            with open('save.json', 'r') as f:
                game_data = json.load(f)
            self.board = np.array(game_data['board'])
            self.score = game_data['score']
            self.update_tiles()
        except FileNotFoundError:
            print("No saved game found.")
        self.update_tiles()

    def restart_game(self):
        self.init_board()
        print("Game restarted!")

    def quit_game(self):
        App.get_running_app().stop()

class ScreenManagement(ScreenManager):
    pass

class Menu(Screen):
    def load_game(self):
        app = App.get_running_app()
        game_screen = app.root.get_screen('game')
        game_screen.load_game()
        self.manager.current = 'game'

class GameResume(Screen):
    pass

if __name__ == '__main__':
    LoginApp().run()