f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("Yes, twinkle is present")
else:
    print("No, twinkle is not present")


f.close()