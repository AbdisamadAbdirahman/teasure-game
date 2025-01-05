import random
import time

class TicTacToe:
  def __init__(self):
    self.winner = ' '
    self.user_turn = True
    self.board = [  
              [ ' ', ' ', ' ' ],
              [ ' ', ' ', ' ' ],
              [ ' ', ' ', ' ' ]
            ]

    self.win_groups = [
      [[0, 0], [0, 1], [0, 2]],
      [[1, 0], [1, 1], [1, 2]],
      [[2, 0], [2, 1], [2, 2]],
      [[0, 0], [1, 0], [2, 0]],
      [[0, 1], [1, 1], [2, 1]],
      [[0, 2], [1, 2], [2, 2]],
      [[0, 0], [1, 1], [2, 2]],
      [[0, 2], [1, 1], [2, 0]]
    ]

  def draw_board(self):
    print(self.board[0][0] + '|' + self.board[0][1] + '|' + self.board[0][2])
    print("-+-+-")
    print(self.board[1][0] + '|' + self.board[1][1] + '|' + self.board[1][2])
    print("-+-+-")
    print(self.board[2][0] + '|' + self.board[2][1] + '|' + self.board[2][2])


  def find_winner(self):
    if all(cell != ' ' for row in self.board for cell in row):
      return 'D'

    for group in self.win_groups:
      coord0 = group[0]
      coord1 = group[1]
      coord2 = group[2]
      if self.board[coord0[1]][coord0[0]] == self.board[coord1[1]][coord1[0]] and self.board[coord1[1]][coord1[0]] == self.board[coord2[1]][coord2[0]] and self.board[coord0[1]][coord0[0]] != ' ':
        return self.board[coord0[1]][coord0[0]]
    return ' '

  def find_winning_move(self,x_or_o):
    for group in self.win_groups:
      coord0 = group[0]
      coord1 = group[1]
      coord2 = group[2]
      value0 = self.board[coord0[1]][coord0[0]]
      value1 = self.board[coord1[1]][coord1[0]]
      value2 = self.board[coord2[1]][coord2[0]]
      correct = (value0 == x_or_o) + (value1 == x_or_o) + (value2 == x_or_o)
      spaces = (value0 == ' ') + (value1 == ' ') + (value2 == ' ')
      if correct == 2 and spaces == 1:
        if value0 == ' ':
          return coord0
        elif value1 == ' ':
          return coord1
        elif value2 == ' ':
          return coord2
    return None

  def can_place(self,x, y):
    if x > 2 or y > 2 or x < 0 or y < 0:
      return False
    if self.board[y][x] != ' ':
      return False
    return True

  def end_turn_routine(self):
    self.winner = self.find_winner()
    if self.winner == 'X':
      self.draw_board()
      print("You win!")
      return
    elif self.winner == 'O':
      self.draw_board()
      print("You lose!")
      self.board = [  
              [ ' ', ' ', ' ' ],
              [ ' ', ' ', ' ' ],
              [ ' ', ' ', ' ' ]
            ]
      return
    elif self.winner == 'D':
      self.draw_board()
      print("Draw!")
      self.board = [  
              [ ' ', ' ', ' ' ],
              [ ' ', ' ', ' ' ],
              [ ' ', ' ', ' ' ]
            ]
      return
    self.user_turn = not self.user_turn
    self.draw_board()

  def start_game(self):
    while self.winner == ' ':
      if self.user_turn:
        # --- USER TURN --- #
        x = int(input("Enter the x coordinate "))
        y = int(input("Enter the y coordinate "))
        if not self.can_place(x, y):
          print("Invalid coordinates.")
          continue
        self.board[y][x] = 'X'

        self.end_turn_routine()
      else:
        # --- COMPUTER TURN --- #
        print("Computer is thinking....")
        time.sleep(2)

        for group in self.win_groups:
          coord0 = group[0]
          coord1 = group[1]
          coord2 = group[2]

        win_move = self.find_winning_move('O')
        defense_move = self.find_winning_move('X')
        if win_move != None:
          self.board[win_move[1]][win_move[0]] = 'O'
        elif defense_move != None:
          self.board[defense_move[1]][defense_move[0]] = 'O'
        elif self.board[1][1] == ' ':
          self.board[1][1] = 'O'
        else:
          spot = '-'
          col = 0
          row = 0
          while spot != ' ':
            col = random.randint(0,2)
            row = random.randint(0,2)
            spot = self.board[row][col]
          self.board[row][col] = 'O'

        self.end_turn_routine()

  def restart_game(self):
    self.board = [  
                [ ' ', ' ', ' ' ],
                [ ' ', ' ', ' ' ],
                [ ' ', ' ', ' ' ]
            ]
    self.winner = ' '
    self.user_turn = True

class Hangman:
  def __init__(self):
    self.guesses_left = 6
    self.number_of_guesses = 0
    self.winner = False
    self.word = ""
    self.wrong_letters = []
    self.generated_list = []
    self.generated_underscore_list = []
  word_list = []
  
  with open("text.txt", "r") as file:
    for line in file:
        if len(line) > 2:
            word_list.append(line.strip())

  def restart(self):
      self.guesses_left = 6
      self.number_of_guesses = 0
      self.wrong_letters = []

      self.word = random.choice(Hangman.word_list)
      print("The word has",str(len(self.word)),"letters.")
      
      self.generated_list = []
      self.generated_underscore_list = []
      for i in range(len(self.word)):
          self.generated_list.append(self.word[i])
          self.generated_underscore_list.append("_")

  def display_hangman(self,guesses_left):
      stages = [  
                  """
                    --------
                    |      |
                    |      O
                    |     \\ /
                    |      |
                    |     / \\
                    -
                  """,

                  """
                    --------
                    |      |
                    |      O
                    |     \\ /
                    |      |
                    |     / 
                    -
                  """,

                  """
                    --------
                    |      |
                    |      O
                    |     \\ /
                    |      |
                    |      
                    -
                  """,

                  """
                    --------
                    |      |
                    |      O
                    |     \\|
                    |      |
                    |     
                    -
                  """,

                  """
                    --------
                    |      |
                    |      O
                    |      |
                    |      |
                    |     
                    -
                  """,

                  """
                    --------
                    |      |
                    |      O
                    |    
                    |      
                    |     
                    -
                  """,

                  """
                    --------
                    |      |
                    |      
                    |    
                    |      
                    |     
                    -
                  """
      ]
      return stages[guesses_left]



  def start_game(self):
    while self.guesses_left != 0 and not self.winner:
        if "_" not in self.generated_underscore_list:
            print(self.display_hangman(self.guesses_left))
            print("Congratulations! You guessed the word correctly! The word was "+self.word+"!")
            print("It took you",str(7 - self.guesses_left),"attempts.")
            self.winner = True
            break
        print(self.display_hangman(self.guesses_left))
        print(self.generated_underscore_list)

        guess = input("Enter your guess: ")
        if not guess.isalpha():
            print("You need to guess letters (in English).")
            continue
        if len(guess) < 1:
            print("An input needs to be given.")
            continue
        elif guess == "idk":
          self.guesses_left = 0
          continue
        elif guess == "no":
          self.winner = True
          continue
        elif len(guess) > 1:   
            if guess == self.word:
                self.number_of_guesses += 1
                print(self.display_hangman(self.guesses_left))
                print("Correct! Well done!")
                print("It took you",str(7 - self.guesses_left),"attempts.")
                self.winner = True
            else:
                self.number_of_guesses += 1
                print("Wrong!")

        if guess not in self.generated_list:
            self.number_of_guesses += 1
            print("Letter not in word.")
            self.guesses_left -= 1
            if guess not in self.wrong_letters:
                self.wrong_letters.append(guess)
            else:
                print("You already guessed that")
                self.number_of_guesses -= 1
            if self.guesses_left == 0:
                print(self.display_hangman(self.guesses_left))
                print("You lose! The word was",self.word)
                continue
            print("You have",self.guesses_left, "guesses left")
            print("Wrong letters:", self.wrong_letters)
        else:
            print("Letter in word.")
            for i in range(len(self.word)):
                if guess == self.generated_list[i]:
                    self.generated_underscore_list[i] = guess
            print("You have ",self.guesses_left,"guesses left")
            print("Wrong letters: ",self.wrong_letters)