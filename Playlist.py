from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None

  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    new_song = Song(title)
    new_song.next = self.__first_song
    self.__first_song = new_song

  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    song = self.__first_song
    index = 0

    while song != None:
      if song.get_title() == title:
        return index
      index += 1
      song = song.get_next_song()
    
    return -1

  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    song = self.__first_song
    previous = None

    while song.get_title() != None:
      if song.get_title() != title:
        previous = song
        song = song.next
      
      if song.get_title() == title:
        if previous == None:
          self.__first_song = None
          return
        
        if song.next == None:
          previous.next = None
          return
        
        previous.next = song.next
        return 

  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    counter = 0
    song = self.__first_song
    
    while song != None:
      counter += 1
      song = song.next

    return counter


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    counter = 1
    song = self.__first_song

    while song != None:
      print (f'{counter}. {song}')
      song = song.next
      counter += 1

  