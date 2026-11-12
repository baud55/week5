
#TASK2
def directions():

#Creates and returns a list of maze directions.

# Create a list containing the navigation steps
    steps = [
        "Move Forward",
        "Move Backward",
        "Turn Left",
        "Turn Right"
    ]

# Return the list
    return steps
def run_task1():

    #Calls the directions function and displays the list.


    # Retrieve the list of directions
    steps = directions()

    # Display the list
    print(steps)

# Call the function only when this file is run directly
if __name__ == "__main__":
    run_task1()

