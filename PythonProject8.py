import random
# Health
monsterHealth = 100
playerHealth = 100
# Damage
punchDmg = 5
swordDmg = 10
fireballDmg = 30


print  "A monster is approaching, prepare to fight!"
print "------------------------------------------------------------------"
print "Press 1 to punch, 2 to use your sword, and 3 to throw a fireball"
print "------------------------------------------------------------------"
a = True

while(a):
    damageByMonster = random.randint(1,35)
    userInput = int(raw_input())
    
    if userInput == 1:
        monsterHealth = monsterHealth - punchDmg
        print "You have damaged the monster with your fists, he has lost 5 health!"

    if userInput == 2:
        monsterHealth = monsterHealth - swordDmg
        print "You have damaged the monster with your sword, he has lost 10 health!"

    if userInput == 3:
        monsterHealth = monsterHealth - fireballDmg
        print "You have damaged the monster with a fireball, he has lost 30 health!"
        
    playerHealth = playerHealth - damageByMonster
    print "------------------------------------------------------------------"
    print "The monster has caused " + str(damageByMonster) + " damage"
    print "------------------------------------------------------------------"
    print "The monster's health is: " + str(monsterHealth)
    print "Your health is: " + str(playerHealth)
    print "Press 1 to punch, 2 to use sword, and 3 to throw fireball"
    print "------------------------------------------------------------------"
    if playerHealth <= 0:
        print "The fight is over! You have been defeated!"
        a = False
    if monsterHealth <= 0:
        print "The fight is over! You defeated the monster!!!"
        a = False