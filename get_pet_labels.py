#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Shih-Chi Liu
# DATE CREATED: 02/09/2020                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Retrieve the filenames from folder pet_images/
    filename_list = listdir(image_dir)

    # Print 10, or all if <10, of the filenames from folder pet_images/
    print("\nPrints 10 filenames from folder pet_images/")
    num_print = 10
    if len(filename_list)<10:
        num_print = len(filename_list)
        
    for idx in range(0, num_print, 1):
        print("{:2d} file: {:>25}".format(idx + 1, filename_list[idx]) )
    
    # Creates empty dictionary named results_dic
    results_dic = dict()

    # Determines number of items in dictionary
    items_in_dic = len(results_dic)
    print("\nEmpty Dictionary results_dic - n items=", items_in_dic)

    # Adds new key-value pairs to dictionary ONLY when key doesn't already exist. This dictionary's value is
    # a List that contains only one item - the pet image label
    filenames = filename_list
    pet_labels = []
    
    for filename in filenames:
        # Sets string to lower case letters
        low_pet_image = filename.lower()

        # Splits lower case string by _ to break into words 
        word_list_pet_image = low_pet_image.split("_")

        # Create pet_name starting as empty string
        pet_name = ""

        # Loops to check if word in pet name is only
        # alphabetic characters - if true append word
        # to pet_name separated by trailing space 
        for word in word_list_pet_image:
           if word.isalpha():
                pet_name += word + " "
        
        # Strip off starting/trailing whitespace characters
        pet_name = pet_name.strip()

        # Prints resulting pet_name
        print("\nFilename=", filename, "   Label=", pet_name)
        pet_labels.append(pet_name)
     
    for idx in range(0, len(filenames), 1):
       if filenames[idx] not in results_dic:
           results_dic[filenames[idx]] = [pet_labels[idx]]
       else:
            print("** Warning: Key=", filenames[idx], 
                 "already exists in results_dic with value =", 
                 results_dic[filenames[idx]])

    #Iterating through a dictionary printing all keys & their associated values
    print("\nPrinting all key-value pairs in dictionary results_dic:")
    for key in results_dic:
        print("Filename=", key, "   Pet Label=", results_dic[key][0])   
    
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic