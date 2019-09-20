```python
print(ord("A"),ord("Z"))
```

    65 90
    49
    


```python
print(ord('a'),ord('z'))
```

    97 122
    


```python
x=65
lis=[]
for x in range(65,91):
    tup = (chr(x),chr(x+32))
    lis.append(tup)
for i in range (26):
    for x,y in  zip (lis[i][0],lis[i][1]):
        print(x,'-',y)
```

    A - a
    B - b
    C - c
    D - d
    E - e
    F - f
    G - g
    H - h
    I - i
    J - j
    K - k
    L - l
    M - m
    N - n
    O - o
    P - p
    Q - q
    R - r
    S - s
    T - t
    U - u
    V - v
    W - w
    X - x
    Y - y
    Z - z
    


```python
import os 
filename = []
for i in range(1,51):
    name="./file"+str(i)
    filename.append(name)
path = r"C:\Download"
for name in filename:
    os.mkdir(path+name)

```


```python

```
