# Game Logic

print('Import Othello_Logic successfully!')
print()

class DropOutOfBoardException(Exception):
  pass
class NonEmptyCellException(Exception):
  pass
class NotValidDropException(Exception):
  pass


#[up:[-1,0],down:[1,0],left:[0,-1],right:[0,1]]
#[top_left:[-1,-1],top_right:[-1,1],low_left:[1,-1],low_right:[1,1]]


class OthelloState:
  def __init__(self,row:int,col:int,top_left:str,turn:str):
    self._row = row
    self._col = col
    self._top_left = top_left
    self._turn = turn
    self._end = False
    self._board = self.initial_board()

    

  def initial_board(self):
    ''' Make intial board with top left '''
    board = []
    for r in range(self._row):
      board.append(self._col * ['*'])
    if self._top_left == 'White':
      board[int((self._row/2)-1)][int((self._col/2)-1)] = 'White'
      board[int((self._row/2)-1)][int((self._col/2))] = 'Black'
      board[int((self._row/2))][int((self._col/2)-1)] = 'Black'
      board[int((self._row/2))][int((self._col/2))] = 'White'
    else:
      self._top_left =='Black'
      board[int((self._row/2)-1)][int((self._col/2)-1)] = 'Black'
      board[int((self._row/2)-1)][int((self._col/2))] = 'White'
      board[int((self._row/2))][int((self._col/2)-1)] = 'White'
      board[int((self._row/2))][int((self._col/2))] = 'Black'
    return board
  
  def _drop_disc(self,drop_row,drop_col):
    ''' take user's input and drop disc'''
    
    all_reverse_lists = self._get_all_diretions_reverse_list(drop_row,drop_col)
    
    if len(all_reverse_lists) == 0:
      return False
    
    else:
      self._board[drop_row-1][drop_col-1] = self._turn
      for i in all_reverse_lists:
        self._board [i[0]] [i[1]] = self._opposite_disc(self._board [i[0]] [i[1]])
      self._opposite_turn()


  def _opposite_turn(self):
    ''' change user's turn after valid move or return to user's turn
         if  ther is no valid move for next user'''
    self._turn = self._opposite_disc(self._turn)
    if not self._check_valid_turn():
      self._turn = self._opposite_disc(self._turn)
      if not self._check_valid_turn():
        self._end = True
        #self._check_winner()
        
        

  def _check_valid_turn(self):
    ''' check whether valid turn exist'''
    for r in range(1,self._row+1):
      for c in range(1,self._col+1):
        if self._if_valid_move(r,c):
          return True
    return False


  def _opposite_disc(self,disc:str):
    ''' change disc's color'''
    if disc == 'White':
      return 'Black'
    elif disc =='Black':
      return 'White'
    else:
      return None
    
    
  def _is_in_board(self,row,col):
    ''' check whether user's move in the board'''
    return 0 <= row <= self._row -1  and 0 <= col <= self._col-1
    
  def _if_valid_move(self,drop_row:int,drop_col:int):
    ''' check whether valid move exist'''
    try:
      return len(self._get_all_diretions_reverse_list(drop_row,drop_col)) > 0
    except:
      return False
  
  def _get_all_diretions_reverse_list(self,drop_row:int,drop_col:int):
    
    all_reverse_lists = []
    all_reverse_lists.extend(self._one_direction_reverse_list(drop_row,drop_col,[-1,0]))
    all_reverse_lists.extend(self._one_direction_reverse_list(drop_row,drop_col,[1,0]))
    all_reverse_lists.extend(self._one_direction_reverse_list(drop_row,drop_col,[0,-1]))
    all_reverse_lists.extend(self._one_direction_reverse_list(drop_row,drop_col,[0,1]))
    all_reverse_lists.extend(self._one_direction_reverse_list(drop_row,drop_col,[-1,-1]))
    all_reverse_lists.extend(self._one_direction_reverse_list(drop_row,drop_col,[-1,1]))
    all_reverse_lists.extend(self._one_direction_reverse_list(drop_row,drop_col,[1,-1]))
    all_reverse_lists.extend(self._one_direction_reverse_list(drop_row,drop_col,[1,1]))
    
    if len(all_reverse_lists) == 0:
      raise NotValidDropException
    return all_reverse_lists


  def _one_direction_reverse_list(self,drop_row:int,drop_col:int,direction:list):
    ''' check surrouding disc first, whther they are differnt color from turn, then get the reverse list'''
    
    if not self._is_in_board(drop_row-1,drop_col-1):
      raise DropOutOfBoardException()
    
    if self._board[drop_row-1][drop_col-1] != '*':
      raise NonEmptyCellException()
    
    else:
      reverse_list = []
      
      while True:
        
        drop_row += direction[0]
        drop_col += direction[1]
        
        if not self._is_in_board(drop_row-1,drop_col-1):
          return []
        
        if self._board[drop_row-1][drop_col-1] == self._opposite_disc(self._turn):
          reverse_list.append( [drop_row-1,drop_col-1] )
        elif self._board[drop_row-1][drop_col-1] == self._turn:
          break
        else:
          reverse_list = []
          break
      return reverse_list
        
  def _check_winner(self):
    ''' check who is the winter'''
    Scores= self._check_score()
    W_count = Scores['White_discs']
    B_count = Scores['Black_discs']
    
    if W_count > B_count:
      return 'White'
    if W_count < B_count:
      return 'Black'
    if W_count == B_count:
      return 'EVEN'


        
  def _check_score(self):
    ''' check how many discs of each side'''
    W_count = 0
    B_count = 0
    for r in range(self._row):
      for c in range(self._col):
        if self._board[r][c] == 'White':
          W_count +=1
        elif self._board[r][c] == 'Black':
          B_count += 1
    return {'White_discs':W_count,'Black_discs':B_count}
  


