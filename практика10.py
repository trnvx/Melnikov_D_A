file_1 = open("Мельников Дмитрий Александрович У-244_vvod.txt", "r")
file_2 = open("Мельников Дмитрий Александрович У-244_vivod.txt", "w")
file_2.write(file_1.read())