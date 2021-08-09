import random
bottom, top = 1, 19
x = random.randint(bottom, top)
print(x, bottom, top)
ans = input("only 'c' for correct ansewr ,'l' for lower answer,'b' for bigger answer allowed!")
while ans != "c":
    if ans == "l":
        top = x - 1
        x = random.randint(bottom, top)
        print(x, bottom, top)
        ans = input("only 'c' for correct ansewr ,'l' for lower answer,'b' for bigger answer allowed!")
        continue
    elif ans == "b":
        bottom = x + 1
        x = random.randint(bottom, top)
        print(x, bottom, top)
        ans = input("only 'c' for correct ansewr ,'l' for lower answer,'b' for bigger answer allowed!")
        continue
print("yes, you've done!")