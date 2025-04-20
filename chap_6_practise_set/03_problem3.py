comment1 = "This is my video"
comment2 = "click this"
comment3 = "Rate my video"
comment3 = "subscribe this"

message = input("Enter your message")

if((comment1 in message) or (comment2 in message) or (comment3 in message)):
    print("This comment is spam")

else:
    print("This message is not spam")    