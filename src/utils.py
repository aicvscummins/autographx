import datetime
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path
import json

def split_paragraph(para, n):
    """Returns a string that's sliced after n words.

      Input -> string, n->after n words, adding a \n.
  """
    res = para.split()
    ans = [" ".join(res[i : i + n]) for i in range(0, len(res), n)]
    return "\n".join(ans)


def get_autographs(pathtofile):
    """Takes input to the yearbook dir and return a dictionary of all the autographs

    Arguments:
        pathtofile {[type]} -- path to the yearbook dir

    Returns:
        [dict] -- {name : {nameofautographer : autograph}
    """

    autos = {}

    path = Path(pathtofile)
    assert path.is_dir()
    file_list = []
    for x in path.iterdir():
        if x.is_dir():
            file_list.append(x)
    print(f"Found files {len(file_list)} -- {file_list}")

    for f in file_list:
        name = str(f)[len(pathtofile) + 1 :]
        autos[name] = {}
        for x in f.iterdir():
            if str(x) == f"{pathtofile}/{name}/{name}.txt":
                info_file = x
                f = open(info_file, "r").readlines()
                info_name = f[0]
                info_quote = f[1]
            elif (
                str(x) == f"{pathtofile}/{name}/{name}.jpg"
                or str(x) == f"{pathtofile}/{name}/{name}.png"
            ):
                info_img = x
            else:
                l = len(pathtofile) + len(name) + 12
                f = open(x, "r").read().replace("\n", " ").split()
                s = []
                for i in range(0, len(f), 20):
                    s.append(" ".join(f[i : i + 20]))
                output = "\n".join(s)
                autos[name][str(x)[l:-4]] = output

    return autos

    def writetofile(autos):
      with open('data.txt','w') as outfile:
        json.dump(autos,outfile)