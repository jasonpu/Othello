# Game GUI

import tkinter
import math
import Othello_Logic as Logic

DEFAULT_FONT = ('Courier', 14)

class SettingGame:
  def __init__(self):

    self._dialog_window = tkinter.Tk()
    self._dialog_window.title('Game Setting')


    self._first = tkinter.StringVar()
    self._first.set('White')
    self._top_left = tkinter.StringVar()
    self._top_left.set('White')
    self._howwin = tkinter.StringVar()
    self._howwin.set('More')
    self._row = tkinter.IntVar()
    self._row.set(6)
    self._column = tkinter.IntVar()
    self._column.set(6)

    self._get_info()

  def _get_info(self):

      info_label = tkinter.Label(
        master = self._dialog_window, text = 'Please setting the game!',
        font = DEFAULT_FONT)
      info_label.grid(
        row = 0, column = 0, columnspan = 5, padx = 10, pady = 10,
        sticky = tkinter.W + tkinter.E)

# get rows
      row_label = tkinter.Label(
        master = self._dialog_window, text = 'Row: ',
        font = DEFAULT_FONT)
      row_label.grid(
        row = 1, column = 0, padx = 10, pady = 10,
        sticky = tkinter.W)
      self._row_entry = tkinter.OptionMenu(
        self._dialog_window,self._row,
        4, 6, 8, 10, 12, 14, 16)
      self._row_entry.grid(
        row =1 , column = 1, padx = 10, pady = 10,
        sticky = tkinter.W + tkinter.E)

# get columns
      column_label = tkinter.Label(
        master = self._dialog_window, text = 'Column: ',
        font = DEFAULT_FONT)
      column_label.grid(
        row = 2, column = 0, padx = 10, pady = 10,
        sticky = tkinter.W)
      self._column_entry = tkinter.OptionMenu(
        self._dialog_window,self._column,
        4, 6, 8, 10, 12, 14, 16)
      self._column_entry.grid(
        row =2 , column = 1, padx = 10, pady = 10,
        sticky = tkinter.W + tkinter.E)

# get top left
      top_left_label = tkinter.Label(
       master = self._dialog_window, text = 'Top Left',
       font = DEFAULT_FONT)
      top_left_label.grid(
       row = 3, column = 0, padx = 10, pady =10,
       sticky = tkinter.W)
      top_left_entry = tkinter.OptionMenu(
       self._dialog_window, self._top_left,
       'Black','White')
      top_left_entry.grid(
       row = 3, column = 1, padx = 10, pady = 10,
       sticky = tkinter.W + tkinter.E)

# get first turn
      who_first_label = tkinter.Label(
       master = self._dialog_window, text = 'First Turn:',
       font = DEFAULT_FONT)
      who_first_label.grid(
       row = 4, column = 0, padx = 10, pady =10,
       sticky = tkinter.W)
      who_first_entry = tkinter.OptionMenu(
       self._dialog_window, self._first,
       'Black','White')
      who_first_entry.grid(
       row = 4, column = 1, padx = 10, pady = 10,
       sticky = tkinter.W + tkinter.E)

# who is winner
      howwin_label = tkinter.Label(
       master = self._dialog_window, text = 'Determine Winner:',
       font = DEFAULT_FONT)
      howwin_label.grid(
       row = 5, column = 0, padx = 10, pady =10,
       sticky = tkinter.W)
      howwin_entry = tkinter.OptionMenu(
       self._dialog_window, self._howwin,
       'Less','More')
      howwin_entry.grid(
       row = 5, column = 1, padx = 10, pady = 10,
       sticky = tkinter.W + tkinter.E)

# start button
      start_button = tkinter.Button(
        master = self._dialog_window, text = 'Start',
        command = self._new_game)

      start_button.grid(
        row = 6, column = 0, padx =10, pady =10,
        sticky = tkinter.S + tkinter.E)

# quit button
      quit_button = tkinter.Button(
        master = self._dialog_window, text = 'Quit ',
        command = self._dialog_window.destroy)

      quit_button.grid(
        row = 6, column = 1, padx =10, pady =10,
        sticky = tkinter.S + tkinter.W)

      self._default_size()

      self._center_window()

      #self._dialog_window.mainloop()

  def _check_replay(self,OthelloGUI):

    self._check_replay_window = tkinter.Toplevel()
    self._check_replay_window.title('Replay?')

    if self._howwin.get() == 'More':
      if OthelloGUI._get_winner() == 'EVEN':
        result_label = tkinter.Label(
          master = self._check_replay_window, text = ( 'There is no winner'),
          font = DEFAULT_FONT)

        result_label.grid(
          row = 0, column = 0, columnspan = 2, padx =10, pady =10,
          sticky = tkinter.E + tkinter.W)

      elif OthelloGUI._get_winner() == 'White' or 'Black':
        result_label = tkinter.Label(
          master = self._check_replay_window, text = ( 'Game Result: {} side Won!'.format(OthelloGUI._get_winner())),
          font = DEFAULT_FONT)

        result_label.grid(
          row = 0, column = 0, columnspan = 2, padx =10, pady =10,
          sticky = tkinter.E + tkinter.W)

    elif self._howwin.get() == 'Less':
      if OthelloGUI._get_winner() == 'EVEN':
        result_label = tkinter.Label(
          master = self._check_replay_window, text = ( 'There is no winner'),
          font = DEFAULT_FONT)
        result_label.grid(
          row = 0, column = 0, columnspan = 2, padx =10, pady =10,
          sticky = tkinter.E + tkinter.W)

      elif OthelloGUI._get_winner() == 'White' or 'Black':
        result_label = tkinter.Label(
          master = self._check_replay_window, text = ( 'Game Result: {} side Lose!'.format(OthelloGUI._get_winner())),
          font = DEFAULT_FONT)
        result_label.grid(
          row = 0, column = 0, columnspan = 2, padx =10, pady =10,
          sticky = tkinter.E + tkinter.W)

    check_label = tkinter.Label(
      master = self._check_replay_window, text = ( 'Do you want to replay?'),
      font = DEFAULT_FONT)

    check_label.grid(
      row = 1, column = 0, columnspan = 2, padx =10, pady =10,
      sticky = tkinter.E + tkinter.W)

    def my_command():
      self._replay(OthelloGUI)

    replay_button = tkinter.Button(
      master = self._check_replay_window, text = 'Replay',
      font = DEFAULT_FONT,
      command = my_command)

    replay_button.grid(
      row = 2, column = 0, padx = 10,pady = 10,
      sticky = tkinter.E)

    quit_button = tkinter.Button(
      master = self._check_replay_window, text = 'Quit',
      font = DEFAULT_FONT,
      command = self._check_replay_window.destroy)

    quit_button.grid(
      row = 2, column = 1, padx = 10,pady = 10,
      sticky = tkinter.W)


    self._check_replay_window.resizable(width = False, height = False)

    self._check_replay_window.update()
    w = self._check_replay_window.winfo_width()
    h = self._check_replay_window.winfo_height()
    x = (self._check_replay_window.winfo_screenwidth() - w) // 2
    y = (self._check_replay_window.winfo_screenheight() - h) // 2
    self._check_replay_window.geometry('{:d}x{:d}+{:d}+{:d}'.format(w, h, x, y))


  def _center_window(self):
    self._dialog_window.update()
    w = self._dialog_window.winfo_width()
    h = self._dialog_window.winfo_height()
    x = (self._dialog_window.winfo_screenwidth() - w) // 2
    y = (self._dialog_window.winfo_screenheight() - h) // 2
    self._dialog_window.geometry('{:d}x{:d}+{:d}+{:d}'.format(w, h, x, y))

  def _default_size(self):
    self._dialog_window.resizable(width = False, height = False)

  def _replay(self,OthelloGUI):
    self._dialog_window.update()
    self._dialog_window.deiconify()
    self._check_replay_window.destroy()


  def _new_game(self):
    self._dialog_window.update()
    self._dialog_window.withdraw()

    self._GameSetting = {'rows':self._row.get(),
                 'columns':self._column.get(),
                 'first':self._first.get(),
                         'top_left':self._top_left.get(),
                         'howwin':self._howwin.get()}

    _game_window = OthelloGUI(self,Logic)







# -----------------------------------------------------------------------------



class OthelloGUI:
  def __init__(self,setting,Logic):

    self._setting = setting

    self._initial_info = setting._GameSetting

# import game logic
    self._logic = Logic.OthelloState(self._initial_info['rows'],self._initial_info['columns'],
                                    self._initial_info['top_left'],self._initial_info['first'])
# create game window
    self._game_window = tkinter.Toplevel()
    self._canvas = tkinter.Canvas(
      master = self._game_window,
      width = 500, height = 500,highlightthickness = 0)
    self._game_window.title('Othello')

    self._canvas.grid(
      row = 1, column = 0, padx = 10, pady = 10,
      sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

    self._game_window.aspect(self._initial_info['columns'], self._initial_info['rows'],
                             self._initial_info['columns'], self._initial_info['rows'])


# create statue bar
    self._status_bar = tkinter.Label(
      master = self._game_window, text = self._status_bar_text())
    self._status_bar.grid(
      row = 0 , column = 0, padx = 10, pady =10,
      sticky = tkinter.N + tkinter.W + tkinter.E)

#when I delete the ganme_window, pop out a new dialog window that ask user whther play again.
    self._game_window.protocol('WM_DELETE_WINDOW',self._close_window)

# create some empty staffs
    self._coordinates_list = []



# Actions
    self._game_window.bind('<Configure>',self._on_canvas_resized)
    self._canvas.bind('<Button-1>',self._on_canvas_clicked)

    self._game_window.rowconfigure(1, weight = 1)
    self._game_window.columnconfigure(0, weight = 1)




# get the right size of discs
  def _on_canvas_resized(self,event:tkinter.Event):
    current_width = self._canvas.winfo_width()
    current_height = self._canvas.winfo_height()


    xdis = current_width//self._initial_info['columns']
    ydis = current_height//self._initial_info['rows']

    self._dis = min(xdis,ydis)
    self._draw_board()

# draw board
  def _draw_board(self):
    self._canvas.delete(tkinter.ALL)
    dis = self._dis
    self._canvas.create_rectangle(0,0,dis*self._initial_info['columns'],dis*self._initial_info['rows'],fill = '#0080FF',outline = 'black',width = 1)

    for r in range(1,self._initial_info['rows']):
        self._canvas.create_line(0, dis*r, dis*self._initial_info['columns'], dis*r)

    for c in range(1,self._initial_info['columns']):
        self._canvas.create_line(dis*c,0,dis*c,dis*self._initial_info['rows'])

    for i in range(self._initial_info['rows']):
      for j in range(self._initial_info['columns']):
        if self._logic._board[i][j] == "Black":
          self._canvas.create_oval((i*dis+5),(j*dis+5),((i+1)*dis-5),((j+1)*dis-5),fill = 'black')
        elif self._logic._board[i][j] == "White":
          self._canvas.create_oval((i*dis+5),(j*dis+5),((i+1)*dis-5),((j+1)*dis-5),fill = 'white')

  def _on_canvas_clicked(self,event:tkinter.Event):
    self._draw_disc(event)

  def _draw_disc(self,event:tkinter.Event):
    clicked_xy = [event.x,event.y]

    current_width = self._canvas.winfo_width()
    current_height = self._canvas.winfo_height()

    xdis = current_width//self._initial_info['columns']
    ydis = current_height//self._initial_info['rows']

    r = event.x//xdis + 1
    c = event.y//ydis + 1

    try:
      self._logic._drop_disc(r,c)
      self._draw_board()
      self._status_bar.config(text=self._status_bar_text())

      if self._logic._end:
        self._close_window()
    except:
      pass

# get game status
  def _status_bar_text(self):
    white_disc = 0
    black_disc = 0
    for r in range(self._initial_info['rows']):
      for c in range(self._initial_info['columns']):
        if self._logic._board[r][c] == 'White':
          white_disc += 1
        elif self._logic._board[r][c] == 'Black':
          black_disc += 1
    return ("{} 's Turn, {} White discs, {} Black discs".format(self._logic._turn,white_disc,black_disc))


# get winter

  def _get_winner(self):
    return self._logic._check_winner()



  def _close_window(self):
    self._game_window.destroy()
    self._setting._check_replay(self)


if __name__ == '__main__':
  SettingGame()
