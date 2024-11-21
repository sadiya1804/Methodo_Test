from datetime import datetime

def is_palindrome(text):
    clean_text = ''.join(text.lower().split())
    return clean_text == clean_text[::-1]


def main():
  now = datetime.now().hour
  
  if now < 12:
    print("Bonjour!")
  elif now < 18:
    print("Bonsoir!")
  else:
    print("Bonne nuit!")
    
  while True:
        user_input = input("Ecrivez quelque chose (ou 'exit' pour quitter): ")
        if user_input.lower() == 'exit':
             if now < 12:
                return "Bonne journée!"
             elif now < 17: 
                return "Bon aprés midi!"
             elif now < 21:
                return "Bonne soirée!"
             else:
                return "Bonne nuit!"
             break  
        print(f"Vous avez écrit: {user_input}")  
        
        if is_palindrome(user_input):
          print("Bien dit!")

if __name__ == "__main__":
    main()