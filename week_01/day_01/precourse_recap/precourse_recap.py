import random

name = "Paul"
surname = "Ross"
profesion =  "cyclist"
age = 31
day_1 = 3.5
day_2 = 2.6
day_3 = 3
placed = 2

# It calculates and returns the average km that he traveled per day
def cal_ave(sum,times):
    average = sum/times
    return average


# It returns the number of the cyclist
def cyclist_number(name: str,surname: str):
     rand = random.randint(0, 300)
     str_num = str(rand)
     cap_name = name.capitalize()
     cap_sur = surname.capitalize()
     cycl_num = ""
     # it checks the random number digits and add zeros so it would be 3 digits number
     if len(str_num) == 3:
         cycl_num = cap_name[0] + cap_sur[0] + str_num
     elif len(str_num) == 2:
         cycl_num = cap_name[0] + cap_sur[0] + "0" + str_num   
     else:
          cycl_num = cap_name[0] + cap_sur[0] + "00" + str_num
     
     return cycl_num
          
     

# It returns the position of the cyclist     
def pos_num (pos: int):
    str_num = str(pos)
    if int(str_num[-1]) == 1:
        return str_num + "st"
    elif int(str_num[-1]) == 2:
        return str_num + "nd"
    elif int(str_num[-1]) == 3:
        return str_num + "rd"
    else:
        return str_num + "th" 
    
sum = day_1 + day_2 + day_3 #it calculates the total distance that he traveled
average = format(cal_ave(sum,3), '.2f')# it displays the average km with 2 decimal digits

# it prints a article about the cyclist
print( name.capitalize() + " " + surname.capitalize() + 
      " who particepated in Velo Grand Prix 2022 with the number " + str(cyclist_number(name,surname)) + 
      ", finished " +  pos_num(placed) + " between 300 cyclists. He traveled " + str(sum) +
      "km at the age of " + str(age) + ". He was able to do an average of " 
       + average + "km per day.")

