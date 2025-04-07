def reverse(s):
    l = list(s)
    if len(l) == 0:
        return ''
    else:
        r = l.pop()
        return r + reverse(''.join(l))

print(reverse('python'))
