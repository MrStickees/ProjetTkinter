token = input("Qu'elle est votre token ?\n")

with open("private/token.priv", "w") as f:
    f.write(token)