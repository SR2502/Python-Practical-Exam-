#SOUMYA ROUT (20214020) B.SC (HONS) ENVIRONMENTAL SCIENCE


#FIRST QUESTION
# (A)

def oddSum(n):
  def oddSum(n) :
    return (n * n);
 
#test run
n = int(input("type your number - "))
print(f"sum of first {n} odd numbers is {oddSum(n)}")
 
#(B)

def evensum(n):
    return n * (n + 1)

#test run
n = int(input("type your number - "))
print(f"sum of first {n} even numbers is {evensum(n)}")

#(C)

# i cant seem to undersatnd the pattern, sorry

# question 2 Consider a tuple t1=(1,2,5,7,9,2,4,6,8,10). Write a program to perform following operations:
t1 = (1,2,5,7,9,2,4,6,8,10)
#(A)

t_a = int(len(t1) / 2)
print(f'the new tuples are {t1[:t_a]}, {t1[t_a:]}')

#(B)

t1_b = tuple(i for i in t1 if i%2 == 0)
print(f"all the even numbers are {t1_b}")

#(C)

t2=(11,13,15)

con_tup = t1 + t2
print(f"concentated tuple - {con_tup}")

#(D)

print(f"The maximum and minimum value in this tuple are {max(t1)} and {min(t1)} respectively")

# question 3 - Write a menu driven program to perform the following functions on strings:
#( A - D , menu question)

x = str(input("enter your word/sentence - "))
print(f'your typed word is - {x}')

print('''choose one of the following-
            1. Find the number of letters in the word
            2. Highest value among 3 
            3. Replace every successive character with ‘#’
            4. Count number of words in the sentence
              ''')
y = int(input('ENTER 1/2/3/4 - '))

if y == 1:
    print(f'the numbers of letters in this string are {len(x)}')

elif y == 2:
    b = str(input("enter your second word- "))
    c = str(input("enter your third word- "))
    l1 = [x,b,c]
    l2 = max(l1)
    print(f"highest value string among the three is {max(l1)}")

elif y == 3:
    ch = []
    for i in x:
        ch.append(i)
    for j in range(1, len(ch), 2):
        if ch[j] != " ":  
            ch[j] = '#'

    string = ''.join(ch)
    print(string)

elif y == 4:
    a_string = x
    word_list = a_string.split()
    number_of_words = len(word_list)
    print(f'number of words in the sentence are {number_of_words}')

else:
    print('invalid input')



