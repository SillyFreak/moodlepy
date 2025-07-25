from moodle.attr import dataclass


@dataclass
class File:
    """File

    Args:
        component (str): component
        contextid (int): contextid
        userid (str): userid
        filearea (str): filearea
        filename (str): filename
        filepath (str): filepath
        itemid (int): itemid
        license (str): license
        author (str): author
        source (str): source
        filesize (int): filesize
    """

    component: str
    contextid: int
    userid: str
    filearea: str
    filename: str
    filepath: str
    itemid: int
    license: str
    author: str
    source: str
    filesize: int
