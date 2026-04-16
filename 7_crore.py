questions = [
    ["India ki rajdhani kya hai?", "Mumbai", "Delhi", "Kolkata", "Chennai", 2],
    
    ["National Animal of India kaunsa hai?", "Lion", "Tiger", "Elephant", "Leopard", 2],
    
    ["Kaun sa planet Red Planet ke naam se jaana jata hai?", "Earth", "Mars", "Jupiter", "Venus", 2],
    
    ["Zero ka concept kis desh se aaya?", "China", "India", "Greece", "Egypt", 2],
    
    ["India ka national sport traditionally kya maana jata hai?", "Cricket", "Hockey", "Football", "Kabaddi", 4],
    
    ["Jallianwala Bagh Massacre kis saal hua tha?", "1915", "1919", "1921", "1930", 2],
    
    ["भारत ka rashtriya geet kaunsa hai?", "Vande Mataram", "Jana Gana Mana", "Sare Jahan Se Achha", "Ae Mere Watan Ke Logon", 1],
    
    ["Taj Mahal kis shahar mein hai?", "Delhi", "Jaipur", "Agra", "Lucknow", 3],
    
    ["Computer ka brain kise kaha jata hai?", "Monitor", "CPU", "Keyboard", "Mouse", 2],
    
    ["भारत ka Samvidhan kab lagu hua?", "15 August 1947", "26 January 1950", "2 October 1947", "26 November 1949", 2],
    
    ["India ki rajdhani kya hai?", "Mumbai", "Delhi", "Kolkata", "Chennai", 2],
    
    ["National Animal of India kaunsa hai?", "Lion", "Tiger", "Elephant", "Leopard", 2],
    
    ["Kaun sa planet Red Planet ke naam se jaana jata hai?", "Earth", "Mars", "Jupiter", "Venus", 2],
    
    ["Zero ka concept kis desh se aaya?", "China", "India", "Greece", "Egypt", 2],
    
    ["India ka national sport traditionally kya maana jata hai?", "Cricket", "Hockey", "Football", "Kabaddi", 4],
    
    ["Jallianwala Bagh Massacre kis saal hua tha?", "1915", "1919", "1921", "1930", 2],
    
    ["भारत ka rashtriya geet kaunsa hai?", "Vande Mataram", "Jana Gana Mana", "Sare Jahan Se Achha", "Ae Mere Watan Ke Logon", 1],
    
    ["Taj Mahal kis shahar mein hai?", "Delhi", "Jaipur", "Agra", "Lucknow", 3],
    
    ["Computer ka brain kise kaha jata hai?", "Monitor", "CPU", "Keyboard", "Mouse", 2],
    
    ["भारत ka Samvidhan kab lagu hua?", "15 August 1947", "26 January 1950", "2 October 1947", "26 November 1949", 2],
    
    ["India ki rajdhani kya hai?", "Mumbai", "Delhi", "Kolkata", "Chennai", 2],
    
    ["National Animal of India kaunsa hai?", "Lion", "Tiger", "Elephant", "Leopard", 2],
    
    ["Kaun sa planet Red Planet ke naam se jaana jata hai?", "Earth", "Mars", "Jupiter", "Venus", 2],
    
    ["Zero ka concept kis desh se aaya?", "China", "India", "Greece", "Egypt", 2],
    
    ["India ka national sport traditionally kya maana jata hai?", "Cricket", "Hockey", "Football", "Kabaddi", 4],
    
    ["Jallianwala Bagh Massacre kis saal hua tha?", "1915", "1919", "1921", "1930", 2],
    
    ["भारत ka rashtriya geet kaunsa hai?", "Vande Mataram", "Jana Gana Mana", "Sare Jahan Se Achha", "Ae Mere Watan Ke Logon", 1],
    
    ["Taj Mahal kis shahar mein hai?", "Delhi", "Jaipur", "Agra", "Lucknow", 3],
    
    ["Computer ka brain kise kaha jata hai?", "Monitor", "CPU", "Keyboard", "Mouse", 2],
    
    ["भारत ka Samvidhan kab lagu hua?", "15 August 1947", "26 January 1950", "2 October 1947", "26 November 1949", 2],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000,320000,640000,12500000,5000000,70000000]

money = 0
for i in range(0, len(questions)):

  question = questions[i]
  print(f"\n\n{question[0]} for Rs. {levels[i]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 
#total  money
print(f"Your take home money is {money}")
