#ACTIVITY 3: ITERATE

#Create function
def direction():
#Create the list
    path = ["Move Forward","Move Backward","Turn Left","Turn Right"]
#Return the list
    return path


def menu():
    #Display the menu heading
    print("Please select the direction :")
#Get the list of the direction
    steps = direction()

    for i in range(len(steps)):
        print(f"{i}: {steps[i]}")

def run_task_3():

#Run the menu function
    menu()

#Call the function only when file is executed directly

if __name__ == "__main__":
    run_task_3()