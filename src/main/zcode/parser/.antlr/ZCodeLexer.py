# Generated from c:/Users/hoang/Desktop/New folder (2)/ppl232/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,60,459,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,1,0,1,0,1,0,
        3,0,133,8,0,1,1,1,1,3,1,137,8,1,1,2,1,2,1,2,1,2,3,2,143,8,2,1,3,
        1,3,3,3,147,8,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,155,8,4,1,5,1,5,1,5,
        1,5,5,5,161,8,5,10,5,12,5,164,9,5,1,5,1,5,1,5,1,6,1,6,1,6,5,6,172,
        8,6,10,6,12,6,175,9,6,1,6,1,6,1,6,1,7,1,7,3,7,182,8,7,1,7,1,7,1,
        7,3,7,187,8,7,3,7,189,8,7,1,8,3,8,192,8,8,1,8,5,8,195,8,8,10,8,12,
        8,198,9,8,1,9,1,9,5,9,202,8,9,10,9,12,9,205,9,9,1,10,1,10,3,10,209,
        8,10,1,10,5,10,212,8,10,10,10,12,10,215,9,10,1,11,1,11,3,11,219,
        8,11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,18,
        1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,
        1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,
        1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,
        1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,
        1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,
        1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,33,1,33,1,34,1,34,
        1,35,1,35,1,36,1,36,1,37,1,37,1,37,1,37,1,38,1,38,1,38,1,38,1,39,
        1,39,1,39,1,40,1,40,1,41,1,41,1,41,1,42,1,42,1,42,1,43,1,43,1,44,
        1,44,1,44,1,45,1,45,1,46,1,46,1,46,1,47,1,47,1,47,1,47,1,48,1,48,
        1,48,1,49,1,49,1,50,1,50,1,51,1,51,1,52,1,52,1,53,1,53,1,54,1,54,
        1,55,1,55,1,56,1,56,1,56,5,56,394,8,56,10,56,12,56,397,9,56,1,56,
        3,56,400,8,56,1,57,3,57,403,8,57,1,57,5,57,406,8,57,10,57,12,57,
        409,9,57,1,58,3,58,412,8,58,1,58,1,58,1,59,4,59,417,8,59,11,59,12,
        59,418,1,59,1,59,1,60,1,60,1,60,1,61,1,61,1,61,1,61,5,61,430,8,61,
        10,61,12,61,433,9,61,1,61,1,61,1,61,1,62,1,62,5,62,440,8,62,10,62,
        12,62,443,9,62,1,62,1,62,5,62,447,8,62,10,62,12,62,450,9,62,1,62,
        3,62,453,8,62,1,62,1,62,1,63,1,63,1,63,3,162,173,395,0,64,1,1,3,
        2,5,3,7,4,9,5,11,0,13,6,15,7,17,0,19,0,21,0,23,8,25,9,27,10,29,11,
        31,12,33,13,35,14,37,15,39,16,41,17,43,18,45,19,47,20,49,21,51,22,
        53,23,55,24,57,25,59,26,61,27,63,28,65,29,67,30,69,31,71,32,73,33,
        75,34,77,35,79,36,81,37,83,38,85,39,87,40,89,41,91,42,93,43,95,44,
        97,45,99,46,101,47,103,48,105,49,107,50,109,51,111,52,113,53,115,
        54,117,55,119,56,121,57,123,58,125,59,127,60,1,0,11,2,0,34,34,39,
        39,1,0,48,57,2,0,69,69,101,101,2,0,43,43,45,45,1,1,13,13,3,0,65,
        90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,2,0,9,9,32,32,1,0,34,
        34,1,1,34,34,7,0,39,39,92,92,98,98,102,102,110,110,114,114,116,116,
        485,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,
        0,13,1,0,0,0,0,15,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,
        0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,
        0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,
        0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,
        0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,
        0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,
        0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,
        0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,0,0,0,
        0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,1,0,
        0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,0,115,1,0,0,0,0,117,
        1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,0,123,1,0,0,0,0,125,1,0,0,0,
        0,127,1,0,0,0,1,132,1,0,0,0,3,136,1,0,0,0,5,142,1,0,0,0,7,146,1,
        0,0,0,9,154,1,0,0,0,11,156,1,0,0,0,13,168,1,0,0,0,15,188,1,0,0,0,
        17,191,1,0,0,0,19,199,1,0,0,0,21,206,1,0,0,0,23,218,1,0,0,0,25,220,
        1,0,0,0,27,225,1,0,0,0,29,231,1,0,0,0,31,238,1,0,0,0,33,243,1,0,
        0,0,35,250,1,0,0,0,37,257,1,0,0,0,39,261,1,0,0,0,41,269,1,0,0,0,
        43,274,1,0,0,0,45,278,1,0,0,0,47,284,1,0,0,0,49,287,1,0,0,0,51,293,
        1,0,0,0,53,302,1,0,0,0,55,305,1,0,0,0,57,310,1,0,0,0,59,315,1,0,
        0,0,61,321,1,0,0,0,63,325,1,0,0,0,65,330,1,0,0,0,67,332,1,0,0,0,
        69,334,1,0,0,0,71,336,1,0,0,0,73,338,1,0,0,0,75,340,1,0,0,0,77,344,
        1,0,0,0,79,348,1,0,0,0,81,351,1,0,0,0,83,353,1,0,0,0,85,356,1,0,
        0,0,87,359,1,0,0,0,89,361,1,0,0,0,91,364,1,0,0,0,93,366,1,0,0,0,
        95,369,1,0,0,0,97,373,1,0,0,0,99,376,1,0,0,0,101,378,1,0,0,0,103,
        380,1,0,0,0,105,382,1,0,0,0,107,384,1,0,0,0,109,386,1,0,0,0,111,
        388,1,0,0,0,113,390,1,0,0,0,115,402,1,0,0,0,117,411,1,0,0,0,119,
        416,1,0,0,0,121,422,1,0,0,0,123,425,1,0,0,0,125,437,1,0,0,0,127,
        456,1,0,0,0,129,133,3,29,14,0,130,133,3,33,16,0,131,133,3,31,15,
        0,132,129,1,0,0,0,132,130,1,0,0,0,132,131,1,0,0,0,133,2,1,0,0,0,
        134,137,3,37,18,0,135,137,3,39,19,0,136,134,1,0,0,0,136,135,1,0,
        0,0,137,4,1,0,0,0,138,143,3,65,32,0,139,143,3,69,34,0,140,143,3,
        73,36,0,141,143,3,67,33,0,142,138,1,0,0,0,142,139,1,0,0,0,142,140,
        1,0,0,0,142,141,1,0,0,0,143,6,1,0,0,0,144,147,3,77,38,0,145,147,
        3,79,39,0,146,144,1,0,0,0,146,145,1,0,0,0,147,8,1,0,0,0,148,155,
        3,81,40,0,149,155,3,85,42,0,150,155,3,87,43,0,151,155,3,89,44,0,
        152,155,3,93,46,0,153,155,3,91,45,0,154,148,1,0,0,0,154,149,1,0,
        0,0,154,150,1,0,0,0,154,151,1,0,0,0,154,152,1,0,0,0,154,153,1,0,
        0,0,155,10,1,0,0,0,156,157,5,39,0,0,157,158,5,34,0,0,158,162,1,0,
        0,0,159,161,9,0,0,0,160,159,1,0,0,0,161,164,1,0,0,0,162,163,1,0,
        0,0,162,160,1,0,0,0,163,165,1,0,0,0,164,162,1,0,0,0,165,166,5,39,
        0,0,166,167,5,34,0,0,167,12,1,0,0,0,168,173,5,34,0,0,169,172,8,0,
        0,0,170,172,3,11,5,0,171,169,1,0,0,0,171,170,1,0,0,0,172,175,1,0,
        0,0,173,174,1,0,0,0,173,171,1,0,0,0,174,176,1,0,0,0,175,173,1,0,
        0,0,176,177,5,34,0,0,177,178,6,6,0,0,178,14,1,0,0,0,179,181,3,17,
        8,0,180,182,3,21,10,0,181,180,1,0,0,0,181,182,1,0,0,0,182,189,1,
        0,0,0,183,184,3,17,8,0,184,186,3,19,9,0,185,187,3,21,10,0,186,185,
        1,0,0,0,186,187,1,0,0,0,187,189,1,0,0,0,188,179,1,0,0,0,188,183,
        1,0,0,0,189,16,1,0,0,0,190,192,2,48,57,0,191,190,1,0,0,0,192,196,
        1,0,0,0,193,195,7,1,0,0,194,193,1,0,0,0,195,198,1,0,0,0,196,194,
        1,0,0,0,196,197,1,0,0,0,197,18,1,0,0,0,198,196,1,0,0,0,199,203,5,
        46,0,0,200,202,7,1,0,0,201,200,1,0,0,0,202,205,1,0,0,0,203,201,1,
        0,0,0,203,204,1,0,0,0,204,20,1,0,0,0,205,203,1,0,0,0,206,208,7,2,
        0,0,207,209,7,3,0,0,208,207,1,0,0,0,208,209,1,0,0,0,209,213,1,0,
        0,0,210,212,7,1,0,0,211,210,1,0,0,0,212,215,1,0,0,0,213,211,1,0,
        0,0,213,214,1,0,0,0,214,22,1,0,0,0,215,213,1,0,0,0,216,219,3,25,
        12,0,217,219,3,27,13,0,218,216,1,0,0,0,218,217,1,0,0,0,219,24,1,
        0,0,0,220,221,5,116,0,0,221,222,5,114,0,0,222,223,5,117,0,0,223,
        224,5,101,0,0,224,26,1,0,0,0,225,226,5,102,0,0,226,227,5,97,0,0,
        227,228,5,108,0,0,228,229,5,115,0,0,229,230,5,101,0,0,230,28,1,0,
        0,0,231,232,5,110,0,0,232,233,5,117,0,0,233,234,5,109,0,0,234,235,
        5,98,0,0,235,236,5,101,0,0,236,237,5,114,0,0,237,30,1,0,0,0,238,
        239,5,98,0,0,239,240,5,111,0,0,240,241,5,111,0,0,241,242,5,108,0,
        0,242,32,1,0,0,0,243,244,5,115,0,0,244,245,5,116,0,0,245,246,5,114,
        0,0,246,247,5,105,0,0,247,248,5,110,0,0,248,249,5,103,0,0,249,34,
        1,0,0,0,250,251,5,114,0,0,251,252,5,101,0,0,252,253,5,116,0,0,253,
        254,5,117,0,0,254,255,5,114,0,0,255,256,5,110,0,0,256,36,1,0,0,0,
        257,258,5,118,0,0,258,259,5,97,0,0,259,260,5,114,0,0,260,38,1,0,
        0,0,261,262,5,100,0,0,262,263,5,121,0,0,263,264,5,110,0,0,264,265,
        5,97,0,0,265,266,5,109,0,0,266,267,5,105,0,0,267,268,5,99,0,0,268,
        40,1,0,0,0,269,270,5,102,0,0,270,271,5,117,0,0,271,272,5,110,0,0,
        272,273,5,99,0,0,273,42,1,0,0,0,274,275,5,102,0,0,275,276,5,111,
        0,0,276,277,5,114,0,0,277,44,1,0,0,0,278,279,5,117,0,0,279,280,5,
        110,0,0,280,281,5,116,0,0,281,282,5,105,0,0,282,283,5,108,0,0,283,
        46,1,0,0,0,284,285,5,98,0,0,285,286,5,121,0,0,286,48,1,0,0,0,287,
        288,5,98,0,0,288,289,5,114,0,0,289,290,5,101,0,0,290,291,5,97,0,
        0,291,292,5,107,0,0,292,50,1,0,0,0,293,294,5,99,0,0,294,295,5,111,
        0,0,295,296,5,110,0,0,296,297,5,116,0,0,297,298,5,105,0,0,298,299,
        5,110,0,0,299,300,5,117,0,0,300,301,5,101,0,0,301,52,1,0,0,0,302,
        303,5,105,0,0,303,304,5,102,0,0,304,54,1,0,0,0,305,306,5,101,0,0,
        306,307,5,108,0,0,307,308,5,105,0,0,308,309,5,102,0,0,309,56,1,0,
        0,0,310,311,5,101,0,0,311,312,5,108,0,0,312,313,5,115,0,0,313,314,
        5,101,0,0,314,58,1,0,0,0,315,316,5,98,0,0,316,317,5,101,0,0,317,
        318,5,103,0,0,318,319,5,105,0,0,319,320,5,110,0,0,320,60,1,0,0,0,
        321,322,5,101,0,0,322,323,5,110,0,0,323,324,5,100,0,0,324,62,1,0,
        0,0,325,326,5,109,0,0,326,327,5,97,0,0,327,328,5,105,0,0,328,329,
        5,110,0,0,329,64,1,0,0,0,330,331,5,43,0,0,331,66,1,0,0,0,332,333,
        5,45,0,0,333,68,1,0,0,0,334,335,5,42,0,0,335,70,1,0,0,0,336,337,
        5,47,0,0,337,72,1,0,0,0,338,339,5,37,0,0,339,74,1,0,0,0,340,341,
        5,110,0,0,341,342,5,111,0,0,342,343,5,116,0,0,343,76,1,0,0,0,344,
        345,5,97,0,0,345,346,5,110,0,0,346,347,5,100,0,0,347,78,1,0,0,0,
        348,349,5,111,0,0,349,350,5,114,0,0,350,80,1,0,0,0,351,352,5,61,
        0,0,352,82,1,0,0,0,353,354,5,60,0,0,354,355,5,45,0,0,355,84,1,0,
        0,0,356,357,5,33,0,0,357,358,5,61,0,0,358,86,1,0,0,0,359,360,5,60,
        0,0,360,88,1,0,0,0,361,362,5,60,0,0,362,363,5,61,0,0,363,90,1,0,
        0,0,364,365,5,62,0,0,365,92,1,0,0,0,366,367,5,62,0,0,367,368,5,61,
        0,0,368,94,1,0,0,0,369,370,5,46,0,0,370,371,5,46,0,0,371,372,5,46,
        0,0,372,96,1,0,0,0,373,374,5,61,0,0,374,375,5,61,0,0,375,98,1,0,
        0,0,376,377,5,40,0,0,377,100,1,0,0,0,378,379,5,41,0,0,379,102,1,
        0,0,0,380,381,5,123,0,0,381,104,1,0,0,0,382,383,5,125,0,0,383,106,
        1,0,0,0,384,385,5,91,0,0,385,108,1,0,0,0,386,387,5,93,0,0,387,110,
        1,0,0,0,388,389,5,44,0,0,389,112,1,0,0,0,390,391,5,35,0,0,391,395,
        5,35,0,0,392,394,9,0,0,0,393,392,1,0,0,0,394,397,1,0,0,0,395,396,
        1,0,0,0,395,393,1,0,0,0,396,399,1,0,0,0,397,395,1,0,0,0,398,400,
        7,4,0,0,399,398,1,0,0,0,400,114,1,0,0,0,401,403,7,5,0,0,402,401,
        1,0,0,0,403,407,1,0,0,0,404,406,7,6,0,0,405,404,1,0,0,0,406,409,
        1,0,0,0,407,405,1,0,0,0,407,408,1,0,0,0,408,116,1,0,0,0,409,407,
        1,0,0,0,410,412,5,13,0,0,411,410,1,0,0,0,411,412,1,0,0,0,412,413,
        1,0,0,0,413,414,5,10,0,0,414,118,1,0,0,0,415,417,7,7,0,0,416,415,
        1,0,0,0,417,418,1,0,0,0,418,416,1,0,0,0,418,419,1,0,0,0,419,420,
        1,0,0,0,420,421,6,59,1,0,421,120,1,0,0,0,422,423,9,0,0,0,423,424,
        6,60,2,0,424,122,1,0,0,0,425,431,5,34,0,0,426,430,8,8,0,0,427,428,
        5,39,0,0,428,430,5,34,0,0,429,426,1,0,0,0,429,427,1,0,0,0,430,433,
        1,0,0,0,431,429,1,0,0,0,431,432,1,0,0,0,432,434,1,0,0,0,433,431,
        1,0,0,0,434,435,5,0,0,1,435,436,6,61,3,0,436,124,1,0,0,0,437,441,
        5,34,0,0,438,440,9,0,0,0,439,438,1,0,0,0,440,443,1,0,0,0,441,439,
        1,0,0,0,441,442,1,0,0,0,442,444,1,0,0,0,443,441,1,0,0,0,444,448,
        3,127,63,0,445,447,9,0,0,0,446,445,1,0,0,0,447,450,1,0,0,0,448,446,
        1,0,0,0,448,449,1,0,0,0,449,452,1,0,0,0,450,448,1,0,0,0,451,453,
        7,9,0,0,452,451,1,0,0,0,453,454,1,0,0,0,454,455,6,62,4,0,455,126,
        1,0,0,0,456,457,5,92,0,0,457,458,8,10,0,0,458,128,1,0,0,0,30,0,132,
        136,142,146,154,162,171,173,181,186,188,191,196,203,208,213,218,
        395,399,402,405,407,411,418,429,431,441,448,452,5,1,6,0,6,0,0,1,
        60,1,1,61,2,1,62,3
    ]

class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TYPE = 1
    IMPLIKEYS = 2
    NUMOP = 3
    LOGICOPBIN = 4
    NUMRELAOPS = 5
    STRINGLIT = 6
    NUMLIT = 7
    BOOLIT = 8
    TRUE = 9
    FALSE = 10
    NUMBER = 11
    BOOL = 12
    STRING = 13
    RETURN = 14
    VAR = 15
    DYNAMIC = 16
    FUNC = 17
    FOR = 18
    UNTIL = 19
    BY = 20
    BREAK = 21
    CONTINUE = 22
    IF = 23
    ELIF = 24
    ELSE = 25
    BEGIN = 26
    END = 27
    MAIN = 28
    PLUS = 29
    MINUS = 30
    STAR = 31
    SLASH = 32
    PERCENT = 33
    NOT = 34
    AND = 35
    OR = 36
    EQUAL = 37
    ASSIGN = 38
    INEQUAL = 39
    LESSTHAN = 40
    LESSEQUAL = 41
    MORETHAN = 42
    MOREEQUAL = 43
    ELLIPSIS = 44
    EQUALITY = 45
    LB = 46
    RB = 47
    LC = 48
    RC = 49
    LS = 50
    RS = 51
    COMMA = 52
    COMMENT = 53
    ID = 54
    NEWLINE = 55
    WS = 56
    ERROR_CHAR = 57
    UNCLOSE_STRING = 58
    ILLEGAL_ESCAPE = 59
    ES = 60

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'elif'", "'else'", "'begin'", 
            "'end'", "'main'", "'+'", "'-'", "'*'", "'/'", "'%'", "'not'", 
            "'and'", "'or'", "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", 
            "'>='", "'...'", "'=='", "'('", "')'", "'{'", "'}'", "'['", 
            "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "TYPE", "IMPLIKEYS", "NUMOP", "LOGICOPBIN", "NUMRELAOPS", "STRINGLIT", 
            "NUMLIT", "BOOLIT", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
            "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
            "CONTINUE", "IF", "ELIF", "ELSE", "BEGIN", "END", "MAIN", "PLUS", 
            "MINUS", "STAR", "SLASH", "PERCENT", "NOT", "AND", "OR", "EQUAL", 
            "ASSIGN", "INEQUAL", "LESSTHAN", "LESSEQUAL", "MORETHAN", "MOREEQUAL", 
            "ELLIPSIS", "EQUALITY", "LB", "RB", "LC", "RC", "LS", "RS", 
            "COMMA", "COMMENT", "ID", "NEWLINE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ES" ]

    ruleNames = [ "TYPE", "IMPLIKEYS", "NUMOP", "LOGICOPBIN", "NUMRELAOPS", 
                  "SUBSTR", "STRINGLIT", "NUMLIT", "INTERGER", "DECIMAL", 
                  "EXPONENT", "BOOLIT", "TRUE", "FALSE", "NUMBER", "BOOL", 
                  "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                  "BY", "BREAK", "CONTINUE", "IF", "ELIF", "ELSE", "BEGIN", 
                  "END", "MAIN", "PLUS", "MINUS", "STAR", "SLASH", "PERCENT", 
                  "NOT", "AND", "OR", "EQUAL", "ASSIGN", "INEQUAL", "LESSTHAN", 
                  "LESSEQUAL", "MORETHAN", "MOREEQUAL", "ELLIPSIS", "EQUALITY", 
                  "LB", "RB", "LC", "RC", "LS", "RS", "COMMA", "COMMENT", 
                  "ID", "NEWLINE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ES" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[6] = self.STRINGLIT_action 
            actions[60] = self.ERROR_CHAR_action 
            actions[61] = self.UNCLOSE_STRING_action 
            actions[62] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text.replace("\"",""); raise UncloseString(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            					self.text = self.text.replace("\"", "")
            					pos = self.text.find("\\") + 2
            					self.text = self.text[0:pos:]; raise IllegalEscape(self.text)
     


