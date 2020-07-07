def mergeInBetween(list1, list2, a, b):
    if list1 is None:
        return list2
    result_list = None
    if a == 1:
        counter = 1
        pos = list1.next
        while counter <= b and pos is not None:
            pos = pos.next
            counter += 1
        if list2 is not None:
            result_list = list2
            start = result_list
            next_node = list2.next
            while next_node is not None:
                result_list.next = next_node
                next_node = next_node.next
                result_list = result_list.next
            result_list.next = pos
            return start
        else:
            return pos

    else:
        counter = 1
        result_list = list1
        pos = list1.next
        while counter < (a - 1) and pos is not None:
            result_list.next = pos
            pos = pos.next
            result_list = result_list.next
            counter += 1
        while counter < b and pos is not None:
            pos = pos.next
        if list2 is not None:
            second_list = list2
            while second_list is not None:
                result_list.next = second_list
                second_list = second_list.next
                result_list = result_list.next
            result_list.next = pos
        else:
            result_list.next = pos
        return list1
