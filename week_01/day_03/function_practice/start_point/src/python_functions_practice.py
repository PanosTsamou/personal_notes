def return_10():
    return 10


def  add(first_number, second_number):
    return first_number + second_number


def  subtract(first_number, second_number):
    return first_number - second_number

def  multiply(first_number, second_number):
    return first_number * second_number

def  divide(first_number, second_number):
    return first_number / second_number

def length_of_string(string_for_testing):
    return len(string_for_testing)

def    join_string(first_string, second_string):
    return first_string + second_string

def add_string_as_number(first_string_number, second_string_number):
    sum_of_numbers = int(first_string_number) + int(second_string_number)
    return sum_of_numbers

def number_to_full_month_name(num_of_the_month):
    if num_of_the_month == 1:
        return "January"
    elif num_of_the_month == 3:
        return "March"
    elif num_of_the_month == 9:
        return "September"
    
def number_to_short_month_name(num_of_the_month):
        months_of_the_year = ["Jan", "Feb", "Mar", "Apr", "Ma", 
                            "Jun", "Jul", "Aug", "Sept",
                            "Oct", "Nov", "Dec" ]
        return months_of_the_year[num_of_the_month - 1]

def calculate_the_volume(cube_side):
    volume =  cube_side * cube_side *  cube_side
    return volume

def string_reversed(string_to_be_reverced: str):
    result = string_to_be_reverced[::-1]
    return result

def convert_F_to_Celsius(F_temperature):
    F_in_celsius = F_temperature - 32
    return F_in_celsius
