i=1
sum=0
while i<=10:
  sum= sum+i
  i=i+1
print(sum)
#problem 
a=4
b=9
c=19
def numbers(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
numbers(a)
numbers(b)
numbers(c)
#problem 
a=4
b=9
c=19
def numbers (n):
    if n%3==0:
        print("divisible by 3")
    else:
        print("not divisible")
numbers(a)
numbers(b)
numbers(c)
#problem 
a=[1,2,3]
def print_list(list):
    for x in list:
        print(x)
print_list(a)
#problem 
i=1
L=[1,2,3,4,5,6]
L.pop(0)
L.pop(1)
L.pop(2)
print(L)
#problem 
i=0
L=[1,2,3,4,5,6]
L.pop(4)
L.pop(2)
L.pop(0)
print(L)
#problem
d={"Ram"=30,"Vijay"=40,"Radha"=60}
print(d["vijay"])
#problem
d={"Ram"=30,"Vijay"=40,"Radha"=60}
d.update({"Tom"=2,"Don"=10})
print(d)
#problem#
s={'a','b','c','d'}
s.update({'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z'})
print(s)
count=0
count= 26
vowels ={'a','e','i', 'o', 'u'}

for x in s:
     if x in vowels:
        count = count - 1

print("Vowel count:", count)

#problem 2

letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g',
           'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z'}

vowels = set()
consonants = set()

for ch in letters:
    if ch in {'a', 'e', 'i', 'o', 'u'}:
        vowels.add(ch)
    else:
        consonants.add(ch)

print("Vowels Set =", vowels)
print("Consonants Set =", consonants)
#problem
num = 10
guess = int(input("Guess a number 1 to 10: "))

if guess == num:
    print("Correct guess")
elif guess < num:
    print("Too low")
else:
    print("Too high")


 
