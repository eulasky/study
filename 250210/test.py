N = 7
switch = [1, 1, 0, 0, 1, 1, 0]
curP = 2
st = curP
end = curP
while st>=0 and end<N and switch[st] == switch[end]:
    st -= 1
    end += 1
