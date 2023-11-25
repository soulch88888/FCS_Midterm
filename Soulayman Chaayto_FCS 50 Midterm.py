tabs_order = []   #this list will contain the keys of the opened tabs which will help us to keep track of their order.
tab = {}          #this dictionary will contain the title, the url, the html content and the nested tabs(if there is any) for each opened tab.


def openTab(tabs_order,tab):
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
  tab.update({title : url})        #add the title,url pair to the dictionary
  tabs_order.append(title)      #add the title to the end of list




def mainMenu(tabs_order,tab):
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
      openTab(tabs_order,tab)
    elif choice == 2:
      print("Closing a tab...")
      closetab()
    elif choice == 3:
      print("Switching tabs...")
      switchTab()
    elif choice == 4:
      print("Displaying all tabs...")
      displayAllTabs()
    elif choice == 5:
      print("Opening nested tabs...")
      openNestedTabs()
    elif choice == 6:
      print("Sorting All tabs...")
      sortAllTabs()
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

mainMenu(tabs_order,tab)
#the last two lines are just for me, will be removed in future commits.
print("tabs_order: ", tabs_order)
print("tab: ", tab.items())
