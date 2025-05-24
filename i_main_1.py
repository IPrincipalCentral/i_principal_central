










'''



i_hello 




i : my official link on youtube : 

www.youtube.com/@i_principal_central_official



github.com/IPrincipalCentral/i_principal_central


github.com/IPrincipalCentral1/i_principal_central_1


'''






import i_principal_central_1

import os

import time


global i


i = {}

i["i_class"] = i_principal_central_1.i_class()

i["i_class"].i_am_you()

i["i_class"].i_develope()








def min_func(min_, ele, n):


    v = min_[0]



    v1 = ele

    one_ = True

    one = True

    # anné

    if (int(v) <= int(v1)):

        if (int(v) < int(v1)):

            one_ = False


    else:

        one = False


    if (not one_):

        return min_

    elif (one):

        return min_

    else:

        return (ele, n, )



def sort_dict_element(l):


    l_ = []

    while (0 < len(l)):

        i = 0

        min_ = (l[i][1], i, )



        while (i < len(l)):

            min_0 = min_func(min_=min_, ele=l[i][1], n=i)



            if (min_0 != min_):

                min_ = min_0

            i += 1
        
        #print("min_ = ", min_)

        l_.append(l[min_[1]])

        l.pop(min_[1])

    return l_



'''








'''



t1 = time.time()

i["i_class"].i_function("i")

t2 = time.time()



print("\n\n\ni . time = ", t2 - t1, " second .\n\n\n\n")


print("\n\n\n---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("i get the list of the content of the unity-s of unity that i have here .\n\n\n\n")


i["i_list_of_i_unity"] = i["i_class"].i_get_list_of_i_unity()


print("i['i_list_of_i_unity'] = ", i["i_list_of_i_unity"])




print("\n\n\n---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("i get the list of the content of the unity-s of money that i have here .\n\n\n\n")




i["i_list_of_i_money"] = i["i_class"].i_get_list_of_i_money()


print("i['i_list_of_i_money'] = ", i["i_list_of_i_money"])





print("\n\n\n---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("i calculate how much there is in a specific folder .\n\n\n\n")


i["i_i_calcul_from_folder"] = i["i_class"].i_calcul_from_folder(i_folder=os.path.join(os.getcwd(), "i", "i_unity"))



print("i['i_i_calcul_from_folder'] = ", i["i_i_calcul_from_folder"])





i["i_list_of_dictionary"] = []

i["i_dict_to_list"] = list(i["i_i_calcul_from_folder"])


i["i_counter"] = 0


while (i["i_counter"] < len(i["i_dict_to_list"])):


    if ((len(i["i_dict_to_list"][i["i_counter"]]) > len("TheQualityOf"))):
        
        if ((not (i["i_dict_to_list"][i["i_counter"]] in i["i_list_of_dictionary"]))):
        
            if ((i["i_dict_to_list"][i["i_counter"]][:len("TheQualityOf")] != "TheQualityOf")):


               i["i_list_of_dictionary"].append(i["i_dict_to_list"][i["i_counter"]])

    else:

        if ((not (i["i_dict_to_list"][i["i_counter"]] in i["i_list_of_dictionary"]))):


            i["i_list_of_dictionary"].append(i["i_dict_to_list"][i["i_counter"]])


    i["i_counter"] += 1



print("\n\n\n\ni['i_list_of_dictionary'] = ", i["i_list_of_dictionary"])





print("\n\n\n---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("i print aspecific number from the list of i money in a specific folder .\n\n\n\n")





i["i_class"].i_print_from_money( i_unity="USD", i_quantity=1, i_folder=os.path.join(os.getcwd(), "i", "i_main"), i_number=2)








print("\n\n\n---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("i print aspecific number from the list of i unity in a specific folder .\n\n\n\n")





i["i_class"].i_print_from_unity(i_unity="I", i_quantity=1, i_folder=os.path.join(os.getcwd(), "i", "i_main"), i_number=2)



i["i_class"].i_print_from_unity(i_unity="Point", i_quantity=1, i_folder=os.path.join(os.getcwd(), "i", "i_main"), i_number=2)










print("\n\n\n---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("i get all the qualtity-s that are disponible in a specific unity from money .\n\n\n\n")


i["i_list_of_unity_in_i_money"] = i["i_class"].i_get_quanity_from_money(i_unity="PowerSupplyMoney")


print("i['i_list_of_unity_in_i_money'] = ", i["i_list_of_unity_in_i_money"])











print("\n\n\n---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("i get all the qualtity-s that are disponible in a specific unity from unity .\n\n\n\n")


i["i_list_of_unity_in_i_unity"] = i["i_class"].i_get_quanity_from_unity(i_unity="Lust")



i["list_"] = list(i["i_list_of_unity_in_i_unity"].items())



i["list_sort-ed"] = sort_dict_element(l=i["list_"])


print("i['list_sort-ed'] = ", i["list_sort-ed"])









print("\n\n\n---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("i get all the qualtity-s that are disponible in a specific unity from a specific folder .\n\n\n\n")


i["i_list_of_unity_in_i_unity_from_folder"] = i["i_class"].i_get_quanity_of_unity_from_folder(i_unity="NotSleep", i_folder=os.path.join(os.getcwd(), "i", "i_unity"))



i["list_"] = list(i["i_list_of_unity_in_i_unity_from_folder"].items())



i["list_sort-ed"] = sort_dict_element(l=i["list_"])


print("i['list_sort-ed'] = ", i["list_sort-ed"])












