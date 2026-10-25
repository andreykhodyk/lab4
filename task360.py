text = input()

text_no_spaces = text.replace(" ", "")

clean_text = text_no_spaces.lower()

reversed_text = clean_text[::-1]

if clean_text == reversed_text:
    print("Yes")
else:
    print("No")