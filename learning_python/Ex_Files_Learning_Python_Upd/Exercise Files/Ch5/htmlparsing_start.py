# 
# Example file for parsing and processing HTML
#
from html.parser import HTMLParser

metacount = 0

class MyHTMLParser(HTMLParser):
  def handle_comment(self, data):
    print("Encountered comment: ", data)
    pos = self.getpos() # get position where comment was encountered
    print("\tAt line: ", pos[0], " position ", pos[1])
  
  def handle_starttag(self, tag, attrs): # calls func when > reached
    global metacount
    
    if tag == 'meta':
      metacount += 1
    
    print("Encountered comment: ", tag)
    pos = self.getpos() # get position where comment was encountered
    print("\tAt line: ", pos[0], " position ", pos[1])
    
    if attrs.__len__() > 0:
      print("\tAttributes:")
      for a in attrs:
        print("\t", a[0], "=", a[1])

  def handle_endtag(self, tag):
    print("Encountered tag: ", tag) # checks for end tags
    pos = self.getpos() # get position where comment was encountered
    print("\tAt line: ", pos[0], " position ", pos[1])

  def handle_data(self, data):
    if data.isspace(): # checks for white spaces
      return
    print("Encountered data: ", data)
    pos = self.getpos() # get position where comment was encountered
    print("\tAt line: ", pos[0], " position ", pos[1])

def main():
  # instantiate the parser and feed it some HTML
  parser = MyHTMLParser()
  f = open("samplehtml.html") 
  if f.mode == 'r':
    contents = f.read()
    parser.feed(contents) # runs through html code line by line; finds code, then calls function you override in subclass

  print("Meta tags found: " + str(metacount))

if __name__ == "__main__":
  main();
  