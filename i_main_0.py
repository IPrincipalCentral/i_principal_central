










'''



i_hello 


'''






import i_principal_central

import os

import time


global i


i = {}

i["i_class"] = i_principal_central.i_class()

i["i_class"].i_am_you()

i["i_class"].i_develope()




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


i["i_list_of_unity_in_i_unity"] = i["i_class"].i_get_quanity_from_unity(i_unity="I")


print("i['i_list_of_unity_in_i_unity'] = ", i["i_list_of_unity_in_i_unity"])
























