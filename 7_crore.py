questions = [
    ["India ki rajdhani kya hai?", "Mumbai", "Delhi", "Kolkata", "Chennai", 2],
    
    ["National Animal of India kaunsa hai?", "Lion", "Tiger", "Elephant", "Leopard", 2],
    
    ["Kaun sa planet Red Planet ke naam se jaana jata hai?", "Earth", "Mars", "Jupiter", "Venus", 2],
    
    ["Which city is known as the Pink City of India?","jaipur","delhi","ranchi","agra"],
    
    ["Zero ka concept kis desh se aaya?", "China", "India", "Greece", "USA", 2],
    
    ["India ka national sport traditionally kya maana jata hai?", "Cricket", "Hockey", "Football", "Kabaddi", 4],
    
    ["Jallianwala Bagh Massacre kis saal hua tha?", "1915", "1919", "1921", "1930", 2],
    
    ["Bharat ka rashtriya geet kaunsa hai?", "Vande Mataram", "Jana Gana Mana", "Sare Jahan Se Achha", "Ae Mere Watan Ke Logon", 1],
    
    ["Taj Mahal kis shahar mein hai?", "Delhi", "Jaipur", "Agra", "Lucknow", 3],
    
    ["Computer ka brain kise kaha jata hai?", "Monitor", "CPU", "Keyboard", "Mouse", 2],
    
    ["Bharat ka Samvidhan kab lagu hua?", "15 August 1947", "26 January 1950", "2 October 1947", "26 November 1949", 2],
    
    ["Bharat ki sabse lambi nadi kaunsi hai?", "Yamuna", "Ganga", "Brahmaputra", "Godavari", 2],
    
    ["Bharat ke pehle Pradhan Mantri kaun the?", "Sardar Patel", "Jawaharlal Nehru", "Rajendra Prasad", "Lal Bahadur Shastri", 2],
    
    ["Chess ka udgam kis desh se mana jata hai?", "China", "India", "Iran", "Russia", 2],
    
    ["Insaan ke sharir mein kitni haddiyan hoti hain?", "196", "206", "216", "226", 2],
    
    ["Bharat ka Swatantrata Diwas kab hai?", "26 January", "15 August", "2 October", "14 November", 2],
    
    ["jharkhand bhihar kis year me alag hua tha?", "2000", "2001", "2003", "2005", 1],
    
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,
          640000, 1250000, 2500000, 5000000, 10000000]

safe_levels = [4, 9]  

money = 0
safe_money = 0

for i in range(len(questions)):
    question = questions[i]
    print(f"\n{i+1}: {question[0]}  for Rs. {levels[i]}")
    print(f"a. {question[1]}          b. {question[2]}")
    print(f"c. {question[3]}          d. {question[4]}")

    reply = input("Enter your answer (1-4) or 0 to quit:\n")

    if not reply.isdigit():
        print("Invalid input, treating as quit.")
        reply = 0
    else:
        reply = int(reply)

    if reply == 0:
        money = safe_money
        print(f"\nYou quit. Take home money: Rs. {money}")
        break

    if reply == question[-1]:
        money = levels[i]
        print(f"Correct answer! You have won Rs. {money}")
        if i in safe_levels:
            safe_money = money
            print(f"(Safe level reached - Rs. {safe_money} is now guaranteed)")
    else:
        print(f"Wrong answer! Correct answer was: {question[question[-1]]}")
        money = safe_money
        break

print(f"\nYour final take home money is Rs. {money}")
