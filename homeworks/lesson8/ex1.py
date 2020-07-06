# encoding: utf-8
class Date:
    VALUE_ERROR_TEXT = 'Неправильный формат даты!'

    def __init__(self, sourceline):
        dateline = Date.parse_dateline(sourceline)
        if self.validate(*dateline):
            self.day, self.month, self.year = dateline
        else:
            raise ValueError(Date.VALUE_ERROR_TEXT)
        print(self.day, self.month, self.year)

    @classmethod
    def parse_dateline(cls, dateline):
        datestr = dateline.split('-')
        dateint = []
        for el in datestr:
            if el.isdigit():
                dateint.append(int(el))
            else:
                raise ValueError(Date.VALUE_ERROR_TEXT)
        return dateint

    @staticmethod
    def validate(day, month, year):
        if not 0 < month < 13:
            return False

        if (not year % 4) and (year % 100 or not year % 400):
            visokos = True
        else:
            visokos = False

        if month in (1, 3, 5, 7, 8, 10, 12):
            maxday = 32
        elif month in (4, 6, 9, 11):
            maxday = 31
        elif visokos:
            maxday = 30
        else:
            maxday = 29

        if 0 < day < maxday:
            return True
        else:
            return False


datetest = Date('29-02-2000')
