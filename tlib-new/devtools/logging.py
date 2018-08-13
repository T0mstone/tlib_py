from ..basic_tools.number_tools import clamp
from ..basic_tools.string_tools import replace_multiple as replace_multi


class Colors:
    Black, Red, Green, Yellow, Blue, Magenta, Cyan, White = range(8)


class Modifiers:
    Reset, Bold, Light, Italic, Underlined, Blinking, _no_clue, InvertColors, Invisible = range(9)


class Formatter:
    _template = '\x1b[{0}m'

    @classmethod
    def get_format_sequence(cls, modifiers=None, fgcol=None, bgcol=None):
        _fgadd = 30
        _bgadd = 40

        mod_nums = []
        if type(modifiers) == list:
            for modifier in modifiers:
                mod_nums.append(str(clamp(modifier, 0, 9)))
        elif type(modifiers) == int:
            mod_nums.append(str(clamp(modifiers, 0, 9)))

        if type(fgcol) is int:
            mod_nums.append(str(_fgadd + clamp(fgcol, 0, 8)))
        if type(bgcol) is int:
            mod_nums.append(str(_bgadd + clamp(bgcol, 0, 8)))

        return cls._template.format(';'.join(mod_nums))

    @classmethod
    def format_text(cls, txt, modifiers=None, fgcol=None, bgcol=None):
        return cls.get_format_sequence(modifiers, fgcol, bgcol) + txt + cls.get_format_sequence(Modifiers.Reset)


def _replace_curlies(s):
    """ This replaces curly braces by {0} and {1} for later use in format('{', '}', ...) """
    return '{0}'.join(['{1}'.join(l) for l in [x.split('}') for x in s.split('{')]])


class Logger:
    def __init__(self, pattern, name=None, loglevel=0):
        self.name = name
        self.pattern = replace_multi(_replace_curlies(pattern), {'$text': '{2}', '$name': '{3}'})
        self.loglevel = loglevel

    def log(self, *args, sep=' ', lvl=0, levelfunc=lambda l,a: l>=a):
        if levelfunc(self.loglevel, lvl):
            text = sep.join(args)
            print(self.pattern.format('{', '}', text, self.name), end='')


fancy_logger_pattern = '[%s]: $text\n' % Formatter.format_text('$name', [Modifiers.Bold, Modifiers.Underlined])
default_logger_pattern = '[$name]: $text\n'

fancy_logger = Logger(fancy_logger_pattern, 'debug')
logger = Logger(default_logger_pattern, 'debug')