def swapFiles():

    data_a = open('D:/PROJECTS/Python/Class Works/text1.txt', 'r').read()
    data_b = open('D:/PROJECTS/Python/Class Works/text2.txt', 'r').read()

    open('D:/PROJECTS/Python/Class Works/text1.txt','w').write(data_b)
    open('D:/PROJECTS/Python/Class Works/text2.txt','w').write(data_a)

swapFiles()