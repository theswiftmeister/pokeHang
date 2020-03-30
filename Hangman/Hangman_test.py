from tkinter import *
from PIL import Image, ImageTk
import random
from win32api import GetSystemMetrics


class CreateTkinterWidgets:

    def __init__(self, window, color, width=0, height=0):
        self.window = window
        self.color = color
        self.width = width
        self.height = height

    def create_frame(self):
        frame = Frame(self.window)
        frame.config(bg=self.color, width=self.width, height=self.height)
        frame.pack()
        return frame


class HangmanGame:

    def __init__(self):
        # Variables
        self.player_name = ''
        self.users = {}
        self.score = 0
        self.name_holder = []
        self.pokemon_name = ''
        self.chances_left = 5
        self.pokemon_description = {}
        self.letter_input = []
        self.button_list = []
        self.selected_gen_list = []
        self.chk_list = []
        self.game_over_popup = None
        self.high_score = None

        self.title_screen = Tk()
        self.title_screen.title('Poke-The HangMan')
        self.title_screen.geometry('600x150+650+350')
        self.title_screen.iconbitmap(r'pikachu.ico')
        self.title_screen.maxsize(600, 150)
        self.title_screen.configure(background='#212121')

        self.name_label = Label(self.title_screen, text='Enter your name')
        self.name_label.config(font=('Omega Ruby', 35), width=25, bg='#212121', fg='#14ffec')
        self.name_label.grid(row=0, column=0, )

        self.name = Entry(self.title_screen)
        self.name.config(width=20, font=('Amarante', 20), fg='#ffffff', bg='#323232', borderwidth=0)
        self.name.grid(row=1, column=0, pady=8)

        start_button = Button(self.title_screen, text='Submit', command=lambda: self.get_player_name(self.name.get()))
        start_button.config(width=10, font=('Annon', 15), bg='#212121', fg='#14ffec', borderwidth=0,
                            activebackground='#323232', activeforeground='#0d7377', )
        start_button.grid(row=2, column=0, )

        self.title_screen.mainloop()

        if len(self.player_name) > 0:
            self.main_menu_screen = Tk()
            self.main_menu_screen.title('POKE-MENU')
            # self.main_menu_screen.geometry('700x950+600+50')  # width x height + position-right + position-left
            self.main_menu_screen.geometry(
                f'{int(GetSystemMetrics(0) / 3)}x{int(GetSystemMetrics(1) - 125)}+{int(GetSystemMetrics(0)/4)}+50')

            self.main_menu_screen.iconbitmap(r'pikachu.ico')
            self.main_menu_screen.configure(background='#212121')

            # CreateTkinterWidgets(self.main_menu_screen, '#212121', 700, 100).create_frame()
            load = Image.open(r"POKEHANG1.png")
            load = load.resize((500, 275), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = Label(self.main_menu_screen, image=render)
            img.image = render
            img.configure(borderwidth=0)
            img.pack()

            name_label = Label(self.main_menu_screen, text=f'WELCOME, {self.player_name.upper()}')
            name_label.config(font=("Amarante", 27), width=20, padx=87, pady=25, wraplength=375,
                              bg='#212121',
                              fg='#14ffec')
            name_label.pack()

            new_game_button = Button(self.main_menu_screen, text='Start Game',
                                     command=self.poke_names_generator)
            new_game_button.config(font=("Omega Ruby", 25), pady=15, width=20, bg='#212121',
                                   fg='#14ffec',
                                   borderwidth=0, activebackground='#323232',
                                   activeforeground='#0d7377', )
            new_game_button.pack(fill=X)

            self.high_score_button = Button(self.main_menu_screen, text='High Score',
                                            command=self.get_high_scores)
            self.high_score_button.config(font=("Omega Ruby", 25), pady=15, width=20, bg='#212121',
                                          fg='#14ffec',
                                          borderwidth=0, activebackground='#323232',
                                          activeforeground='#0d7377')
            self.high_score_button.pack(fill=X)

            quit_game_button = Button(self.main_menu_screen, text='Quit', command=sys.exit)
            quit_game_button.config(font=("Omega Ruby", 25), pady=15, width=20, bg='#212121',
                                    fg='#14ffec',
                                    borderwidth=0, activebackground='#323232',
                                    activeforeground='#0d7377', )
            quit_game_button.pack(fill=X)

            chk_box_frame1 = CreateTkinterWidgets(self.main_menu_screen, '#212121', 700, 0).create_frame()

            self.chk1 = BooleanVar()
            chk_gen1 = Checkbutton(self.main_menu_screen, text='Gen-1', var=self.chk1, )
            chk_gen1.config(font=("Pokemon Solid", 17), bg='#212121', fg='#14ffec', activebackground='#212121',
                            activeforeground='#0d7377', selectcolor='#212121', padx=100)
            chk_gen1.pack(in_=chk_box_frame1, side=LEFT)

            self.chk2 = BooleanVar()
            chk_gen2 = Checkbutton(self.main_menu_screen, text='Gen-2', var=self.chk2)
            chk_gen2.config(font=("Pokemon Solid", 17), bg='#212121', fg='#14ffec', activebackground='#212121',
                            activeforeground='#0d7377', selectcolor='#212121', padx=100)
            chk_gen2.pack(in_=chk_box_frame1, side=LEFT)

            chk_box_frame2 = CreateTkinterWidgets(self.main_menu_screen, '#212121', 700, 0).create_frame()

            self.chk3 = BooleanVar()
            chk_gen3 = Checkbutton(self.main_menu_screen, text='Gen-3', var=self.chk3)
            chk_gen3.config(font=("Pokemon Solid", 17), bg='#212121', fg='#14ffec', activebackground='#212121',
                            activeforeground='#0d7377', selectcolor='#212121', padx=100)
            chk_gen3.pack(in_=chk_box_frame2, side=LEFT)

            self.chk4 = BooleanVar()
            chk_gen4 = Checkbutton(self.main_menu_screen, text='Gen-4', var=self.chk4)
            chk_gen4.config(font=("Pokemon Solid", 17), bg='#212121', fg='#14ffec', activebackground='#212121',
                            activeforeground='#0d7377', selectcolor='#212121', padx=100)
            chk_gen4.pack(in_=chk_box_frame2, side=LEFT)

            chk_box_frame3 = CreateTkinterWidgets(self.main_menu_screen, '#212121', 700, 0).create_frame()

            self.chk5 = BooleanVar()
            chk_gen5 = Checkbutton(self.main_menu_screen, text='Gen-5', var=self.chk5)
            chk_gen5.config(font=("Pokemon Solid", 17), bg='#212121', fg='#14ffec', activebackground='#212121',
                            activeforeground='#0d7377', selectcolor='#212121', padx=100)
            chk_gen5.pack(in_=chk_box_frame3, side=LEFT)

            self.chk6 = BooleanVar()
            chk_gen6 = Checkbutton(self.main_menu_screen, text='Gen-6', var=self.chk6)
            chk_gen6.config(font=("Pokemon Solid", 17), bg='#212121', fg='#14ffec', activebackground='#212121',
                            activeforeground='#0d7377', selectcolor='#212121', padx=100)
            chk_gen6.pack(in_=chk_box_frame3, side=LEFT)

            self.chk78 = BooleanVar()
            chk_gen78 = Checkbutton(self.main_menu_screen, text='All-Gen', var=self.chk78)
            chk_gen78.config(font=("Pokemon Solid", 17), bg='#212121', fg='#14ffec', activebackground='#212121',
                             activeforeground='#0d7377', selectcolor='#212121')
            chk_gen78.pack()

            self.main_menu_screen.mainloop()

            if len(self.name_holder) != 0:
                self.root = Tk()
                self.root.title('POKE-HANG')
                self.root.geometry(
                    f'{int(GetSystemMetrics(0)/2.8)}x{int(GetSystemMetrics(1) - 125)}'
                    f'+{int(GetSystemMetrics(0)/4)}+50')
                self.root.maxsize(700, 950)
                self.root.iconbitmap(r'pikachu.ico')
                self.root.configure(background='#212121')

                current_player_name_label = Label(self.root, text=f'Player: {self.player_name.capitalize()}')
                current_player_name_label.config(font=("Acme", 40), pady=45, justify=LEFT, bg='#212121', fg='#14ffec')
                current_player_name_label.grid(row=1, column=0, columnspan=12)

                # Chances left
                self.counter_label = Label(self.root, text=f'Chances Left: {self.chances_left}')
                self.counter_label.config(font=("Consolas", 15), justify=RIGHT, bg='#212121', fg='#14ffec')
                self.counter_label.grid(row=2, column=8, columnspan=3)

                # Points
                self.point_label = Label(self.root, text=f'Points: {self.score}')
                self.point_label.config(font=("Consolas", 15), justify=LEFT, bg='#212121', fg='#14ffec')
                self.point_label.grid(row=2, column=0, columnspan=4)

                self.selected_gen_label = Label(self.root, text=f'Gens - ')
                self.selected_gen_label.config(font=("Acme", 12), justify=LEFT, bg='#212121', fg='#14ffec')
                self.selected_gen_label.grid(row=0, column=1, columnspan=3)

                if self.chk78.get() == 1:
                    self.selected_gen_label['text'] = f'Gens- All-Gens'
                else:
                    for i in range(len(self.chk_list)):
                        if self.chk_list[i] == 1:
                            self.selected_gen_label['text'] += f'Gen-{i + 1},'

                # # Highscore of current player
                self.h_score_label = Label(self.root, text=f'')
                self.h_score_label.config(font=("Consolas", 10), justify=RIGHT, bg='#212121', fg='#14ffec')
                self.h_score_label.grid(row=0, column=9, columnspan=3)

                if len(self.users.keys()) > 0:
                    if self.player_name in self.users.keys():
                        self.h_score_label['text'] = f'Highest-score: {self.users[self.player_name]}'
                    else:
                        self.h_score_label['text'] = 'Highest-score: N/A'

                self.update_poke_description_dictionary()

                # Word Length
                self.word_length_label = Label(self.root, text=f'Word Length: {len(self.pokemon_name)}')
                self.word_length_label.config(font=("Consolas", 15), justify=CENTER, bg='#212121', fg='#14ffec')
                self.word_length_label.grid(row=2, column=4, columnspan=4)

                self.desc_label = Label(self.root, text=self.poke_description_generator())
                self.desc_label.config(font=("Acme", 25), wraplength=600, justify=LEFT, pady=45, bg='#212121',
                                       fg='#14ffec')
                self.desc_label.grid(row=6, column=0, columnspan=12)

                # Blank strings generator
                self.gaps_label = Label(self.root, text='_' * len(self.pokemon_name))
                self.gaps_label.config(font=("Alata", 40), pady=25, bg='#212121', fg='#14ffec')
                self.gaps_label.grid(row=7, column=0, columnspan=12)

                self.create_input_buttons()

                self.root.mainloop()

    def get_player_name(self, name_string):

        def check_name():
            for n in name_string:
                if n.isdigit():
                    return False

            return True

        if check_name():
            if len(name_string) < 3 or len(name_string) > 10:
                self.name_label['text'] = 'Invalid Name, at least 3-10 letters'
                self.name_label['font'] = ('Omega Ruby', 25)
                self.name_label['width'] = 36
                self.name_label['pady'] = 8
            else:
                self.player_name = name_string.lower()
                self.read_high_scores()
                self.title_screen.destroy()

        else:
            self.name_label['text'] = 'Invalid Name, alpahbets only'
            self.name_label['font'] = ('Omega Ruby', 25)
            self.name_label['width'] = 36
            self.name_label['pady'] = 8

    def poke_names_generator(self):

        self.chk_list = [self.chk1.get(), self.chk2.get(), self.chk3.get(), self.chk4.get(), self.chk5.get(),
                         self.chk6.get()]

        def check_items(l):
            return all(0 == items for items in l)

        self.name_holder.clear()
        self.selected_gen_list.clear()

        if self.chk78.get() == 1:
            with open('pokemon_desc.txt', 'r', encoding='utf-8') as file:
                for line in file.readlines():
                    line = line.split(':')
                    self.selected_gen_list.append(f'{line[0]}')
                file.close()
            self.insert_pokemon()
            self.main_menu_screen.destroy()
        elif check_items(self.chk_list):
            warn = Tk()
            warn.title('Selection error!!')
            warn.geometry('400x100+750+450')
            warn.maxsize(400, 100)
            warn.configure(bg='#212121')

            warn_frame = CreateTkinterWidgets(warn, '#212121', 400, 25).create_frame()

            warn_label = Label(warn, text='Please select atleast 1 Gen')
            warn_label.config(font=("Amarante", 17), bg='#212121', fg='#14ffec')
            warn_label.pack(in_=warn_frame)

            warn_cont_button = Button(warn, text='continue', command=warn.destroy)
            warn_cont_button.config(font=("Omega Ruby", 25), width=10, bg='#212121', fg='#14ffec',
                                    borderwidth=0, activebackground='#323232', activeforeground='#0d7377')
            warn_cont_button.pack()

            warn.mainloop()
        else:
            for i in range(len(self.chk_list)):
                if self.chk_list[i] == 1:
                    lst = []
                    with open(f'Pokemon List gen-{i + 1}.txt', 'r', encoding='utf-8') as file:
                        for line in file.readlines():
                            line = line.lower()
                            lst.append(f'{line.strip()}')
                        file.close()
                    self.selected_gen_list += lst
                    lst.clear()
            self.insert_pokemon()
            self.main_menu_screen.destroy()

    def insert_pokemon(self):
        for names in self.selected_gen_list:
            self.name_holder.append(names)
        self.pokemon_name = random.choice(self.name_holder)

    def update_poke_description_dictionary(self):

        with open('pokemon_desc.txt', 'r', encoding='utf-8') as file:
            for line in file.readlines():
                line = line.split(':')
                self.pokemon_description[f'{line[0]}'] = f'{line[1].lower().strip()}'
            file.close()

    def poke_description_generator(self):
        description = self.pokemon_description[self.pokemon_name]
        if self.pokemon_name in description:
            description = description.replace(self.pokemon_name, 'pokemon')
        description = description.split('.')
        description = '. '.join([x.strip().capitalize() for x in description])
        return description

    def guess_counter(self):
        self.chances_left -= 1
        return self.chances_left

    def check_input(self, letter):
        gaps_string = self.gaps_label.cget('text')
        if letter not in self.letter_input:
            self.letter_input.append(letter)
            for button in self.button_list:
                if letter.upper() == button['text']:
                    button['state'] = DISABLED

            if letter in self.pokemon_name:
                for i in range(len(self.pokemon_name)):
                    if letter == self.pokemon_name[i]:
                        gaps_string = list(gaps_string)
                        gaps_string[i] = letter.upper()
                    self.gaps_label['text'] = ''.join(gaps_string)
                self.word_checker()
            else:
                if self.chances_left > 0:
                    remaining_chances = self.guess_counter()
                    self.counter_label['text'] = f'Chances Left: {remaining_chances}'
                else:
                    self.on_game_over()
        # Console INFO-------------------------------------------------------------------------------#####
        for item in [self.player_name, self.pokemon_name, self.pokemon_description[self.pokemon_name],
                     self.users, len(self.letter_input), len(self.name_holder)]:
            print(item)
        # Console INFO-------------------------------------------------------------------------------#####

    def next_ques(self):

        for button in self.button_list:
            button.config(state=NORMAL)

        self.chances_left = 5
        self.counter_label['text'] = f'Chances Left: {self.chances_left}'
        self.score += 1
        self.point_label['text'] = f'Points: {self.score}'
        self.pokemon_name = random.choice(self.name_holder)
        self.gaps_label['text'] = '_' * len(self.pokemon_name)
        self.word_length_label['text'] = f'Word Length: {len(self.pokemon_name)}'
        self.desc_label['text'] = self.poke_description_generator()
        self.letter_input.clear()
        if self.pokemon_name in self.desc_label['text']:
            description = self.desc_label['text'].replace(self.pokemon_name, 'pokemon')
            self.desc_label['text'] = description.capitalize()

    def word_checker(self):
        if self.gaps_label['text'] == self.pokemon_name.upper():
            self.name_holder.remove(self.pokemon_name)
            self.next_ques()

    def restart(self):

        self.game_over_popup.destroy()

        for button in self.button_list:
            button.config(state=NORMAL)

        self.name_holder.clear()
        self.insert_pokemon()
        self.chances_left = 5
        self.counter_label['text'] = f'Chances Left: {self.chances_left}'
        self.score = 0
        self.point_label['text'] = f'Points: {self.score}'
        self.pokemon_name = random.choice(self.name_holder)
        self.gaps_label['text'] = '_' * len(self.pokemon_name)
        self.word_length_label['text'] = f'Word Length: {len(self.pokemon_name)}'
        self.desc_label['text'] = self.pokemon_description[self.pokemon_name]
        self.letter_input.clear()
        self.desc_label['text'] = self.pokemon_description[self.pokemon_name].lower()
        if self.pokemon_name in self.desc_label['text']:
            description = self.desc_label['text'].replace(self.pokemon_name, 'pokemon')
            self.desc_label['text'] = description.capitalize()

        if self.player_name in self.users.keys():
            self.h_score_label['text'] = f'Highest-score: {self.users[self.player_name]}'
        else:
            self.h_score_label['text'] = 'Highest-score: N/A'

    def on_game_over(self):
        self.save_high_scores()
        self.read_high_scores()

        self.game_over_popup = Toplevel()
        self.game_over_popup.title('GAMEOVER')
        self.game_over_popup.geometry(
                f'{int(GetSystemMetrics(0) / 3)}x{int(GetSystemMetrics(1) - 125)}+{int(GetSystemMetrics(0)/4)}+50')
        self.game_over_popup.maxsize(700, 950)
        self.game_over_popup.maxsize(700, 950)
        self.game_over_popup.configure(background='#212121')
        self.game_over_popup.iconbitmap(r'pikachu.ico')

        CreateTkinterWidgets(self.game_over_popup, '#212121', 700, 45).create_frame()

        game_over_label = Label(self.game_over_popup, text='GameOver')
        game_over_label.config(font=("Omega Ruby", 50), bg='#212121', fg='#14ffec', )
        game_over_label.pack()

        CreateTkinterWidgets(self.game_over_popup, '#212121', 700, 45).create_frame()

        wrong_guessed_ans = Label(self.game_over_popup, text='answer:')
        wrong_guessed_ans.config(font=("Omega Ruby", 25), bg='#212121', fg='#14ffec', )
        wrong_guessed_ans.pack()

        wrong_guessed_name = Label(self.game_over_popup, text=f'{self.pokemon_name.capitalize()}')
        wrong_guessed_name.config(font=("Acme", 35), width=17, pady=25, bg='#212121', fg='#14ffec')
        wrong_guessed_name.pack()

        CreateTkinterWidgets(self.game_over_popup, '#212121', 700, 45).create_frame()

        restart_game_name = Label(self.game_over_popup, text='Restart Game?')
        restart_game_name.config(font=("Omega Ruby", 25), pady=10, bg='#212121', fg='#14ffec')
        restart_game_name.pack()

        restart_game = Button(self.game_over_popup, text='Restart', command=self.restart)
        restart_game.config(font=("Omega Ruby", 25), width=10, bg='#212121', fg='#14ffec',
                            borderwidth=0, activebackground='#323232', activeforeground='#0d7377')
        restart_game.pack(fill=X)

        CreateTkinterWidgets(self.game_over_popup, '#212121', 700, 35).create_frame()

        new_game_name = Label(self.game_over_popup, text='Start again with new name')
        new_game_name.config(font=("Omega Ruby", 25), pady=10, bg='#212121', fg='#14ffec')
        new_game_name.pack()

        new_game = Button(self.game_over_popup, text='New Game', command=self.start_new_game)
        new_game.config(font=("Omega Ruby", 25), width=10, bg='#212121', fg='#14ffec',
                        borderwidth=0, activebackground='#323232', activeforeground='#0d7377')
        new_game.pack(fill=X)

        CreateTkinterWidgets(self.game_over_popup, '#212121', 700, 35).create_frame()

        quit_game_name = Label(self.game_over_popup, text='Quit to Windows?')
        quit_game_name.config(font=("Omega Ruby", 25), pady=10, bg='#212121', fg='#14ffec')
        quit_game_name.pack()

        quit_game = Button(self.game_over_popup, text='Quit', command=sys.exit)
        quit_game.config(font=("Omega Ruby", 25), width=10, bg='#212121', fg='#14ffec',
                         borderwidth=0, activebackground='#323232', activeforeground='#0d7377')
        quit_game.pack(fill=X)

        for button in self.button_list:
            button.config(state=DISABLED)

        self.game_over_popup.mainloop()

    def start_new_game(self):
        self.game_over_popup.destroy()
        self.root.destroy()
        self.__init__()

    def create_input_buttons(self):
        # Button variables
        b_blank0 = Button(self.root, text=' ', )
        b_blank1 = Button(self.root, text=' ', )
        b_blank2 = Button(self.root, text=' ', )

        b_q = Button(self.root, text='Q', command=lambda: self.check_input('q'))
        b_w = Button(self.root, text='W', command=lambda: self.check_input('w'))
        b_e = Button(self.root, text='E', command=lambda: self.check_input('e'))
        b_r = Button(self.root, text='R', command=lambda: self.check_input('r'))
        b_t = Button(self.root, text='T', command=lambda: self.check_input('t'))
        b_y = Button(self.root, text='Y', command=lambda: self.check_input('y'))
        b_u = Button(self.root, text='U', command=lambda: self.check_input('u'))
        b_i = Button(self.root, text='I', command=lambda: self.check_input('i'))
        b_o = Button(self.root, text='O', command=lambda: self.check_input('o'))
        b_p = Button(self.root, text='P', command=lambda: self.check_input('p'))

        b_a = Button(self.root, text='A', command=lambda: self.check_input('a'))
        b_s = Button(self.root, text='S', command=lambda: self.check_input('s'))
        b_d = Button(self.root, text='D', command=lambda: self.check_input('d'))
        b_f = Button(self.root, text='F', command=lambda: self.check_input('f'))
        b_g = Button(self.root, text='G', command=lambda: self.check_input('g'))
        b_h = Button(self.root, text='H', command=lambda: self.check_input('h'))
        b_j = Button(self.root, text='J', command=lambda: self.check_input('j'))
        b_k = Button(self.root, text='K', command=lambda: self.check_input('k'))
        b_l = Button(self.root, text='L', command=lambda: self.check_input('l'))

        b_z = Button(self.root, text='Z', command=lambda: self.check_input('z'))
        b_x = Button(self.root, text='X', command=lambda: self.check_input('x'))
        b_c = Button(self.root, text='C', command=lambda: self.check_input('c'))
        b_v = Button(self.root, text='V', command=lambda: self.check_input('v'))
        b_b = Button(self.root, text='B', command=lambda: self.check_input('b'))
        b_n = Button(self.root, text='N', command=lambda: self.check_input('n'))
        b_m = Button(self.root, text='M', command=lambda: self.check_input('m'))
        b_hypen = Button(self.root, text='-', command=lambda: self.check_input('-'))

        # Button variables grids

        b_q.grid(row=8, column=1)
        b_w.grid(row=8, column=2)
        b_e.grid(row=8, column=3)
        b_r.grid(row=8, column=4)
        b_t.grid(row=8, column=5)
        b_y.grid(row=8, column=6)
        b_u.grid(row=8, column=7)
        b_i.grid(row=8, column=8)
        b_o.grid(row=8, column=9)
        b_p.grid(row=8, column=10)

        b_a.grid(row=9, column=1, )
        b_s.grid(row=9, column=2, )
        b_d.grid(row=9, column=3, )
        b_f.grid(row=9, column=4, )
        b_g.grid(row=9, column=5, )
        b_h.grid(row=9, column=6, )
        b_j.grid(row=9, column=7, )
        b_k.grid(row=9, column=8)
        b_l.grid(row=9, column=9, )
        b_blank0.grid(row=9, column=10)

        b_z.grid(row=10, column=1, )
        b_x.grid(row=10, column=2, )
        b_c.grid(row=10, column=3, )
        b_v.grid(row=10, column=4, )
        b_b.grid(row=10, column=5, )
        b_n.grid(row=10, column=6, )
        b_m.grid(row=10, column=7, )
        b_hypen.grid(row=10, column=8, )
        b_blank1.grid(row=10, column=9)
        b_blank2.grid(row=10, column=10)

        # Button config
        self.button_list = [b_a, b_b, b_c, b_d, b_e, b_f, b_g, b_h, b_hypen,
                            b_i, b_j, b_k, b_l, b_m, b_n, b_o, b_p, b_q, b_r,
                            b_s, b_t, b_u, b_v, b_w, b_x, b_y, b_z, b_blank0, b_blank1, b_blank2]

        for buttons in self.button_list:
            buttons.config(font=("Consolas", 20), width=4, bg='#212121', fg='#14ffec',
                           borderwidth=0, activebackground='#323232', activeforeground='#0d7377')

        for buttons in [b_blank0, b_blank1, b_blank2]:
            buttons.config(state=DISABLED)

        def key_down(e):
            self.check_input(e.char)
            print(e.char)

        self.root.bind("<KeyPress>", key_down)

    def get_high_scores(self):
        self.high_score = Toplevel()
        self.high_score.title('HIGH-SCORES')
        self.high_score.configure(background='#212121')

        if len(self.users.keys()) > 0:
            self.high_score.geometry(
                f'{len(max(self.users.keys())) * 75}x{len(self.users.keys()) * 100}')
        else:
            self.high_score.geometry()

        self.high_score.minsize(300, 200)
        self.high_score.maxsize(5 * 75, 1080)
        self.high_score.iconbitmap(r'C:\Users\User\Desktop\JavaScript\Django\Hangman\pikachu.ico')

        v_list = sorted([v for v in self.users.values()], reverse=True)
        temp = []
        if len(v_list) > 10:
            for i in range(10):
                for k, v in self.users.items():
                    if v_list[i] in v and k not in temp:
                        temp.append(f'{k}')
        else:
            for i in range(len(v_list)):
                for k, v in self.users.items():
                    if v_list[i] in v and k not in temp:
                        temp.append(f'{k}')

        label = Label(self.high_score, text='HIGH-SCORES')
        label.config(font=("Pokemon Hollow", 25), bg='#212121', fg='#14ffec')
        label.pack()

        for i in temp:
            player_name_label = Label(self.high_score, text=f"{i} {' ' * (30 - len(i) + 12 - len(i))}{self.users[i]}")
            player_name_label.config(font=("Omega Ruby", 20), width=20, bg='#212121', fg='#14ffec')
            player_name_label.pack(expand=True)

        self.high_score.mainloop()

    def read_high_scores(self):
        with open('highscore.txt', 'r') as file:
            for line in file.readlines():
                line = line.split(',')
                self.users[line[0]] = line[1].strip()
            file.close()
        print(self.users)

    def save_high_scores(self):
        if self.player_name not in self.users.keys():
            self.users[self.player_name] = self.score
        else:
            if self.score > int(self.users[self.player_name]):
                self.users[self.player_name] = self.score

        with open('highscore.txt', 'w') as file:
            for k, v in self.users.items():
                file.write(f'{k},{v}\n')
            file.close()


g = HangmanGame()
