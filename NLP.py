import random
import time
import linecache

Urn_Main = []
Urn_Txt = []

Tokens_txt ={}      # was in urn_txt
Out_Tokens = {}
Sorted_Tokens = {}

def Urn_main_CREATE(urn_main, start_size):        # Створюю робочу урну
    Dictionary = open('Dictionary.txt', 'r')      # Відкрили словник
    for i in range(0, start_size):                # В циклі по розмір урни
        word = Dictionary.readline().strip("\n")  # Берем слово під номером лінії і, видаляємо \n
        urn_main.append(word)                     # Додаєм в робочу урну
    Dictionary.close()

def main(urn_main,urn_txt,text_len,start_size, Ro, Nu):
    start_time = time.time()

    Dictionary = open('Dictionary.txt', 'r')  # файл словнику
    dictionary_counter = start_size+1         # для вибору з словнику. не включає слова робочої урни

    line_count = -1                 # змінна для перевірки всинаження словника
    if text_len > 50000:            # виконується у разі потреби великого тексту
        line_count = 0
        for line in Dictionary:
            if line != "\n":
                line_count += 1


    for iterable in range(text_len):                          # по потрібну довжину тексту
        random_element = random.choice(urn_main)              # беремо випадковий елемент робочої урни
        urn_txt.append(random_element)                        # додаємо в вихідний текст

        if random_element in Tokens_txt:                      # якщо є в словнику використаних слів
            Tokens_txt[random_element] += Ro                  # додаємо ро копій використань

            for k in range(Ro):                               # додаємо ро копій в урну
                urn_main.append(random_element)

        else:                                                 # якщо немає в словнику використаних слів
            Tokens_txt[random_element] = Ro+1

            for k in range(Ro):                               # додаємо ро копій в урну
                urn_main.append(random_element)
            for j in range(Nu):                                                         # додаємо ню нових слів
                new_word = linecache.getline('Dictionary.txt', dictionary_counter).strip("\n") # обираємо наступне з словника
                dictionary_counter += 1                                                     # збільшення ітератору по словнику
                urn_main.append(new_word)                                                   # додаємо нове в текст

        if dictionary_counter == line_count-1:                                  # Якщо виснажився словник, перериваємо роботу програми
            print("Dictionary end is reached! Text will be of smaller size!")
            break

    Dictionary.close()  # закрили файл словника

    end_time = time.time()
    return end_time - start_time


def Interface():
    # Вводи змінних
    start_size = 5
    lenth = 1
    Ro_in_main = 4
    Nu_in_main = 3

    for upper in range(10):
        for it in range(10):
            start_size = int(input("Enter the size of starting urn: "))
            if start_size > 0: break
            else: print("The size must be bigger than 0, " + str(10-it) + " attempts remains.")

        for it in range(10):
            lenth = int(input("Enter the text length in words: "))
            if lenth > 0: break
            else: print("The number must be bigger than 0, " + str(10-it) + " attempts remains.")

        for it in range(10):
            Ro_in_main = int(input("Enter Ro: "))
            if Ro_in_main > -1: break
            else: print("Ro must be at least 0, " + str(10-it) + " attempts remains.")

        for it in range(10):
            Nu_in_main = int(input("Enter Nu: "))
            if Nu_in_main > -1: break
            else: print("Nu must be at least 0, " + str(10-it) + " attempts remains.")

        ret = input("To input again press 2, to continue press 1: ")
        if ret != 2: break

    Urn_main_CREATE(Urn_Main, start_size)                                    # створили основну урну
    print("Processing might take some time...\n")
    get_time = main(Urn_Main,Urn_Txt,lenth,start_size,Ro_in_main,Nu_in_main) # взяли return-час виконання і створили текст
    print("Finished in " + str(get_time))                                    # Час

    for iterable in range(15):
        ch = int(input("To view created txt array press 1\nTo viev tokens press 2\nTo get .txt file press 3\nElse to exit "))

        if ch == 1:                 # сирий масив слів, з яких створено текст
            print(Urn_Txt)
            print('Len of txt:'+str(len(Urn_Txt)))
            print('\n-----')
            any = int(input("To choose again press 1, else - exit: "))
            if any == 1: continue
            if any != 1: quit()


        if ch == 2:                 # токени начастіше->найрідше
            for i in Urn_Txt:
                if i not in Out_Tokens:
                    Out_Tokens[i] = 1
                else:
                    Out_Tokens[i] += 1

            sorted_keys = sorted(Out_Tokens, key=Out_Tokens.get, reverse=True)
            for w in sorted_keys:
                Sorted_Tokens[w] = Out_Tokens[w]
            print(Sorted_Tokens)
            print("Number of words = "+ str(len(Urn_Txt)))
            print('\n-----')
            any = int(input("To choose again press 1, else - exit: "))
            if any == 1: continue
            if any != 1: quit()


        if ch == 3:                   # вивід в файл
            Created_Text = open('Created_Text.txt', 'w')
            txt_str = ""
            for i in Urn_Txt:
                txt_str += i
                txt_str += ' '
            start_time = time.time()
            Created_Text.write(txt_str)
            Created_Text.close()
            fin_time = time.time()
            print('Created in !' + str(fin_time-start_time)+'\n-----')
            any = int(input("To choose again press 1, else - exit: "))
            if any == 1: continue
            if any != 1: quit()


Interface()