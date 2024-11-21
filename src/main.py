from datetime import datetime

def is_palindrome(text):
    clean_text = ''.join(text.lower().split())
    return clean_text == clean_text[::-1]

def say_goodbye():
   now = datetime.now().hour
   if now < 12:
    return "Bonne journée!"
   elif now < 17: 
    return "Bon aprés midi!"
   elif now < 21:
    return "Bonne soirée!"
   else:
    return "Bonne nuit!"

def say_hello():
  now = datetime.now().hour
  if now < 16:
    return "Bonjour!"
  elif now > 17:
    return "Bonsoir!"
 

def main():
  print(say_hello())
  
  while True:
        user_input = input("Ecrivez quelque chose (ou 'exit' pour quitter): ")
        if user_input.lower() == 'exit':
             print(say_goodbye())
             break  
        print(f"Vous avez écrit: {user_input}")  
        
        if is_palindrome(user_input):
          print("Bien dit!")

if __name__ == "__main__":
    main()