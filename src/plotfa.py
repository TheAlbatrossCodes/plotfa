"""
plotfa defines a set of helper functions that will aid you in creating
beautifully formatted persian/farsi plots, as well as annotate them
and lots of other things.    
"""
import matplotlib as mpl
from bidi.algorithm import get_display
from arabic_reshaper import ArabicReshaper


def farsi(text):
    """Make persian text ready for plots

    Args:
        text (str): Persian text to be modified

    Returns:
        str: Modified persian text, ready to be used in plots
    """
    configuration = {
        'delete_harekat': False,
        'support_ligatures': True,
        'language': 'Farsi'
    }
    reshaper = ArabicReshaper(configuration)

    return get_display(reshaper.reshape(text))


def set_font(font_name='B Yekan'):
    """Set the font for the plot

    It's important to note that if you wish for the numbers on the plot
    to be shown in persian, you have to use the older B fonts. Using
    corrected fonts (Yekan+, etc) will make the numbers in your plots to
    show up as English.

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
    """Define a couple of settings (default, can be modified) that prettify
    the plot

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
