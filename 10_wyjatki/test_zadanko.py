def party_planner(cookies, people):
    leftovers = None
    num_each = None

    try:
        num_each = cookies // people
        lefovers = cookies % people
    except(ZeroDivisionError) as err:
        print("pamiętaj cholero, nie dziel przez zero!" + err)

    return(num_each, leftovers)


party_planner(0, 0)