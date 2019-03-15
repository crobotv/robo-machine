def name():
    print("What's your first name?")
    x = input()
    print("The name game! "+x+"! " +x+ ", "+x+" something mumble, mumble, mumble! "+x+"!")

def like():
    print("So, did you like it? Y or N?")
    y = input()
    if y=="Y":
        print("Thank you! Thank you very much. I'll be here all night.")
    else:
        print("Everybody's a critic!")
name()
like()

