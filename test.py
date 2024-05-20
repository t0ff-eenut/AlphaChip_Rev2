
def OPCount(num: int) -> int:
    print(num)
    plus = 1
    
    if num == 1:
        return plus
    elif num % 3 == 1:
        count = OPCount(num-1)
    elif num % 3 == 0:
        count = OPCount(num / 3)
    elif num % 2 == 1:
        count = OPCount(num-1)
    elif num % 2 == 0:
        count = OPCount(num / 2)
        
    return count + plus
    #################

    #### Do not edit here ####

def main():
    num = 10000000000
    ### Edit Here ###

    #################

    #### Do not edit here ####
        
    count = OPCount(num)
    
    print("result:", count)

if __name__ == "__main__":
    main()