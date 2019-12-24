"""In this challenge, the user enters a string and a substring.
You have to print the number of times that the substring occurs in the given string.
 String traversal will take place from left to right, not from right to left."""
def count_substring(string, sub_string):
    count = 0
    counter = 0
    for s in string[:len(string)-(len(sub_string)-1)]:
        if s == sub_string[0]:
            temp_str = string[counter:counter+len(sub_string)]
            if temp_str == sub_string:
                count = count + 1
        counter = counter + 1
    return count


if __name__ == '__main__':
    # string = input().strip()
    # sub_string = input().strip()
    string = "ThIsisCoNfUsInGis"
    sub_string = "is"
    count = count_substring(string, sub_string)
    print(count)
