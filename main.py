import sys
import translate
from timeit import timeit

orig = '''# mqtl _ AlxArjy _ EvmAn _ |l _ nAzH
Allh yjEl kl mn yTEn fy AlmjAhdyn
An ytmnY Almwt wlAyjdh Allh yblAh bAnymy&amp;gt;
wlA yjd lhA mskn .
Amyn . . .'''

out = '''# mqtl _ AlxArjy _ EvmAn _ Al _ nAzH
Allh yjEl kl mn yTEn fy AlmjAhdyn
An ytmny Almwt w+ lA+ yjd +h Allh yblA +h bAnymy&amp;gt;
w+ lA yjd l +hA mskn .
Amyn ...'''

arabic_in = '''#مقتل_الخارجي_عثمان_آل_نازح
الله يجعل كل من يطعن في المجاهدين
ان يتمنى الموت ولايجده الله يبلاه بانيميأ
ولا يجد لها مسكن.
امين…'''

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("must give threads as first arg")
    threads = sys.argv[1]
    for i in range(1):
        arabic_in += '\n' + arabic_in

    print(timeit("translate.main(arabic_in, threads)", setup="from __main__ import threads, translate, arabic_in", number=1))
