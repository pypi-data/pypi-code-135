#!/usr/bin/env python3

# SPDX-FileCopyrightText: © 2022 Decompollaborate
# SPDX-License-Identifier: MIT

from __future__ import annotations

import rabbitizer

from ... import common

from . import SymbolBase


class SymbolRodata(SymbolBase):
    def __init__(self, context: common.Context, vromStart: int, vromEnd: int, inFileOffset: int, vram: int, words: list[int], segmentVromStart: int, overlayCategory: str|None):
        super().__init__(context, vromStart, vromEnd, inFileOffset, vram, words, common.FileSectionType.Rodata, segmentVromStart, overlayCategory)

        self.stringEncoding: str = "EUC-JP"


    def isString(self) -> bool:
        return self.contextSym.isString()

    def isFloat(self, index: int) -> bool:
        if self.contextSym.isFloat():
            word = self.words[index]
            # Filter out NaN and infinity
            if (word & 0x7F800000) != 0x7F800000:
                return True
        return False

    def isDouble(self, index: int) -> bool:
        if self.contextSym.isDouble():
            if index + 1 < self.sizew:
                word0 = self.words[index]
                word1 = self.words[index+1]
                # Filter out NaN and infinity
                if (((word0 << 32) | word1) & 0x7FF0000000000000) != 0x7FF0000000000000:
                    # Prevent accidentally losing symbols
                    currentVram = self.getVramOffset(index*4)
                    if self.getSymbol(currentVram+4, tryPlusOffset=False) is None:
                        return True
        return False

    def isJumpTable(self) -> bool:
        # jumptables must have at least 3 labels
        if self.sizew < 3:
            return False
        return self.contextSym.isJumpTable()


    def isRdata(self) -> bool:
        "Checks if the current symbol is .rdata"
        if self.contextSym.isMaybeConstVariable():
            return True

        # This symbol could be an unreferenced non-const variable
        if self.contextSym.referenceCounter == 1:
            # This const variable was already used in a function
            return False

        return True


    def renameBasedOnType(self):
        if not common.GlobalConfig.AUTOGENERATED_NAMES_BASED_ON_DATA_TYPE:
            return

        if not self.contextSym.isAutogenerated:
            return

        if not self.isJumpTable():
            if self.isFloat(0):
                self.contextSym.name = f"FLT_{self.vram:08X}"
            elif self.isDouble(0):
                self.contextSym.name = f"DBL_{self.vram:08X}"
            elif self.isString():
                self.contextSym.name = f"STR_{self.vram:08X}"

    def analyze(self):
        if self.contextSym.isDouble():
            if self.sizew % 2 != 0:
                # doubles require an even amount of words
                self.contextSym.type = None
            else:
                for i in range(self.sizew // 2):
                    if not self.isDouble(i*2):
                        # checks there's no other overlaping symbols
                        self.contextSym.type = None
                        break

        super().analyze()


    def countExtraPadding(self) -> int:
        count = 0
        if self.isString():
            for i in range(len(self.words)-1, 0, -1):
                if self.words[i] != 0:
                    break
                if (self.words[i-1] & 0x000000FF) != 0:
                    break
                count += 1
        elif self.isDouble(0):
            for i in range(len(self.words)-1, 0, -2):
                if self.words[i] != 0 or self.words[i-1] != 0:
                    break
                count += 2
        else:
            for i in range(len(self.words)-1, 0, -1):
                if self.words[i] != 0:
                    break
                count += 1
        return count


    def getNthWord(self, i: int, canReferenceSymbolsWithAddends: bool=False, canReferenceConstants: bool=False) -> tuple[str, int]:
        if self.contextSym.isByte() or self.contextSym.isShort():
            return super().getNthWord(i, canReferenceSymbolsWithAddends, canReferenceConstants)

        localOffset = 4*i
        w = self.words[i]

        label = ""
        rodataWord: int|None = w
        value: str = f"0x{w:08X}"

        # try to get the symbol name from the offset of the file (possibly from a .o elf file)
        possibleSymbolName = self.context.getOffsetGenericSymbol(self.inFileOffset + localOffset, self.sectionType)
        if possibleSymbolName is not None:
            labelName = possibleSymbolName.getSymbolLabel()
            if labelName:
                label = labelName + common.GlobalConfig.LINE_ENDS
                if common.GlobalConfig.ASM_DATA_SYM_AS_LABEL:
                    label += f"{possibleSymbolName.getName()}:" + common.GlobalConfig.LINE_ENDS

        if len(self.context.relocSymbols[self.sectionType]) > 0:
            possibleReference = self.context.getRelocSymbol(self.inFileOffset + localOffset, self.sectionType)
            if possibleReference is not None:
                value = possibleReference.getNamePlusOffset(w)
                if possibleReference.type == common.SymbolSpecialType.jumptablelabel:
                    if w in self.context.offsetJumpTablesLabels:
                        value = self.context.offsetJumpTablesLabels[w].getName()

        dotType = ".word"
        skip = 0

        if self.isFloat(i):
            dotType = ".float"
            value = str(common.Utils.wordToFloat(w))
        elif self.isDouble(i):
            dotType = ".double"
            otherHalf = self.words[i+1]
            doubleWord = (w << 32) | otherHalf
            value = str(common.Utils.qwordToDouble(doubleWord))
            rodataWord = doubleWord
            skip = 1
        else:
            if self.contextSym.isJumpTable() and self.contextSym.isGot and common.GlobalConfig.GP_VALUE is not None:
                labelAddr = common.GlobalConfig.GP_VALUE + rabbitizer.Utils.from2Complement(w, 32)
                labelSym = self.getSymbol(labelAddr, tryPlusOffset=False)
            else:
                labelSym = self.getSymbol(w, tryPlusOffset=False)
            if labelSym is not None:
                value = labelSym.getName()
            elif self.isString():
                try:
                    buffer = bytearray(4*len(self.words))
                    common.Utils.wordsToBytes(self.words, buffer)
                    decodedStrings, rawStringSize = common.Utils.decodeString(buffer, 4*i, self.stringEncoding)

                    # dotType = ".asciz"
                    # value = f'"{decodedValue}"'
                    # value += common.GlobalConfig.LINE_ENDS + (22 * " ") + ".balign 4"
                    # rodataWord = None
                    skip = rawStringSize // 4
                    comment = self.generateAsmLineComment(localOffset)
                    result = f"{label}{comment} "

                    commentPaddingNum = 22
                    if not common.GlobalConfig.ASM_COMMENT:
                        commentPaddingNum = 1

                    if rawStringSize == 0:
                        decodedStrings.append("")
                    for decodedValue in decodedStrings[:-1]:
                        result += f'.ascii "{decodedValue}"'
                        result += common.GlobalConfig.LINE_ENDS + (commentPaddingNum * " ")
                    result += f'.asciz "{decodedStrings[-1]}"'
                    result += common.GlobalConfig.LINE_ENDS + (commentPaddingNum * " ")
                    if common.GlobalConfig.COMPILER == common.Compiler.SN64:
                        result += ".align 2"
                    else:
                        result += ".balign 4"
                    result += common.GlobalConfig.LINE_ENDS

                    return result, skip
                except (UnicodeDecodeError, RuntimeError):
                    # Not a string
                    pass

        comment = self.generateAsmLineComment(localOffset, rodataWord)
        return f"{label}{comment} {dotType} {value}" + common.GlobalConfig.LINE_ENDS, skip
