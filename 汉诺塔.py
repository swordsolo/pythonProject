# *_*coding:utf-8 *_*
# author:jijian


def hanoitower(num, a, b, c):

    if num == 1:
        print("第",1,"盘子从", a, "-->", c,sep='')

    else:
        hanoitower(num - 1, a, c, b)

        print("第", num, "盘子从", a, "-->", c,sep='')

        # hanoitower(1, a, b, c)
        hanoitower(num - 1, b, a, c)



if __name__ == "__main__":
    hanoitower(3, "A", "B", "C")
