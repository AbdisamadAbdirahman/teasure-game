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
    self.guesses_left = 0
    self.number_of_guesses = 0
  word_list = []
  generated_list = []
  generated_underscore_list = []
  wrong_letters = []
  def load_words():
      with open('text.txt') as word_file:
          valid_words = set(word_file.read().split())

      with open('words_beta.txt', "a") as word_file:
          word_file.write(str(valid_words))
      return valid_words

  def generate_word_list(num1,num2):
      global word_list
      with open("text.txt", "r") as file:
          for line in file:
              if len(line) > num1 and len(line) < num2:
                  word_list = []
                  word_list.append(line.strip())
      for i in range(len(generated_list)):
          generated_list.append(word[i-1])
          generated_underscore_list = []
          generated_underscore_list.append("_")
      return word_list
      
  with open("text.txt", "r") as file:
      for line in file:
          if len(line) > 2:
              word_list.append(line.strip())


  def restart(self):
      global guesses_left, word, generated_list, generated_underscore_list, number_of_guesses, wrong_letters
      self.guesses_left = 6
      self.number_of_guesses = 0
      generated_list = []
      generated_underscore_list = []
      wrong_letters = []
      
      word = random.choice(word_list)
      print("The word has",str(len(word)),"letters.")
      for i in range(len(word)):
          generated_list.append(word[i])
          generated_underscore_list.append("_")
      
  def anothergo(self):
      anothergo_str = input("Another go? y/n: ").lower()
      if anothergo_str == "y":
          self.restart()
      elif anothergo_str == "n":
          print("Alright, have a nice day.")
          exit()
      else:
          print("Invalid input, assuming you do not want another go")
          exit() 

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
    while self.guesses_left != 0:
        if "_" not in generated_underscore_list:
            print(self.display_hangman(self.guesses_left))
            print("Congratulations! You guessed the word correctly! The word was "+word+"!")
            print("It took you",str(7 - self.guesses_left),"attempts.")
            self.anothergo()
        print(self.display_hangman(self.guesses_left))
        print(generated_underscore_list)
        
        guess = input("Enter your guess: ")
        if not guess.isalpha():
            print("You need to guess letters (in English).")
            continue
        if len(guess) < 1:
            print("An input needs to be given.")
            continue
        elif len(guess) > 1:   
            if guess == word:
                number_of_guesses += 1
                print(self.display_hangman(guesses_left))
                print("Correct! Well done!")
                print("It took you",str(7 - self.guesses_left),"attempts.")
                self.anothergo()
            else:
                self.number_of_guesses += 1
                print("Wrong!")

        if guess not in generated_list:
            self.number_of_guesses += 1
            print("Letter not in word.")
            self.guesses_left -= 1
            if guess not in wrong_letters:
                wrong_letters.append(guess)
            else:
                print("You already guessed that")
                self.number_of_guesses -= 1
            if self.guesses_left == 0:
                print(self.display_hangman(guesses_left))
                print("You lose! The word was",word)
                self.anothergo()
                continue
            print("You have",self.guesses_left, "guesses left")
            print("Wrong letters:", wrong_letters)
        else:
            print("Letter in word")
            for i in range(len(word)):
                if guess == generated_list[i]:
                    generated_underscore_list[i] = guess
            print("You have ",self.guesses_left,"guesses left")
            print("Wrong letters: ",wrong_letters)