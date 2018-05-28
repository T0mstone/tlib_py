class FormatCodes:
    RESET = '\033[0m'
    @staticmethod
    def FORMAT(fgcol=None, bgcol=None, modifiers=None):
        prefix = '\033['
        suffix = 'm'

        mfs = {
            'bold': 1,
            'underline': 4,
            'blink': 5,
            'rev video': 7,
            'concealed': 8,
        }
        fgadd = 30
        bgadd = 40

        colors = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

        result = ''
        if modifiers is not None:
            for modifier in modifiers:
                if type(modifier) is int and modifier in mfs.values():
                    if result == '':
                        result = str(modifier)
                    else:
                        result += ';' + str(modifier)
                elif type(modifier) is str and modifier in mfs.keys():
                    if result == '':
                        result = str(mfs[modifier])
                    else:
                        result += ';' + str(mfs[modifier])

        if fgcol in colors:
            i = colors.index(fgcol)
            result += ';' + str(i + fgadd)
        if bgcol in colors:
            i = colors.index(fgcol)
            result += ';' + str(i + bgadd)

        return prefix + result + suffix

class logger:
    def __init__(self, name):
        self.name = name

    def log(self, *args, **kwargs):
        COL = FormatCodes.FORMAT(modifiers=('bold','underline'))
        RES = FormatCodes.RESET
        COL2 = FormatCodes.FORMAT(modifiers=['bold'])
        print(COL + self.name + RES, COL2 + ':  ' + RES, *args, **kwargs)
