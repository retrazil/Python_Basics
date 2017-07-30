file_name = "ore.txt"

# open closes f on its own
with open(file_name, 'w') as f:
    f.write('kono ore sama\n')
    f.write('saiko desu')


filwa = open("omae.txt", 'w')
filwa.write('nanda kono yaro\n')
filwa.write('shinee')
filwa.close()

dusra = open("omae.txt", 'a')
dusra.write("\nkorosu zo")
dusra.close()
