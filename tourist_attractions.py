# PROGRAMMING ASSIGNMENT 08
# Filename: 'exercise1.py'
#
# See instructions in pdf file
#

def build_attraction_dict(filename):
    # write your code here for Task 1
    f = open(filename, 'r')
    d = {}
    for line in f:
        L = (line.strip('\n').split(','))
        d[L[1]] = L[0]      # put the keys/values into the dictionary
    f.close()
    return d
    
    
def add_attraction(d):
    # write your code here for Task 2
    attraction = input("input a new attraction: ")
    province = input("input a province: ")
    d[attraction] = province
def build_province_attraction_dict(d):
    # write your code here for Task 3
    d2 = {}
    for k, v in d.items():
        d2[v] = d2.get(v, []) + [k]     #putting provinces into keys and add attractions into the list
    return d2
        
def most_attractions(d2):
    # write your code here for Task 4
    s = set()
    for k, v in d2.items():     # add the provinces into the set if the value of that key has 3 or more items
        if len(v) >= 3:     
            s.add(k)
    return s
    
def main():
    # write your code here for Task 5
    d1 = build_attraction_dict("top_tourist_attractions.txt")
    add_attraction(d1)
    d2 = build_province_attraction_dict(d1)
    p_set = most_attractions(d2)
    print("Provinces with at least 3 attractions:")
    for province in p_set:
        print(province)
    

##########################################
# DO NOT MODIFY ANYTHING AFTER THIS LINE #
##########################################
if __name__ == '__main__':
    # run the main() function
    main()
