def fcmb0(l):
    if len(l) == 0:
        return 0
    if l[0] == 0:
        return 1 + fcmb0(l[1:])
    return fcmb0(l[1:])


def fcmbi(l,i):
    if len(l) == 0:
        return 0
    if l[0] == i:
        return 1 + fcmbi(l[1:],i)
    return fcmbi(l[1:],i)

liste=[3,0,9,0,0,3]

print(fcmbi(liste,3))


