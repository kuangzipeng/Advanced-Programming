```python
#第一题

#方法一
i=1
total1=0
while (i<=1000):
    if(i%2==0):
        total1=total1+i  
    i=i+1 
print(total1)

##

i=0
total2=0
while (i<=1000):
    if(i%3==0):
        total2=total2+i  
    i=i+1 
print(total2)

#方法二
i=0
total3=0
for i in range (4,1001,4):
    total3+=i
print(total3)

##

i=0
total4=0
for i in range (5,1001,5):
    total4+=i
print(total4)
```

    250500
    166833
    125500
    100500
    


```python
#第二题
asciilist = []
for i in range(32,128):
    asciilist.append(chr(i))
print(len(asciilist))
for i in range(0,len(asciilist),20):
    print(asciilist[i:i+20])
```

    96
    [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3']
    ['4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
    ['H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[']
    ['\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    ['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '\x7f']
    


```python

```
