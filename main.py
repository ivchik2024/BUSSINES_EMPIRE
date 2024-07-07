meme_dict = {
    "GG": "с язика геймеров GG означает хорошая игра или легкая победа" ,
    "ЛУТ": "с язика геймеров ЛУТ означает вещь или вещи"
    }

word = input ()

if word in meme_dict.keys():
    print (meme_dict[word])
else:
    print ("Такого слова нету!!!")
