# Technical specification

**Please install blessed library**
```bash
pip install blessed
```

## Tasks

### Create an algorithm that finds most optimal next move for 'x' or 'o' given current grid
> assuming that the opponent is another perfect algorithm that does not make any mistakes
- Always win if possible
- If win is impossible make a draw
- Else avoid losing for as long as possible

---
### Create an tui for playing tic-tac-toe vs algorithm
- you can choose to play as **X** or **O**
- you can edit starting grid configuration
- **X** always makes first move

---
### Implement test system
- all tests are stores in **tests.txt** file
- format:
	- 9 characters for starting grid configuration
	- 11th character is **'x'** or **'o'** (whos turn it is now)
	- 13th and 15th characters are expected next move **(x y)**
- example:
```xx_o_o___ o 1 1```
