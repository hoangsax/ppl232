# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3>")
        buf.write("\u01b8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2\7\2")
        buf.write("\\\n\2\f\2\16\2_\13\2\3\2\3\2\7\2c\n\2\f\2\16\2f\13\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\6\3m\n\3\r\3\16\3n\3\3\5\3r\n\3\3")
        buf.write("\4\3\4\3\4\5\4w\n\4\3\4\3\4\3\4\5\4|\n\4\3\4\3\4\5\4\u0080")
        buf.write("\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\7\7\u0090\n\7\f\7\16\7\u0093\13\7\3\7\3\7\6\7\u0097")
        buf.write("\n\7\r\7\16\7\u0098\3\7\3\7\3\7\6\7\u009e\n\7\r\7\16\7")
        buf.write("\u009f\3\7\5\7\u00a3\n\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\5\t\u00ae\n\t\3\t\6\t\u00b1\n\t\r\t\16\t\u00b2")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00bb\n\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\5\13\u00c2\n\13\3\f\3\f\5\f\u00c6\n\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\5\17\u00d8\n\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\5\20\u00df\n\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\23\3\23\6\23\u00ee\n\23\r\23\16\23")
        buf.write("\u00ef\3\23\3\23\6\23\u00f4\n\23\r\23\16\23\u00f5\5\23")
        buf.write("\u00f8\n\23\5\23\u00fa\n\23\3\23\3\23\5\23\u00fe\n\23")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\7\25\u0106\n\25\f\25\16")
        buf.write("\25\u0109\13\25\3\25\3\25\3\26\3\26\3\26\5\26\u0110\n")
        buf.write("\26\3\26\3\26\3\27\3\27\3\27\7\27\u0117\n\27\f\27\16\27")
        buf.write("\u011a\13\27\3\30\3\30\3\30\7\30\u011f\n\30\f\30\16\30")
        buf.write("\u0122\13\30\3\30\5\30\u0125\n\30\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\7\32\u0130\n\32\f\32\16\32\u0133")
        buf.write("\13\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\5\33\u013f\n\33\3\34\3\34\3\35\3\35\3\35\5\35\u0146")
        buf.write("\n\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\5\37\u014f\n")
        buf.write("\37\3 \3 \3 \3 \3 \5 \u0156\n \3!\3!\3!\3!\3!\5!\u015d")
        buf.write("\n!\3\"\3\"\3\"\3\"\3\"\5\"\u0164\n\"\3#\3#\3#\3#\3#\3")
        buf.write("$\3$\3$\3$\3$\3$\7$\u0171\n$\f$\16$\u0174\13$\3%\3%\3")
        buf.write("%\3%\3%\3%\7%\u017c\n%\f%\16%\u017f\13%\3&\3&\3&\5&\u0184")
        buf.write("\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u018d\n\'\3(\3(\5")
        buf.write("(\u0191\n(\3)\3)\3)\3)\5)\u0197\n)\3)\3)\3)\7)\u019c\n")
        buf.write(")\f)\16)\u019f\13)\3*\3*\3*\5*\u01a4\n*\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\5+\u01ae\n+\3,\3,\5,\u01b2\n,\3-\3-\5-\u01b6")
        buf.write("\n-\3-\2\6\62FHP.\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX\2\7\4\2\3\3")
        buf.write("\22\22\3\2\3\4\4\2\t\t88\3\2\27\30\3\2\b\n\2\u01ce\2]")
        buf.write("\3\2\2\2\4q\3\2\2\2\6\177\3\2\2\2\b\u0081\3\2\2\2\n\u0087")
        buf.write("\3\2\2\2\f\u00a2\3\2\2\2\16\u00a4\3\2\2\2\20\u00ad\3\2")
        buf.write("\2\2\22\u00ba\3\2\2\2\24\u00c1\3\2\2\2\26\u00c5\3\2\2")
        buf.write("\2\30\u00ca\3\2\2\2\32\u00cf\3\2\2\2\34\u00d7\3\2\2\2")
        buf.write("\36\u00de\3\2\2\2 \u00e0\3\2\2\2\"\u00e3\3\2\2\2$\u00fd")
        buf.write("\3\2\2\2&\u00ff\3\2\2\2(\u0101\3\2\2\2*\u010c\3\2\2\2")
        buf.write(",\u0113\3\2\2\2.\u0124\3\2\2\2\60\u0126\3\2\2\2\62\u0129")
        buf.write("\3\2\2\2\64\u013e\3\2\2\2\66\u0140\3\2\2\28\u0145\3\2")
        buf.write("\2\2:\u0147\3\2\2\2<\u014e\3\2\2\2>\u0155\3\2\2\2@\u015c")
        buf.write("\3\2\2\2B\u0163\3\2\2\2D\u0165\3\2\2\2F\u016a\3\2\2\2")
        buf.write("H\u0175\3\2\2\2J\u0183\3\2\2\2L\u018c\3\2\2\2N\u0190\3")
        buf.write("\2\2\2P\u0196\3\2\2\2R\u01a3\3\2\2\2T\u01ad\3\2\2\2V\u01b1")
        buf.write("\3\2\2\2X\u01b5\3\2\2\2Z\\\5\4\3\2[Z\3\2\2\2\\_\3\2\2")
        buf.write("\2][\3\2\2\2]^\3\2\2\2^`\3\2\2\2_]\3\2\2\2`d\5\b\5\2a")
        buf.write("c\5\4\3\2ba\3\2\2\2cf\3\2\2\2db\3\2\2\2de\3\2\2\2eg\3")
        buf.write("\2\2\2fd\3\2\2\2gh\7\2\2\3h\3\3\2\2\2ir\5\n\6\2jl\5\6")
        buf.write("\4\2km\79\2\2lk\3\2\2\2mn\3\2\2\2nl\3\2\2\2no\3\2\2\2")
        buf.write("or\3\2\2\2pr\5\20\t\2qi\3\2\2\2qj\3\2\2\2qp\3\2\2\2r\5")
        buf.write("\3\2\2\2st\t\2\2\2tv\78\2\2uw\5(\25\2vu\3\2\2\2vw\3\2")
        buf.write("\2\2w\u0080\3\2\2\2xy\t\3\2\2y{\78\2\2z|\5(\25\2{z\3\2")
        buf.write("\2\2{|\3\2\2\2|}\3\2\2\2}~\7(\2\2~\u0080\5\62\32\2\177")
        buf.write("s\3\2\2\2\177x\3\2\2\2\u0080\7\3\2\2\2\u0081\u0082\7\23")
        buf.write("\2\2\u0082\u0083\7\36\2\2\u0083\u0084\7\60\2\2\u0084\u0085")
        buf.write("\7\61\2\2\u0085\u0086\5\f\7\2\u0086\t\3\2\2\2\u0087\u0088")
        buf.write("\7\23\2\2\u0088\u0089\78\2\2\u0089\u008a\7\60\2\2\u008a")
        buf.write("\u008b\5.\30\2\u008b\u008c\7\61\2\2\u008c\u008d\5\f\7")
        buf.write("\2\u008d\13\3\2\2\2\u008e\u0090\79\2\2\u008f\u008e\3\2")
        buf.write("\2\2\u0090\u0093\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092")
        buf.write("\3\2\2\2\u0092\u0094\3\2\2\2\u0093\u0091\3\2\2\2\u0094")
        buf.write("\u0096\7\34\2\2\u0095\u0097\79\2\2\u0096\u0095\3\2\2\2")
        buf.write("\u0097\u0098\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099\3")
        buf.write("\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\5\24\13\2\u009b")
        buf.write("\u009d\7\35\2\2\u009c\u009e\79\2\2\u009d\u009c\3\2\2\2")
        buf.write("\u009e\u009f\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0\3")
        buf.write("\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u00a3\5\20\t\2\u00a2")
        buf.write("\u0091\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3\r\3\2\2\2\u00a4")
        buf.write("\u00a5\3\2\2\2\u00a5\17\3\2\2\2\u00a6\u00ae\5\6\4\2\u00a7")
        buf.write("\u00ae\5\26\f\2\u00a8\u00ae\5*\26\2\u00a9\u00ae\5\62\32")
        buf.write("\2\u00aa\u00ae\5\30\r\2\u00ab\u00ac\7\20\2\2\u00ac\u00ae")
        buf.write("\5\62\32\2\u00ad\u00a6\3\2\2\2\u00ad\u00a7\3\2\2\2\u00ad")
        buf.write("\u00a8\3\2\2\2\u00ad\u00a9\3\2\2\2\u00ad\u00aa\3\2\2\2")
        buf.write("\u00ad\u00ab\3\2\2\2\u00ae\u00b0\3\2\2\2\u00af\u00b1\7")
        buf.write("9\2\2\u00b0\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b0")
        buf.write("\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\21\3\2\2\2\u00b4\u00b5")
        buf.write("\7\34\2\2\u00b5\u00b6\5\24\13\2\u00b6\u00b7\7\35\2\2\u00b7")
        buf.write("\u00bb\3\2\2\2\u00b8\u00bb\5\20\t\2\u00b9\u00bb\3\2\2")
        buf.write("\2\u00ba\u00b4\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00b9")
        buf.write("\3\2\2\2\u00bb\23\3\2\2\2\u00bc\u00bd\5\20\t\2\u00bd\u00be")
        buf.write("\5\24\13\2\u00be\u00c2\3\2\2\2\u00bf\u00c2\5\20\t\2\u00c0")
        buf.write("\u00c2\3\2\2\2\u00c1\u00bc\3\2\2\2\u00c1\u00bf\3\2\2\2")
        buf.write("\u00c1\u00c0\3\2\2\2\u00c2\25\3\2\2\2\u00c3\u00c6\78\2")
        buf.write("\2\u00c4\u00c6\5D#\2\u00c5\u00c3\3\2\2\2\u00c5\u00c4\3")
        buf.write("\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8\7(\2\2\u00c8\u00c9")
        buf.write("\5\62\32\2\u00c9\27\3\2\2\2\u00ca\u00cb\7\31\2\2\u00cb")
        buf.write("\u00cc\5\32\16\2\u00cc\u00cd\5\36\20\2\u00cd\u00ce\5\34")
        buf.write("\17\2\u00ce\31\3\2\2\2\u00cf\u00d0\7\60\2\2\u00d0\u00d1")
        buf.write("\5\62\32\2\u00d1\u00d2\7\61\2\2\u00d2\u00d3\5\22\n\2\u00d3")
        buf.write("\33\3\2\2\2\u00d4\u00d5\7\33\2\2\u00d5\u00d8\5\22\n\2")
        buf.write("\u00d6\u00d8\3\2\2\2\u00d7\u00d4\3\2\2\2\u00d7\u00d6\3")
        buf.write("\2\2\2\u00d8\35\3\2\2\2\u00d9\u00da\5 \21\2\u00da\u00db")
        buf.write("\5\36\20\2\u00db\u00df\3\2\2\2\u00dc\u00df\5 \21\2\u00dd")
        buf.write("\u00df\3\2\2\2\u00de\u00d9\3\2\2\2\u00de\u00dc\3\2\2\2")
        buf.write("\u00de\u00dd\3\2\2\2\u00df\37\3\2\2\2\u00e0\u00e1\7\32")
        buf.write("\2\2\u00e1\u00e2\5\32\16\2\u00e2!\3\2\2\2\u00e3\u00e4")
        buf.write("\7\24\2\2\u00e4\u00e5\t\4\2\2\u00e5\u00e6\7\25\2\2\u00e6")
        buf.write("\u00e7\5P)\2\u00e7\u00e8\7\26\2\2\u00e8\u00e9\5\62\32")
        buf.write("\2\u00e9\u00ea\5$\23\2\u00ea#\3\2\2\2\u00eb\u00f9\7\34")
        buf.write("\2\2\u00ec\u00ee\5\20\t\2\u00ed\u00ec\3\2\2\2\u00ee\u00ef")
        buf.write("\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0")
        buf.write("\u00f7\3\2\2\2\u00f1\u00f3\5&\24\2\u00f2\u00f4\79\2\2")
        buf.write("\u00f3\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f3\3")
        buf.write("\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f8\3\2\2\2\u00f7\u00f1")
        buf.write("\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00fa\3\2\2\2\u00f9")
        buf.write("\u00ed\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb\3\2\2\2")
        buf.write("\u00fb\u00fe\7\35\2\2\u00fc\u00fe\5\20\t\2\u00fd\u00eb")
        buf.write("\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe%\3\2\2\2\u00ff\u0100")
        buf.write("\t\5\2\2\u0100\'\3\2\2\2\u0101\u0102\7\64\2\2\u0102\u0107")
        buf.write("\7\t\2\2\u0103\u0104\7\66\2\2\u0104\u0106\7\t\2\2\u0105")
        buf.write("\u0103\3\2\2\2\u0106\u0109\3\2\2\2\u0107\u0105\3\2\2\2")
        buf.write("\u0107\u0108\3\2\2\2\u0108\u010a\3\2\2\2\u0109\u0107\3")
        buf.write("\2\2\2\u010a\u010b\7\65\2\2\u010b)\3\2\2\2\u010c\u010d")
        buf.write("\78\2\2\u010d\u010f\7\60\2\2\u010e\u0110\5\62\32\2\u010f")
        buf.write("\u010e\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0111\3\2\2\2")
        buf.write("\u0111\u0112\7\61\2\2\u0112+\3\2\2\2\u0113\u0118\5\62")
        buf.write("\32\2\u0114\u0115\7\66\2\2\u0115\u0117\5\62\32\2\u0116")
        buf.write("\u0114\3\2\2\2\u0117\u011a\3\2\2\2\u0118\u0116\3\2\2\2")
        buf.write("\u0118\u0119\3\2\2\2\u0119-\3\2\2\2\u011a\u0118\3\2\2")
        buf.write("\2\u011b\u0120\5\60\31\2\u011c\u011d\7\66\2\2\u011d\u011f")
        buf.write("\5\60\31\2\u011e\u011c\3\2\2\2\u011f\u0122\3\2\2\2\u0120")
        buf.write("\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0125\3\2\2\2")
        buf.write("\u0122\u0120\3\2\2\2\u0123\u0125\3\2\2\2\u0124\u011b\3")
        buf.write("\2\2\2\u0124\u0123\3\2\2\2\u0125/\3\2\2\2\u0126\u0127")
        buf.write("\7\3\2\2\u0127\u0128\78\2\2\u0128\61\3\2\2\2\u0129\u012a")
        buf.write("\b\32\1\2\u012a\u012b\5\64\33\2\u012b\u0131\3\2\2\2\u012c")
        buf.write("\u012d\f\4\2\2\u012d\u012e\7\5\2\2\u012e\u0130\5\64\33")
        buf.write("\2\u012f\u012c\3\2\2\2\u0130\u0133\3\2\2\2\u0131\u012f")
        buf.write("\3\2\2\2\u0131\u0132\3\2\2\2\u0132\63\3\2\2\2\u0133\u0131")
        buf.write("\3\2\2\2\u0134\u013f\5L\'\2\u0135\u013f\5P)\2\u0136\u013f")
        buf.write("\5T+\2\u0137\u013f\58\35\2\u0138\u013f\5:\36\2\u0139\u013f")
        buf.write("\7\b\2\2\u013a\u013b\7\60\2\2\u013b\u013c\5\64\33\2\u013c")
        buf.write("\u013d\7\61\2\2\u013d\u013f\3\2\2\2\u013e\u0134\3\2\2")
        buf.write("\2\u013e\u0135\3\2\2\2\u013e\u0136\3\2\2\2\u013e\u0137")
        buf.write("\3\2\2\2\u013e\u0138\3\2\2\2\u013e\u0139\3\2\2\2\u013e")
        buf.write("\u013a\3\2\2\2\u013f\65\3\2\2\2\u0140\u0141\t\6\2\2\u0141")
        buf.write("\67\3\2\2\2\u0142\u0146\78\2\2\u0143\u0146\5D#\2\u0144")
        buf.write("\u0146\5*\26\2\u0145\u0142\3\2\2\2\u0145\u0143\3\2\2\2")
        buf.write("\u0145\u0144\3\2\2\2\u01469\3\2\2\2\u0147\u0148\7\64\2")
        buf.write("\2\u0148\u0149\5<\37\2\u0149\u014a\7\65\2\2\u014a;\3\2")
        buf.write("\2\2\u014b\u014f\5> \2\u014c\u014f\5@!\2\u014d\u014f\5")
        buf.write("B\"\2\u014e\u014b\3\2\2\2\u014e\u014c\3\2\2\2\u014e\u014d")
        buf.write("\3\2\2\2\u014f=\3\2\2\2\u0150\u0151\7\t\2\2\u0151\u0152")
        buf.write("\7\66\2\2\u0152\u0156\5> \2\u0153\u0156\7\t\2\2\u0154")
        buf.write("\u0156\58\35\2\u0155\u0150\3\2\2\2\u0155\u0153\3\2\2\2")
        buf.write("\u0155\u0154\3\2\2\2\u0156?\3\2\2\2\u0157\u0158\7\b\2")
        buf.write("\2\u0158\u0159\7\66\2\2\u0159\u015d\5@!\2\u015a\u015d")
        buf.write("\7\b\2\2\u015b\u015d\58\35\2\u015c\u0157\3\2\2\2\u015c")
        buf.write("\u015a\3\2\2\2\u015c\u015b\3\2\2\2\u015dA\3\2\2\2\u015e")
        buf.write("\u015f\7\n\2\2\u015f\u0160\7\66\2\2\u0160\u0164\5B\"\2")
        buf.write("\u0161\u0164\7\n\2\2\u0162\u0164\58\35\2\u0163\u015e\3")
        buf.write("\2\2\2\u0163\u0161\3\2\2\2\u0163\u0162\3\2\2\2\u0164C")
        buf.write("\3\2\2\2\u0165\u0166\78\2\2\u0166\u0167\7\64\2\2\u0167")
        buf.write("\u0168\5F$\2\u0168\u0169\7\65\2\2\u0169E\3\2\2\2\u016a")
        buf.write("\u016b\b$\1\2\u016b\u016c\5H%\2\u016c\u0172\3\2\2\2\u016d")
        buf.write("\u016e\f\4\2\2\u016e\u016f\7\66\2\2\u016f\u0171\5F$\2")
        buf.write("\u0170\u016d\3\2\2\2\u0171\u0174\3\2\2\2\u0172\u0170\3")
        buf.write("\2\2\2\u0172\u0173\3\2\2\2\u0173G\3\2\2\2\u0174\u0172")
        buf.write("\3\2\2\2\u0175\u0176\b%\1\2\u0176\u0177\5J&\2\u0177\u017d")
        buf.write("\3\2\2\2\u0178\u0179\f\4\2\2\u0179\u017a\7\5\2\2\u017a")
        buf.write("\u017c\5J&\2\u017b\u0178\3\2\2\2\u017c\u017f\3\2\2\2\u017d")
        buf.write("\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017eI\3\2\2\2\u017f")
        buf.write("\u017d\3\2\2\2\u0180\u0184\7\t\2\2\u0181\u0184\5L\'\2")
        buf.write("\u0182\u0184\58\35\2\u0183\u0180\3\2\2\2\u0183\u0181\3")
        buf.write("\2\2\2\u0183\u0182\3\2\2\2\u0184K\3\2\2\2\u0185\u0186")
        buf.write("\5N(\2\u0186\u0187\7\5\2\2\u0187\u0188\5L\'\2\u0188\u018d")
        buf.write("\3\2\2\2\u0189\u018a\7 \2\2\u018a\u018d\5L\'\2\u018b\u018d")
        buf.write("\5N(\2\u018c\u0185\3\2\2\2\u018c\u0189\3\2\2\2\u018c\u018b")
        buf.write("\3\2\2\2\u018dM\3\2\2\2\u018e\u0191\7\t\2\2\u018f\u0191")
        buf.write("\58\35\2\u0190\u018e\3\2\2\2\u0190\u018f\3\2\2\2\u0191")
        buf.write("O\3\2\2\2\u0192\u0193\b)\1\2\u0193\u0197\5R*\2\u0194\u0195")
        buf.write("\7$\2\2\u0195\u0197\5P)\3\u0196\u0192\3\2\2\2\u0196\u0194")
        buf.write("\3\2\2\2\u0197\u019d\3\2\2\2\u0198\u0199\f\5\2\2\u0199")
        buf.write("\u019a\7\6\2\2\u019a\u019c\5R*\2\u019b\u0198\3\2\2\2\u019c")
        buf.write("\u019f\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019e\3\2\2\2")
        buf.write("\u019eQ\3\2\2\2\u019f\u019d\3\2\2\2\u01a0\u01a4\7\n\2")
        buf.write("\2\u01a1\u01a4\5T+\2\u01a2\u01a4\58\35\2\u01a3\u01a0\3")
        buf.write("\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a2\3\2\2\2\u01a4S")
        buf.write("\3\2\2\2\u01a5\u01a6\5V,\2\u01a6\u01a7\7\7\2\2\u01a7\u01a8")
        buf.write("\5V,\2\u01a8\u01ae\3\2\2\2\u01a9\u01aa\5X-\2\u01aa\u01ab")
        buf.write("\7/\2\2\u01ab\u01ac\5X-\2\u01ac\u01ae\3\2\2\2\u01ad\u01a5")
        buf.write("\3\2\2\2\u01ad\u01a9\3\2\2\2\u01aeU\3\2\2\2\u01af\u01b2")
        buf.write("\7\t\2\2\u01b0\u01b2\58\35\2\u01b1\u01af\3\2\2\2\u01b1")
        buf.write("\u01b0\3\2\2\2\u01b2W\3\2\2\2\u01b3\u01b6\7\b\2\2\u01b4")
        buf.write("\u01b6\58\35\2\u01b5\u01b3\3\2\2\2\u01b5\u01b4\3\2\2\2")
        buf.write("\u01b6Y\3\2\2\2\60]dnqv{\177\u0091\u0098\u009f\u00a2\u00ad")
        buf.write("\u00b2\u00ba\u00c1\u00c5\u00d7\u00de\u00ef\u00f5\u00f7")
        buf.write("\u00f9\u00fd\u0107\u010f\u0118\u0120\u0124\u0131\u013e")
        buf.write("\u0145\u014e\u0155\u015c\u0163\u0172\u017d\u0183\u018c")
        buf.write("\u0190\u0196\u019d\u01a3\u01ad\u01b1\u01b5")
        return buf.getvalue()


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
        self.checkVersion("4.9.2")
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TYPE) | (1 << ZCodeParser.IMPLIKEYS) | (1 << ZCodeParser.STRINGLIT) | (1 << ZCodeParser.NUMLIT) | (1 << ZCodeParser.BOOLIT) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FUNC) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LS) | (1 << ZCodeParser.ID))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOther" ):
                return visitor.visitOther(self)
            else:
                return visitor.visitChildren(self)




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
                    if not (_la==ZCodeParser.NEWLINE):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValdecl" ):
                return visitor.visitValdecl(self)
            else:
                return visitor.visitChildren(self)




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
                if not(_la==ZCodeParser.TYPE or _la==ZCodeParser.DYNAMIC):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 114
                self.match(ZCodeParser.ID)
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.LS:
                    self.state = 115
                    self.arraydecl()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.TYPE or _la==ZCodeParser.IMPLIKEYS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 119
                self.match(ZCodeParser.ID)
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.LS:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMainfunc" ):
                return visitor.visitMainfunc(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncblock" ):
                return visitor.visitFuncblock(self)
            else:
                return visitor.visitChildren(self)




    def funcblock(self):

        localctx = ZCodeParser.FuncblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcblock)
        self._la = 0 # Token type
        try:
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BEGIN, ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NEWLINE:
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
                    if not (_la==ZCodeParser.NEWLINE):
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
                    if not (_la==ZCodeParser.NEWLINE):
                        break

                pass
            elif token in [ZCodeParser.TYPE, ZCodeParser.IMPLIKEYS, ZCodeParser.STRINGLIT, ZCodeParser.NUMLIT, ZCodeParser.BOOLIT, ZCodeParser.RETURN, ZCodeParser.DYNAMIC, ZCodeParser.IF, ZCodeParser.MINUS, ZCodeParser.NOT, ZCodeParser.LB, ZCodeParser.LS, ZCodeParser.ID]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmts" ):
                return visitor.visitStmts(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtblock" ):
                return visitor.visitStmtblock(self)
            else:
                return visitor.visitChildren(self)




    def stmtblock(self):

        localctx = ZCodeParser.StmtblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_stmtblock)
        try:
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(ZCodeParser.BEGIN)
                self.state = 179
                self.stmtlist()
                self.state = 180
                self.match(ZCodeParser.END)
                pass
            elif token in [ZCodeParser.TYPE, ZCodeParser.IMPLIKEYS, ZCodeParser.STRINGLIT, ZCodeParser.NUMLIT, ZCodeParser.BOOLIT, ZCodeParser.RETURN, ZCodeParser.DYNAMIC, ZCodeParser.IF, ZCodeParser.MINUS, ZCodeParser.NOT, ZCodeParser.LB, ZCodeParser.LS, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.stmt()
                pass
            elif token in [ZCodeParser.ELIF, ZCodeParser.ELSE, ZCodeParser.NEWLINE]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfblock" ):
                return visitor.visitIfblock(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseblk" ):
                return visitor.visitElseblk(self)
            else:
                return visitor.visitChildren(self)




    def elseblk(self):

        localctx = ZCodeParser.ElseblkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_elseblk)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.match(ZCodeParser.ELSE)
                self.state = 211
                self.stmtblock()
                pass
            elif token in [ZCodeParser.NEWLINE]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifblk" ):
                return visitor.visitElifblk(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifblk_0" ):
                return visitor.visitElifblk_0(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




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
            if not(_la==ZCodeParser.NUMLIT or _la==ZCodeParser.ID):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopblock" ):
                return visitor.visitLoopblock(self)
            else:
                return visitor.visitChildren(self)




    def loopblock(self):

        localctx = ZCodeParser.LoopblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_loopblock)
        self._la = 0 # Token type
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.match(ZCodeParser.BEGIN)
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TYPE) | (1 << ZCodeParser.IMPLIKEYS) | (1 << ZCodeParser.STRINGLIT) | (1 << ZCodeParser.NUMLIT) | (1 << ZCodeParser.BOOLIT) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LS) | (1 << ZCodeParser.ID))) != 0):
                    self.state = 235 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 234
                        self.stmt()
                        self.state = 237 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TYPE) | (1 << ZCodeParser.IMPLIKEYS) | (1 << ZCodeParser.STRINGLIT) | (1 << ZCodeParser.NUMLIT) | (1 << ZCodeParser.BOOLIT) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LS) | (1 << ZCodeParser.ID))) != 0)):
                            break

                    self.state = 245
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==ZCodeParser.BREAK or _la==ZCodeParser.CONTINUE:
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
                            if not (_la==ZCodeParser.NEWLINE):
                                break





                self.state = 249
                self.match(ZCodeParser.END)
                pass
            elif token in [ZCodeParser.TYPE, ZCodeParser.IMPLIKEYS, ZCodeParser.STRINGLIT, ZCodeParser.NUMLIT, ZCodeParser.BOOLIT, ZCodeParser.RETURN, ZCodeParser.DYNAMIC, ZCodeParser.IF, ZCodeParser.MINUS, ZCodeParser.NOT, ZCodeParser.LB, ZCodeParser.LS, ZCodeParser.ID]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopkey" ):
                return visitor.visitLoopkey(self)
            else:
                return visitor.visitChildren(self)




    def loopkey(self):

        localctx = ZCodeParser.LoopkeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_loopkey)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.BREAK or _la==ZCodeParser.CONTINUE):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydecl" ):
                return visitor.visitArraydecl(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==ZCodeParser.COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.STRINGLIT) | (1 << ZCodeParser.NUMLIT) | (1 << ZCodeParser.BOOLIT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LS) | (1 << ZCodeParser.ID))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamcall" ):
                return visitor.visitParamcall(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==ZCodeParser.COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = ZCodeParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_paramlist)
        self._la = 0 # Token type
        try:
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.params()
                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.COMMA:
                    self.state = 282
                    self.match(ZCodeParser.COMMA)
                    self.state = 283
                    self.params()
                    self.state = 288
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [ZCodeParser.RB]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)



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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_01" ):
                return visitor.visitExp_01(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_00" ):
                return visitor.visitExp_00(self)
            else:
                return visitor.visitChildren(self)




    def exp_00(self):

        localctx = ZCodeParser.Exp_00Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exp_00)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.STRINGLIT) | (1 << ZCodeParser.NUMLIT) | (1 << ZCodeParser.BOOLIT))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpall" ):
                return visitor.visitExpall(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplist" ):
                return visitor.visitExplist(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplist_1" ):
                return visitor.visitExplist_1(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplist_2" ):
                return visitor.visitExplist_2(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplist_3" ):
                return visitor.visitExplist_3(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexp" ):
                return visitor.visitIndexp(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndop" ):
                return visitor.visitIndop(self)
            else:
                return visitor.visitChildren(self)



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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndop_0" ):
                return visitor.visitIndop_0(self)
            else:
                return visitor.visitChildren(self)



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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndop_1" ):
                return visitor.visitIndop_1(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAriexp" ):
                return visitor.visitAriexp(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAriexp_00" ):
                return visitor.visitAriexp_00(self)
            else:
                return visitor.visitChildren(self)




    def ariexp_00(self):

        localctx = ZCodeParser.Ariexp_00Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_ariexp_00)
        try:
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.match(ZCodeParser.NUMLIT)
                pass
            elif token in [ZCodeParser.ID]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicexp" ):
                return visitor.visitLogicexp(self)
            else:
                return visitor.visitChildren(self)



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
            if token in [ZCodeParser.STRINGLIT, ZCodeParser.NUMLIT, ZCodeParser.BOOLIT, ZCodeParser.ID]:
                self.state = 401
                self.logicexp_00()
                pass
            elif token in [ZCodeParser.NOT]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicexp_00" ):
                return visitor.visitLogicexp_00(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelatexp" ):
                return visitor.visitRelatexp(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelatexp_00" ):
                return visitor.visitRelatexp_00(self)
            else:
                return visitor.visitChildren(self)




    def relatexp_00(self):

        localctx = ZCodeParser.Relatexp_00Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_relatexp_00)
        try:
            self.state = 431
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.match(ZCodeParser.NUMLIT)
                pass
            elif token in [ZCodeParser.ID]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelatexp_01" ):
                return visitor.visitRelatexp_01(self)
            else:
                return visitor.visitChildren(self)




    def relatexp_01(self):

        localctx = ZCodeParser.Relatexp_01Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_relatexp_01)
        try:
            self.state = 435
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.match(ZCodeParser.STRINGLIT)
                pass
            elif token in [ZCodeParser.ID]:
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
         




