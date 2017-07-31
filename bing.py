import urllib
import webbrowser
import time
import random

def dictionary():
    words = random.choice(open("C:\Python\dictionary.txt").read().split())
    contents_of_file = words.read()
    words.close()
    enter_search(contents_of_file)

#def enter_search(text_to_enter):    
    current_time = time.ctime()
    print ("start time = " + current_time)
    connection = urllib.urlopen("https://www.bing.com/search?q="+text_to_enter)
    output = connection.read()
    print(output)
    connection.close()

dictionary()

#i = 0
#while(i<51):
    #time.sleep(0)
    #connection = urllib.urlopen("https://www.bing.com/search?q="+text_to_enter)
    #output = connection.read()
    #connection.close()
    #i=i+1
