# 
# Example file for retrieving data from the internet
#
import urllib.request # provides classes and code for http requests

def main():
  webUrl = urllib.request.urlopen("http://www.google.com")
  print("result code: " + str(webUrl.getcode()))
  data = webUrl.read() #html code for url
  print(data)

if __name__ == "__main__":
  main()
