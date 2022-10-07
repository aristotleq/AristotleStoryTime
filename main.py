#Title
print("~ Tales of Sir Elif ~")
print("A fictional medieval story")
print()
# Intro medieval story for user
print("You are a knight in the year 650 CE, and you are trying to become the most legendary knight of them all!")
print()
print("You decide to go on a quest at Castle Python to earn your glory! ")
print()
print("You are outside the castle grounds, and see three different people asking for help. You could talk to: ")
print("  A. The local blacksmith, who needs a rare sword")
print("  B. The town's teacher, who has a question")
print("  C. The king, who needs a brave warrior")
userTalk = input("Who will you talk to? Please select option A through C: ")
print()
#Story starts to break into three different paths
#Blacksmith Storyline
if(userTalk == "A"):
  print("You meet with the town blacksmith, looking for a  legendary sword.  ")
  print("They tell you that the legend is the sword is frozen in ice waiting to be found.")
  print("You choose to search for it:")
  print("  A. In the Desert")
  print("  B. In the Forest")
  print("  C. In the Arctic")
  userSword = input("Please select option A through C: ")
  print()
  if(userSword == "B"):
    print("After looking long and hard through the forest, you found it - the ultimate sword of coding! ")
    print()
    print("The blacksmith is thrilled and rewards you with a magical chain mail armor worthy of a hero!!")
  else:
    print("You searched and searched for the rest of your life, but never found it. It might be a good idea to heed the blacksmith's advice and go to a cold place")
    print()
    print("~ The End ~")
print()
# Teacher's storyline
if(userTalk == "B"):
  print("You meet with the town teacher, who is asking you a question")
  print("'I have to be honest with you,' they say. 'I'm not really qualified to teach and am struggling with this question.'")
  print("They gesture to a math equation that reads as follows:")
  print()
  print("y = 6 + 2 + 1")
  userAnswer = input("Please enter the solution to this problem: ")
  userAnswer = int(userAnswer)
  if(userAnswer == 9):
    print()
    print("'This makes perfect sense!,' the teacher cries, and they award you with an honorary degree.")
    print()
    print("You are forever known as one of the high level sages in the realm!")
    print()
    print("~ The End ~")
  else:
    print()
    print("'This does not make any sense.,' the teacher quickly replies, and motions you away with their hand.")
#King's storyline
if(userTalk == "C"):
  print("You meet with the King of Python, looking for a brave warrior.")
  print("'I need someone to conquer a nearby dragon to save the kingdom! There is no time, head east and be ready for battle!, says the king.")
  print()
  print("You head east and find the dragon. You ready yourself for battle. But in a twist, the dragon asks you to solve a riddle in exchange for your realm.")
  print("'What two numbers, when added together, equals ten?,' asks the dragon.'")
  print()
  print("You ponder for a moment. There's multiple answers to this question, aren't there?")
  print("After thinking for a moment, you answer with two answers...")
  userFirstNumber = input("Enter the first number: ")
  userSecondNumber = input("Enter the second number: ")
  userFirstNumber = int(userFirstNumber)
  userSecondNumber = int(userSecondNumber)
  result = userFirstNumber + userSecondNumber                 
  if(result == 10):
    print()
    print(f"Ah yes, {userFirstNumber} and {userSecondNumber} add up to 10!,' the dragon explained")
    print()
    print("The dragon decides to leave your realm alone, and the king proclaims, 'You are the greatest hero in all the realm!'")
    print()
    print("~ The End ~")
  else:
    print()
    print("'No!,' the dragon loudly says.'")
    print("The dragon flies past you and opens their mouth. Large waves of fire rain over Castle Python.")