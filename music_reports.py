# CODECOOL MUSIC LIBRARY
import math
import display


def read_albums(file_path):
    data = []

    with open(file_path) as file:
        lines = file.readlines()

    for line in lines:
        splitted_line = line.strip().split(',')
        splitted_line[2] = int(splitted_line[2])
        data.append(splitted_line)

    return data


def find_albums_by_genre(genre, data):
    filtered_albums = []
    for album in data:
        if genre in album[3]:
            filtered_albums.append(album)
    return filtered_albums


def find_albums_by_time_range(data, from_time, to_time):
    filtered_albums = []
    for album in data:
        if album[2] >= from_time and album[2] <= to_time:
            filtered_albums.append(album)
    return filtered_albums


def input_time_range():
    incorrect_from_time = True
    incorrect_to_time = True

    while incorrect_from_time:
        from_time = input("Please enter from year: ")

        try:
            if from_time == "":
                from_time = 0

            from_time = int(from_time)
            incorrect_from_time = False
        except ValueError:
            print("Please enter correct number")

    while incorrect_to_time:
        to_time = input("Please enter to year: ")
        try:
            if to_time == "":
                to_time = 3000
            to_time = int(to_time)
            if from_time > to_time:
                raise ValueError

            incorrect_to_time = False
        except ValueError:
            print("Please enter correct number")

    return from_time, to_time


def find_albums_by_artist(artist, data):
    filtered_albums = []
    for album in data:
        if artist in album[0]:
            filtered_albums.append(album)
    return filtered_albums


def find_albums_by_name(name, data):
    filtered_albums = []
    for album in data:
        if name.lower() in album[1].lower():
            filtered_albums.append(album)
    return filtered_albums


def add_new_album(file_path):
    add_artist = input("Enter an artist: ")
    add_album = input("Enter an album name: ")
    incorrect_year = True
    while incorrect_year:
        try:
            add_year = int(input("Enter release year: "))
            if isinstance(add_year, int):
                incorrect_year = False
        except ValueError:
            print("Wrong value: input only digits")
    add_genre = input("Enter genre: ")
    incorrect_length = True
    while incorrect_length:
        add_length = input("Enter album length in 00:00 format: ")

        if ':' in add_length:
            try:
                split_length = add_length.split(':')
                if isinstance(int(split_length[0]), int) and isinstance(int(
                        split_length[1]), int) and len(split_length[1]) == 2 and int(split_length[1]) < 60:
                    incorrect_length = False
            except BaseException:
                print("Wrong time syntax")
        else:
            try:
                if isinstance(int(add_length), int):
                    add_length = add_length + ":00"
                    incorrect_length = False
            except BaseException:
                print("Wrong time syntax")
    with open(file_path, "a") as file:
        file.write(
            f"{add_artist},{add_album},{add_year},{add_genre},{add_length}\n")

    print(
        f"Added new album: {add_artist} | {add_album} | {add_year} | {add_genre} | {add_length}\n")


def find_shortest_longest_time(data):

    list_of_length = []

    for album in data:
        time = album[4]
        time_length = time_to_seconds(time)
        list_of_length.append(time_length)

    shortest_time = min(list_of_length)
    longest_time = max(list_of_length)

    return shortest_time, longest_time


def find_shortest_or_longest_album(data):
    length = input("Enter S for shortest or L for longest album: ")
    incorrect_length = True

    while incorrect_length:
        length = length.upper()
        if length == "S":
            incorrect_length = False
        elif length == "L":
            incorrect_length = False
        else:
            length = input("Enter S for shortest or L for longest album: ")

    if length == "S":
        return find_shortest_album(data)
    elif length == "L":
        return find_longest_album(data)


def find_longest_album(data):
    longest_time = find_shortest_longest_time(data)[1]
    longest_time_in_minutes = f"{math.floor(longest_time/60)}:{longest_time%60}"
    longest_album = []

    for album in data:
        if longest_time_in_minutes in album:
            longest_album.append(album)
    return longest_album


def find_shortest_album(data):
    shortest_time = find_shortest_longest_time(data)[0]
    shortest_time_in_minutes = f"{math.floor(shortest_time/60)}:{shortest_time%60}"
    shortest_album = []

    for album in data:
        if shortest_time_in_minutes in album:
            shortest_album.append(album)
    return shortest_album


def time_to_seconds(time):
    time = time.split(":")
    minutes_to_seconds = int(time[0]) * 60
    seconds = int(time[1])
    time_in_seconds = minutes_to_seconds + seconds

    return time_in_seconds


def years_list(data):
    list_years = []
    for year in data:
        list_years.append(int(year[2]))
    return list_years


def find_oldest_album(data):
    min_year = []
    oldest_album = []
    list_years = years_list(data)
    oldest = min(list_years)
    for index, year in enumerate(list_years):
        if oldest == year:
            min_year.append(index)
    for year in min_year:
        oldest_album.append(data[year])
    return oldest_album


def find_newest_album(data):
    max_year = []
    newest_album = []
    list_years = years_list(data)
    newest = max(list_years)
    for index, year in enumerate(list_years):
        if newest == year:
            max_year.append(index)
    for year in max_year:
        newest_album.append(data[year])
    return newest_album


def print_statistics(data):

    longest_albums = find_longest_album(data)
    longest_albums_to_print = ""
    for album in longest_albums:
        longest_albums_to_print += str(album[1]) + ", "
    longest_albums_to_print += " Length: " + str(longest_albums[0][-1])

    shortest_albums = find_shortest_album(data)
    shortest_albums_to_print = ""
    for album in shortest_albums:
        shortest_albums_to_print += str(album[1]) + ", "
    shortest_albums_to_print += " Length: " + str(shortest_albums[0][-1])

    oldest_albums = find_oldest_album(data)
    oldest_albums_to_print = ""
    for album in oldest_albums:
        oldest_albums_to_print += str(album[1]) + ", "
    oldest_albums_to_print += " Year: " + str(oldest_albums[0][2])

    youngest_albums = find_newest_album(data)
    youngest_albums_to_print = ""
    for album in youngest_albums:
        youngest_albums_to_print += str(album[1]) + ", "
    youngest_albums_to_print += " Year: " + str(youngest_albums[0][2])

    all_albums_count = str(len(data))
    additional_info = "to_be_implemented"

    print()
    print("Longest album: " + longest_albums_to_print)
    print("Shortest album: " + shortest_albums_to_print)
    print("Oldest album: " + oldest_albums_to_print)
    print("Youngest album: " + youngest_albums_to_print)
    print("All albums count: " + all_albums_count)
    print("Additional info: " + additional_info)
    print()


def main():
    path = 'text_albums_data.txt'
    albums = read_albums(path)
    is_running = True

    while is_running:

        option = display.choose_option()

        if option == "1":
            display.print_table(albums)
        elif option == "2":
            filtered_albums_by_genre = find_albums_by_genre(
                input("What type of genre do you want to find? "), albums)
            display.print_table(filtered_albums_by_genre)
        elif option == "3":
            from_time, to_time = input_time_range()
            filtered_albums_by_time_range = find_albums_by_time_range(
                albums, from_time, to_time)
            display.print_table(filtered_albums_by_time_range)
        elif option == "4":
            wanted_album = find_shortest_or_longest_album(albums)
            display.print_table(wanted_album)
        elif option == "5":
            filtered_albums_by_artist = find_albums_by_artist(
                input("Which artist do you want to find? ").title(), albums)
            display.print_table(filtered_albums_by_artist)
        elif option == "6":
            filtered_albums_by_name = find_albums_by_name(
                input("Which album do you want to find? ").title(), albums)
            display.print_table(filtered_albums_by_name)
        elif option == "add":
            add_album = add_new_album(path)
        elif option == "7":
            print_statistics(albums)
        elif option == "q":
            is_running = False


main()
