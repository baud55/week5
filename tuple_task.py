#ACTIVITY 1: SIMPLE TUPLE

#Create function
def likelihood():
#Populate tuple with data
    likelihoods = (50,38,27,99,4)
    #Return the smallest value in the tuple
    return min(likelihoods)

#Function to run Task 1
def run_task1():
    #Call the likelihood function and store the returned value
    minimum_value = likelihood()

    #Display the result
    print(f"Minimum likelihood of falling: {minimum_value} %")

#Call the function when the file is executed directly

if __name__ == "__main__":
    run_task1()


