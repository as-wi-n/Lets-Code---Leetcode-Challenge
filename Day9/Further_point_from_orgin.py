class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        move=0
        movl=0
        movr=0
        for ch in moves:
            if ch=="L":
                movl+=1
            elif ch=="R":
                movr+=1
            else:
                move+=1
        return abs(movl-movr)+move
