class ResponseModel:
    message:str
    result:int
    body:any

    def __init__(self, msg:str = 'Success', res:int = 200, body:any = None):
        self.message = msg
        self.result = res
        self.body = body
        pass