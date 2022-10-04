class AsciiContext:
    """
    Context class for drawing ascii shapes.
    Different mathematical shapes can be constructed with a given symbol.

    Attributes
    ----------
    symbol : char
        Symbol used for drawing.

    Methods
    -------
    get_triangle(height)
    """



    def __init__(self, symbol):
        self.symbol = symbol

    def get_triangle(self, height):
        """
        Returns ascii tirangle.

        Parameters
        ----------
        height : int
            Height of the triangle.

        Returns
        -------
        string

        Examples
        --------
        >>> self.get_triangle(15)
                      #
                     ###
                    #####
                   #######
                  #########
                 ###########
                #############
               ###############
              #################
             ###################
            #####################
           #######################
          #########################
         ###########################
        #############################
        """
        shape = ''

        for i in range(height):
            shape += (height - i - 1) * " " + (2*(i + 1) - 1) * self.symbol + (height - i - 1) * " " + '\n'

        return shape
