dic= {
    "Dhairya":"Brother",
    "Sohan":"Friend"
}
dic["Sohan"]="Brother" #mutable
updic={
    "Ishaan":"Friend",
    "Dhruv":"Friend"
}
dic.update(updic) #updating the dictionary
print(dic)
print(list(dic.keys())) #prints the list of all the keys in the dictionary
print(list(dic.values())) #prints the list of all the values in the dictionary