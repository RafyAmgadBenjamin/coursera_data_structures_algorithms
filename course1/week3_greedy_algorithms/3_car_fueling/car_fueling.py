# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    current_pos = 0
    refills = 0
    index = 0
    original_tank = tank
    stops.append(distance)

    # counter = 0
    while current_pos <= distance:
        # counter = 0
        for i in range(index, len(stops)):
            if (current_pos + tank) - stops[i] >= 0:
                # tank -= stops[i] - current_pos
                tank = (current_pos + tank) - stops[i]
                # counter += 1  # we have fueled at least once
                current_pos = stops[i]
                index = i  # keep last reached position
                if current_pos >= distance:  # Reached the destination don't need to refill
                    return refills
            else:
                break
        if tank < original_tank:  # reached a stop station and able to fuel
            refills += 1
            tank = original_tank
            index += 1  # to get the next position and not get the same position next time
        else:
            return -1
    return refills


if __name__ == "__main__":
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
