class happyNumbers:
    def isHappy(self, n):
        isSean = set()
        n = str(n)#Need to be a string on oreder to be iterable

        while n not in isSean:
            isSean.add(n)
            summ = 0
            for i in n:
                summ += int(i)**2#Int for maths
            if summ == 1: return True
            n = str(summ)
        return False

def main():
    f = happyNumbers()
    print(f.isHappy(19))


if __name__== '__main__':
    main()
