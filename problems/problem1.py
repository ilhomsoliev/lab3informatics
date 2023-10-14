import re
def solve(string):
    """ Возвращает количество смайликов вида =-{) в строке
    367081 % 6 = 4 => Глаза: =
    367081 % 4 = 2 => Нос: -{
    367081 % 7 = 1 => Рот: )
    """
    pattern = r'=-{\)'
    return len(re.findall(pattern, string))
