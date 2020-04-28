#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))
print("0")
print("-------------------------------")

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))
print("1")
print("-------------------------------")

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
print("2")
print("-------------------------------")

boxes = [[1, 4, 6], [2, 20], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))
print("3")
print("-------------------------------")

boxes = [[], [], [], [], [], [], [6]]
print(canUnlockAll(boxes))
print("4")
print("-------------------------------")

boxes = [[],[5],[666],[],[],[1,2,3,4,5]]
print(canUnlockAll(boxes))
print("44")
print("-------------------------------")

boxes = [[1], [1], [], [], [], [], []]
print(canUnlockAll(boxes))
print("5")
print("-------------------------------")

boxes = [[3], [], [], [], [], [], []]
print(canUnlockAll(boxes))
print("6")
print("-------------------------------")

boxes = [[34], [], [], [], [], [], []]
print(canUnlockAll(boxes))
print("7")
print("-------------------------------")

boxes = []
print(canUnlockAll(boxes))
print("8")
print("-------------------------------")

boxes = [[1],[2],[3],[],[]],[[5],[6]]
print(canUnlockAll(boxes))
print("8")
print("-------------------------------")