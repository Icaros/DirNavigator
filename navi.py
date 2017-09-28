import os
import webbrowser
import glob


def traverseDir(path) :

    hyphen = '--'

    # Print the name of current folder.
    if path == "." :
        print(os.path.split(os.getcwd())[-1])

    # Print all the files in current directory.
    for item in os.listdir(path):
        if os.path.isfile(path + '/' + item) :
            count = path.count('/') + 1
            print( (hyphen*count), item)

    # Print recursively all the directories and all their subfolders and contents.
    for item in os.listdir(path) :
        #print(item, ' item found in ', path)
        if os.path.isdir(path + '/' + item) :
            count = path.count('/') + 1
            print((hyphen * count),  item + '/')
            traverseDir(path + '/' + item)


def gui() :

    print("####################################################################")
    print("###                                                              ###")
    print("###               /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\               ###")
    print("###               Howdy Stranger, up 4 some recon?               ###")
    print("###               \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/               ###")
    print("###                                                              ###")
    print("### Please, select the origin of your destination:               ###")
    print("### 1. [ current directory ]                                     ###")
    print("### 2. [ enter directory you wish to explore ]                   ###")
    print("### 3. [ script-kiddie hotline, 4 emergencies only! ]            ###")
    print("### 4. [ exit() ]                                                ###")
    print("###                                                              ###")
    print("####################################################################")

    while True :

        cmd = input('\nselect [1-4] : ')
        if cmd == '4' :
            print(' Sayonara, Seilor!')
            break
        elif cmd == '3' :
            webbrowser.open_new(url='https://goo.gl/ceNZ5y')
        elif cmd == '2' :
            origin = input(' enter dir: ')
            print(' ', os.path.split(origin)[-1])
            traverseDir(origin)
        else :
            traverseDir(".")


gui()
