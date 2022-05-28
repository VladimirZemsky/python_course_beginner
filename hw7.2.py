def get_season(num_month: int):
    if 1 == num_month or 2 == num_month or 12 == num_month:
        return 'Winter'

    elif 3 == num_month or 4 == num_month or 5 == num_month:
        return 'Spring'

    elif 6 == num_month or 7 == num_month or 8 == num_month:
        return 'Summer'

    elif 9 == num_month or 10 == num_month or 11 == num_month:
        return 'Autumn'


def main():
    months = input('Enter num of month: ')
    print(get_season(int(months)))


if __name__ == "__main__":
    main()
