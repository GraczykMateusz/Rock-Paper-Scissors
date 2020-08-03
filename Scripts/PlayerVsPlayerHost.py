import tkinter as tk
import threading

from Host import Host

class PlayerVsPlayerHost(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.ROCK = "0"
        self.PAPER = "1"
        self.SCISSORS = "2"

        self.host_move_label = None
        self.client_move_label = None

        self.background_image = tk.PhotoImage(file = '../Backgrounds/playervsplayer1_background.png')
        self.background = tk.Label(self, borderwidth=0, highlightthickness=0, image = self.background_image)
        self.background.place(x=0, y=0)

        self.back_button_image = tk.PhotoImage(file = '../Graphics/back_button.png')
        self.back_button = tk.Button(self, activebackground='black', image = self.back_button_image, command = lambda: controller.show_frame("HostClientPage"))
        self.back_button.place(x=1000, y=600)

        self.rock_image = tk.PhotoImage(file = '../Graphics/rock.png')
        self.rock_button = tk.Button(self, activebackground='black', image = self.rock_image, command=lambda: self.host_makes_move(self.ROCK))
        self.rock_button.place(x=149.5, y=180)

        self.paper_image = tk.PhotoImage(file = '../Graphics/paper.png')
        self.paper_button = tk.Button(self, activebackground='black', image = self.paper_image, command=lambda: self.host_makes_move(self.PAPER))
        self.paper_button.place(x=449.5, y=180)

        self.scissors_image = tk.PhotoImage(file = '../Graphics/scissors.png')
        self.scissors_button = tk.Button(self, activebackground='black', image = self.scissors_image, command=lambda: self.host_makes_move(self.SCISSORS))
        self.scissors_button.place(x=749.5, y=180)

        self.player1_score = 0
        self.player1_score_label = tk.Label(self, text=self.player1_score, bg='#28b4e5', fg='#023661', font=('DejaVu Serif', 38))
        self.player1_score_label.place(x=770, y=505)

        self.player2_score = 0
        self.player2_score_label = tk.Label(self, text=self.player2_score, bg='#28b4e5', fg='#023661', font=('DejaVu Serif', 38))
        self.player2_score_label.place(x=770, y=580)

    def host_makes_move(self, host_move):             
        self.set_move_labels(host_move, Host.msg_decoded)

    def set_move_labels(self, host_move, client_move=None):
        if (self.host_move_label and self.client_move_label) is not None:
            self.host_move_label.destroy()
            self.client_move_label.destroy()
        
        if client_move is not None:
            self.check_winner(host_move, client_move)
            Host.msg_decoded = None

            self.after(2000, self.host_move_label.destroy)
            self.after(2000, self.client_move_label.destroy)
        else:
            pass
        
    def check_winner(self, host_move, client_move):
        if host_move == client_move:
            
            if (host_move or client_move) == self.ROCK:
                self.host_move_label = tk.Label(self, text="PLAYER 1", bg='#28b4e5', fg='#023661', font=('DejaVu Serif', 15))
                self.client_move_label = tk.Label(self, text="/PLAYER 2", bg='#28b4e5', fg='#b526ae',font=('DejaVu Serif', 15))

                self.host_move_label.place(x=160, y=150)
                self.client_move_label.place(x=260, y=150)

            elif (host_move or client_move) == self.PAPER:
                self.host_move_label = tk.Label(self, text="PLAYER 1", bg='#28b4e5', fg='#023661', font=('DejaVu Serif', 15))
                self.client_move_label = tk.Label(self, text="/PLAYER 2", bg='#28b4e5', fg='#b526ae',font=('DejaVu Serif', 15))

                self.host_move_label.place(x=462, y=150)
                self.client_move_label.place(x=562, y=150)

            elif (host_move or client_move) == self.SCISSORS:
                self.host_move_label = tk.Label(self, text="PLAYER 1", bg='#28b4e5', fg='#023661', font=('DejaVu Serif', 15))
                self.client_move_label = tk.Label(self, text="/PLAYER 2", bg='#28b4e5', fg='#b526ae',font=('DejaVu Serif', 15))

                self.host_move_label.place(x=764, y=150)
                self.client_move_label.place(x=864, y=150)
        else:
            if host_move == self.ROCK:
                self.host_move_label = tk.Label(self, text="PLAYER 1", bg='#28b4e5', fg='#023661', font=('DejaVu Serif', 15))
                self.host_move_label.place(x=205, y=150)

                if client_move == self.PAPER:
                    self.client_move_label = tk.Label(self, text="PLAYER 2", bg='#28b4e5', fg='#b526ae',font=('DejaVu Serif', 15))
                    self.client_move_label.place(x=523, y=150)

                elif client_move == self.SCISSORS:
                    self.client_move_label = tk.Label(self, text="PLAYER 2", bg='#28b4e5', fg='#b526ae',font=('DejaVu Serif', 15))
                    self.client_move_label.place(x=825, y=150)

            elif host_move == self.PAPER:
                self.host_move_label = tk.Label(self, text="PLAYER 1", bg='#28b4e5', fg='#023661', font=('DejaVu Serif', 15))
                self.host_move_label.place(x=503, y=150)

                if client_move == self.ROCK:
                    self.client_move_label = tk.Label(self, text="PLAYER 2", bg='#28b4e5', fg='#b526ae',font=('DejaVu Serif', 15))
                    self.client_move_label.place(x=218, y=150)

                elif client_move == self.SCISSORS:
                    self.client_move_label = tk.Label(self, text="PLAYER 2", bg='#28b4e5', fg='#b526ae',font=('DejaVu Serif', 15))
                    self.client_move_label.place(x=825, y=150)

            elif host_move == self.SCISSORS:
                self.host_move_label = tk.Label(self, text="PLAYER 1", bg='#28b4e5', fg='#023661', font=('DejaVu Serif', 15))
                self.host_move_label.place(x=803, y=150)

                if client_move == self.ROCK:
                    self.client_move_label = tk.Label(self, text="PLAYER 2", bg='#28b4e5', fg='#b526ae',font=('DejaVu Serif', 15))
                    self.client_move_label.place(x=218, y=150)

                elif client_move == self.PAPER:
                    self.client_move_label = tk.Label(self, text="PLAYER 2", bg='#28b4e5', fg='#b526ae',font=('DejaVu Serif', 15))
                    self.client_move_label.place(x=523, y=150)