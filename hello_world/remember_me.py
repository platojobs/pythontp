import  json
filename = 'user_name.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
      username = input("what is your name?")
      with open(filename,'w') as f:
          json.dump(username,f)
          print(f"we'll remember your name is {username}")
else:
    print(f"welcome back {username}")
