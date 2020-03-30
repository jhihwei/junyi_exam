#Q1.A
word = input("Q1.A Please Enter a word:")

def resver_word(word: str):
    length = len(word)
    new_string = ''
    for i in range(0, length):
        new_string = new_string + word[length-1-i]
    # return word[::-1]
    return new_string

print(resver_word(word))

#Q1.B
sentence = input("Q1.B Please Enter a sentence:")

def resver_sentence(sentence:str):
    sentence = sentence.split()
    length = len(sentence)
    new_sentence = ''
    for i in range(0, length):
        new_sentence = new_sentence + resver_word(sentence[i]) + ' '
    return new_sentence
    
print(resver_sentence(sentence))

#Q2
num = input("Q2 Please Enter a number:")

def number_filtter(num):
    print('Input：'+num)
    num = int(num)
    triple = []
    quintuple = []
    result = []
    keep = []
    #將LIST轉為字串，並以' ,'為區隔
    nums = ', '.join([ str(i) for i in range(1, num+1)])
    print('所有的數字是：' + nums)
    for i in range(1, num+1):
        if i % 15 == 0: keep.append(i)
        if i % 3 == 0 and i % 15 !=0:
            triple.append(i)
        elif i % 5 == 0 and i % 15 !=0:
            quintuple.append(i)
        else:
            result.append(i)
    #將LIST轉為字串，並以' ,'為區隔       
    triple = ", ".join([str(i) for i in triple])
    quintuple = ", ".join([str(i) for i in quintuple])
    remain = ', '.join([ str(i) for i in result])
    keep = ', '.join([ str(i) for i in keep])
    print(f'其中 {triple} 被剔除；{quintuple} 被剔除；但是 {keep} 被保留')
    print('所以剩下來的數字是 ' + remain + ', 因此')
    print(f'Output：{len(result)}')

number_filtter(num)

