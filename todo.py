import sys
import os

todo = "todo.txt"
count = 1

# ensure proper usage
if len(sys.argv) <= 1:
    print("to add: python todo.py -a \"task here\"")
    print("to view: python todo.py -l")
    print("not enough arguments. exiting...")
    sys.exit(1)

# add new task
if sys.argv[1] == '-a':
    task = sys.argv[2]

    if not task:
        print("no task provided. exiting...")
        sys.exit(1)

    # first time 
    if not os.path.isfile(todo):
        with open(todo, 'w') as f:
            f.write(str(count) + ". " + task + "\n")
    
    # add new task
    else:
        count += 1
        with open(todo, 'a') as f:
            f.write(str(count) + ". " + task + "\n")

# display 
if sys.argv[1] == '-l':
    if not todo:
        print("nothing to display. add something. exiting...")
        sys.exit(1)
        
    # throw error if nothing to show
    try:
        with open(todo, 'r') as f:
            print(f.read())
    except Exception as e:
        print("nothing added. exiting...")

# further
# -a for add ... DONE
# -d delete a task
# -l display all tasks ... DONE
# -u update a task
# -t track time
# -h help page
# -v version
# -t tags/labels 
