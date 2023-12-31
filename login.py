"""
Module for the Login Screen GUI and start of the application.
"""

import PySimpleGUI as sg

import home_screen.home as home

def make_login():
    """
    Create and display the login screen for the application.

    This function creates the login screen GUI, allowing users to enter a username and password.
    It checks the entered credentials against a hardcoded dictionary of usernames and passwords.
    If the credentials are valid, it opens the home screen; otherwise, it displays an error message.

    Parameters:
        None

    Returns:
        None
    """
    
    sg.theme('DarkGrey5')

    # Set the default font for the GUI
    title = ("Century Gothic", 18)
    sg.set_options(font=('Century Gothic', 10))
    
    # Hardcoded login credentials (username: password)
    credentials = {
        'user1': 'password123',
        'user2': 'password123',
        'user3': 'password123'
    }    

    layout = [
        [sg.T("Login", font=title)],
        [sg.HSeparator(pad=(70, (10, 40)))],
        [sg.Text("Username:"), sg.Input(key='-USERNAME-', size=(18,1))],
        [sg.Text("Password:"), sg.Input(key='-PASSWORD-', password_char='•', size=(18,1))],
        [sg.Text(size=(40,1), key='-OUTPUT-', pad=(0, 30), justification='c')],
        [sg.Button('Submit', key='-LOGIN-'), sg.Button('Quit')]
    ]

    window = sg.Window('Login screen', layout, size=(400, 300), element_justification='c', margins=(0, 20))
    
    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            window.close()
            break
        if event == '-LOGIN-':
            username = values['-USERNAME-']
            password = values['-PASSWORD-']
            # Check if the entered credentials are in the dictionary
            if username in credentials and credentials[username] == password:
                window.close()
                # Run the home screen GUI
                home.main()
                break
            else:
                window['-OUTPUT-'].update('Error: Invalid credentials')

    window.close()

if __name__ == '__main__':
    make_login()
    
