import sys


class NewSpinner:
    """Creates new spinner"""
    def __init__(self, spinner_type=1, spinner_only=True, prefix='Progress:'):
        self.spinner_type = spinner_type
        self.prefix = prefix
        self.spinner_only= spinner_only
        self.selected_spinner = self._get_spinner_type(self.spinner_type)
    
    
    def spin(self, iteration, length):
        """This method will be used ideally in a for loop

        Args:
            iteration (int): The iteration number
            length (int): The length of the iterator used
        """
        if self.spinner_only:
            sys.stdout.write(f'{self.selected_spinner[iteration%len(self.selected_spinner)]}\r')
        else:
            sys.stdout.write(f'{self.prefix} {int(((iteration / length) * 100))}% {self.selected_spinner[iteration%len(self.selected_spinner)]}\r')
        sys.stdout.flush()
    
    def _get_spinner_type(self, spinner_type):
        """Collection of spinners.

        Args:
            spinner_type (int): Integer that will be used to get the value from the spinners dictionary.

        Raises:
            NoSpinnerFoundError: This will be raised when the given spinner type is not present in the spinners dictionary.

        Returns:
            list: It contains the spinner - Each item contains a phase of the animation.
        """
        self.spinners = {1: ['|', '/', '-', '\\'],
                         2: ['.', 'o', 'O', 'o', '.'],
                         3: ['.', 'o', 'O', '@', '*', '@', 'O', 'o', '.'],
                         4: ['←', '↖', '↑', '↗', '→', '↘', '↓', '↙'],
                         5: ['▁', '▂', '▃', '▄', '▅', '▆', '▇', '█', '▇', '▆', '▅', '▄', '▃', '▁'],
                         6: ['▖', '▘', '▝', '▗'],
                         7: ['◐', '◓', '◑', '◒'],
                         8: ['◴', '◷', '◶', '◵',],
                         9: ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷'],
                         10: ['⠁', '⠂', '⠄', '⡀', '⢀', '⠠', '⠐', '⠈'],
                         11: ['◡◡', '⊙⊙', '◠◠'],
                         12: ['◢', '◣', '◤', '◥'],
                         13: ['┤', '┘', '┴', '└', '├', '┌', '┬', '┐'],
                         14: ['▉', '▊', '▋', '▌', '▍', '▎', '▏', '▎', '▍', '▌', '▋', '▊', '▉'],
                         15: ['▌', '▀', '▐', '▄'],
                         16: ['◜ ', ' ◝', ' ◞', '◟ '],
                         17: ['@', '_@', '__@', '___@', '____@', '_____@', '______@', '_____@_', '____@__', '___@___', '__@____', '_@_____', '@______'],
                         18: ['◰', '◳', '◲', '◱'],
                         19: ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'],
                         20: ['.  ', '.. ', '...', ' ..', '  .', '   '],
                         21: ['+', 'x', '*'],
                         22: ['□', '■'],
                         23: ['■', '□', '▪', '▫'],
                         24: [' ●    ', '  ●   ', '   ●  ', '    ● ', '     ●', '    ● ', '   ●  ', '  ●   ', ' ●    ', '●     '],
                         25: ['d', 'q', 'p', 'b'],
                         26: ['oOoOoOoOoOo', 'OoOoOoOoOoO'],
                         27: ['[o_o]', '[-_o]', '[o_o]', '[o_-]'],
                         28: ['[o_o]', '[O_O]'],
                         29: ['><>     ', ' ><>    ', '  ><>   ', '   ><>  ', '    ><> ', '     ><>', '     <><', '    <>< ', '   <><  ', '  <><   ', ' <><    ', '<><     '],
                         30: ['Oooooooooo', 'oOoooooooo', 'ooOooooooo', 'oooOoooooo', 'ooooOooooo', 'oooooOoooo', 'ooooooOooo', 'oooooooOoo', 'ooooooooOo', 'oooooooooO']}
        
        if spinner_type > len(self.spinners):
            raise NoSpinnerFoundError("The given spinner doesn't exist.")
        
        return self.spinners[spinner_type]


class Error(Exception):
    """Base class for other exceptions"""
    pass


class NoSpinnerFoundError(Error):
    """Raised when given spinner doesn't exist"""
    pass
