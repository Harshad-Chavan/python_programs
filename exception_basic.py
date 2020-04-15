num = int(input())
input_list = []
for _ in range(num):
    input_list.append(input())

for _ in input_list:
    try:
        x, y = list(map(int,_.split()))
        z = x // y
        print(z)
    except ZeroDivisionError as e:
        print("Error Code: " + str(e))
    except ValueError as e:
        print("Error Code: " + str(e))
    except Exception as e:
        print("Error Code: " + str(e))