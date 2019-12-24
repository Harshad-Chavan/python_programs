if __name__ == '__main__':
    N, M = map(int, input().split())
    def welcome_str(M):
        final_string = 'WELCOME'.center(M,'-')
        return final_string
    def pattern_str(M, num):
        final_string = (".|." * num).center(M,'-')
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
        
        
        
