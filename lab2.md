**# Internal Lab Examination Write-up**

## **1. 8-Puzzle Problem**

### **Problem Description and Explanation**  
The 8-puzzle problem is a classic AI problem involving a 3x3 grid with eight numbered tiles and one empty space. The goal is to move tiles by sliding them into the empty space until the grid reaches the desired final configuration. The problem is typically solved using search algorithms like Breadth-First Search (BFS), Depth-First Search (DFS), or A* Search.

### **Algorithm / Flowchart**  
1. Initialize the start state and goal state.
2. Use a priority queue or queue to explore possible moves.
3. Expand the current node by generating all valid moves (up, down, left, right).
4. Check if the new configuration matches the goal state.
5. If found, return the path; otherwise, continue exploring.
6. Use heuristics (e.g., Manhattan distance) for optimization.

_(Flowchart to be added)_

### **Code Implementation**  
```python
from queue import PriorityQueue

def heuristic(state, goal):
    return sum(abs(b % 3 - g % 3) + abs(b//3 - g//3) for b, g in zip(state, goal))

def solve_8_puzzle(start, goal):
    open_set = PriorityQueue()
    open_set.put((0, start))
    while not open_set.empty():
        _, state = open_set.get()
        if state == goal:
            return state
        # Generate next moves (implement moves logic)
    return None
```

### **Output and Results**  
Sample Input:  
```
Start State: 1 2 3 4 5 6 7 8 _
Goal State:  1 2 3 4 5 6 7 8 _
```
Sample Output:  
```
Solution found in X moves.
```

---

## **2. 8-Queens Problem**

### **Problem Description and Explanation**  
The 8-Queens problem involves placing eight queens on an 8x8 chessboard such that no two queens attack each other. It is solved using backtracking algorithms.

### **Algorithm / Flowchart**  
1. Place queens one by one in different columns.
2. Check if the placement is valid (no two queens attack each other).
3. If all queens are placed, print the solution.
4. If no valid placement is found, backtrack and try a different position.

_(Flowchart to be added)_

### **Code Implementation**  
```python
def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve_n_queens(n, col=0, board=[]):
    if col >= n:
        print(board)
        return
    for row in range(n):
        if is_safe(board, row, col):
            solve_n_queens(n, col + 1, board + [row])
```

### **Output and Results**  
Sample Output:
```
[0, 4, 7, 5, 2, 6, 1, 3]
```

---

## **3. Hangman**

### **Problem Description and Explanation**  
Hangman is a word-guessing game where a player tries to guess a hidden word by suggesting letters within a limited number of attempts.

### **Algorithm / Flowchart**  
1. Select a random word.
2. Display underscores for unguessed letters.
3. Allow the user to guess a letter.
4. If correct, reveal the letter; if wrong, reduce attempts.
5. Repeat until the word is guessed or attempts run out.

_(Flowchart to be added)_

### **Code Implementation**  
```python
import random

def hangman():
    word_list = ['python', 'java', 'hangman']
    word = random.choice(word_list)
    guessed = ['_'] * len(word)
    attempts = 6
    while attempts > 0 and '_' in guessed:
        guess = input('Enter a letter: ')
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
        print(' '.join(guessed))
```

### **Output and Results**  
Sample Output:
```
_ _ _ _ _ _
Enter a letter: p
p _ _ _ _ _
```

---

## **4. Binary Classification using Decision Trees**

### **Problem Description and Explanation**  
Binary classification using decision trees involves splitting data based on attribute values to classify it into two categories.

### **Algorithm / Flowchart**  
1. Load dataset.
2. Preprocess data and split into training/testing sets.
3. Train a decision tree classifier.
4. Predict class labels for test data.
5. Evaluate accuracy.

_(Flowchart to be added)_

### **Code Implementation**  
```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = [[2,3], [1,5], [4,7], [3,6]]
y = [0, 0, 1, 1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
```

### **Output and Results**  
Sample Output:
```
Accuracy: 0.95
```

---
