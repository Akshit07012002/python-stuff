import random
import time

# GLOBAL VARIABLES
flag = 1
comp_toss = 1
player_runs = 0
comp_runs = 0
batting_done = False
bowling_done = False
overs = 0
no_of_chances = 0
no_of_chances_2 = 0


# INIT METHOD FOR REINITIALIZATION OF ALL GLOBAL VARIABLES
def initializeVar():
    global batting_done
    batting_done = False
    global bowling_done
    bowling_done = False
    global player_runs
    player_runs = 0
    global comp_runs
    comp_runs = 0
    global comp_toss
    comp_toss = 1
    global overs
    overs = 0


# CONTROLLER METHOD FOR RESULT
def result(name, balls_taken):
    global batting_done
    global player_runs
    global comp_runs
    global bowling_done
    if name == "PLAYER":
        print("\t\t#######################################################")
        print("\t\t\t\t\t\tPLAYER WON BY ", (player_runs - comp_runs), " RUNS")
        print("\t\t#######################################################")
        print("\t\t\t\t\t     STATS    ")
        print("\t\t\t\t\tCOMPUTER RUNS   :   ", comp_runs)
        print("\t\t\t\t\tPLAYER RUNS     :   ", player_runs)
        print("\t\t\t\t\tBALLS TAKEN     :   ", balls_taken)
    else:
        print("\t\t#######################################################")
        print("\t\t\t\t\t\tCOMPUTER WON BY ", (comp_runs - player_runs), " RUNS")
        print("\t\t#######################################################")
        print("\t\t\t\t\t     STATS    ")
        print("\t\t\t\t\tCOMPUTER RUNS   :   ", comp_runs)
        print("\t\t\t\t\tPLAYER RUNS     :   ", player_runs)
        print("\t\t\t\t\tBALLS TAKEN     :   ", balls_taken)


# CONTROLLER METHOD FOR PLAYER'S BOWLING
def playerBowling():
    global batting_done
    global player_runs
    global comp_runs
    global bowling_done
    global no_of_chances
    global no_of_chances_2
    bowling_done = True
    global overs
    # print(overs)

    # print(batting_done, bowling_done, player_runs, comp_runs)
    print("\t\t#######################################################")
    print("\t\t\t\t\t\t   PLAYER TO BOWL    ")
    print("\t\t#######################################################")

    lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    chances_2 = overs * 6
    no_of_chances_2 = 0

    while no_of_chances_2 < chances_2:

        bowl = int(input("\t\t\t\t\t   Enter Runs      :    "))
        comp_bat = random.choice(lst2)
        if comp_bat == bowl:
            print("\t\t\t\t\t   Computer Guess  :   ", comp_bat, "\n\t\t\t\t\t   Your Guess       :   ", bowl)
            print("\t\t#######################################################")
            print(
                "\t\t\t\t\t    !!! COMPUTER IS OUT !!! \n\t\t-------------------------------------------------------\n\t\t\t\t\t\tTOTAL RUNS  :  ",
                comp_runs)
            print("\t\t#######################################################")
            if comp_runs < player_runs:
                result("PLAYER", no_of_chances)
            break
        else:
            comp_runs = comp_runs + comp_bat
            print("\t\t\t\t\t   Your Guess      :   ", bowl, "\n\t\t\t\t\t   Computer Guess  :   ", comp_bat)
            print("\t\t\t\t\t   Computer Runs   :   ", comp_runs, "\n")

        if batting_done:
            if comp_runs > player_runs:
                result("COMPUTER", no_of_chances_2 + 1)
                break
            # elif player_runs > comp_runs:
            #     print('im here batting done')
            #     result("PLAYER", no_of_chances_2)
            #     break

        no_of_chances_2 = no_of_chances_2 + 1
    if player_runs > comp_runs and no_of_chances_2 >= chances_2:
        # print('im here batting done')
        result("PLAYER", no_of_chances)


# CONTROLLER METHOD FOR PLAYER'S BATTING
def playerBatting():
    global batting_done
    global player_runs
    global comp_runs
    global bowling_done
    global no_of_chances
    global no_of_chances_2
    # batting_done  is set to True if the player gets to bat
    batting_done = True
    global overs
    # print(overs)

    # print(batting_done, bowling_done, player_runs, comp_runs)

    print("\t\t#######################################################")
    print("\t\t\t\t\t\t   PLAYER TO BAT    ")
    print("\t\t#######################################################")

    runs_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    max_chances = overs * 6
    no_of_chances = 0

    while no_of_chances < max_chances:
        runs = int(input("\t\t\t\t\t   Enter Runs      :    "))
        comp_bowl = random.choice(runs_list)
        if runs == comp_bowl:
            print("\t\t\t\t\t   Your Guess      :   ", runs, "\n\t\t\t\t\t   Computer Guess  :   ", comp_bowl)
            print("\t\t#######################################################")
            print("\t\t\t\t\t\t!!! YOU ARE OUT !!! \n\t\t-------------------------------------------------------\n\t\t\t\t\t\tTOTAL RUNS  :  ",
                player_runs)
            print("\t\t#######################################################")
            if player_runs < comp_runs:
                result("COMPUTER", no_of_chances_2)
            break
        elif runs > 10:
            print("\t\t#######################################################")
            print("\t\t\t\t\t\t\t    ! ALERT ! \n\t\t\t\t\t     KEEP YOUR ENTRY BELOW 10")
            print("\t\t#######################################################")
            continue
        else:
            player_runs = player_runs + runs
            print("\t\t\t\t\t   Your Guess      :   ", runs, "\n\t\t\t\t\t   Computer Guess  :   ", comp_bowl)
            print("\t\t\t\t\t   Your runs now   :   ", player_runs, "\n")

        #  SECOND INNINGS CASE
        if bowling_done:
            if comp_runs < player_runs:
                result("PLAYER", no_of_chances + 1)
                break

        no_of_chances = no_of_chances + 1
    if player_runs < comp_runs and no_of_chances >= max_chances:
        # print('im here bowling done')
        result("COMPUTER", no_of_chances_2)


# CONTROLLER FOR CONDITION THAT PLAYER HAS WON THE TOSS
def playerWonToss():
    print("\t\t-------------------------------------------------------")
    print("\t\t#\t\t\t\t       PICK ONE                       #")
    print("\t\t#\t\t\t\t      0 - Batting                     #")
    print("\t\t#\t\t\t\t      1 - Bowling                     #")

    print("\t\t-------------------------------------------------------")
    res = int(input("\t\t\t\t\t   YOUR CHOICE : "))
    print("\t\t-------------------------------------------------------")

    if res == 0:
        playerBatting()
        playerBowling()
    else:
        playerBowling()
        playerBatting()


# MAIN DRIVER
class HandCricketSimulator:

    # works as a do-while loop
    while True:
        print("\t\txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("\t\t#\t\t\t     H A N D   C R I C K E T              #")
        print("\t\txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

        print("\t\t-------------------------------------------------------")
        global overs
        overs = int(input("\t\t\t\t\tNO. OF OVERS   :   "))
        print(overs)
        print("\t\t-------------------------------------------------------")

        print("\t\t#\t\t\t\t       PICK ONE                       #")
        print("\t\t#\t\t\t\t      0 - Tails                       #")
        print("\t\t#\t\t\t\t      1 - Heads                       #")

        print("\t\t-------------------------------------------------------")
        toss = int(input("\t\t\t\t\t     YOUR CHOICE   :   "))
        print("\t\t-------------------------------------------------------")

        time.sleep(1)

        # print("\n\t\t\t\t\t   !!! TOSSING THE COIN !!!\n")
        # print("\n\n")
        print("\t    -------------------- (xxx)(xxx) -----------------------")
        time.sleep(0.1)
        print("\t    -------------------- (xxx)(xxx) -----------------------")
        time.sleep(0.1)
        print("\t    -------------------- (xxx)(xxx) -----------------------")
        time.sleep(0.1)

        for x in range(0, 3):
            time.sleep(0.05)
            print("\t    ------------------   (xxx)(xxx)   ---------------------")
            time.sleep(0.05)
            print("\t    ----------------   (xxx)<<>>(xxx)   -------------------")
            time.sleep(0.05)
            print("\t    -------------   (xxx)<<<<<>>>>>(xxx)   ----------------")
            time.sleep(0.05)
            print("\t    -----------   (xxx)..............(xxx)   --------------")
            time.sleep(0.05)
            print("\t    ----------   (xxx)  TOSSING COIN  (xxx)   -------------")
            time.sleep(0.05)
            print("\t    -----------   (xxx)..............(xxx)   --------------")
            time.sleep(0.05)
            print("\t    -------------   (xxx)<<<<<>>>>>(xxx)   ----------------")
            time.sleep(0.05)
            print("\t    ----------------   (xxx)<<>>(xxx)   -------------------")
        time.sleep(0.05)
        print("\t    ------------------   (xxx)(xxx)   ---------------------")
        time.sleep(0.1)
        print("\t    ------------------   (xxx)(xxx)   ---------------------")
        time.sleep(0.1)
        print("\t    ------------------   (xxx)(xxx)   ---------------------")
        time.sleep(0.1)

        randomTossValue = int(random.randint(0, 1))

        temp = "Heads" if randomTossValue == 1 else "Tails"
        temp2 = "Heads" if toss == 1 else "Tails"

        print("\t\txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("\t\t-------------------------------------------------------")
        print("\t\t\t\t\t   TOSS RESULT    :    ", temp)
        print("\t\t\t\t\t   YOUR CHOICE    :    ", temp2)
        print("\t\t-------------------------------------------------------")

        # PLAYER WON THE TOSS
        if toss == randomTossValue:
            print("\t\t#######################################################")
            print("\t\t\t\t  CONGRATULATIONS ! YOU WON THE TOSS  :)")
            print("\t\t#######################################################")
            playerWonToss()

        #     COMPUTER WON THE TOSS
        else:
            comp_toss = int(random.randint(0, 1))
            comp_decision = "BAT" if comp_toss == 0 else "BOWL"

            print("\t\t#######################################################")
            print("\t\t\t\t     OOPS ! YOU LOSS THE TOSS  :(")
            print("\t\t-------------------------------------------------------")
            print("\t\t\t\t     COMPUTER CHOSE TO", comp_decision)

            if comp_decision == "BAT":
                playerBowling()
                playerBatting()
            else:
                playerBatting()
                playerBowling()

        if player_runs == comp_runs:
            result("TIE", 0)

        print("\t\txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("\t\t\t\t   PRESS 1 TO TOSS AGAIN, 0 TO EXIT ")
        flag = int(input("\n\t\t\t\t\tPLAY AGAIN ?   :   "))
        print("\t\t-------------------------------------------------------")
        initializeVar()
        if flag == 0:
            print("\t\t\t\t\t\t     #pythoncricket")
            break
    print("\t\txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
