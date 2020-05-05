import webbrowser, sys, pyperclip

sys.argv #['mapit.py'. '870', 'Valencia', 'st.']
if len(sys.argv) > 1:
    #['mapit.py'. '870', 'Valencia', 'st.'] -> '870 Valencia st.'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

#https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)

