def func_up(text):
    new_text =''
    for current_word in text.split():
        new_text += current_word[0].upper()+current_word[1:]+' '
    return new_text

print(func_up('hello world how are you'))
