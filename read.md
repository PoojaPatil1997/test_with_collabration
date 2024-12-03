Got it! Here are 10 easy examples of **`for`** loops in Python:

### 1. **Simple `for` loop**
Print numbers from 1 to 5.

```python
for i in range(1, 6):
    print(i)
```

### 2. **Sum of numbers from 1 to 10**
Add numbers from 1 to 10.

```python
total = 0 
for i in range(1, 11):
    total += i
print(total)
```

### 3. **Loop through a list of fruits**
Print each fruit from the list.

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### 4. **Loop through a string**
Print each character in a string.

```python
word = "hello"
for char in word:
    print(char)
```

### 5. **Multiplication table of 3**
Print the multiplication table of 3.

```python
for i in range(1, 11):
    print(f"3 x {i} = {3 * i}")
```

### 6. **Even numbers from 1 to 10**
Print only the even numbers between 1 and 10.

```python
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
```

### 7. **Squares of numbers from 1 to 5**
Print the square of each number from 1 to 5.

```python
for i in range(1, 6):
    print(i ** 2)
```

### 8. **Counting down from 5 to 1**
Print numbers from 5 down to 1.

```python
for i in range(5, 0, -1):
    print(i)
```

### 9. **Print the length of each word in a list**
Print the length of each word in the list.

```python
words = ["hello", "world", "python"]
for word in words:
    print(len(word))
```

### 10. **Repeat a message 3 times**
Print "Hello, world!" 3 times.

```python
for _ in range(3):
    print("Hello, world!")
```

These are simple and easy examples of using `for` loops!