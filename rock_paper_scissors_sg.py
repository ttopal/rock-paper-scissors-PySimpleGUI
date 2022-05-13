import PySimpleGUI as sg   
import random as r
import time


def btn_rock_click():
    #print('Button Rock Clicked')
    plyr1.ply_choice = 'rock' 
    plyr2.ply_choice = rand_choice()
    window['-IMG1-'].Update(filename=choices[plyr1.ply_choice])
    window['-IMG2-'].Update(filename=choices[plyr2.ply_choice])
    game()
    return True    

def btn_paper_click():
    #print('Button Paper Clicked')
    plyr1.ply_choice = 'paper'
    plyr2.ply_choice = rand_choice()
    window['-IMG1-'].Update(filename=choices[plyr1.ply_choice])
    window['-IMG2-'].Update(filename=choices[plyr2.ply_choice])
    game()
    return True

def btn_scissors_click():
    #print('Button Scissors Clicked')
    plyr1.ply_choice = 'scissors' 
    plyr2.ply_choice = rand_choice()
    window['-IMG1-'].Update(filename=choices[plyr1.ply_choice])
    window['-IMG2-'].Update(filename=choices[plyr2.ply_choice])
    game()
    return True

def btn_restart():
    global plyr1
    global plyr2
    del plyr1
    del plyr2
    plyr1 = Player('Ali')
    plyr2 = Player('Computer')
    window['-SCORE1-'].Update('0')
    window['-SCORE2-'].Update('0')
    window['-MSG-'].Update(f'Ready to Start')
    window['-IMG1-'].Update(filename=choices['None'])
    window['-IMG2-'].Update(filename=choices['None'])


def rst_popup():
    winner_msg = "it is a tie" if plyr1.user_score == plyr2.user_score else ("Player1 won!" if plyr1.user_score > plyr2.user_score else "Player2 won!")
    message = "-------------------------------------------------"
    message += "\n"
    message += f"\nYour Score: {plyr1.user_score}"
    message += f"\nThe computer Score: {plyr2.user_score}"
    message += f"\nNumber of Tie games: {plyr1.tie_no}"
    message += f"\n{winner_msg}"
    message += "\n"
    message += "\n-------------------------------------------------"
    message += "\n"
    sg.Popup(message, title="Results...")




def btn_exit():
    winner_msg = "it is a tie" if plyr1.user_score == plyr2.user_score else ("Player1 won!" if plyr1.user_score > plyr2.user_score else "Player2 won!")
    message = "-------------------------------------------------"
    message += "\n"
    message += f"\nYour Score: {plyr1.user_score}"
    message += f"\nThe computer Score: {plyr2.user_score}"
    message += f"\nNumber of Tie games: {plyr1.tie_no}"
    message += f"\n{winner_msg}"
    message += "\n"
    message += "\n-------------------------------------------------"
    message += "\nThanks for playing. Please play again!"
    sg.Popup(message, title="Results...")


class Player:
    """docstring for ClassName"""
    def __init__(self, name):
        self.name = name
        self.user_score = 0
        self.tie_no = 0
        self.ply_choice = 'None'


def game():
    global plyr1
    global plyr2
    winner = winner_choice(plyr1.ply_choice, plyr2.ply_choice)
    if winner!=None:
        if winner==plyr1.ply_choice:
            plyr1.user_score += 1
            window['-SCORE1-'].Update(str(plyr1.user_score))
            window['-MSG-'].Update(f'Player1 won!')
        else:
            plyr2.user_score += 1
            window['-SCORE2-'].Update(str(plyr2.user_score))
            window['-MSG-'].Update(f'Player2 won!')
    else:
        plyr1.tie_no += 1
        plyr2.tie_no += 1
        window['-MSG-'].Update(f'It is a tie!')
    
    return True    



def rand_choice():
    options=["rock", "paper", "scissors"]
    return r.choice(options)

        
def winner_choice(chc1, chc2):
        
    winners = {
        "rock":{
            "rock": None,       # it is a tie
            "paper": "paper",   # winners["rock"]["paper"] = "paper" winner 
            "scissors": "rock", # winners["rock"]["scissors"] = "rock" winner
        },
        "paper":{
            "rock": "paper",
            "paper": None,      # it is a tie
            "scissors": "scissors",
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,   # it is a tie
        },
    }

    winner = winners[chc1][chc2]

    return winner


plyr1 = Player('Ali')
plyr2 = Player('Computer')



rock_icon = './assets/rock2.png'
paper_icon = './assets/paper2.png'
scissors_icon = './assets/scissors2.png'
player1_icon = './assets/player175.png'
player2_icon = './assets/player275.png'
vs_icon = './assets/vs15.png'
think_icon = './assets/thinking.png'

images={'player_1': './assets/player11.png', 'player_2': './assets/player2.png', 'vs': './assets/vs1.png'}
choices={'rock': './assets/rock75.png', 'paper': './assets/paper75.png', 'scissors': './assets/scissors75.png', 'None': ''}
img1=plyr1.ply_choice

sg.theme('Dark Amber')    # Add some color for fun

# 1- the layout
layout = [
            [sg.Text(text='Rock-Paper-Scissors', justification='c',pad=(0,3), font='Cambria 25 bold', expand_x=True)],  #row 1
            [
                sg.Column([[sg.T('PLAYER-1', font='Cambria 15 bold', text_color = 'red')],[sg.Image(filename=player1_icon)]], element_justification='l'), 
                sg.Image(filename=vs_icon, expand_x=True),
                sg.Column([[sg.T('PLAYER-2', font='Cambria 15 bold', text_color = 'blue')],[sg.Image(filename=player2_icon)]], element_justification='r')
            ],  #row 2
            [
                sg.Text(text='0', size=(3,0), key='-SCORE1-', font='Cambria 35 bold', background_color = 'black', justification ='c'),
                sg.Text(text='Ready to Start', key='-MSG-', font='Cambria 25', justification ='c', expand_x=True),
                sg.Text(text='0', size=(3,0), key='-SCORE2-', font='Cambria 35 bold', background_color = 'black', justification ='c'),
            ],  #row 3
            [
                sg.Image(filename=choices['None'], key='-IMG1-', pad=(10,0)),
                sg.Text(text='What is your choice :', justification='c', pad=(0,5), font='Cambria 20', expand_x=True),
                sg.Image(filename=choices['None'], key='-IMG2-', pad=(10,0))
            ],  #row 4
            [
                sg.Column([[sg.Button(image_filename=rock_icon, key='-ROCK-', expand_x=True)],[sg.T('ROCK', font='Cambria 12', justification ='c', expand_x=True)]], expand_x=True), 
                sg.Column([[sg.Button(image_filename=paper_icon, key='-PAPER-', expand_x=True)],[sg.T('PAPER', font='Cambria 12', justification ='c', expand_x=True)]], expand_x=True), 
                sg.Column([[sg.Button(image_filename=scissors_icon, key='-SCISSORS-', expand_x=True)],[sg.T('SCISSORS', font='Cambria 12', justification ='c', expand_x=True)]], expand_x=True)

            ],[sg.Push(), sg.T('', font='Cambria 10')],
            [sg.Push(), sg.Button('Exit', size=(7,1), font='Cambria 15'), sg.Button('Restart', size=(10,1), font='Cambria 15')]]

# 2 - the window
window = sg.Window('Rock-Paper-Scissors', layout, size=(700, 660))

# 3 - the event loop
while True:
    event, values = window.read()
    #print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        btn_exit()
        break
    
    if event == 'Restart':
        # Update the "output" text element to be the value of "input" element
        rst_popup()
        btn_restart()

        #window['-OUTPUT-'].update(values['-IN-'])
        # In older code you'll find it written using FindElement or Element
        # window.FindElement('-OUTPUT-').Update(values['-IN-'])
        # A shortened version of this update can be written without the ".Update"
        # window['-OUTPUT-'](values['-IN-'])     

    if event == '-ROCK-':
        btn_rock_click()

    if event == '-PAPER-':
        btn_paper_click()

    if event == '-SCISSORS-':
        btn_scissors_click()


# 4 - the close
window.close()