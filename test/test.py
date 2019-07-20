@decorator(param=1)
def f(x):
    """ Syntax Highlighting Demo
        @param x Parameter

        语义高亮：
        生成光谱以选择局部变量和参数的颜色：
         Color#1 SC1.1 SC1.2 SC1.3 SC1.4 Color#2 SC2.1 SC2.2 SC2.3 SC2.4 Color#3
         Color#3 SC3.1 SC3.2 SC3.3 SC3.4 Color#4 SC4.1 SC4.2 SC4.3 SC4.4 Color#5
    """
    s = ("Test", 2 + 3, {'a': 'b'}, f'{x!s:{"^10"}}')  # Comment
    f(s[0].lower())


class Foo:
    tags: List[str]

    def __init__(self: Foo):
        byte_string: bytes = b'newline:\n also newline:\x0a'
        text_string = u"Cyrillic Я is \u042f. Oops: \u042g"
        self.makeSense(whatever=1)

    def makeSense(self, whatever):
        self.sense = whatever


x = len('abc')
print(f.__doc__)