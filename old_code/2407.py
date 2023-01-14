import math
import sys
a, b = map(int, sys.stdin.readline().split(' '))
sys.stdout.write(str(math.comb(a, b)))
#! 파이썬에는 숨겨져있지만 math.comb() 라는 조합의 개수를 리턴하는 함수도 있다.
