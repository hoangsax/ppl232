# Generated from c:/Users/hoang/Desktop/New folder (2)/ppl232/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,60,438,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,1,0,5,0,90,8,0,10,0,12,0,
        93,9,0,1,0,1,0,5,0,97,8,0,10,0,12,0,100,9,0,1,0,1,0,1,1,1,1,1,1,
        4,1,107,8,1,11,1,12,1,108,1,1,3,1,112,8,1,1,2,1,2,1,2,3,2,117,8,
        2,1,2,1,2,1,2,3,2,122,8,2,1,2,1,2,3,2,126,8,2,1,3,1,3,1,3,1,3,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,5,5,142,8,5,10,5,12,5,145,
        9,5,1,5,1,5,4,5,149,8,5,11,5,12,5,150,1,5,1,5,1,5,4,5,156,8,5,11,
        5,12,5,157,1,5,3,5,161,8,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,
        7,172,8,7,1,7,4,7,175,8,7,11,7,12,7,176,1,8,1,8,1,8,1,8,1,8,1,8,
        3,8,185,8,8,1,9,1,9,1,9,1,9,1,9,3,9,192,8,9,1,10,1,10,3,10,196,8,
        10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,
        12,1,13,1,13,1,13,3,13,214,8,13,1,14,1,14,1,14,1,14,1,14,3,14,221,
        8,14,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,17,
        1,17,4,17,236,8,17,11,17,12,17,237,1,17,1,17,4,17,242,8,17,11,17,
        12,17,243,3,17,246,8,17,3,17,248,8,17,1,17,1,17,3,17,252,8,17,1,
        18,1,18,1,19,1,19,1,19,1,19,5,19,260,8,19,10,19,12,19,263,9,19,1,
        19,1,19,1,20,1,20,1,20,3,20,270,8,20,1,20,1,20,1,21,1,21,1,21,5,
        21,277,8,21,10,21,12,21,280,9,21,1,22,1,22,1,22,5,22,285,8,22,10,
        22,12,22,288,9,22,1,22,3,22,291,8,22,1,23,1,23,1,23,1,24,1,24,1,
        24,1,24,1,24,1,24,5,24,302,8,24,10,24,12,24,305,9,24,1,25,1,25,1,
        25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,317,8,25,1,26,1,26,1,
        27,1,27,1,27,3,27,324,8,27,1,28,1,28,1,28,1,28,1,29,1,29,1,29,3,
        29,333,8,29,1,30,1,30,1,30,1,30,1,30,3,30,340,8,30,1,31,1,31,1,31,
        1,31,1,31,3,31,347,8,31,1,32,1,32,1,32,1,32,1,32,3,32,354,8,32,1,
        33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,34,5,34,367,8,
        34,10,34,12,34,370,9,34,1,35,1,35,1,35,1,35,1,35,1,35,5,35,378,8,
        35,10,35,12,35,381,9,35,1,36,1,36,1,36,3,36,386,8,36,1,37,1,37,1,
        37,1,37,1,37,1,37,1,37,3,37,395,8,37,1,38,1,38,3,38,399,8,38,1,39,
        1,39,1,39,1,39,3,39,405,8,39,1,39,1,39,1,39,5,39,410,8,39,10,39,
        12,39,413,9,39,1,40,1,40,1,40,3,40,418,8,40,1,41,1,41,1,41,1,41,
        1,41,1,41,1,41,1,41,3,41,428,8,41,1,42,1,42,3,42,432,8,42,1,43,1,
        43,3,43,436,8,43,1,43,0,4,48,68,70,78,44,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,
        64,66,68,70,72,74,76,78,80,82,84,86,0,5,2,0,1,1,16,16,1,0,1,2,2,
        0,7,7,54,54,1,0,21,22,1,0,6,8,460,0,91,1,0,0,0,2,111,1,0,0,0,4,125,
        1,0,0,0,6,127,1,0,0,0,8,133,1,0,0,0,10,160,1,0,0,0,12,162,1,0,0,
        0,14,171,1,0,0,0,16,184,1,0,0,0,18,191,1,0,0,0,20,195,1,0,0,0,22,
        200,1,0,0,0,24,205,1,0,0,0,26,213,1,0,0,0,28,220,1,0,0,0,30,222,
        1,0,0,0,32,225,1,0,0,0,34,251,1,0,0,0,36,253,1,0,0,0,38,255,1,0,
        0,0,40,266,1,0,0,0,42,273,1,0,0,0,44,290,1,0,0,0,46,292,1,0,0,0,
        48,295,1,0,0,0,50,316,1,0,0,0,52,318,1,0,0,0,54,323,1,0,0,0,56,325,
        1,0,0,0,58,332,1,0,0,0,60,339,1,0,0,0,62,346,1,0,0,0,64,353,1,0,
        0,0,66,355,1,0,0,0,68,360,1,0,0,0,70,371,1,0,0,0,72,385,1,0,0,0,
        74,394,1,0,0,0,76,398,1,0,0,0,78,404,1,0,0,0,80,417,1,0,0,0,82,427,
        1,0,0,0,84,431,1,0,0,0,86,435,1,0,0,0,88,90,3,2,1,0,89,88,1,0,0,
        0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,91,
        1,0,0,0,94,98,3,6,3,0,95,97,3,2,1,0,96,95,1,0,0,0,97,100,1,0,0,0,
        98,96,1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,98,1,0,0,0,101,102,
        5,0,0,1,102,1,1,0,0,0,103,112,3,8,4,0,104,106,3,4,2,0,105,107,5,
        55,0,0,106,105,1,0,0,0,107,108,1,0,0,0,108,106,1,0,0,0,108,109,1,
        0,0,0,109,112,1,0,0,0,110,112,3,14,7,0,111,103,1,0,0,0,111,104,1,
        0,0,0,111,110,1,0,0,0,112,3,1,0,0,0,113,114,7,0,0,0,114,116,5,54,
        0,0,115,117,3,38,19,0,116,115,1,0,0,0,116,117,1,0,0,0,117,126,1,
        0,0,0,118,119,7,1,0,0,119,121,5,54,0,0,120,122,3,38,19,0,121,120,
        1,0,0,0,121,122,1,0,0,0,122,123,1,0,0,0,123,124,5,38,0,0,124,126,
        3,48,24,0,125,113,1,0,0,0,125,118,1,0,0,0,126,5,1,0,0,0,127,128,
        5,17,0,0,128,129,5,28,0,0,129,130,5,46,0,0,130,131,5,47,0,0,131,
        132,3,10,5,0,132,7,1,0,0,0,133,134,5,17,0,0,134,135,5,54,0,0,135,
        136,5,46,0,0,136,137,3,44,22,0,137,138,5,47,0,0,138,139,3,10,5,0,
        139,9,1,0,0,0,140,142,5,55,0,0,141,140,1,0,0,0,142,145,1,0,0,0,143,
        141,1,0,0,0,143,144,1,0,0,0,144,146,1,0,0,0,145,143,1,0,0,0,146,
        148,5,26,0,0,147,149,5,55,0,0,148,147,1,0,0,0,149,150,1,0,0,0,150,
        148,1,0,0,0,150,151,1,0,0,0,151,152,1,0,0,0,152,153,3,18,9,0,153,
        155,5,27,0,0,154,156,5,55,0,0,155,154,1,0,0,0,156,157,1,0,0,0,157,
        155,1,0,0,0,157,158,1,0,0,0,158,161,1,0,0,0,159,161,3,14,7,0,160,
        143,1,0,0,0,160,159,1,0,0,0,161,11,1,0,0,0,162,163,1,0,0,0,163,13,
        1,0,0,0,164,172,3,4,2,0,165,172,3,20,10,0,166,172,3,40,20,0,167,
        172,3,48,24,0,168,172,3,22,11,0,169,170,5,14,0,0,170,172,3,48,24,
        0,171,164,1,0,0,0,171,165,1,0,0,0,171,166,1,0,0,0,171,167,1,0,0,
        0,171,168,1,0,0,0,171,169,1,0,0,0,172,174,1,0,0,0,173,175,5,55,0,
        0,174,173,1,0,0,0,175,176,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,
        0,177,15,1,0,0,0,178,179,5,26,0,0,179,180,3,18,9,0,180,181,5,27,
        0,0,181,185,1,0,0,0,182,185,3,14,7,0,183,185,1,0,0,0,184,178,1,0,
        0,0,184,182,1,0,0,0,184,183,1,0,0,0,185,17,1,0,0,0,186,187,3,14,
        7,0,187,188,3,18,9,0,188,192,1,0,0,0,189,192,3,14,7,0,190,192,1,
        0,0,0,191,186,1,0,0,0,191,189,1,0,0,0,191,190,1,0,0,0,192,19,1,0,
        0,0,193,196,5,54,0,0,194,196,3,66,33,0,195,193,1,0,0,0,195,194,1,
        0,0,0,196,197,1,0,0,0,197,198,5,38,0,0,198,199,3,48,24,0,199,21,
        1,0,0,0,200,201,5,23,0,0,201,202,3,24,12,0,202,203,3,28,14,0,203,
        204,3,26,13,0,204,23,1,0,0,0,205,206,5,46,0,0,206,207,3,48,24,0,
        207,208,5,47,0,0,208,209,3,16,8,0,209,25,1,0,0,0,210,211,5,25,0,
        0,211,214,3,16,8,0,212,214,1,0,0,0,213,210,1,0,0,0,213,212,1,0,0,
        0,214,27,1,0,0,0,215,216,3,30,15,0,216,217,3,28,14,0,217,221,1,0,
        0,0,218,221,3,30,15,0,219,221,1,0,0,0,220,215,1,0,0,0,220,218,1,
        0,0,0,220,219,1,0,0,0,221,29,1,0,0,0,222,223,5,24,0,0,223,224,3,
        24,12,0,224,31,1,0,0,0,225,226,5,18,0,0,226,227,7,2,0,0,227,228,
        5,19,0,0,228,229,3,78,39,0,229,230,5,20,0,0,230,231,3,48,24,0,231,
        232,3,34,17,0,232,33,1,0,0,0,233,247,5,26,0,0,234,236,3,14,7,0,235,
        234,1,0,0,0,236,237,1,0,0,0,237,235,1,0,0,0,237,238,1,0,0,0,238,
        245,1,0,0,0,239,241,3,36,18,0,240,242,5,55,0,0,241,240,1,0,0,0,242,
        243,1,0,0,0,243,241,1,0,0,0,243,244,1,0,0,0,244,246,1,0,0,0,245,
        239,1,0,0,0,245,246,1,0,0,0,246,248,1,0,0,0,247,235,1,0,0,0,247,
        248,1,0,0,0,248,249,1,0,0,0,249,252,5,27,0,0,250,252,3,14,7,0,251,
        233,1,0,0,0,251,250,1,0,0,0,252,35,1,0,0,0,253,254,7,3,0,0,254,37,
        1,0,0,0,255,256,5,50,0,0,256,261,5,7,0,0,257,258,5,52,0,0,258,260,
        5,7,0,0,259,257,1,0,0,0,260,263,1,0,0,0,261,259,1,0,0,0,261,262,
        1,0,0,0,262,264,1,0,0,0,263,261,1,0,0,0,264,265,5,51,0,0,265,39,
        1,0,0,0,266,267,5,54,0,0,267,269,5,46,0,0,268,270,3,48,24,0,269,
        268,1,0,0,0,269,270,1,0,0,0,270,271,1,0,0,0,271,272,5,47,0,0,272,
        41,1,0,0,0,273,278,3,48,24,0,274,275,5,52,0,0,275,277,3,48,24,0,
        276,274,1,0,0,0,277,280,1,0,0,0,278,276,1,0,0,0,278,279,1,0,0,0,
        279,43,1,0,0,0,280,278,1,0,0,0,281,286,3,46,23,0,282,283,5,52,0,
        0,283,285,3,46,23,0,284,282,1,0,0,0,285,288,1,0,0,0,286,284,1,0,
        0,0,286,287,1,0,0,0,287,291,1,0,0,0,288,286,1,0,0,0,289,291,1,0,
        0,0,290,281,1,0,0,0,290,289,1,0,0,0,291,45,1,0,0,0,292,293,5,1,0,
        0,293,294,5,54,0,0,294,47,1,0,0,0,295,296,6,24,-1,0,296,297,3,50,
        25,0,297,303,1,0,0,0,298,299,10,2,0,0,299,300,5,3,0,0,300,302,3,
        50,25,0,301,298,1,0,0,0,302,305,1,0,0,0,303,301,1,0,0,0,303,304,
        1,0,0,0,304,49,1,0,0,0,305,303,1,0,0,0,306,317,3,74,37,0,307,317,
        3,78,39,0,308,317,3,82,41,0,309,317,3,54,27,0,310,317,3,56,28,0,
        311,317,5,6,0,0,312,313,5,46,0,0,313,314,3,50,25,0,314,315,5,47,
        0,0,315,317,1,0,0,0,316,306,1,0,0,0,316,307,1,0,0,0,316,308,1,0,
        0,0,316,309,1,0,0,0,316,310,1,0,0,0,316,311,1,0,0,0,316,312,1,0,
        0,0,317,51,1,0,0,0,318,319,7,4,0,0,319,53,1,0,0,0,320,324,5,54,0,
        0,321,324,3,66,33,0,322,324,3,40,20,0,323,320,1,0,0,0,323,321,1,
        0,0,0,323,322,1,0,0,0,324,55,1,0,0,0,325,326,5,50,0,0,326,327,3,
        58,29,0,327,328,5,51,0,0,328,57,1,0,0,0,329,333,3,60,30,0,330,333,
        3,62,31,0,331,333,3,64,32,0,332,329,1,0,0,0,332,330,1,0,0,0,332,
        331,1,0,0,0,333,59,1,0,0,0,334,335,5,7,0,0,335,336,5,52,0,0,336,
        340,3,60,30,0,337,340,5,7,0,0,338,340,3,54,27,0,339,334,1,0,0,0,
        339,337,1,0,0,0,339,338,1,0,0,0,340,61,1,0,0,0,341,342,5,6,0,0,342,
        343,5,52,0,0,343,347,3,62,31,0,344,347,5,6,0,0,345,347,3,54,27,0,
        346,341,1,0,0,0,346,344,1,0,0,0,346,345,1,0,0,0,347,63,1,0,0,0,348,
        349,5,8,0,0,349,350,5,52,0,0,350,354,3,64,32,0,351,354,5,8,0,0,352,
        354,3,54,27,0,353,348,1,0,0,0,353,351,1,0,0,0,353,352,1,0,0,0,354,
        65,1,0,0,0,355,356,5,54,0,0,356,357,5,50,0,0,357,358,3,68,34,0,358,
        359,5,51,0,0,359,67,1,0,0,0,360,361,6,34,-1,0,361,362,3,70,35,0,
        362,368,1,0,0,0,363,364,10,2,0,0,364,365,5,52,0,0,365,367,3,68,34,
        0,366,363,1,0,0,0,367,370,1,0,0,0,368,366,1,0,0,0,368,369,1,0,0,
        0,369,69,1,0,0,0,370,368,1,0,0,0,371,372,6,35,-1,0,372,373,3,72,
        36,0,373,379,1,0,0,0,374,375,10,2,0,0,375,376,5,3,0,0,376,378,3,
        72,36,0,377,374,1,0,0,0,378,381,1,0,0,0,379,377,1,0,0,0,379,380,
        1,0,0,0,380,71,1,0,0,0,381,379,1,0,0,0,382,386,5,7,0,0,383,386,3,
        74,37,0,384,386,3,54,27,0,385,382,1,0,0,0,385,383,1,0,0,0,385,384,
        1,0,0,0,386,73,1,0,0,0,387,388,3,76,38,0,388,389,5,3,0,0,389,390,
        3,74,37,0,390,395,1,0,0,0,391,392,5,30,0,0,392,395,3,74,37,0,393,
        395,3,76,38,0,394,387,1,0,0,0,394,391,1,0,0,0,394,393,1,0,0,0,395,
        75,1,0,0,0,396,399,5,7,0,0,397,399,3,54,27,0,398,396,1,0,0,0,398,
        397,1,0,0,0,399,77,1,0,0,0,400,401,6,39,-1,0,401,405,3,80,40,0,402,
        403,5,34,0,0,403,405,3,78,39,1,404,400,1,0,0,0,404,402,1,0,0,0,405,
        411,1,0,0,0,406,407,10,3,0,0,407,408,5,4,0,0,408,410,3,80,40,0,409,
        406,1,0,0,0,410,413,1,0,0,0,411,409,1,0,0,0,411,412,1,0,0,0,412,
        79,1,0,0,0,413,411,1,0,0,0,414,418,5,8,0,0,415,418,3,82,41,0,416,
        418,3,54,27,0,417,414,1,0,0,0,417,415,1,0,0,0,417,416,1,0,0,0,418,
        81,1,0,0,0,419,420,3,84,42,0,420,421,5,5,0,0,421,422,3,84,42,0,422,
        428,1,0,0,0,423,424,3,86,43,0,424,425,5,45,0,0,425,426,3,86,43,0,
        426,428,1,0,0,0,427,419,1,0,0,0,427,423,1,0,0,0,428,83,1,0,0,0,429,
        432,5,7,0,0,430,432,3,54,27,0,431,429,1,0,0,0,431,430,1,0,0,0,432,
        85,1,0,0,0,433,436,5,6,0,0,434,436,3,54,27,0,435,433,1,0,0,0,435,
        434,1,0,0,0,436,87,1,0,0,0,46,91,98,108,111,116,121,125,143,150,
        157,160,171,176,184,191,195,213,220,237,243,245,247,251,261,269,
        278,286,290,303,316,323,332,339,346,353,368,379,385,394,398,404,
        411,417,427,431,435
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'elif'", "'else'", "'begin'", "'end'", "'main'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'not'", "'and'", 
                     "'or'", "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'...'", "'=='", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "TYPE", "IMPLIKEYS", "NUMOP", "LOGICOPBIN", 
                      "NUMRELAOPS", "STRINGLIT", "NUMLIT", "BOOLIT", "TRUE", 
                      "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
                      "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                      "CONTINUE", "IF", "ELIF", "ELSE", "BEGIN", "END", 
                      "MAIN", "PLUS", "MINUS", "STAR", "SLASH", "PERCENT", 
                      "NOT", "AND", "OR", "EQUAL", "ASSIGN", "INEQUAL", 
                      "LESSTHAN", "LESSEQUAL", "MORETHAN", "MOREEQUAL", 
                      "ELLIPSIS", "EQUALITY", "LB", "RB", "LC", "RC", "LS", 
                      "RS", "COMMA", "COMMENT", "ID", "NEWLINE", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ES" ]

    RULE_program = 0
    RULE_other = 1
    RULE_valdecl = 2
    RULE_mainfunc = 3
    RULE_funcdecl = 4
    RULE_funcblock = 5
    RULE_stmts = 6
    RULE_stmt = 7
    RULE_stmtblock = 8
    RULE_stmtlist = 9
    RULE_assignstmt = 10
    RULE_ifstmt = 11
    RULE_ifblock = 12
    RULE_elseblk = 13
    RULE_elifblk = 14
    RULE_elifblk_0 = 15
    RULE_forstmt = 16
    RULE_loopblock = 17
    RULE_loopkey = 18
    RULE_arraydecl = 19
    RULE_funcall = 20
    RULE_paramcall = 21
    RULE_paramlist = 22
    RULE_params = 23
    RULE_exp = 24
    RULE_exp_01 = 25
    RULE_exp_00 = 26
    RULE_expall = 27
    RULE_array = 28
    RULE_explist = 29
    RULE_explist_1 = 30
    RULE_explist_2 = 31
    RULE_explist_3 = 32
    RULE_indexp = 33
    RULE_indop = 34
    RULE_indop_0 = 35
    RULE_indop_1 = 36
    RULE_ariexp = 37
    RULE_ariexp_00 = 38
    RULE_logicexp = 39
    RULE_logicexp_00 = 40
    RULE_relatexp = 41
    RULE_relatexp_00 = 42
    RULE_relatexp_01 = 43

    ruleNames =  [ "program", "other", "valdecl", "mainfunc", "funcdecl", 
                   "funcblock", "stmts", "stmt", "stmtblock", "stmtlist", 
                   "assignstmt", "ifstmt", "ifblock", "elseblk", "elifblk", 
                   "elifblk_0", "forstmt", "loopblock", "loopkey", "arraydecl", 
                   "funcall", "paramcall", "paramlist", "params", "exp", 
                   "exp_01", "exp_00", "expall", "array", "explist", "explist_1", 
                   "explist_2", "explist_3", "indexp", "indop", "indop_0", 
                   "indop_1", "ariexp", "ariexp_00", "logicexp", "logicexp_00", 
                   "relatexp", "relatexp_00", "relatexp_01" ]

    EOF = Token.EOF
    TYPE=1
    IMPLIKEYS=2
    NUMOP=3
    LOGICOPBIN=4
    NUMRELAOPS=5
    STRINGLIT=6
    NUMLIT=7
    BOOLIT=8
    TRUE=9
    FALSE=10
    NUMBER=11
    BOOL=12
    STRING=13
    RETURN=14
    VAR=15
    DYNAMIC=16
    FUNC=17
    FOR=18
    UNTIL=19
    BY=20
    BREAK=21
    CONTINUE=22
    IF=23
    ELIF=24
    ELSE=25
    BEGIN=26
    END=27
    MAIN=28
    PLUS=29
    MINUS=30
    STAR=31
    SLASH=32
    PERCENT=33
    NOT=34
    AND=35
    OR=36
    EQUAL=37
    ASSIGN=38
    INEQUAL=39
    LESSTHAN=40
    LESSEQUAL=41
    MORETHAN=42
    MOREEQUAL=43
    ELLIPSIS=44
    EQUALITY=45
    LB=46
    RB=47
    LC=48
    RC=49
    LS=50
    RS=51
    COMMA=52
    COMMENT=53
    ID=54
    NEWLINE=55
    WS=56
    ERROR_CHAR=57
    UNCLOSE_STRING=58
    ILLEGAL_ESCAPE=59
    ES=60

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mainfunc(self):
            return self.getTypedRuleContext(ZCodeParser.MainfuncContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def other(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.OtherContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.OtherContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_program




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 88
                    self.other() 
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 94
            self.mainfunc()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 19210685422715334) != 0):
                self.state = 95
                self.other()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 101
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OtherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdecl(self):
            return self.getTypedRuleContext(ZCodeParser.FuncdeclContext,0)


        def valdecl(self):
            return self.getTypedRuleContext(ZCodeParser.ValdeclContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_other




    def other(self):

        localctx = ZCodeParser.OtherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_other)
        self._la = 0 # Token type
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.funcdecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.valdecl()
                self.state = 106 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 105
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 108 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==55):
                        break

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 110
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def TYPE(self):
            return self.getToken(ZCodeParser.TYPE, 0)

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def arraydecl(self):
            return self.getTypedRuleContext(ZCodeParser.ArraydeclContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def IMPLIKEYS(self):
            return self.getToken(ZCodeParser.IMPLIKEYS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_valdecl




    def valdecl(self):

        localctx = ZCodeParser.ValdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_valdecl)
        self._la = 0 # Token type
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                _la = self._input.LA(1)
                if not(_la==1 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 114
                self.match(ZCodeParser.ID)
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==50:
                    self.state = 115
                    self.arraydecl()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 119
                self.match(ZCodeParser.ID)
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==50:
                    self.state = 120
                    self.arraydecl()


                self.state = 123
                self.match(ZCodeParser.ASSIGN)
                self.state = 124
                self.exp(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def MAIN(self):
            return self.getToken(ZCodeParser.MAIN, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def funcblock(self):
            return self.getTypedRuleContext(ZCodeParser.FuncblockContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_mainfunc




    def mainfunc(self):

        localctx = ZCodeParser.MainfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_mainfunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(ZCodeParser.FUNC)
            self.state = 128
            self.match(ZCodeParser.MAIN)
            self.state = 129
            self.match(ZCodeParser.LB)
            self.state = 130
            self.match(ZCodeParser.RB)
            self.state = 131
            self.funcblock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def paramlist(self):
            return self.getTypedRuleContext(ZCodeParser.ParamlistContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def funcblock(self):
            return self.getTypedRuleContext(ZCodeParser.FuncblockContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcdecl




    def funcdecl(self):

        localctx = ZCodeParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(ZCodeParser.FUNC)
            self.state = 134
            self.match(ZCodeParser.ID)
            self.state = 135
            self.match(ZCodeParser.LB)
            self.state = 136
            self.paramlist()
            self.state = 137
            self.match(ZCodeParser.RB)
            self.state = 138
            self.funcblock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncblockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcblock




    def funcblock(self):

        localctx = ZCodeParser.FuncblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcblock)
        self._la = 0 # Token type
        try:
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 55]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==55:
                    self.state = 140
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 145
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 146
                self.match(ZCodeParser.BEGIN)
                self.state = 148 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 147
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 150 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==55):
                        break

                self.state = 152
                self.stmtlist()
                self.state = 153
                self.match(ZCodeParser.END)
                self.state = 155 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 154
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 157 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==55):
                        break

                pass
            elif token in [1, 2, 6, 7, 8, 14, 16, 23, 30, 34, 46, 50, 54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmts




    def stmts(self):

        localctx = ZCodeParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stmts)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def valdecl(self):
            return self.getTypedRuleContext(ZCodeParser.ValdeclContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(ZCodeParser.AssignstmtContext,0)


        def funcall(self):
            return self.getTypedRuleContext(ZCodeParser.FuncallContext,0)


        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.IfstmtContext,0)


        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 164
                self.valdecl()
                pass

            elif la_ == 2:
                self.state = 165
                self.assignstmt()
                pass

            elif la_ == 3:
                self.state = 166
                self.funcall()
                pass

            elif la_ == 4:
                self.state = 167
                self.exp(0)
                pass

            elif la_ == 5:
                self.state = 168
                self.ifstmt()
                pass

            elif la_ == 6:
                self.state = 169
                self.match(ZCodeParser.RETURN)
                self.state = 170
                self.exp(0)
                pass


            self.state = 174 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 173
                    self.match(ZCodeParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 176 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtblockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtblock




    def stmtblock(self):

        localctx = ZCodeParser.StmtblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_stmtblock)
        try:
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(ZCodeParser.BEGIN)
                self.state = 179
                self.stmtlist()
                self.state = 180
                self.match(ZCodeParser.END)
                pass
            elif token in [1, 2, 6, 7, 8, 14, 16, 23, 30, 34, 46, 50, 54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.stmt()
                pass
            elif token in [24, 25, 55]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtlist




    def stmtlist(self):

        localctx = ZCodeParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_stmtlist)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.stmt()
                self.state = 187
                self.stmtlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def indexp(self):
            return self.getTypedRuleContext(ZCodeParser.IndexpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignstmt




    def assignstmt(self):

        localctx = ZCodeParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 193
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 194
                self.indexp()
                pass


            self.state = 197
            self.match(ZCodeParser.ASSIGN)
            self.state = 198
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def ifblock(self):
            return self.getTypedRuleContext(ZCodeParser.IfblockContext,0)


        def elifblk(self):
            return self.getTypedRuleContext(ZCodeParser.ElifblkContext,0)


        def elseblk(self):
            return self.getTypedRuleContext(ZCodeParser.ElseblkContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ifstmt




    def ifstmt(self):

        localctx = ZCodeParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(ZCodeParser.IF)
            self.state = 201
            self.ifblock()
            self.state = 202
            self.elifblk()
            self.state = 203
            self.elseblk()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfblockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def stmtblock(self):
            return self.getTypedRuleContext(ZCodeParser.StmtblockContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ifblock




    def ifblock(self):

        localctx = ZCodeParser.IfblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ifblock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(ZCodeParser.LB)
            self.state = 206
            self.exp(0)
            self.state = 207
            self.match(ZCodeParser.RB)
            self.state = 208
            self.stmtblock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseblkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def stmtblock(self):
            return self.getTypedRuleContext(ZCodeParser.StmtblockContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elseblk




    def elseblk(self):

        localctx = ZCodeParser.ElseblkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_elseblk)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.match(ZCodeParser.ELSE)
                self.state = 211
                self.stmtblock()
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifblkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elifblk_0(self):
            return self.getTypedRuleContext(ZCodeParser.Elifblk_0Context,0)


        def elifblk(self):
            return self.getTypedRuleContext(ZCodeParser.ElifblkContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifblk




    def elifblk(self):

        localctx = ZCodeParser.ElifblkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_elifblk)
        try:
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.elifblk_0()
                self.state = 216
                self.elifblk()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.elifblk_0()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elifblk_0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def ifblock(self):
            return self.getTypedRuleContext(ZCodeParser.IfblockContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifblk_0




    def elifblk_0(self):

        localctx = ZCodeParser.Elifblk_0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_elifblk_0)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(ZCodeParser.ELIF)
            self.state = 223
            self.ifblock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def logicexp(self):
            return self.getTypedRuleContext(ZCodeParser.LogicexpContext,0)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def loopblock(self):
            return self.getTypedRuleContext(ZCodeParser.LoopblockContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_forstmt




    def forstmt(self):

        localctx = ZCodeParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_forstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(ZCodeParser.FOR)
            self.state = 226
            _la = self._input.LA(1)
            if not(_la==7 or _la==54):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 227
            self.match(ZCodeParser.UNTIL)
            self.state = 228
            self.logicexp(0)
            self.state = 229
            self.match(ZCodeParser.BY)
            self.state = 230
            self.exp(0)
            self.state = 231
            self.loopblock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopblockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StmtContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StmtContext,i)


        def loopkey(self):
            return self.getTypedRuleContext(ZCodeParser.LoopkeyContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_loopblock




    def loopblock(self):

        localctx = ZCodeParser.LoopblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_loopblock)
        self._la = 0 # Token type
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.match(ZCodeParser.BEGIN)
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 19210685422584262) != 0):
                    self.state = 235 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 234
                        self.stmt()
                        self.state = 237 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 19210685422584262) != 0)):
                            break

                    self.state = 245
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==21 or _la==22:
                        self.state = 239
                        self.loopkey()
                        self.state = 241 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 240
                            self.match(ZCodeParser.NEWLINE)
                            self.state = 243 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==55):
                                break





                self.state = 249
                self.match(ZCodeParser.END)
                pass
            elif token in [1, 2, 6, 7, 8, 14, 16, 23, 30, 34, 46, 50, 54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopkeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_loopkey




    def loopkey(self):

        localctx = ZCodeParser.LoopkeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_loopkey)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            _la = self._input.LA(1)
            if not(_la==21 or _la==22):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def NUMLIT(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NUMLIT)
            else:
                return self.getToken(ZCodeParser.NUMLIT, i)

        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.COMMA)
            else:
                return self.getToken(ZCodeParser.COMMA, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arraydecl




    def arraydecl(self):

        localctx = ZCodeParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_arraydecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(ZCodeParser.LS)
            self.state = 256
            self.match(ZCodeParser.NUMLIT)
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==52:
                self.state = 257
                self.match(ZCodeParser.COMMA)
                self.state = 258
                self.match(ZCodeParser.NUMLIT)
                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 264
            self.match(ZCodeParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcall




    def funcall(self):

        localctx = ZCodeParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(ZCodeParser.ID)
            self.state = 267
            self.match(ZCodeParser.LB)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 19210685414113728) != 0):
                self.state = 268
                self.exp(0)


            self.state = 271
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamcallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.COMMA)
            else:
                return self.getToken(ZCodeParser.COMMA, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_paramcall




    def paramcall(self):

        localctx = ZCodeParser.ParamcallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_paramcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.exp(0)
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==52:
                self.state = 274
                self.match(ZCodeParser.COMMA)

                self.state = 275
                self.exp(0)
                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ParamsContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ParamsContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.COMMA)
            else:
                return self.getToken(ZCodeParser.COMMA, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_paramlist




    def paramlist(self):

        localctx = ZCodeParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_paramlist)
        self._la = 0 # Token type
        try:
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.params()
                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==52:
                    self.state = 282
                    self.match(ZCodeParser.COMMA)
                    self.state = 283
                    self.params()
                    self.state = 288
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(ZCodeParser.TYPE, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_params




    def params(self):

        localctx = ZCodeParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(ZCodeParser.TYPE)
            self.state = 293
            self.match(ZCodeParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_01(self):
            return self.getTypedRuleContext(ZCodeParser.Exp_01Context,0)


        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def NUMOP(self):
            return self.getToken(ZCodeParser.NUMOP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.exp_01()
            self._ctx.stop = self._input.LT(-1)
            self.state = 303
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.ExpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                    self.state = 298
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 299
                    self.match(ZCodeParser.NUMOP)
                    self.state = 300
                    self.exp_01() 
                self.state = 305
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp_01Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ariexp(self):
            return self.getTypedRuleContext(ZCodeParser.AriexpContext,0)


        def logicexp(self):
            return self.getTypedRuleContext(ZCodeParser.LogicexpContext,0)


        def relatexp(self):
            return self.getTypedRuleContext(ZCodeParser.RelatexpContext,0)


        def expall(self):
            return self.getTypedRuleContext(ZCodeParser.ExpallContext,0)


        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def exp_01(self):
            return self.getTypedRuleContext(ZCodeParser.Exp_01Context,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp_01




    def exp_01(self):

        localctx = ZCodeParser.Exp_01Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exp_01)
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.ariexp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
                self.logicexp(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 308
                self.relatexp()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 309
                self.expall()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 310
                self.array()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 311
                self.match(ZCodeParser.STRINGLIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 312
                self.match(ZCodeParser.LB)
                self.state = 313
                self.exp_01()
                self.state = 314
                self.match(ZCodeParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_00Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def BOOLIT(self):
            return self.getToken(ZCodeParser.BOOLIT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp_00




    def exp_00(self):

        localctx = ZCodeParser.Exp_00Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exp_00)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def indexp(self):
            return self.getTypedRuleContext(ZCodeParser.IndexpContext,0)


        def funcall(self):
            return self.getTypedRuleContext(ZCodeParser.FuncallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expall




    def expall(self):

        localctx = ZCodeParser.ExpallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expall)
        try:
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.indexp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 322
                self.funcall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def explist(self):
            return self.getTypedRuleContext(ZCodeParser.ExplistContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array




    def array(self):

        localctx = ZCodeParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(ZCodeParser.LS)
            self.state = 326
            self.explist()
            self.state = 327
            self.match(ZCodeParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def explist_1(self):
            return self.getTypedRuleContext(ZCodeParser.Explist_1Context,0)


        def explist_2(self):
            return self.getTypedRuleContext(ZCodeParser.Explist_2Context,0)


        def explist_3(self):
            return self.getTypedRuleContext(ZCodeParser.Explist_3Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_explist




    def explist(self):

        localctx = ZCodeParser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_explist)
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.explist_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                self.explist_2()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 331
                self.explist_3()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Explist_1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def explist_1(self):
            return self.getTypedRuleContext(ZCodeParser.Explist_1Context,0)


        def expall(self):
            return self.getTypedRuleContext(ZCodeParser.ExpallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_explist_1




    def explist_1(self):

        localctx = ZCodeParser.Explist_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_explist_1)
        try:
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(ZCodeParser.NUMLIT)
                self.state = 335
                self.match(ZCodeParser.COMMA)
                self.state = 336
                self.explist_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
                self.match(ZCodeParser.NUMLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 338
                self.expall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Explist_2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def explist_2(self):
            return self.getTypedRuleContext(ZCodeParser.Explist_2Context,0)


        def expall(self):
            return self.getTypedRuleContext(ZCodeParser.ExpallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_explist_2




    def explist_2(self):

        localctx = ZCodeParser.Explist_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_explist_2)
        try:
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.match(ZCodeParser.STRINGLIT)
                self.state = 342
                self.match(ZCodeParser.COMMA)
                self.state = 343
                self.explist_2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.match(ZCodeParser.STRINGLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 345
                self.expall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Explist_3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLIT(self):
            return self.getToken(ZCodeParser.BOOLIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def explist_3(self):
            return self.getTypedRuleContext(ZCodeParser.Explist_3Context,0)


        def expall(self):
            return self.getTypedRuleContext(ZCodeParser.ExpallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_explist_3




    def explist_3(self):

        localctx = ZCodeParser.Explist_3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_explist_3)
        try:
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.match(ZCodeParser.BOOLIT)
                self.state = 349
                self.match(ZCodeParser.COMMA)
                self.state = 350
                self.explist_3()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.match(ZCodeParser.BOOLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 352
                self.expall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def indop(self):
            return self.getTypedRuleContext(ZCodeParser.IndopContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_indexp




    def indexp(self):

        localctx = ZCodeParser.IndexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_indexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(ZCodeParser.ID)
            self.state = 356
            self.match(ZCodeParser.LS)
            self.state = 357
            self.indop(0)
            self.state = 358
            self.match(ZCodeParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indop_0(self):
            return self.getTypedRuleContext(ZCodeParser.Indop_0Context,0)


        def indop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IndopContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IndopContext,i)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_indop



    def indop(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.IndopContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_indop, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.indop_0(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 368
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.IndopContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_indop)
                    self.state = 363
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 364
                    self.match(ZCodeParser.COMMA)
                    self.state = 365
                    self.indop(0) 
                self.state = 370
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Indop_0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indop_1(self):
            return self.getTypedRuleContext(ZCodeParser.Indop_1Context,0)


        def indop_0(self):
            return self.getTypedRuleContext(ZCodeParser.Indop_0Context,0)


        def NUMOP(self):
            return self.getToken(ZCodeParser.NUMOP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_indop_0



    def indop_0(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Indop_0Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_indop_0, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.indop_1()
            self._ctx.stop = self._input.LT(-1)
            self.state = 379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Indop_0Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_indop_0)
                    self.state = 374
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 375
                    self.match(ZCodeParser.NUMOP)
                    self.state = 376
                    self.indop_1() 
                self.state = 381
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Indop_1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def ariexp(self):
            return self.getTypedRuleContext(ZCodeParser.AriexpContext,0)


        def expall(self):
            return self.getTypedRuleContext(ZCodeParser.ExpallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_indop_1




    def indop_1(self):

        localctx = ZCodeParser.Indop_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_indop_1)
        try:
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.match(ZCodeParser.NUMLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
                self.ariexp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 384
                self.expall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AriexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ariexp_00(self):
            return self.getTypedRuleContext(ZCodeParser.Ariexp_00Context,0)


        def NUMOP(self):
            return self.getToken(ZCodeParser.NUMOP, 0)

        def ariexp(self):
            return self.getTypedRuleContext(ZCodeParser.AriexpContext,0)


        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ariexp




    def ariexp(self):

        localctx = ZCodeParser.AriexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_ariexp)
        try:
            self.state = 394
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.ariexp_00()
                self.state = 388
                self.match(ZCodeParser.NUMOP)
                self.state = 389
                self.ariexp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
                self.match(ZCodeParser.MINUS)
                self.state = 392
                self.ariexp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 393
                self.ariexp_00()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ariexp_00Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def expall(self):
            return self.getTypedRuleContext(ZCodeParser.ExpallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ariexp_00




    def ariexp_00(self):

        localctx = ZCodeParser.Ariexp_00Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_ariexp_00)
        try:
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.match(ZCodeParser.NUMLIT)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.expall()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicexp_00(self):
            return self.getTypedRuleContext(ZCodeParser.Logicexp_00Context,0)


        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def logicexp(self):
            return self.getTypedRuleContext(ZCodeParser.LogicexpContext,0)


        def LOGICOPBIN(self):
            return self.getToken(ZCodeParser.LOGICOPBIN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_logicexp



    def logicexp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.LogicexpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_logicexp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 8, 54]:
                self.state = 401
                self.logicexp_00()
                pass
            elif token in [34]:
                self.state = 402
                self.match(ZCodeParser.NOT)
                self.state = 403
                self.logicexp(1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 411
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.LogicexpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicexp)
                    self.state = 406
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 407
                    self.match(ZCodeParser.LOGICOPBIN)
                    self.state = 408
                    self.logicexp_00() 
                self.state = 413
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logicexp_00Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLIT(self):
            return self.getToken(ZCodeParser.BOOLIT, 0)

        def relatexp(self):
            return self.getTypedRuleContext(ZCodeParser.RelatexpContext,0)


        def expall(self):
            return self.getTypedRuleContext(ZCodeParser.ExpallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_logicexp_00




    def logicexp_00(self):

        localctx = ZCodeParser.Logicexp_00Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_logicexp_00)
        try:
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 414
                self.match(ZCodeParser.BOOLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
                self.relatexp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 416
                self.expall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelatexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relatexp_00(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Relatexp_00Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Relatexp_00Context,i)


        def NUMRELAOPS(self):
            return self.getToken(ZCodeParser.NUMRELAOPS, 0)

        def relatexp_01(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Relatexp_01Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Relatexp_01Context,i)


        def EQUALITY(self):
            return self.getToken(ZCodeParser.EQUALITY, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_relatexp




    def relatexp(self):

        localctx = ZCodeParser.RelatexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_relatexp)
        try:
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 419
                self.relatexp_00()
                self.state = 420
                self.match(ZCodeParser.NUMRELAOPS)
                self.state = 421
                self.relatexp_00()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.relatexp_01()
                self.state = 424
                self.match(ZCodeParser.EQUALITY)
                self.state = 425
                self.relatexp_01()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relatexp_00Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def expall(self):
            return self.getTypedRuleContext(ZCodeParser.ExpallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_relatexp_00




    def relatexp_00(self):

        localctx = ZCodeParser.Relatexp_00Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_relatexp_00)
        try:
            self.state = 431
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.match(ZCodeParser.NUMLIT)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.expall()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relatexp_01Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def expall(self):
            return self.getTypedRuleContext(ZCodeParser.ExpallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_relatexp_01




    def relatexp_01(self):

        localctx = ZCodeParser.Relatexp_01Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_relatexp_01)
        try:
            self.state = 435
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.match(ZCodeParser.STRINGLIT)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
                self.expall()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[24] = self.exp_sempred
        self._predicates[34] = self.indop_sempred
        self._predicates[35] = self.indop_0_sempred
        self._predicates[39] = self.logicexp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def indop_sempred(self, localctx:IndopContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def indop_0_sempred(self, localctx:Indop_0Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def logicexp_sempred(self, localctx:LogicexpContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         




