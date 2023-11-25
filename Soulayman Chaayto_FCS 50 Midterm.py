def mainMenu():
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
      openTab()
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
      print("ivalid input")

mainMenu()