# city_populations.py

import sqlite3

def connect_to_database():
    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()
    return conn, cur

def display_sorted_cities(cur, order='ASC'):
    if order == 'ASC':
        cur.execute('SELECT * FROM Cities ORDER by Population ASC')
    elif order == 'DESC':
        cur.execute('SELECT * FROM Cities ORDER by Population DESC')
    elif order == 'NAME':
        cur.execute('SELECT * FROM Cities ORDER by CityName ASC')
    else:
        print("Invalid order specified.")
        return
    results = cur.fetchall()
    print('\nCities:')
    for row in results:
        print(f'{row[1]:20}Population: {row[2]:,.0f}')

def display_highest_population_city(cur):
    cur.execute('SELECT * FROM Cities ORDER BY Population DESC LIMIT 1')
    highest_population = cur.fetchone()
    print(f'\nCity with the Highest Population:')
    print(f'{highest_population[1]} (Population: {highest_population[2]:,.0f})')

def display_lowest_population_cities(cur):
    cur.execute('SELECT * FROM Cities ORDER BY Population ASC LIMIT 1')
    lowest_population = cur.fetchone()
    print(f'\nCity with the Lowest Population:')
    print(f'{lowest_population[1]} (Population: {lowest_population[2]:,.0f})')

def display_total_population(cur):
    cur.execute('SELECT SUM(Population) FROM Cities')
    total_population = cur.fetchone()[0]
    print(f'\nTotal Population of All Cities: {total_population:,.2f}')

def display_average_population(cur):
    cur.execute('SELECT AVG(Population) FROM Cities')
    average_population = cur.fetchone()[0]
    print(f'\nAverage Population of All Cities: {average_population:,.2f}')

def main():
    conn, cur = connect_to_database()

    while True:
        print("\nOperations:")
        print("1. Display cities sorted by population (ascending)")
        print("2. Display cities sorted by population (descending)")
        print("3. Display cities sorted by name")
        print("4. Display total population of all cities")
        print("5. Display average population of all cities")
        print("6. Display city with the highest population")
        print("7. Display city with the lowest population")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            display_sorted_cities(cur, 'ASC')
        elif  choice == '2':
            display_sorted_cities(cur, 'DESC')
        elif  choice == '3':
            display_sorted_cities(cur, 'NAME')
        elif  choice == '4':
            display_total_population(cur)
        elif  choice == '5':
            display_average_population(cur)
        elif  choice == '6':
            display_highest_population_city(cur)
        elif  choice == '7':
            display_lowest_population_cities(cur)
        elif  choice == '8':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

    conn.close()

if __name__ == "__main__":
    main()
