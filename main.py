# This is a sample Python script.
import pnr2py

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
    '10 BA 190 Q 14JUN 3 AUSLHR HK2             620P 950A+1 *1A/E*',
    '11 BA 206 Y 10JUN 2 MIALHR NN15            450P 635A+1 744 E0M',
    '1*AY4025R 09JUL SA DUBORD HK5  0930  1140 /O $ E',
    '1 DL  41K 15JUL FR LAXSYD SS1  2255  0645 #2/O $ E',
    '1 JL   5O 23JAN MO JFKHND HK2  1250  1710 #1/O $ J01 E',
    '4 JL   6Q 31DEC TH HNDJFK HK2  1105  1000 -1/O $ J02 E',
    '4 JL   6Q 31DEC TH HNDJFK HK2  1105  1000 -2/O $ J02 E',
    '1  AF3647 Y 15SEP 4 JFKFRA DK1   755P 950A 16SEP  E  0 332 D',
    '2  DL 107 Y 25SEP 7 FRAJFK DK1  1100A 130P 25SEP  E  0 332 L',
    '1  DL 041 Y 15JUL 5 LAXSYD DK1  1055P 645A 17JUL  E  0 359 D',
]
linestring = '\n'.join(map(str, lines))
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
