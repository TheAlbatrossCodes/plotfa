"""
plotfa defines a set of helper functions that will aid you in creating
beautifully formatted persian/farsi plots, as well as annotate them
and lots of other things.    
"""

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


