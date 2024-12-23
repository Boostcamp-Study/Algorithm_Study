word = input()
explosion = input()
explo_len = len(explosion)

answer = []
for ch in word:
    answer.append(ch)

    if len(answer) >= explo_len and "".join(answer[-explo_len:]) == explosion:
        for _ in range(explo_len):
            answer.pop()

if len(answer) == 0:
    print("FRULA")
else:
    print("".join(answer))
