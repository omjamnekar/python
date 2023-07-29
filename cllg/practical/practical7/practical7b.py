class GradeError(Exception):
    def __init__(self):
        self.msg = "Invaild Grade"
    
class FailError(Exception):
    def __init__(self):
        self.msg = "Fail"

try:
    gr =input("Enter your Grade:")
    if gr.upper() not in ['O','A+','A','B+','C','D','F']:
        raise GradeError
    elif gr.upper() == 'F':
      raise FailError
except GradeError as ge:
    print(ge.msg)
except FailError as fe:
    print(fe.msg)

else:
    print('pass')

