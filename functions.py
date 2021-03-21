def function():
    ans = [0x71, 0x01, 0x02, 0x03]
    ans += [0x40]
    if len(ans) > 3:
        flag = True
    else:
        flag = False
    return ans, flag

print(function()[1])

expected = function()