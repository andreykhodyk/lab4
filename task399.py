text = input()

if len(text) > 0:
    result = ""
    
    current_char = text[0]
    count = 1
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            if count == 1:
                result += current_char
            else:
                result += str(count) + current_char
                
            current_char = text[i]
            count = 1
            
    if count == 1:
        result += current_char
    else:
        result += str(count) + current_char

    print(result)