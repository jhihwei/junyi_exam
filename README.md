# 均一基金會評分用
## 題目1.A
```python
word = input("Q1.A Please Enter a word:")

def resver_word(word: str):
    length = len(word)
    new_string = ''
    for i in range(0, length):
        new_string = new_string + word[length-1-i]
    # return word[::-1]
    return new_string

print(resver_word(word))
```
## 題目1.B
```python
sentence = input("Q1.B Please Enter a sentence:")

def resver_sentence(sentence:str):
    sentence = sentence.split()
    length = len(sentence)
    new_sentence = ''
    for i in range(0, length):
        new_sentence = new_sentence + resver_word(sentence[i]) + ' '
    return new_sentence
    
print(resver_sentence(sentence))
```
## 題目2
```python
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
```
## 題目3
 房間裡有三個袋子，一個只裝鉛筆，一個只裝原子筆，第三個有鉛筆也有原子筆。
袋子是不透明的，單從袋子的外表上看不出任何差異，你不知道哪個袋子裝什麼。 除了袋子上各貼了一個標示（"鉛筆"、"原子筆"、"混和"），且標示都是錯的 （e.g. 標示鉛筆的袋子可能是混和的或是只裝原子筆）。 
你只能選一個袋子，拿出裡面一支筆，看是鉛筆還是原子筆，然後你要推論出這三 個袋子分別的情況。請列出你的作法，以及解釋為什麼這樣可以找到答案。 

>隨意選一袋子，取得一隻筆，摸其貌，沿其狀，記其形。隨後隔著另二個袋子摸筆，不用拿出也可知道是鉛筆或原子筆，便知道三個袋子裡的內容物。

## 題目4
 有三個人一起到迪士尼遊玩，中午肚子餓了，去餐廳點了一份現在最夯的冰雪奇緣 雙人組，要價 900 元，付錢後，服務生發現今天套餐大特價，只要 750 元，因此 服務生應該退還 150 元給這三個人，但是這位服務生一時鬼迷心竅，決定暗槓 60 元，只退了 90 元給這三個遊客。 那麼：三人各出 300 元 - 服務生還給他們一人 30 元 = 三人各出 270 元。270 元 × 3 人+ 服務生私吞的 60 元 = 810 + 60 = 870 !? 怎麼不是 900 元呢？還 有 30 元去哪了呢？請用敘述的方式，儘量清楚解釋問題出在哪裡。 
 >實質上，遊樂園收到750元，員工收到60元，符合三人所繳810元。
在這情境裡，減法與加法是為獨立事件，應分別計算。