# asking for user info
name = input("whats your name?:") 

pass_1 = input(f"{name}:do you have a pass:")

if pass_1 == "yes": #pass confirmation

    #asking for user info

    time_pass = int(input("what time was the pass issued?:"))

    current_time = int(input("what time is it"))

    location = input("where are you going:")
# confirming user info
    if current_time - time_pass <= 2: 
        print("you can go")
    else:
        print("your pass is expired")
    if location == "nurse" or location == "bathroom" or location == "office":
        print("you can go ")
    else:
        print("i dont know where that is no you cant go")

else:
    print("no you dont have a pass")# finalization if they dont have pass







