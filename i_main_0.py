










'''



i_hello 


'''



import i_principal_central

import os 


global i


i = {}

i["i_class"] = i_principal_central.i_class()

i["i_class"].i_am_you()

i["i_class"].i_develope()


i["i_class"].i_function("i")





print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("i get the list of the content of the unity-s of unity that i have here .\n\n\n\n")


i["i_list_of_i_unity"] = i["i_class"].i_get_list_of_i_unity()


print("i['i_list_of_i_unity'] = ", i["i_list_of_i_unity"])




print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("i get the list of the content of the unity-s of money that i have here .\n\n\n\n")




i["i_list_of_i_money"] = i["i_class"].i_get_list_of_i_money()


print("i['i_list_of_i_money'] = ", i["i_list_of_i_money"])





print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("i calculate how much there is in a specific folder .\n\n\n\n")


i["i_i_calcul_from_folder"] = i["i_class"].i_calcul_from_folder(i_folder=os.path.join(os.getcwd(), "i", "i_money"))



print("i['i_i_calcul_from_folder'] = ", i["i_i_calcul_from_folder"])










print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("i print aspecific number from the list of i money in a specific folder .\n\n\n\n")





i["i_class"].i_print_from_money(i_quantity=1, i_unity="USD", i_folder=os.path.join(os.getcwd(), "i", "i_main"), i_number=2)








print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("i print aspecific number from the list of i unity in a specific folder .\n\n\n\n")





i["i_class"].i_print_from_unity(i_quantity=1, i_unity="I", i_folder=os.path.join(os.getcwd(), "i", "i_main"), i_number=2)



i["i_class"].i_print_from_unity(i_quantity=1, i_unity="Point", i_folder=os.path.join(os.getcwd(), "i", "i_main"), i_number=2)











