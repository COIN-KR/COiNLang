class CoinLang():
    class NotSupportUnicode(Exception):
        pass
    class CodeNotString(Exception):
        pass
    class NotCoinLang(Exception):
        pass
    
    def encode(code):
        if type(code) != str:
            raise CoinLang.CodeNotString()
        elif "".join([i for i in code if 0 <= ord(i) <= 44031]) != code:
            raise CoinLang.NotSupportUnicode()
        else:
            return "".join([chr(44032+ord(i)) for i in code[::-1]])
        
    def decode(code):
        return "".join([chr(ord(i)-44032) for i in code[::-1]])
    
    def compile(code):
        try:
            return exec("".join([chr(ord(i)-44032) for i in code[::-1]]))
        except:
            raise CoinLang.NotCoinLang()
