def get_name(given_person):
    return given_person["name"]

def get_favourite_tv_show(given_person):
    return given_person["favourites"]["tv_show"]

def likes_to_eat(given_person, snack_to_check):
    for snack in given_person["favourites"]["snacks"]:
    
        if snack == snack_to_check:
            return True
    
    return False

def add_friend(given_person, new_friend):
    given_person["friends"].append(new_friend)


def remove_friend(given_person,bad_friend):
    given_person["friends"].remove(bad_friend)


def total_money(given_person):
    money = []
    for person in given_person:
        money.append(person["monies"])
    return sum(money)

def lend_money(first_person, second_person, money_to_len):
    if first_person["monies"]  >= money_to_len:
        first_person["monies"] = first_person["monies"]- money_to_len
        second_person["monies"] = second_person["monies"] + money_to_len
    else:
        print(f'{first_person["name"] } can not lent that amount of money' )

    
def all_favourite_foods(given_person):
    all_foods =[]
    for person in given_person:
        for food in person["favourites"]["snacks"]:
            all_foods.append(food)

    return all_foods

def find_no_friends(given_list_of_persons):
    no_friendly_people = []
    for person in given_list_of_persons:
        if len(person["friends"]) == 0:
            no_friendly_people.append(person)

    return no_friendly_people

def unique_favourite_tv_shows(given_list_of_persons):
    all_favourite_shows = []
    flag_oper = True
    for person in given_list_of_persons:
        if all_favourite_shows is None:
            all_favourite_shows.append(person["favourites"]["tv_show"])
        elif person["favourites"]["tv_show"] not in all_favourite_shows:
            all_favourite_shows.append(person["favourites"]["tv_show"])
        # if flag_oper:
        #     all_favourite_shows.append(person["favourites"]["tv_show"])
        #     flag_oper = False
        # else:
            # for show in    all_favourite_shows:
            #     if show != person["favourites"]["tv_show"]:
            #         all_favourite_shows.append(person["favourites"]["tv_show"])
                #     continue 
                # else:
                #     all_favourite_shows.append(person["favourites"]["tv_show"])

    return all_favourite_shows

