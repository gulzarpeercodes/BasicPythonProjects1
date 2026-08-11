print('''   
   .:'                                  `:.
  ::'                                     `::
 :: :.                                  .: ::
  `:. `:.             .             .:'  .:'
   `::. `::           !           ::' .::'
       `::.`::.    .' ! `.    .::'.::'
         `:.  `::::'':!:``::::'   ::'
         :'*:::.  .:' ! `:.  .:::*`:
        :: HHH::.   ` ! '   .::HHH ::
       ::: `H TH::.  `!'  .::HT H' :::
       ::..  `THHH:`:   :':HHHT'  ..::
       `::      `T: `. .' :T'      ::'
         `:. .   :         :   . .:'
           `::'               `::'
             :'  .`.  .  .'.  `:
             :' ::.       .:: `:
             :' `:::     :::' `:
              `.  ``     ''  .'
               :`...........':
               ` :`.     .': '
                `:  `"""'  :'    ''')

print("Welcome to Bosnia, the land of martyrs. Your mission is to liberate Bosnia.")

print("First Mission: Choose your route\nA — Take the mountain route(Longer but less guarded)\nB — Take the main road(Faster but heavily guarded)")
Route = input("Do you want to take route A or route B?\n").upper()
if Route == "A":
    print("Congratulations, You took the right route. Hard work makes Men.")
    Checkpoint = input("Second Mission: You encounter a checkpoint You have limited ammunition and need to decide what to do:\nA - Attack\nB - Sneak past\nC - Retreat\n").upper()
    if Checkpoint == "B":
        print("You made it through undetected. Continue your mission.")
        Village = input("Third Mission: Now You reached a village and met a local who is offering you information.\nA - Trust him\nB - Don't trust him\n").upper()
        if Village == "A":
            print("Congratulations, you got the information you needed.Now plan your next move.")
            Last_mission = input('''Final Mission — The Enemy Outpost\nThe villager you trusted was telling the truth. He has given you the location of the enemy outpost.\nYou look toward the hills. In the distance, you can see the outpost.\nYour commander looks at you and says:"This is it. Everything you have done has brought us here."\nThe night is quiet. Your squad waits for your order.\nA — Attack the outpost now.\nB — Wait until dawn and attack when the sun rises.\n''').upper()
            if Last_mission == "A":
                print("The order is given............Your squad moves forward under the cover of darkness.....For a moment, everything is silent.\nThen.............You say.........GO!\nYour squad charges toward the outpost.\nThe enemy retaliates . After a fierce struggle............, your flag is raised over the outpost.\nYou look around at your squad and sing the song of victory.\nThe mission is complete.\nThe journey was long, the choices were difficult, but you never gave up.\nBOSNIA IS FREE.")
            else:
                Final_choice = input("You decide to wait until dawn.\nAs the sun begins to rise, your squad prepares for the attack........\nBut the enemy has noticed your position.........The element of surprise is gone.\nYou must make one final decision:\nA — Attack anyway.\nB — Retreat and find another way").upper()
                if Final_choice == "A":
                    print('''The enemy has spotted your position, but there is no time to waste.\nYou look at your squad.........And say "We attack. Now."\nYour squad charges toward the outpost.\nThe battle is fierce, but your determination does not break. Step by step, you push forward until the enemy finally retreats.\nSilence falls over the battlefield.......\nYou look toward the outpost as your flag is raised.........You did it.\nYour mission is complete.''')
                else:
                    print("You look toward the outpost and realize the enemy is fully prepared.\nYou know that attacking now would put your entire squad at risk.\nYou Fall back!\nYour squad retreats into the mountains.\nThis was the final chance you had.You chose you lives over your dignity.\n You failed the Mission.")
        else:
            print("Sometimes trusting someone is important when you have no choice. Sorry, You failed the Mission.")
    elif Checkpoint == "A":
        print("You tried but attack is not always an option.\nYou failed the Mission.")
    else:
        print("You are a fu*king coward. You cannot even liberate your ass. You failed the Mission dumba*s. ")

else:
    print("You failed the Mission. Being smart does not make you strong.")