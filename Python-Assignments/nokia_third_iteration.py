def go_home():
    print("\nGoing back to Main Menu...")
    return "home"


def phone_book_options_menu():
    while True:
        print(""" 
--- Options ---
1. Memory in use
2. Type of view
3. Memory status
00. Home
0. Back""")

        options_choice = input("\nEnter your choice: ")

        match options_choice:
            case "1": print("\nMemory in use")
            case "2": print("\nType of view")
            case "3": print("\nMemory status")
            case "00":
                return go_home()
            case "0":
                print("\nGoing back to Phone Book...")
                   
            case _:
                print("\nInvalid choice")


def phone_book_menu():
    while True:
        print("""
--- Phone Book ---
1. Search
2. Service Nos
3. Add name
4. Erase
5. Edit
6. Copy
7. Assign tone
8. Send b'card
9. Options
10. Speed dials
11. Voice tags
00. Home
0. Back""")

        phone_book_choice = input("\nEnter your choice: ")

        match phone_book_choice:
            case "1": print("\nSearch")
            case "2": print("\nService Nos")
            case "3": print("\nAdd name")
            case "4": print("\nErase")
            case "5": print("\nEdit")
            case "6": print("\nCopy")
            case "7": print("\nAssign tone")
            case "8": print("\nSend b'card")
            case "9":
                match phone_book_options_menu():
                    case "home":
                        return "home"
            case "10": print("\nSpeed dials")
            case "11": print("\nVoice tags")
            case "00":
                return go_home()
            case "0":
                print("\nGoing back to Main Menu...")
                
            case _:
                print("\nInvalid choice")


def message_set_menu():
    while True:
        print("""
--- Set ---
1. Message centre number
2. Messages sent as
3. Messages validity
00. Home
0. Back""")

        set_choice = input("\nEnter your choice: ")

        match set_choice:
            case "1": print("\nMessage centre number")
            case "2": print("\nMessages sent as")
            case "3": print("\nMessages validity")
            case "00":
                return go_home()
            case "0":
                print("\nGoing back to Message Settings...")
                
            case _:
                print("\nInvalid choice")


def message_common_menu():
    while True:
        print("""
--- Common ---
1. Delivery reports
2. Reply via same centre
3. Character support
00. Home
0. Back""")

        common_choice = input("\nEnter your choice: ")

        match common_choice:
            case "1": print("\nDelivery reports")
            case "2": print("\nReply via same centre")
            case "3": print("\nCharacter support")
            case "00":
                return go_home()
            case "0":
                print("\nGoing back to Message Settings...")
                
            case _:
                print("\nInvalid choice")


def message_settings_menu():
    while True:
        print("""
--- Message Settings ---
1. Set
2. Common
00. Home
0. Back""")

        message_settings_choice = input("\nEnter your choice: ")

        match message_settings_choice:
            case "1":
                match message_set_menu():
                    case "home":
                        return "home"
            case "2":
                match message_common_menu():
                    case "home":
                        return "home"
            case "00":
                return go_home()
            case "0":
                print("\nGoing back to Messages...")
                
            case _:
                print("\nInvalid choice")


def messages_menu():
    while True:
        print("""
--- Messages ---
1. Write messages
2. Inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
8. Info Service
9. Voice mailbox number
10. Service command editor
00. Home
0. Back""")

        messages_choice = input("\nEnter your choice: ")

        match messages_choice:
            case "1": print("\nWrite messages")
            case "2": print("\nInbox")
            case "3": print("\nOutbox")
            case "4": print("\nPicture messages")
            case "5": print("\nTemplates")
            case "6": print("\nSmileys")
            case "7":
                match message_settings_menu():
                    case "home":
                        return "home"
            case "8": print("\nInfo Service")
            case "9": print("\nVoice mailbox number")
            case "10": print("\nService command editor")
            case "00":
                return go_home()
            case "0":
                print("\nGoing back to Main Menu...")
                
            case _:
                print("\nInvalid choice")


def call_settings_menu():
    while True:
        print("""
--- Call Settings ---
1. Automatic redial
2. Speed dialing
3. Call waiting options
4. Own number sending
5. Phone line in
6. Automatic answer
00. Home
0. Back""")

        call_settings_choice = input("\nEnter your choice: ")

        match call_settings_choice:
            case "1": print("\nAutomatic redial")
            case "2": print("\nSpeed dialing")
            case "3": print("\nCall waiting options")
            case "4": print("\nOwn number sending")
            case "5": print("\nPhone line in")
            case "6": print("\nAutomatic answer")
            case "00":
                return go_home()
            case "0":
                print("\nGoing back to Settings...")
                
            case _:
                print("\nInvalid choice")


def phone_settings_menu():
    while True:
        print("""
--- Phone Settings ---
1. Language
2. Cell info display
3. Welcome note
4. Network selection
5. Confirm SIM service actions
00. Home
0. Back""")

        phone_settings_choice = input("\nEnter your choice: ")

        match phone_settings_choice:
            case "1": print("\nLanguage")
            case "2": print("\nCell info display")
            case "3": print("\nWelcome note")
            case "4": print("\nNetwork selection")
            case "5": print("\nConfirm SIM service actions")
            case "00":
                return go_home()
            case "0":
                print("\nGoing back to Settings...")
                
            case _:
                print("\nInvalid choice")


def security_settings_menu():
    while True:
        print("""
--- Security Settings ---
1. PIN code request
2. Call barring service
3. Fixed dialling
4. Closed user group
5. Security level
6. Change access codes
00. Home
0. Back""")

        security_choice = input("\nEnter your choice: ")

        match security_choice:
            case "1": print("\nPIN code request")
            case "2": print("\nCall barring service")
            case "3": print("\nFixed dialling")
            case "4": print("\nClosed user group")
            case "5": print("\nSecurity level")
            case "6": print("\nChange access codes")
            case "00":
                return go_home()
            case "0":
                print("\nGoing back to Settings...")
                
            case _:
                print("\nInvalid choice")


def settings_menu():
    while True:
        print("""
--- Settings ---
1. Call Settings
2. Phone Settings
3. Security settings
4. Restore factory setting
00. Home
0. Back""")

        settings_choice = input("\nEnter your choice: ")

        match settings_choice:
            case "1":
                match call_settings_menu():
                    case "home":
                        return "home"
            case "2":
                match phone_settings_menu():
                    case "home":
                        return "home"
            case "3":
                match security_settings_menu():
                    case "home":
                        return "home"
            case "4": print("\nRestore factory setting")
            case "00":
                return go_home()
            case "0":
                print("\nGoing back to Main Menu...")
                
            case _:
                print("\nInvalid choice")


def music_menu():
    while True:
        print("""
--- Music ---
1. Music player
2. Radio
3. Recorder
4. Tracklist
00. Home
0. Back""")

        music_choice = input("\nEnter your choice: ")

        match music_choice:
            case "1": print("\nMusic player")
            case "2": print("\nRadio")
            case "3": print("\nRecorder")
            case "4": print("\nTracklist")
            case "00":
                return go_home()
            case "0":
                print("\nGoing back to Main Menu...")
                
            case _:
                print("\nInvalid choice")


def clock_menu():
    while True:
        print("""
--- Clock ---
1. Alarm clock
2. Clock settings
3. Date setting
4. Stopwatch
5. Countdown timer
6. Auto update date and time
00. Home
0. Back""")

        clock_choice = input("\nEnter your choice: ")

        match clock_choice:
            case "1": print("\nAlarm clock")
            case "2": print("\nClock settings")
            case "3": print("\nDate setting")
            case "4": print("\nStopwatch")
            case "5": print("\nCountdown timer")
            case "6": print("\nAuto update date and time")
            case "00":
                return go_home()
            case "0":
                print("\nGoing back to Main Menu...")
                
            case _:
                print("\nInvalid choice")


def main_menu():
    while True:
        print("""
==============================
       NOKIA 5510
==============================
1. Phone Book
2. Messages
3. Chat
4. Call Register
5. Tones
6. Settings
7. Call Divert
8. Music
9. Games
10. Calculator
11. Reminders
12. Clock
13. Profiles
14. Services
15. SIM Services""")

        main_choice = input("\nEnter your choice: ")

        match main_choice:
            case "1": phone_book_menu()
            case "2": messages_menu()
            case "3": print("\nChat")
            case "4": print("\nCall Register")
            case "5": print("\nTones")
            case "6": settings_menu()
            case "7": print("\nCall Divert")
            case "8": music_menu()
            case "9": print("\nGames")
            case "10": print("\nCalculator")
            case "11": print("\nReminders")
            case "12": clock_menu()
            case "13": print("\nProfiles")
            case "14": print("\nServices")
            case "15": print("\nSIM Services")
            case _:
                print("\nInvalid choice")


main_menu()
