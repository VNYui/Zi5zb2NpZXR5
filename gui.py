from PyInquirer import style_from_dict, Token, Separator, prompt

from rich.console import Console
import time
import progressbar
import nmap3
from nested_lookup import nested_lookup
import scanner
import manager
import toolkit
import server
import threading
#MODELS :

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

INPUT_HOST = [
    {
        'type': 'input',
        'name': 'host',
        'message': 'Enter single/multiple target adress (IPV4/WWW) :',
        #'validate': Ip_Validator,
        'default': 'scanme.nmap.org',
    }
]



MODE = [
    {
        'type': 'checkbox',
        'message': 'Attack mode :\n',
        'name': 'toppings',
        'choices': [
            {
                'name' : 'IA',
            },
            {
                'name' : 'MANUAL',
            },
            {
                'name' : 'LOAD'
            },
        ],
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 0 else True
    }
]

INPUT_ARGS = [
    {
        'type': 'input',
        'name': 'args',
        'message': 'Enter nmap command',
        #'validate': Ip_Validator,
        'default': '-Sn -P22-243',
    }
]

def screen1():
    global console
    console = Console()
    console.print("""
        .o88o.                               o8o                .
        888 `"                               `"'              .o8
       o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.  .o888oo oooo    ooo
        888    d88(  "8 d88' `88b d88' `"Y8 `888  d88' `88b   888    `88.  .8'
        888    `"Y88b.  888   888 888        888  888ooo888   888     `88..8'
        888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    `888'
       o888o   8""888P' `Y8bod8P' `Y8bod8P' o888o `Y8bod8P'   "888"      d8'
                                                                    .o...P' """, style="bold red")
    return console

def screen2():
    global h
    h = dict()
    h_in = prompt(INPUT_HOST)
    h = h_in.copy()
    for v in h.values():
        h = v
        return h

def screen3():
    global m
    m = dict()
    m_in = prompt(MODE)
    for v in m_in.values():
        m = v
        return m

def screen4():
    started_IA = False
    if 'IA' in m:
        console.print('Starting IA...', style='bold red')
        t1 = threading.Thread(target=server.run)
        t1.start()
        toolkit.main(h)
        scanner.main(h,m)
    elif 'MANUAL' in m:
        screen5()
    elif 'LOAD' in m:
        manager.restore()

def screen5():
    global a
    a = dict()
    a_in = prompt(INPUT_ARGS)
    for v in a.values():
        a = v
        console.print(a)

def main():
    #RUN
        screen1()
        screen2()
        screen3()
        screen4()
        #debug_screen()
if __name__ == '__main__':
    main()
