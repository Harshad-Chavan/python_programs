# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


def calculate_hypotenuse(sideAB, sideBC):
    sidehypo = sideAB ** 2 + sideBC ** 2
    return math.sqrt(sidehypo)


def find_all_angles(sideBC, MC, MB):
    anlge_btw_MC_BC = (sideBC ** 2 + MC ** 2 - MB ** 2) / (2 * sideBC * MC)
    anlge_btw_MC_BC = math.degrees(math.acos(anlge_btw_MC_BC))
    print(str(round(anlge_btw_MC_BC)) + '\u00b0')


try:
    # lines = []
    # while True:
    #     line = input()
    #     if line:
    #         lines.append(line)
    #     else:
    #         break
    # # print(lines)
    # sideAB, sideBC = lines
    sideAB = input()
    sideBC = input()
    MB = calculate_hypotenuse(int(sideAB), int(sideBC)) / 2
    MC = MB
    # print(MB, MC)
    find_all_angles(int(sideBC), MC, MB)
except Exception as e:
    print(e)
