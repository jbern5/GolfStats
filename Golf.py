import pandas as pd
import matplotlib.pyplot as plt

score_list = pd.Series([49, 44, 46, 42, 48, 45, 44, 45, 42, 43, 47, 41])
putt_list = pd.Series([17, 17, 16, 18, 19, 17, 16, 16, 16, 15, 18, 17])
chip_list = pd.Series([17, 7, 11, 8, 11, 8, 14, 10, 13, 14, 14, 6])
fir_list = pd.Series([3, 2, 3, 2, 2, 2, 2, 2, 3, 2, 1, 4])
gir_list = pd.Series([0, 2, 1, 3, 0, 1, 0, 2, 2, 2, 0, 3])

golf_stats_total_9 = {
    'Score': score_list,
    'Putts': putt_list,
    'Chips': chip_list,
    'FIR': fir_list,
    "GIR": gir_list
}
golf_stats_total_18 = {
    'Score': [92, 90],
    'Putts': [35, 33],
    'Chips': [25, 18],
    'FIR': [4, 4],
    'GIR': [0, 3]
}

df9 = pd.DataFrame(golf_stats_total_9)


def welcome():
    print("Welcome! \n"
          "To see a graph for Score vs Putts for 9 Holes, enter 1, \n"
          "To see a graph for Score vs Chips for 9 Holes, enter 2, \n"
          "To see a graph for Score vs Fairways in Regulation for 9 Holes, enter 3, \n"
          "To see a graph for Score vs Greens in Regulation for 9 Holes, enter 4 \n"
          "If you would like to quit the program, enter 0")
    choice = str(input("Choice: "))
    choices(choice)


def choices(choice):
    while 1:
        if choice == '0':
            exit(1)
        elif choice == '1':
            holes9putt()
            break
        elif choice == '2':
            holes9chip()
            break
        elif choice == '3':
            holes9fir()
            break
        elif choice == '4':
            holes9gir()
            break


def holes9putt():
    plt.scatter(df9['Score'], df9['Putts'])
    plt.title('Score vs Putts')
    plt.xlabel("Score")
    plt.ylabel("Putts")
    print(df9)
    plt.show()


def holes9chip():
    plt.scatter(df9['Score'], df9['Chips'])
    plt.title('Score vs Chips')
    plt.xlabel("Score")
    plt.ylabel("Chips")
    print(df9)
    plt.show()


def holes9fir():
    plt.scatter(df9['Score'], df9['FIR'])
    plt.title('Score vs FIR')
    plt.xlabel("Score")
    plt.ylabel("FIR")
    print(df9)
    plt.show()


def holes9gir():
    plt.scatter(df9['Score'], df9['GIR'])
    plt.title('Score vs GIR')
    plt.xlabel("Score")
    plt.ylabel("GIR")
    print(df9)
    plt.show()


welcome()
