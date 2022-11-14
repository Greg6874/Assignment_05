#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Geisele, 11/13/2022, Modified script for assignment 5
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
dicRow = {}  # dictionary data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('')
print('The Magic CD Inventory')
while True:
    # 1. Display menu allowing the user to choose:
    print('')
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        objFile = open(strFileName,'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'ID':lstRow[0],'Title':lstRow[1],'Artist':lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()
        print()
        print('file inventory loaded to memory')
        print()
        pass
    
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow)
        
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('')
        print('ID, CD Title, Artist')        
        for row in lstTbl:
            print(str(row['ID'])+', '+row['Title']+', '+row['Artist'])
        
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        deleteRow = int(input('enter ID number to remove from database: '))
        del(lstTbl[deleteRow-1])
        pass
    
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            objFile.write(str(row['ID'])+','+row['Title']+','+row['Artist']+'\n')
        objFile.close()
        print('file saved')
        print('')
        
    else:
        print('Please choose either l, a, i, d, s or x!')































