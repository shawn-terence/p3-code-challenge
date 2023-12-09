def bool_check(num1, num2, num3):
    # Create a list containing the input numbers
    num_list = [num1, num2, num3]

    def checker(nums):
        # Initialize an empty list for storing True or False 
        results = []
        for digit in nums:
            # Check if the digit is less than or equal to 0
            if digit <= 0:
                # Append False to results 
                results.append("False")
            else:
                # Append True to resluts
                results.append('True')
        return results

    results = checker(num_list)

    # Count the number of true or false
    result_true = results.count('True')
    result_false = results.count("False")

    # if else statement for checking if false=1 and true=2
    if result_true == 2 and result_false == 1:
        print("True")
        return "True"
    else:
        print("False")
        return "False"


bool_check(8, -1, 8)