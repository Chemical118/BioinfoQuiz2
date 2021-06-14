from pairwise2 import *

s2 = "TGTTACG"  # 얘가 가로줄
s1 = "GGTTGAC"  # 얘가 세로줄

# local aligment에서 gap / extend / extend 와 같은 형태로 이어진다
# local aligment에서 우리가 의도한 바로 작동하도록 하려면 force_generic=True를 localms에서 사용하거나 localmc를 사용하자
t = align.globalms(s1, s2, match=1, mismatch=-1, open=-2, extend=-1, force_generic=True)

print(format_alignment(*t[0]))
