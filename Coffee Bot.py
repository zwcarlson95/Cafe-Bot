def coffee_bot():
  print("Welcome to the cafe!")
  
  size = get_size()

  drink_type = get_drink_type()

  #latte_order = order_latte()
  
  #if drink_type == 'latte':
    #print("Alright, that's a " + str(size) + " " + str(drink_type) + " with " + str(latte_order) + "!")
  #else: 
     #print("Alright, that's a " + str(size) + " " + str(drink_type) + "!")

  print("Alright, that's a " + str(size) + " " + str(drink_type) + "!")

  name = input('Can I get your name please? \n> ')
  print("Thanks, " + str(name) + "! Your drink will be ready shortly.")


def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n>' )
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    return get_size()

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>')
  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return 'mocha'
  elif res == 'c':
    #print('latte')
    return order_latte()
  else:
    print_message()
    return get_drink_type()

def order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n>')
  if res == 'a':
    return '2% milk'
  elif res == 'b':
    return 'non-fat milk'
  elif res == 'c':
    return 'soy milk'
  else:
    print_message()
    return order_latte

coffee_bot()

	
