from urllib.request import urlopen  #this line allows us to use the urlopen() method (got this from google)
tabs_order = []   #this list will contain the keys(titles) of the opened tabs which will help us to keep track of their order.
tabs= {}          #this dictionary will contain the title, the url, the html content and the nested tabs(if there is any) for each opened tab.


def openTab(tabs_order,tabs):
  while True:             #while loop will break if the title is not empty
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
  tabs.update({title : url})        #add the title,url pair to the dictionary
  tabs_order.append(title)      #add the title to the end of list


def closetab(tabs_order,tabs):
  if len(tabs_order) > 0:
    tabIndex = input("Enter the index of the tab to be removed: ")
    if not tabIndex:                                #this condition is true if the input string is empty
      print("deleted the tab with the title: ", tabs_order[-1])
      tabs.popitem()        #this method removes the last added {key,value} pair from the dictionary
      tabs_order.pop()
    elif int(tabIndex) >= 0 and int(tabIndex) < len(tabs_order):
      print("deleted the tab with the title: ", tabs_order[int(tabIndex)])
      tabs.pop(tabs_order[int(tabIndex)])     #this method will take the key saved in the tabs_order list at the index provided by the user input and will remove the {key,value} pair from the dictionary
      tabs_order.pop(int(tabIndex))        #this method will remove the title stored in the order list
    else:
      print("invalid input")
  else:
    print("There isn't any opened tabs yet.")


def switchTab(tabs_order, tabs):
  if len(tabs_order) > 0:
    tabIndex = input("Enter the index of the tab you want to switch to: ")
    if not tabIndex:                                #this condition is true if the input string is empty
      print("Switching to the last opened tab with the title: ", tabs_order[-1])
      url = tabs[tabs_order[-1]]                          #this block of code is optained through google, and modified to fit my needs. we are taking the title of the last opened tab and the corresponding url from the dictionary,
      page = urlopen(url)                                 #and then we are opening the url using urlopen() wich will return an HTTPResponse object, and saving it in the variable page.
      page_html_bytes = page.read()                       #After that we use the .read() method on page which will return the html content as a sequence of bytes, we will store it in page_html_bytes.
      html_content = page_html_bytes.decode("utf-8")      #Finally we are decoding the sequence of bytes to a string that represents the html content, and storing it in html_content
      print("the html content for this tab is: ",html_content)
    elif int(tabIndex) >= 0 and int(tabIndex) < len(tabs_order):
      print("Switching to the tab with the title: ", tabs_order[int(tabIndex)])
      url = tabs[tabs_order[int(tabIndex)]]                          #this block does the same thing as the one above, except this time we are not taking the last opened tab,
      page = urlopen(url)                                #instead we are taking the index of the tab from the user,
      page_html_bytes = page.read()                      #and then we perform the same operations on the tab having this index.
      html_content = page_html_bytes.decode("utf-8")
      print("the html content for this tab is: ", html_content)
    else:
      print("invalid input")
  else:
    print("There isn't any opened tabs yet.")


def sortAllTabs(list1):      #this function will sort the titles of the tabs saved in the order list alphabetically
  border = 1
  while border < len(list1):
    current = border
    while current > 0 and list1[current].lower() < list1[current-1].lower():
      list1[current], list1[current-1] = list1[current-1], list1[current]
      current -= 1
    border += 1





def mainMenu(tabs_order, tabs):
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

    choice=int(input())

    if choice == 1:
      print("Adding a new tab...")
      openTab(tabs_order,tabs)
    elif choice == 2:
      print("Closing a tab...")
      closetab(tabs_order,tabs)
    elif choice == 3:
      print("Switching tabs...")
      switchTab(tabs_order, tabs)
    elif choice == 4:
      print("Displaying all tabs...")
      displayAllTabs()
    elif choice == 5:
      print("Opening nested tabs...")
      openNestedTabs()
    elif choice == 6:
      print("Sorting All tabs...")
      sortAllTabs(tabs_order)
    elif choice == 7:
      print("Saving all tabs...")
      saveAllTabs()
    elif choice == 8:
      print("Importing tabs...")
      importTabs()
    elif choice == 9:
      print("Program is closing, bye bye.")
    else:
      print("invalid input")

mainMenu(tabs_order,tabs)
#the last few lines are just for me, will be removed in future commits.
print("tabs_order: ", tabs_order)
print("tab: ", tabs.items())
print(len(tabs_order))