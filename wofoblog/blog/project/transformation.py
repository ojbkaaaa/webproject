import urllib.parse

class TF:
    def transformation_utf8(old):  # 解码，转换成utf-8中文
        new = urllib.parse.unquote(old)
        return new

    def transformation_quote(old):  # 编码，转换成unicode
        # 只对一个字符串进行urlencode转换
        new = urllib.parse.quote(old)
        return new

    def transformation_urlencode(old):
        # 把key-value这样的键值对转换成我们想要的格式，返回的是a=1&b=2这样的字符串
        new = urllib.parse.urlencode(old)
        return new


# if __name__ == '__main__':
#     old = input('someting:')
#     new = TF.transformation_utf8(old)
#     print(new)
#     t = '武逆'
#     w = TF.transformation_quote(t)
#     print(w)
