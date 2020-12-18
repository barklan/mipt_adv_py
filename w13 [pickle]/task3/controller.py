from binarytree import Node, build
import sys
import pickle


def add(x):
    treelist.append(x)


def find(x):
    pass


def delete(x):
    pass


def print(x):
    root = build(treelist)
    root.pprint()


def clear(x):
    pass


def dump(x):
    with open('backup.pickle', 'wb') as f:
        pickle.dump(treelist, f)


def exit(x):
    sys.exit()


if __name__ == '__main__':
    global treelist

    try:
        with open('backup.pickle', 'rb') as f:
            treelist = pickle.load(f)
    except:
        treelist = []
    

    while True:
        command = list(input().split())
        cmd = command[0]
        try:
            x = int(command[1])
        except IndexError:
            x = None

        cmdlist = ['add', 'find', 'delete', 'print', 'clear', 'dump', 'exit']
        if cmd in cmdlist:
            exec(cmd + '(x)')
        else:
            print('What are you trying to do again?')