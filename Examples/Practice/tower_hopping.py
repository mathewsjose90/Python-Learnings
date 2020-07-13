'''
Given a list of tower heights, check if we can cross the last tower.

At any position i in the list of value, tower[i] is the max number of towers it can travel from
that position

Ex: [3,1,0,2,0,1]

0th tower value is 3 : it means from 0th tower we can go to either 1,2 or 3rd towers.

'''

import copy


def is_hoppable(towers):
    '''
    start push down all towers from end, see if there's gap.
    :param towers:  list of tower heights
    :return:  True or False

    the process of pushing the towers down would go as follows:
    Original [4,2,0,0,2,0]
    Push(5) [4,2,0,0,2,0] (Index 5 is 0; nothing to push)
    Push(4) [4,2,0,0,1,1] (Index 4 is 2; gets pushed to Index 5)
    Push(3) [4,2,0,0,1,1] (Index 3 is 0; nothing to push)
    Push(2) [4,2,0,0,1,1] (Index 2 is 0; nothing to push)
    Push(1) [4,1,1,0,1,1] (Index 1 is 2; gets pushed to Index 2)
    Push(0) [1,2,2,1,1,1] (Index 0 is 4; gets pushed to Index 3)


    This final array does not contain a 0 and is therefore possible to complete.
    '''
    tower_copy = copy.deepcopy(towers)
    # Start from the end of the tower list
    for i in range(len(tower_copy) - 1, -1, -1):
        current_height = tower_copy[i]
        # verify how many steps we can give to the right side towers of the current postions
        extra_steps_available = current_height - 1
        if extra_steps_available >= 1:
            tower_copy[i] -= extra_steps_available
            for pos in range(i + 1, len(tower_copy)):
                # Give 1 additional height to each of the positions in the right side towers
                tower_copy[pos] += 1
                extra_steps_available -= 1
                # If no more extra steps available ,stop the pushing down and consider the next left most tower
                if extra_steps_available <= 0:
                    break
    if 0 in tower_copy:
        return False
    else:
        return True


print(is_hoppable([4, 2, 0, 0, 2, 0]))
print(is_hoppable([3, 0, 0, 2, 0, 2]))
print(is_hoppable([2, 3, 1, 1, 0, 3]))
print(is_hoppable([9, 0, 0, 0, 0, 0, 0, 1, 0]))
print(is_hoppable([5, 0, 0, 0, 0, 2, 0]))
