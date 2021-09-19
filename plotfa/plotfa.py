"""
plotfa defines a set of helper functions that will aid you in creating
beautifully formatted persian/farsi plots, as well as annotate them
and lots of other things.    
"""
import matplotlib as mpl
from bidi.algorithm import get_display
from arabic_reshaper import ArabicReshaper


def fa(text=None, from_list=None):
    """
    Make persian text ready for plots

    Can work on either a string, or a list of strings. If a list is
    passed, it will return a list, otherwise, it will return a string.

    Args:
        text (str, optional): Persian text to be modified. 
        from_list (list, optional): A list of persian text to be
          modified.

    Returns:
        str or list: If only one argument is passed to the function, it
          will return the modified persian text as a string.
          If several arguments are passed to the function, it will
          return a list of modified persian text.
    """
    configuration = {
        'delete_harekat': False,
        'support_ligatures': True,
        'language': 'Farsi'
    }

    reshaper = ArabicReshaper(configuration)
    convert = lambda txt: get_display(reshaper.reshape(txt))

    if text is not None:
        return convert(text)

    if from_list is not None:
        return [convert(txt) for txt in from_list]


def set_font(font_name='B Yekan'):
    """
    Set the font for the plot

    It's important to note that if you wish to have persian numbers on
    the plot, you have to use the older B fonts. Using any of the modern
    or corrected fonts (Yekan+, etc) will result in English numbers on
    the plot.

    You may encounter a lot of Glyph warnings thrown by matplotlib, but
    that's normal, because some of these older fonts which we rely on,
    have not defined some of the standard glyphs.

    Args:
        font_name (str, optional): [description]. Defaults to 'B Yekan'.
    """
    mpl.rcParams['font.family'] = font_name


def prettify(title_size=25,
             title_weight='heavy',
             title_pad=20,
             label_size=20,
             label_weight='heavy',
             label_pad=15,
             grid_thickness=1.3,
             grid_visibility=1.0):
    """
    Defines several modifiable settings to prettify the plots

    The settings set by this function are amongst the settings that
    users are most likely to want to change.

    Args:
        title_size (float, optional): Size of the plot's title. Defaults to 25.
        title_weight (str, optional): Weight of the plot's title.
          Possible values are:
           'ultralight', 'light', 'normal', 'regular', 'book', 'medium',
           'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy',
           'extra bold', 'black'.
          Defaults to 'heavy'.
        title_pad (float, optional): Space between axes and title.
          Defaults to 20.
        label_size (float, optional): Size of the plot's X and Y label.
          This will set the size for both Y and X label, if you wish to
          have different sizes for each X and Y, you should define them
          manually. 
          Defaults to 20.
        label_weight (str, optional): Weight of the plot's X and Y label.
          Possible values are:
           'ultralight', 'light', 'normal', 'regular', 'book', 'medium',
           'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy',
           'extra bold', 'black'.
          Defaults to 'heavy'.
        label_pad (float, optional): Space between axes and label.
          Defaults to 15.
        grid_thickness (float, optional): Thickness of the grid's lines.
          Defaults to 1.3.
        grid_visibility (float, optional): Sets the transparency (alpha
          or visibility) of the grid. Can be between 0.0 to 1.0.
          Defaults to 1.
    """
    mpl.rcParams['axes.titlesize'] = title_size
    mpl.rcParams['axes.titleweight'] = title_weight
    mpl.rcParams['axes.titlepad'] = title_pad
    mpl.rcParams['axes.labelsize'] = label_size
    mpl.rcParams['axes.labelweight'] = label_weight
    mpl.rcParams['axes.labelpad'] = label_pad
    mpl.rcParams['grid.linewidth'] = grid_thickness
    mpl.rcParams['grid.alpha'] = grid_visibility


def modify_plot(plot, title='', xlabel='', ylabel=''):
    """
    Set the plot's title and the label shown on X and Y axis.

    Keep in mind that if you want set Persian title and label on your plot,
    you should wrap the arguments you give to title, xlabel and ylabel with
    the farsi() function.

    If no argument is given to the title, xlabel or ylabel parameter, the
    plot will have no title or label.

    Args:
        plot (ax): The plot you wish to add title, xlabel and ylabel to.
        title (str, optional): The title shown on the plot. Defaults to ''.
        xlabel (str, optional): The label shown on the plot's X axis.
          Defaults to ''.
        ylabel (str, optional): The label showon the plot's Y axis.
          Defaults to ''.
    """
    plot.set_title(title)
    plot.set_xlabel(xlabel)
    plot.set_ylabel(ylabel)
