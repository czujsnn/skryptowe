import re, sys

def text_extract(text):
    number_list = []
    word_list = []

    for number in re.findall("\d+",text):
        number_list.append(number)

    for word in re.findall("[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+",text):
        word_list.append(word)
    
    return number_list,word_list

def run():
    while True:
        user_input = input("")

        extracted_data = text_extract(user_input)

        for number in extracted_data[0]:
            print(f"  Liczba:{number}")
        
        for word in extracted_data[1]:
            print(f"  Wyraz:{word}")
        

if __name__ == "__main__":
    run()
