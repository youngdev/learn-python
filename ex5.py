# http://learnpythonthehardway.org/book/ex5.html

myName = "Matheus"
myAge = 31 # not a lie
myHeight = 90 # Quiles
myWeight = 182 # meters
myEyes = 'Brown'
myTeeh = 'White'
myHair = 'Black'

print ("Let's talk about %s." % myName)
print ("He's %d meters tall." % myHeight)
print ("He's %d quiles heavy." % myWeight)
print ("Actually that's not too heavy.")
print ("He's got $s eyes and %s hair." % myEyes, myHair)
print ("His teeth are usually %s depending on the coffee." % myTeeh)

# this line is tricky, try to get it exactly right
print ("If I add %d, %d, and %d I get %d." % (myAge, myHeight, myWeight, myAge + myHeight + myWeight))
