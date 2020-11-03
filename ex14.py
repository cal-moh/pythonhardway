from sys import argv

script, user_name, workplace = argv
# I see how handy this is. Pretty cool - I like that I can change it here and not worry about changing it everywhere. I also see how various command prompts can be made to work. Very interesting. 
prompt = '\\ '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What do you do at {workplace}?")
work = input(prompt)

print("What kind of a computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is. 
You {work} at {workplace}. That's pretty cool. 
And you have a {computer} computer. Nice.
""")