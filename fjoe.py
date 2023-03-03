class Token():
    def __init__(seth,token, marg_token):
        seth.token = token
        seth.magour_type = marg_token
        seth.tokens=[seth.token,seth.magour_type]
    def token1(seth,pin,kin):
        keywords = [Token(pin,kin),Token(kin,pin)]

        prt = keywords[0].key(kin)
        prt1 = keywords[1].key(pin)
        return [None,prt,prt1]
    
    def key(seth,password):
        return Token.hint(Token,password)
    def hint(seth,btk):
        
        seth.token_numbers = ["0","1","2","3","4","5","6","7","8","9"]
        seth.token =  btk
        for i in range(10):
            if "''" in btk:
                return ["String "+seth.token,seth.token_numbers]
            elif not "''" in btk and seth.token_numbers[i] in seth.token :
                return ["Int "+seth.token,seth.token_numbers]
            elif btk == "truex" or btk == "falsex":
                return ["Bool  "+seth.token,seth.token_numbers]
            else:
                return "ERROR"
while True:
    token = Token("INT##55",205)

    print(token.key(str(token.token1((input("passwords >")),input("pass")))))
    
