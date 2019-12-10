'''
https://leetcode.com/problems/snapshot-array/
'''


class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.snap_dict = dict()
        self.snap_dict[0] = dict()

    def set(self, index: int, val: int) -> None:
        self.snap_dict[self.snap_id][index] = val

    def snap(self) -> int:
        self.snap_dict[self.snap_id + 1] = dict(self.snap_dict[self.snap_id])
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        if index in self.snap_dict[snap_id]:
            return self.snap_dict[snap_id][index]
        else:
            return 0

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
