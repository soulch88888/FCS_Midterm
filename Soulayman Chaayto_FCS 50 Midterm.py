import json   #this will allow us to use the .dumps() method
from urllib.request import urlopen  #this line allows us to use the urlopen() method (got this from google)
tabs_order = []   #this list will contain the tabs(list of dictionaries) which will help us to keep track of their order.
#the dictionary will contain the title, the url, the html content and the nested tabs(if there is any) for each opened tab.

# O(n) n being the number times the user inputs an empty strings
def openTab(tabs_order):
  while True:           #while loop will break if the title is not empty
    title = input("Enter the title of the tab: ")
    if not title:
      continue
    else:
      break
  while True:               #while loop will break if the url is not empty
    url = input("Enter the URL of the tab: ")
    if not url:
      continue
    else:
      break
  tab = {"title": title,
          "url":  url}       #create a new dictionary that represents the tab
  tabs_order.append(tab)      #add the tab to the end of list

#O(n), n being the length of the tabs_order list
def closetab(tabs_order):
  if len(tabs_order) > 0:
    tabIndex = input("Enter the index of the tab to be removed: ")
    if not tabIndex:                                #this condition is true if the input string is empty
      print("deleted the tab with the title: ", tabs_order[-1]["title"])
      tabs_order.pop()
    elif int(tabIndex) >= 0 and int(tabIndex) < len(tabs_order):
      print("deleted the tab with the title: ", tabs_order[int(tabIndex)]["title"])
      tabs_order.pop(int(tabIndex))        #this method will remove the tab stored in the tabs_order list at the input index
    else:
      print("invalid input")
  else:
    print("There isn't any opened tabs yet.")

# O(n), n being the length of the tabs_order list
def switchTab(tabs_order):
  if len(tabs_order) > 0:
    tabIndex = input("Enter the index of the tab you want to switch to: ")
    if not tabIndex:                                #this condition is true if the input string is empty
      print("Switching to the last opened tab with the title: ", tabs_order[-1]["title"])
      url = tabs_order[-1]["url"]                         #this block of code is optained through google, and modified to fit my needs. we are taking the title of the last opened tab and the corresponding url from the list,
      page = urlopen(url)                                 #and then we are opening the url using urlopen() wich will return an HTTPResponse object, and saving it in the variable page.
      page_html_bytes = page.read()                       #After that we use the .read() method on page which will return the html content as a sequence of bytes, we will store it in page_html_bytes.
      html_content = page_html_bytes.decode("utf-8")      #Finally we are decoding the sequence of bytes to a string that represents the html content, and storing it in html_content
      print("the html content for this tab is: ", html_content)
    elif int(tabIndex) >= 0 and int(tabIndex) < len(tabs_order):
      print("Switching to the tab with the title: ", tabs_order[int(tabIndex)]["title"])
      url = tabs_order[int(tabIndex)]["url"]                         #this block does the same thing as the one above, except this time we are not taking the last opened tab,
      page = urlopen(url)                                #instead we are taking the index of the tab from the user,
      page_html_bytes = page.read()                      #and then we perform the same operations on the tab having this index.
      html_content = page_html_bytes.decode("utf-8")
      print("the html content for this tab is: ", html_content)
    else:
      print("invalid input")
  else:
    print("There isn't any opened tabs yet.")

# O(n*m), n being the length of the tabs_order list and m being the length of the nested tabs list
def displayAllTabs(tabs_order):
  if len(tabs_order) > 0:
    for tab in tabs_order:
      print("the title of the tab: ", tab["title"])
      if "nested tabs" in tab.keys():
          print("nested tabs inside of ", tab["title"], " are: ", tab["nested tabs"])
      else:
          print("there is no nested tabs inside: ", tab["title"])
  else:
      print("There isn't any opened tabs yet.")


# O(a*b+c), a being the length of the tabs_order list, b being the number of times the user doesnt input 2, and c being the number of times the user inputs an empty string
def openNestedTabs(tabs_order):
  while True:             #while loop will break if the index is not empty
    Index = input("Enter the index of the tab: ")
    if not Index or int(Index) > len(tabs_order)-1:
      continue
    else:
      break
  list_of_nested_tabs =[]     #we will store all the nested tabs in this list, then we will add it to the tab in the original list
  choice = -99    #dummy value
  while choice != 2:
    print("enter ")
    print("1. To insert a nested tab to: ", tabs_order[int(Index)]["title"])
    print("2. To stop")
    choice = int(input())
    if choice == 1:
      openTab(list_of_nested_tabs)
    else:
      print("added the nested tabs ")
  tabs_order[int(Index)]["nested tabs"] = list_of_nested_tabs

#O(n^2) n being the length of the list1
def sortAllTabs(list1):      #this function will sort the tabs saved in the order list alphabetically by comparing their titles, using insertion sort.
  border = 1
  while border < len(list1):
    current = border
    while current > 0 and list1[current]["title"].lower() < list1[current-1]["title"].lower():
      list1[current], list1[current-1] = list1[current-1], list1[current]
      current -= 1
    border += 1

#O(n+m), n being the length of the tabs_order list and m being the number of time the user inputs an empty path
def saveAllTabs(tabs_order):
  while True:                           #just to make sure the user doesn't input an empty path
    file_path = input("Enter the path of the file: ")
    if not file_path:
      continue
    else:
      break
  tabs_json = json.dumps(tabs_order, indent=4)      #the following code is obtained from w3schools, this line transform the data from python to json
  tabs_file = open(file_path, "w")                  #this line opens the file that has the path provided in file_path , the "w" means that we will overwrite any existing content in the file
  tabs_file.write(tabs_json)                        #this line inserts the data in tabs_json into the file
  tabs_file.close()                                 #it is a good habit to close the file after opening


#O(n+m) n being the number of times the user inputs an empty path, and m being the length of the data imported
def importTabs(tabs_order):
  while True:                           #just to make sure the user doesn't input an empty path
    file_path = input("Enter the path of the file: ")
    if not file_path:
      continue
    else:
      break
  tabs_file = open(file_path, "r")                #the following code is obtained from w3schools, this line opens the file, and since we used "r" we will be reading from this file
  imported_tabs = json.loads(tabs_file.read())    #this line does 2 things:1_ it reads the data from the file using the .read() method to read the data
                                                  #2_ it transforms the data read from json to python using the .loads() method
  tabs_order.extend(imported_tabs)                #this line takes the list (imported_tabs) and adds it to the end of tabs_order list

def mainMenu(tabs_order):
  choice=-99 # dummy value
  while choice !=9:
    print("Welcome to the browser, please choose one of the options below:")
    print("1. Open Tab")
    print("2. Close Tab")
    print("3. Switch Tab")
    print("4. Display All Tabs")
    print("5. Open Nested Tabs")
    print("6. Sort All Tabs")
    print("7. Save Tabs")
    print("8. Import Tabs")
    print("9. Exit")

    choice = int(input())

    if choice == 1:
      print("Adding a new tab...")
      openTab(tabs_order)
    elif choice == 2:
      print("Closing a tab...")
      closetab(tabs_order)
    elif choice == 3:
      print("Switching tabs...")
      switchTab(tabs_order)
    elif choice == 4:
      print("Displaying all tabs...")
      displayAllTabs(tabs_order)
    elif choice == 5:
      print("Opening nested tabs...")
      openNestedTabs(tabs_order)
    elif choice == 6:
      print("Sorting All tabs...")
      sortAllTabs(tabs_order)
    elif choice == 7:
      print("Saving all tabs...")
      saveAllTabs(tabs_order)
    elif choice == 8:
      print("Importing tabs...")
      importTabs(tabs_order)
    elif choice == 9:
      print("Program is closing, bye bye.")
    else:
      print("invalid input")

mainMenu(tabs_order)

#references:
#https://www.w3schools.com/python/
#https://realpython.com/python-web-scraping-practical-introduction/