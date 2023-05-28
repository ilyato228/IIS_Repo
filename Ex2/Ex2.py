import pandas as pd


def read_database(grades_file, students_file):
    df_g = pd.read_csv(grades_file, header=None)
    df_s = pd.read_csv(students_file, header=None)
    return df_g, df_s


def get_teachers(df_grades):
    return pd.unique(df_grades[3])


def __main__():
    grades, students = read_database('./grades.csv', './students.csv')
    print('Список преподавателей:\n')
    for i in get_teachers(grades):
        print(i)


__main__()
