# This is a sample Python script.
import pnr2py
import re

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(pnr2py.constants.PATTERN_DATE)


lines = [
    '1 TK  192P 15SEP T DFWIST*SS1 0815P 0350P 16SEP',
    '2 TK  836P 16SEP F ISTTLV*SS1 0500P 0705P',
    '3 TK  785W 29SEP T TLVIST*SS1 1030A 1250A',
    '4 TK  191W 29SEP T ISTDFW*SS1 0200P 0645P',
    '5 QR 708V 07JUL TH IADDOH HK2  2040  1635 #1/O $ J01 E',
    '6 QR 537S 09AUG TU CCJDOH HK2  0340  0525 /O $ J02 E',
    '7. LX   41 Q  02SEP LAXZRH HK1  1925  #1525  O*       E FR  1',
    '8. LX   41 Q  02SEP LAXZRH HK1  1925  -1525  O*       E FR',
    '9. LX   41 Q  02SEP LAXZRH HK1  1925  *1525  O*       E FR  1',
]
linestring = '\n'.join(map(str,lines))
linesOneString = ("1 TK  192P 15SEP T DFWIST*SS1 0815P 0350P 16SEP\n2 TK  836P 16SEP F ISTTLV*SS1 0500P 0705P\n3 TK  "
                  "785W 29SEP T TLVIST*SS1 1030A 1250A\n4 TK  191W 29SEP T ISTDFW*SS1 0200P 0645P")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    try:
        pnr2py.Parser(linestring).parse()
    except Exception as error:
        print('An error occurred:', error)

    # matches = re.search(regex, test_str)
    #
    # if matches:
    #     print(len(matches.group()),'xxx')
    #     print("Match was found at {start}-{end}: {match}".format(start=matches.start(), end=matches.end(),
    #                                                              match=matches.group()))
    #
    #     for groupNum in range(0, len(matches.groups())):
    #         print('x')
    #         groupNum = groupNum + 1
    #
    #         print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum,
    #                                                                         start=matches.start(groupNum),
    #                                                                         end=matches.end(groupNum),
    #                                                                         group=matches.group(groupNum)))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
