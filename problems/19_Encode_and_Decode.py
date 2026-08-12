test = {
    "input" : ["hello", "world"],
    "output" : "5#hello5#world"
}


def solution(value):
    encoded = ""

    if isinstance(value, list):
        for i in value:
            encoded += f"{len(i)}#" + i
        return encoded

    decoded = []
    i = 0
    j = i
    length = 0
    while i < len(value):
        while value[j] != "#":
            j += 1


        length = int(value[i:j])
        word = value[j+1 : j+1+length]
        decoded.append(word)
        i = j + length + 1
        j = i
    return decoded
        


print(solution(test["output"]))
print(solution(test["input"]))


print(solution([""]))           # empty string
print(solution(["hello#world"])) # string with # inside
print(solution(["5#hello"])) 