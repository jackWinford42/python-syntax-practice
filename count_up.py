def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    # YOUR CODE HERE
    everything_but_stop = range(start,stop)
    for num in everything_but_stop:
        print(num)
    print(stop)

count_up(5, 7)        