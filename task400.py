text = input()
clean_text = ""

for char in text:
    if char.isalpha():
        clean_text += char.lower()

reversed_text = clean_text[::-1]

if clean_text == reversed_text:
    print("Yes")
else:
    print("No")