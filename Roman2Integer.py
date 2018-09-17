__author__ = "Munir Hossain"
__copyright__ = """

    Copyright 2018 <Munir Hossain>

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

"""
__license__ = "Apache 2.0"
__version__ = "1.0"


class RomanNumber(object):
    def __init__(self):
        self.symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']        

    def _int2roman(self, num, lower='I', middle='V', upper='X'):
        if num > 0 and num < 10:
            if num == 4:
                return lower + middle
            elif num == 9:
                return lower + upper
            else:
                return "{}{}".format(middle * (num // 5), lower * (num % 5))
        else:
            return ''
    
    def convert(self, decimal):
        _roman = ''
        for i, _n in enumerate(str(decimal)[::-1]):
            _symb = self.symbols[i*2:i*2+3]    
            _roman = self._int2roman(int(_n), *_symb) + _roman
        return _roman


if __name__ == "__main__":
    roman = RomanNumber()
    print(roman.convert(2021))