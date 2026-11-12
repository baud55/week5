
#TASK3
def movements():
#Create the list and add value to it
    path = ["Move Forward",10,"Move Backward",5,"Move Left",3,"Move Right",1]
#Return the list
    return path

def run_task2():
    print("Moving ....")
#Call the `movements` function
    path = movements()
#Display the movements
    print(f"{path[0]} for {path[1]}")
    print(f"{path[2]} for {path[3]}")
    print(f"{path[4]} for {path[5]}")
    print(f"{path[6]} for {path[7]}")
#Call function only when the file is executed directly
if __name__ == "__main__":
    run_task2()

