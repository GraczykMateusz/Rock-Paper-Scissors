import tkinter as tk
import random as rd

class PlayerVsBot(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.ROCK = 0
        self.PAPER = 1
        self.SCISSORS = 2

        self.player_move_label = None
        self.bot_move_label = None
        
        self.background_image = tk.PhotoImage(file = '../Backgrounds/playervsbot_background.png')
        self.background = tk.Label(self, borderwidth=0, highlightthickness=0, image = self.background_image)
        self.background.place(x=0, y=0)

        self.back_button_image = tk.PhotoImage(file = '../Graphics/back_button.png')
        self.back_button = tk.Button(self, activebackground='black', image = self.back_button_image, command=lambda: controller.show_frame("Menu"))
        self.back_button.place(x=1000, y=600)

        self.rock_image = tk.PhotoImage(file = '../Graphics/rock.png')
        self.rock_button = tk.Button(self, activebackground='black', image = self.rock_image, command=lambda: self.player_makes_move(self.ROCK))
        self.rock_button.place(x=149.5, y=180)

        self.paper_image = tk.PhotoImage(file = '../Graphics/paper.png')
        self.paper_button = tk.Button(self, activebackground='black', image = self.paper_image, command=lambda: self.player_makes_move(self.PAPER))
        self.paper_button.place(x=449.5, y=180)

        self.scissors_image = tk.PhotoImage(file = '../Graphics/scissors.png')
        self.scissors_button = tk.Button(self, activebackground='black', image = self.scissors_image, command=lambda: self.player_makes_move(self.SCISSORS))
        self.scissors_button.place(x=749.5, y=180)

        self.player_score = 0
        self.player_score_label = tk.Label(self, text=self.player_score, bg='#28b4e5', fg='#023661', font=('DejaVu Serif', 38))
        self.player_score_label.place(x=710, y=505)

        self.bot_score = 0
        self.bot_score_label = tk.Label(self, text=self.bot_score, bg='#28b4e5', fg='#023661', font=('DejaVu Serif', 38))
        self.bot_score_label.place(x=615, y=580)

        self.load_comments()

    def player_makes_move(self, player_move):
        if (self.player_move_label and self.bot_move_label) is not None:
            self.player_move_label.destroy()
            self.bot_move_label.destroy()
        
        bot_move = self.bot_makes_move()

        self.set_move_labels(player_move, bot_move)

        winner = self.who_win(player_move, bot_move)

        if winner == 'PLAYER':
            self.player_score += 1

        if winner == 'BOT':
            self.bot_score += 1

        self.refresh_score()
        self.check_comment()

        self.after(2000, self.player_move_label.destroy)
        self.after(2000, self.bot_move_label.destroy)

    def bot_makes_move(self):          
        bot_move_number = rd.randrange(0,3,1)

        if bot_move_number == self.ROCK:
            return self.ROCK
        elif bot_move_number == self.PAPER:
            return self.PAPER
        elif bot_move_number == self.SCISSORS:
            return self.SCISSORS

    def set_move_labels(self, player_move, bot_move):
        if player_move == bot_move:

            if (player_move or bot_move) == self.ROCK:
                self.player_move_label = tk.Label(self, text="PLAYER", bg='#28b4e5', fg='#023661', font=('DejaVu Serif', 15))
                self.bot_move_label = tk.Label(self, text="/  BOT", bg='#28b4e5', fg='#b526ae',font=('DejaVu Serif', 15))

                self.player_move_label.place(x=160, y=150)
                self.bot_move_label.place(x=260, y=150)

            elif (player_move or bot_move) == self.PAPER:
                self.player_move_label = tk.Label(self, text="PLAYER", bg='#28b4e5', fg='#023661', font=('DejaVu Serif', 15))
                self.bot_move_label = tk.Label(self, text="/  BOT", bg='#28b4e5', fg='#b526ae',font=('DejaVu Serif', 15))

                self.player_move_label.place(x=462, y=150)
                self.bot_move_label.place(x=562, y=150)

            elif (player_move or bot_move) == self.SCISSORS:
                self.player_move_label = tk.Label(self, text="PLAYER", bg='#28b4e5', fg='#023661', font=('DejaVu Serif', 15))
                self.bot_move_label = tk.Label(self, text="/  BOT", bg='#28b4e5', fg='#b526ae',font=('DejaVu Serif', 15))

                self.player_move_label.place(x=764, y=150)
                self.bot_move_label.place(x=864, y=150)
        else:
            if player_move == self.ROCK:
                self.player_move_label = tk.Label(self, text="PLAYER", bg='#28b4e5', fg='#023661', font=('DejaVu Serif', 15))
                self.player_move_label.place(x=205, y=150)

                if bot_move == self.PAPER:
                    self.bot_move_label = tk.Label(self, text="BOT", bg='#28b4e5', fg='#b526ae',font=('DejaVu Serif', 15))
                    self.bot_move_label.place(x=523, y=150)

                elif bot_move == self.SCISSORS:
                    self.bot_move_label = tk.Label(self, text="BOT", bg='#28b4e5', fg='#b526ae',font=('DejaVu Serif', 15))
                    self.bot_move_label.place(x=825, y=150)

            elif player_move == self.PAPER:
                self.player_move_label = tk.Label(self, text="PLAYER", bg='#28b4e5', fg='#023661', font=('DejaVu Serif', 15))
                self.player_move_label.place(x=503, y=150)

                if bot_move == self.ROCK:
                    self.bot_move_label = tk.Label(self, text="BOT", bg='#28b4e5', fg='#b526ae',font=('DejaVu Serif', 15))
                    self.bot_move_label.place(x=218, y=150)

                elif bot_move == self.SCISSORS:
                    self.bot_move_label = tk.Label(self, text="BOT", bg='#28b4e5', fg='#b526ae',font=('DejaVu Serif', 15))
                    self.bot_move_label.place(x=825, y=150)

            elif player_move == self.SCISSORS:
                self.player_move_label = tk.Label(self, text="PLAYER", bg='#28b4e5', fg='#023661', font=('DejaVu Serif', 15))
                self.player_move_label.place(x=803, y=150)

                if bot_move == self.ROCK:
                    self.bot_move_label = tk.Label(self, text="BOT", bg='#28b4e5', fg='#b526ae',font=('DejaVu Serif', 15))
                    self.bot_move_label.place(x=218, y=150)

                elif bot_move == self.PAPER:
                    self.bot_move_label = tk.Label(self, text="BOT", bg='#28b4e5', fg='#b526ae',font=('DejaVu Serif', 15))
                    self.bot_move_label.place(x=523, y=150)


    def who_win(self, player_move, bot_move):
        
        '''
                            ----------------------------------------------
                            |               HOW WINS TABLE               |
        ------------------------------------------------------------------
        |   Player / Bot    |    Rock[0]   |    Paper[1]  |  Scissors[2] |   
        |-------------------|--------------|--------------|--------------|
        |        Rock[0]    |    DRAW      |    BOT       |     PLAYER   |
        |-------------------|--------------|--------------|--------------|
        |       Paper[1]    |    PLAYER    |    DRAW      |     BOT      |
        |-------------------|--------------|--------------|--------------|
        |    Scissors[2]    |    BOT       |    PLAYER    |     DRAW     |
        ------------------------------------------------------------------
        '''

        win_arr = [['DRAW',   'BOT',    'PLAYER'],
                   ['PLAYER', 'DRAW',   'BOT'   ],
                   ['BOT',    'PLAYER', 'DRAW'  ]]

        return win_arr[player_move][bot_move]

    def refresh_score(self):
        self.player_score_label = tk.Label(self, text=self.player_score, bg='#28b4e5', fg='#023661', font=('DejaVu Serif', 38))
        self.player_score_label.place(x=710, y=505)

        self.bot_score_label = tk.Label(self, text=self.bot_score, bg='#28b4e5', fg='#023661', font=('DejaVu Serif', 38))
        self.bot_score_label.place(x=615, y=580)

    def load_comments(self):
        COMMENTS_COUNT = 10
        self.comments_images = []
        self.comments_arr = []

        for i in range(0, COMMENTS_COUNT):

            path_to_image = f'../Graphics/Comments/comment{i}.png'
            self.comments_images.append(tk.PhotoImage(file = path_to_image))
            comment = tk.Label(self, borderwidth=0, highlightthickness=0, image = self.comments_images[i])

            self.comments_arr.append(comment)           

    def check_comment(self):
        if self.player_score == 5:
            self.comments_arr[0].place(x=120, y=430)
        elif self.player_score == 10:
            self.comments_arr[1].place(x=120, y=430)
        elif self.player_score == 15:
            self.comments_arr[2].place(x=120, y=430)
        elif self.player_score == 20:
            self.comments_arr[3].place(x=120, y=430)
        elif self.player_score == 25:
            self.comments_arr[4].place(x=120, y=430)
        elif self.player_score == 30:
            self.comments_arr[5].place(x=120, y=430)
        elif self.player_score == 35:
            self.comments_arr[6].place(x=120, y=430)
        elif self.player_score == 40:
            self.comments_arr[7].place(x=120, y=430)
        elif self.player_score == 45:
            self.comments_arr[8].place(x=120, y=430)
        elif self.player_score == 50:
            self.comments_arr[9].place(x=120, y=430)
    