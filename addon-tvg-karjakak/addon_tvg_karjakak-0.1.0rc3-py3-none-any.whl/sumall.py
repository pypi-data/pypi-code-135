# -*- coding: utf-8 -*-
# Copyright (c) 2022, KarjaKAK
# All rights reserved.

import re
import os
from pathlib import Path
from itertools import islice
from dataclasses import dataclass, field
from treeview import TreeView


__all__ = ["SumAll"]


@dataclass(frozen=True, slots=True)
class SumAll(TreeView):
    """Sum all the string that converted to int or float"""

    filename: str 
    sig: str = field(kw_only= True)

    def __post_init__(self):
        if not (filename := self.findext(self.filename)):
            raise FileExistsError(f"This {filename!r} name is not exist!")    
        if not isinstance(self.sig, str):
            raise TypeError(f"Sign need to be a string type!")
        super(TreeView, self).__setattr__("filename", filename)

    def __len__(self) -> int:
        """Get the total number of indexes"""
        
        return len(self.getidx())

    @staticmethod
    def findext(filename) -> str | None:
        """Checker file path existence with TreeView format file"""

        match Path(filename):
            case pt if pt.exists() and ".txt" in pt.name:
                return str(pt.absolute())[:-4]
            case pt if os.path.exists(f"{pt.absolute()}.txt"):
                return str(pt.absolute())
            case _:
                return None

 
    def getsums(self, dt: bool = True) -> dict:
        """Sum-up every sub-node in the list"""

        lid = {}
        dgt = re.compile(r"\d+\.?\d+")
        for id in self.getidx(dt):
            addnum = 0
            for i, t in islice(self.getdata(), id, None):
                if not t.startswith("\n"):
                    match (dt, 
                            s:= dgt.match(
                                t.rpartition(" ")[2].replace(",", "")
                            ),
                            t.strip(" ").startswith("-TOTAL")
                        ):
                        case (True, s , False) if bool(s):
                            match "." in (s := s.group()):
                                case True:
                                    s = float(s)
                                case False:
                                    s = int(s)
                        case (False, s, True) if bool(s):
                            match "." in (s := s.group()):
                                case True:
                                    s = float(s)
                                case False:
                                    s = int(s)
                        case _:
                            s = 0
                    addnum += s
                else:
                    lid[i] = f"{addnum:,.2f}" if dt else addnum
                    break
            else:
                if i not in lid:
                    lid[i+1] = f"{addnum:,.2f}" if dt else addnum
        if dt: 
            return lid
        else:
            return lid.values()

    def getidx(self, dt: bool = True) -> list:
        """Getting the indicies of every node """

        idx = []
        for i, t in self.getdata():
            match (dt, t.startswith(self.sig), t.strip(" ").startswith("-TOTAL")):
                case (True, True, False):
                    idx.append(i)
                case (True, False, True):
                    idx.pop()
                case (False, True, _):
                    idx.append(i)
        return idx

    def for_graph(self) -> dict:
        """For matplotlib graph, pie chart"""

        idx = []
        if not len(self.getidx()):
            for _, t in self.getdata():
                if t.startswith(self.sig):
                    t = t[1:].replace(":","").strip()
                    match len(t) <= 20:
                        case True:
                            idx.append(f"{len(idx)+1}-{t}")
                        case False:
                            idx.append(f"{len(idx)+1}-{t[:21]}...")
            return dict(zip(idx, self.getsums(False)))
        else:
            raise ValueError("Data incomplete!")

    def lumpsum(self) -> str:
        """Summing up all total to a string as grand total"""
        
        if tup:= self.getsums(False):
            return f"{sum(tup):,.2f}"

    def sumway(self) -> None:
        """Writing total to data"""

        if idx := self.getidx():
            tot =  self.getdatanum()
            ap = tuple(f - s for f, s in zip(self.getsums().keys(), idx))
            ni = 0
            tmp = None
            for i, c, w in zip(idx, ap, self.getsums().values()):
                tmp =  ni+i+c
                if tmp < tot:
                    self.insertrow(f"TOTAL {w}", tmp, "child1")
                else:
                    self.quickchild(f"TOTAL {w}", "child1")
                ni += 1
                tot += 1
            del idx, tot, ap, ni, tmp
        else:
            raise IndexError("No indexes available!")