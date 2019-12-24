if __name__ == '__main__':
    N, M = map(int, input().split())
    def front_end_strings(remaning_spaces):
        front_string = "-" * (int(remaning_spaces / 2))
        end_string = "-" * (int(remaning_spaces / 2))
        return front_string, end_string
    def welcome_str(M):
        final_string = front_end_strings(M - 7)[0] + "welcome" + front_end_strings(M - 7)[1]
        return final_string
    def pattern_str(M, num):
        no_of_patterns = num
        final_string = front_end_strings(M - (no_of_patterns * 3))[0] + ".|." * int(num) + front_end_strings(M - (no_of_patterns * 3))[1]
        return final_string
    pattern_counter = 1
    for lines in range(0, N):
        if lines == (N - 1) / 2:
            print(welcome_str(M), end="")
        if lines < (N - 1) / 2:
            print(pattern_str(M, pattern_counter), end="")
            pattern_counter = pattern_counter + 2
        if lines > (N - 1) / 2:
            pattern_counter = pattern_counter - 2
            print(pattern_str(M, pattern_counter), end="")
        print("")

        
 OUTPUT:
---------------.|.---------------
------------.|..|..|.------------
---------.|..|..|..|..|.---------
------.|..|..|..|..|..|..|.------
---.|..|..|..|..|..|..|..|..|.---
-------------WELCOME-------------
---.|..|..|..|..|..|..|..|..|.---
------.|..|..|..|..|..|..|.------
---------.|..|..|..|..|.---------
------------.|..|..|.------------
---------------.|.---------------
        
        
        
