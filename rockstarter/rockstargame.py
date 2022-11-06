#This is going to be my first ever "full" game! :D
print('''Welcome to "Rockstar the Video Game" by Sharkfin!''')
command = ''
game_on = False
while command.lower() != 'q':
    print("Type 's' to start the game! Type 'help' if you ever need a hand.")
    command = input('> ')
    if command.lower() == 'help':
        print("""(!) Help Initiated.
This is an text based RPG game, be the rockstar of your dreams! As John Lennon always said: "Mama... Uuuu...".
Command list:
s       - start the game
help    - help
q       - exit the game
Please note that this is my first ever game, it's nowhere near perfect :)
- Sharkfin 2022""")
    if command.lower() == 's':
        game_on = True
        genre_ready = False
    while game_on and genre_ready == False:
        genre = ''
        print('''(!) Game Started.
Please select your music genre of choice:
(1) Rock            (Normal)
(2) Pop             (Easy)
(3) Hip-hop / Rap   (Very Easy)
(4) Metal           (Hard)
(5) Jazz            (Extreme)''')
        genre = input('> ')
        if genre == str(1):
            intro = "Not bad kid, rock ain't what it used to be. But a reliable choice till this day."
            multiplier = 1.0
            genre_ready = True
        elif genre == str(2):
            intro = "A bit too mainstream... But i won't judge you."
            multiplier = 2.0
            genre_ready = True
        elif genre == str(3):
            intro = "Picking the safest option huh?"
            multiplier = 3.0
            genre_ready = True
        elif genre == str(4):
            intro = "Great choice... if you have balls, which I doubt."
            multiplier = 0.5
            genre_ready = True
        elif genre == str(5):
            intro = "Jazz, only your grandpa listen to these kinds of music. I salute you and I wish you the best of luck."
            multiplier = 0.25
            genre_ready = True
        else:
            print("Hint: Enter a number 1-5 to choose genre.")
        while genre_ready:
            day = 1
            money = 50
            skill = 1.0
            popularity = 1.0
            print(f'''{intro} Multiplier: {multiplier}''')
            input('> Press Enter to continue. ')
            print('You signed up a contract by Abbey Roads Records.')
            while day < 327489:
                salary = 10 * popularity
                if popularity <= 1:
                    status = 'Basement Dweller'
                if popularity > 1 < 10:
                    status = 'Royalty Free Music Maker'
                if popularity >= 10 < 20:
                    status = 'Busker'
                if popularity >= 20 < 30:
                    status = "Elton John's Backup Angklungist"
                if popularity >= 30 < 40:
                    status = "BTS's Trumpet Player"
                if popularity >= 40 < 50:
                    status = "Half-a-Rockstar"
                if popularity >= 50 < 60:
                    status = "Game Music Composer"
                if popularity >= 60 < 70:
                    status = "Mozart The Sequel"
                if popularity >= 80 < 90:
                    status = "Dragonforce's Guitarist"
                if popularity > 100:
                    status = "True Rockstar"
                print("NOTE: PAYDAY EVERY 3 DAYS")
                print(f"Day:        {day}")
                print(f"Money:      ${money}")
                print(f"Skill:      {skill}")
                print(f"Popularity: {popularity}")
                print(f"Status:     {status}")
                print(f"Salary:     ${salary}")
                print("What are we doing today?")
                print("(1) Release a new album  (+ pop, - $15)")
                print("(2) Music Lessons        (+ skl, - $20)")
                print("(3) Gamble               (- $100 to + $100)")
                print("(4) Do nothing           (Skip a day, Robber Alert)")
                print("(5) Help                 (Show how to play)")
                print("(6) Quit                 (Exit the game)")
                if money < 26:
                    print("WARNING: IF YOUR MONEY GOES BELLOW 0, YOU ARE BANKRUPT")
                what_now = input("> ")
                if what_now == '1':
                    album_name = input("> Please enter your album name: ")
                    if len(album_name) > 15:
                        print("Uh, about the name... Don't you think it's too long? ( ͡° ͜ʖ ͡°)")
                        print("That's what she said anyways.")
                    elif len(album_name) < 5:
                        print("You are the type of guy to name your album " + album_name + '.')
                    else:
                        print("That'll work.")
                    pop_gain = ((skill/2) + 1) + multiplier
                    print(f"You gained {pop_gain} popularity!")
                    if pop_gain < 1.0:
                        print("Hint: Get more skills to get more popularity gain!")
                    popularity = popularity + pop_gain
                    day += 1
                    money -= 15
                    input("> Press Enter to continue. ")
                elif what_now == '2':
                    print("Welcome to Yellow Brick Road Music School!")
                    print("""What would you want to learn?
(1) Vocal
(2) Guitar
(3) Drums
(4) Piano
(5) Angklung
(6) Mayonaise""")
                    skill_get = 0
                    while skill_get == 0:
                        lesson_choice = input("> ")
                        if lesson_choice == '1':
                            skill_get = 1
                            print("Maybe singing isn't for you...")
                        elif lesson_choice == '2':
                            skill_get = 2
                            print("You'll shred Free Bird in no time!")
                        elif lesson_choice == '3':
                            skill_get = 1.5
                            print("We already have a drummer in our band...")
                        elif lesson_choice == '4':
                            skill_get = 3
                            print("Mamaaaaa... Uuuuu....")
                        elif lesson_choice == '5':
                            skill_get = 5
                            print("You absolutely killed that angklung solo!")
                        elif lesson_choice == '69':
                            skill_get = 1000
                            print("Secret cheat code activated!")
                        else:
                            print('Type 1-6 to choose music lesson')
                    skill_get = skill_get * multiplier
                    print(f"You gained {skill_get} skill points!")
                    day += 1
                    skill += skill_get
                    money -= 20
                    input("> Press Enter to continue. ")
                elif what_now == '3':
                    print("Welcome to the Ocean Man Casino!")
                    print(f"Balance: ${money}")
                    bet_check = False
                    gambling = False
                    while bet_check == False:
                        bet = input("Bet: ")
                        bet_num = bet.isnumeric()
                        if bet_num:
                            if int(bet) > 0 <= money:
                                bet_check = True
                            else:
                                print("Please enter a valid number (Must be a numeric value, and cannot be higher than balance).")
                        else:
                            print("Please enter a valid number (Must be a numeric value, and cannot be higher than balance).")
                    while gambling == False:
                        gamble = input("Choose (1) or (2): ")
                        if gamble == '1' or gamble == '2':
                            gambling = True
                        else:
                            print("Type either 1 or 2.")
                        import random
                        secret = str(random.randint(1, 2))
                        input("> Press Enter to continue. ")
                        print(f"The secret number is {secret}!")
                        if gamble == secret:
                            print(f"You have won ${bet}!")
                            money += int(bet)
                            print(f"Balance {money}")
                        if gamble != secret:
                            print(f"You have lost ${bet}")
                            money -= int(bet)
                            print(f"Balance: {money}")
                        day += 1
                        input("> Press Enter to continue. ")
                elif what_now == '4':
                    import random
                    chance = random.randint(1, 2)
                    robber = 2
                    print("You slept for 24 hours, a day has passed...")
                    day += 1
                    if chance == robber:
                        money -= 10
                        print("A robber broke in and stole $10!")
                        print(f"Balance: {money}")
                    else:
                        print("No robbers for today.")
                    input("Press Enter to continue. ")
                payday = range(0, 8970, 3)
                for paytime in payday:
                    if paytime == day:
                        money += salary
                if money < 0:
                    print("Monopoly Man came and took all of your properties, and sent you straight to jail.")
                    input("> Press Enter to continue: ")
                    break
                elif what_now == '5':
                    print("""Need some help? Got you covered!
Popularity: Indicates how popular you are, affects your status. More Popularity = More Salary
Money:      Indicates how much money you have, if you are in debt it's game over.
Skill:      Indicates how skilled you are. More skill = More popularity whilst releasing an album.
Status:     The more popularity you have, the better your status
Salary:     You will be paid this amount of money every 3 days
Gamble:     Double it or lose it. Basically it's a 50/50 roulette.
Do Nothing: Skip an entire day, with a 50/50 chance of robbers stealing money from you.""")
                    input("> Press enter if you're done reading ")
                elif what_now == '6':
                    print("Type 6 again to confirm.")
                    quitcom = input("> ")
                    if quitcom == '6':
                        quit()
                    else:
                        print("Cancelled.")
                else:
                    print("Can't understand the command.")