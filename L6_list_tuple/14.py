# 14. Expense Pie Chart
# Create a text file that contains your expenses for last month in the following categories:
# • Rent
# • Gas
# • Food
# • Clothing
# • Car payment
# • Misc
# Write a Python program that reads the data from the file and uses matplotlib to plot a pie
# chart showing how you spend your money.

import matplotlib.pyplot as plt

def main():
    print("Welcome to your personal expenses asssistant")
    print("--------------------------------------------")
    print()
    while True:
        choice = get_choice()
        if choice == 1:
            list_exp = read_data()
            show_graph(list_exp)
        if choice == 2:
            modify_data()
        else:
            return


def get_choice():
    return int(input("What do you want to do?\n[1] Show your expenses\n[2] Modify expenses\n[3] Exit:\n"))


def read_data():
    with open("L6_list_tuple\\14_expense.txt", "r") as f:
        list = f.readlines()
        for i in range(len(list)):
            list[i] = list[i].rstrip('\n')
        return list



def modify_data():
    with open("L6_list_tuple\\14_expense.txt", "r") as f:
        pass


def show_graph(expenses):
    # Create a list of labels for the slices. 
    slice_labels = ['Rent', 'Gas', 'Food', 'Clothing', 'Car Payment', 'Misc']
    
    greatest = max(expenses)
    max_idx = expenses.index(greatest)
    explode = [0] * 6
    explode[max_idx] = 0.1
     
    fig1, ax1 = plt.subplots()
    ax1.pie(expenses, explode=explode, labels=slice_labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle
    centre_circle = plt.Circle((0,0),0.75,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    ax1.axis('equal')  
    plt.tight_layout()
    plt.title("Your Expenses")
    plt.show()


if __name__ == '__main__':
    main()