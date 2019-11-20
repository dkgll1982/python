class Father():
    def __init__(self):
        self.fathermoney = 10000

class Ira(Father):
    def __init__(self):
        self.iramoney = 8000
        super().__init__()

class Ivan(Father):
    '''类注释
    '''
    def __init__(self):
        self.ivanmoney = 3000
        super().__init__()
    def get_money(self):
        '''Documenet Remark
        Documenet Remark
        '''
        print('Ivan资产：',self.ivanmoney,
            '\n父亲资产：',self.fathermoney,
            '\nIra资产：',Ira().iramoney
        )

ivan = Ivan()
ivan.get_money()

ira = Ira()
print(ira.iramoney,ira.fathermoney)
print(ivan.__doc__,ivan.get_money.__doc__)