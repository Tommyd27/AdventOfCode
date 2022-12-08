from collections import deque


def printStacks(stacks):
	for i, stack in enumerate(stacks, 1):
		print(i, stack)
with open("input.txt") as file:
	stacks = [deque() for _ in range(9)]
	for _ in range(8):
		line = file.readline()
		for j, i in zip(range(len(line)), range(1, len(line), 4)):
			if line[i] != " ":
				stacks[j].append(line[i])
	
	file.readline()
	file.readline()
	"""for command in file.readlines():
		command = command.replace("move ", "").replace("from ", "").replace("to ", "")
		toMove, lFrom, lTo = [int(x) for x in command.split(" ")]
		for _ in range(toMove):
			stacks[lTo - 1].appendleft(stacks[lFrom - 1].popleft())"""
	for command in file.readlines():
		command = command.replace("move ", "").replace("from ", "").replace("to ", "")
		toMove, lFrom, lTo = [int(x) for x in command.split(" ")]
		printStacks(stacks)
		print("-----")
		lst = deque()
		for _ in range(toMove):
			lst.appendleft(stacks[lFrom - 1].popleft())
		print(lst)
		for _ in range(toMove):
			stacks[lTo - 1].appendleft(lst.popleft())
		printStacks(stacks)
output = ""
for stack in stacks:
	output += stack[0] if stack else " "
print(output)
