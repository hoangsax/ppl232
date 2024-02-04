# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2>")
        buf.write("\u01cb\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\5\3\u008a\n\3\3\4\3\4\5\4\u008e\n\4\3\5\3")
        buf.write("\5\3\5\3\5\5\5\u0094\n\5\3\6\3\6\5\6\u0098\n\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\5\7\u00a0\n\7\3\b\3\b\3\b\3\b\7\b\u00a6")
        buf.write("\n\b\f\b\16\b\u00a9\13\b\3\b\3\b\3\b\3\t\3\t\3\t\7\t\u00b1")
        buf.write("\n\t\f\t\16\t\u00b4\13\t\3\t\3\t\3\t\3\n\3\n\5\n\u00bb")
        buf.write("\n\n\3\n\3\n\3\n\5\n\u00c0\n\n\5\n\u00c2\n\n\3\13\5\13")
        buf.write("\u00c5\n\13\3\13\7\13\u00c8\n\13\f\13\16\13\u00cb\13\13")
        buf.write("\3\f\3\f\7\f\u00cf\n\f\f\f\16\f\u00d2\13\f\3\r\3\r\5\r")
        buf.write("\u00d6\n\r\3\r\7\r\u00d9\n\r\f\r\16\r\u00dc\13\r\3\16")
        buf.write("\3\16\5\16\u00e0\n\16\3\17\3\17\3\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\3(\3)\3)\3")
        buf.write(")\3)\3*\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\3")
        buf.write("9\39\3:\3:\3;\3;\3;\7;\u018f\n;\f;\16;\u0192\13;\3;\5")
        buf.write(";\u0195\n;\3<\5<\u0198\n<\3<\7<\u019b\n<\f<\16<\u019e")
        buf.write("\13<\3=\6=\u01a1\n=\r=\16=\u01a2\3=\3=\3>\3>\3>\3?\3?")
        buf.write("\3?\3?\7?\u01ae\n?\f?\16?\u01b1\13?\3?\3?\3?\3@\3@\7@")
        buf.write("\u01b8\n@\f@\16@\u01bb\13@\3@\3@\7@\u01bf\n@\f@\16@\u01c2")
        buf.write("\13@\3@\5@\u01c5\n@\3@\3@\3A\3A\3A\5\u00a7\u00b2\u0190")
        buf.write("\2B\3\3\5\4\7\5\t\6\13\7\r\b\17\2\21\t\23\n\25\2\27\2")
        buf.write("\31\2\33\13\35\f\37\r!\16#\17%\20\'\21)\22+\23-\24/\25")
        buf.write("\61\26\63\27\65\30\67\319\32;\33=\34?\35A\36C\37E G!I")
        buf.write("\"K#M$O%Q&S\'U(W)Y*[+],_-a.c/e\60g\61i\62k\63m\64o\65")
        buf.write("q\66s\67u8w9y:{;}<\177=\u0081>\3\2\r\4\2$$))\3\2\62;\4")
        buf.write("\2GGgg\4\2--//\3\3\17\17\5\2C\\aac|\6\2\62;C\\aac|\5\2")
        buf.write("\13\f\17\17\"\"\3\2$$\3\3$$\t\2))^^ddhhppttvv\2\u01e4")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\33\3")
        buf.write("\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2")
        buf.write("\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2")
        buf.write("\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2")
        buf.write("\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2")
        buf.write("\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2")
        buf.write("\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3")
        buf.write("\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]")
        buf.write("\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2")
        buf.write("g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2")
        buf.write("\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2")
        buf.write("\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2")
        buf.write("\3\u0083\3\2\2\2\5\u0089\3\2\2\2\7\u008d\3\2\2\2\t\u0093")
        buf.write("\3\2\2\2\13\u0097\3\2\2\2\r\u009f\3\2\2\2\17\u00a1\3\2")
        buf.write("\2\2\21\u00ad\3\2\2\2\23\u00c1\3\2\2\2\25\u00c4\3\2\2")
        buf.write("\2\27\u00cc\3\2\2\2\31\u00d3\3\2\2\2\33\u00df\3\2\2\2")
        buf.write("\35\u00e1\3\2\2\2\37\u00e6\3\2\2\2!\u00ec\3\2\2\2#\u00f3")
        buf.write("\3\2\2\2%\u00f8\3\2\2\2\'\u00ff\3\2\2\2)\u0106\3\2\2\2")
        buf.write("+\u010a\3\2\2\2-\u0112\3\2\2\2/\u0117\3\2\2\2\61\u011b")
        buf.write("\3\2\2\2\63\u0121\3\2\2\2\65\u0124\3\2\2\2\67\u012a\3")
        buf.write("\2\2\29\u0133\3\2\2\2;\u0136\3\2\2\2=\u013b\3\2\2\2?\u0140")
        buf.write("\3\2\2\2A\u0146\3\2\2\2C\u014a\3\2\2\2E\u014f\3\2\2\2")
        buf.write("G\u0151\3\2\2\2I\u0153\3\2\2\2K\u0155\3\2\2\2M\u0157\3")
        buf.write("\2\2\2O\u0159\3\2\2\2Q\u015d\3\2\2\2S\u0161\3\2\2\2U\u0164")
        buf.write("\3\2\2\2W\u0166\3\2\2\2Y\u0169\3\2\2\2[\u016c\3\2\2\2")
        buf.write("]\u016e\3\2\2\2_\u0171\3\2\2\2a\u0173\3\2\2\2c\u0176\3")
        buf.write("\2\2\2e\u017a\3\2\2\2g\u017d\3\2\2\2i\u017f\3\2\2\2k\u0181")
        buf.write("\3\2\2\2m\u0183\3\2\2\2o\u0185\3\2\2\2q\u0187\3\2\2\2")
        buf.write("s\u0189\3\2\2\2u\u018b\3\2\2\2w\u0197\3\2\2\2y\u01a0\3")
        buf.write("\2\2\2{\u01a6\3\2\2\2}\u01a9\3\2\2\2\177\u01b5\3\2\2\2")
        buf.write("\u0081\u01c8\3\2\2\2\u0083\u0084\7^\2\2\u0084\u0085\7")
        buf.write("t\2\2\u0085\4\3\2\2\2\u0086\u008a\5!\21\2\u0087\u008a")
        buf.write("\5%\23\2\u0088\u008a\5#\22\2\u0089\u0086\3\2\2\2\u0089")
        buf.write("\u0087\3\2\2\2\u0089\u0088\3\2\2\2\u008a\6\3\2\2\2\u008b")
        buf.write("\u008e\5)\25\2\u008c\u008e\5+\26\2\u008d\u008b\3\2\2\2")
        buf.write("\u008d\u008c\3\2\2\2\u008e\b\3\2\2\2\u008f\u0094\5E#\2")
        buf.write("\u0090\u0094\5I%\2\u0091\u0094\5M\'\2\u0092\u0094\5G$")
        buf.write("\2\u0093\u008f\3\2\2\2\u0093\u0090\3\2\2\2\u0093\u0091")
        buf.write("\3\2\2\2\u0093\u0092\3\2\2\2\u0094\n\3\2\2\2\u0095\u0098")
        buf.write("\5Q)\2\u0096\u0098\5S*\2\u0097\u0095\3\2\2\2\u0097\u0096")
        buf.write("\3\2\2\2\u0098\f\3\2\2\2\u0099\u00a0\5U+\2\u009a\u00a0")
        buf.write("\5Y-\2\u009b\u00a0\5[.\2\u009c\u00a0\5]/\2\u009d\u00a0")
        buf.write("\5a\61\2\u009e\u00a0\5_\60\2\u009f\u0099\3\2\2\2\u009f")
        buf.write("\u009a\3\2\2\2\u009f\u009b\3\2\2\2\u009f\u009c\3\2\2\2")
        buf.write("\u009f\u009d\3\2\2\2\u009f\u009e\3\2\2\2\u00a0\16\3\2")
        buf.write("\2\2\u00a1\u00a2\7)\2\2\u00a2\u00a3\7$\2\2\u00a3\u00a7")
        buf.write("\3\2\2\2\u00a4\u00a6\13\2\2\2\u00a5\u00a4\3\2\2\2\u00a6")
        buf.write("\u00a9\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a7\u00a5\3\2\2\2")
        buf.write("\u00a8\u00aa\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa\u00ab\7")
        buf.write(")\2\2\u00ab\u00ac\7$\2\2\u00ac\20\3\2\2\2\u00ad\u00b2")
        buf.write("\7$\2\2\u00ae\u00b1\n\2\2\2\u00af\u00b1\5\17\b\2\u00b0")
        buf.write("\u00ae\3\2\2\2\u00b0\u00af\3\2\2\2\u00b1\u00b4\3\2\2\2")
        buf.write("\u00b2\u00b3\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00b5\3")
        buf.write("\2\2\2\u00b4\u00b2\3\2\2\2\u00b5\u00b6\7$\2\2\u00b6\u00b7")
        buf.write("\b\t\2\2\u00b7\22\3\2\2\2\u00b8\u00ba\5\25\13\2\u00b9")
        buf.write("\u00bb\5\31\r\2\u00ba\u00b9\3\2\2\2\u00ba\u00bb\3\2\2")
        buf.write("\2\u00bb\u00c2\3\2\2\2\u00bc\u00bd\5\25\13\2\u00bd\u00bf")
        buf.write("\5\27\f\2\u00be\u00c0\5\31\r\2\u00bf\u00be\3\2\2\2\u00bf")
        buf.write("\u00c0\3\2\2\2\u00c0\u00c2\3\2\2\2\u00c1\u00b8\3\2\2\2")
        buf.write("\u00c1\u00bc\3\2\2\2\u00c2\24\3\2\2\2\u00c3\u00c5\4\62")
        buf.write(";\2\u00c4\u00c3\3\2\2\2\u00c5\u00c9\3\2\2\2\u00c6\u00c8")
        buf.write("\t\3\2\2\u00c7\u00c6\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9")
        buf.write("\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\26\3\2\2\2\u00cb")
        buf.write("\u00c9\3\2\2\2\u00cc\u00d0\7\60\2\2\u00cd\u00cf\t\3\2")
        buf.write("\2\u00ce\u00cd\3\2\2\2\u00cf\u00d2\3\2\2\2\u00d0\u00ce")
        buf.write("\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\30\3\2\2\2\u00d2\u00d0")
        buf.write("\3\2\2\2\u00d3\u00d5\t\4\2\2\u00d4\u00d6\t\5\2\2\u00d5")
        buf.write("\u00d4\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00da\3\2\2\2")
        buf.write("\u00d7\u00d9\t\3\2\2\u00d8\u00d7\3\2\2\2\u00d9\u00dc\3")
        buf.write("\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00db\3\2\2\2\u00db\32")
        buf.write("\3\2\2\2\u00dc\u00da\3\2\2\2\u00dd\u00e0\5\35\17\2\u00de")
        buf.write("\u00e0\5\37\20\2\u00df\u00dd\3\2\2\2\u00df\u00de\3\2\2")
        buf.write("\2\u00e0\34\3\2\2\2\u00e1\u00e2\7v\2\2\u00e2\u00e3\7t")
        buf.write("\2\2\u00e3\u00e4\7w\2\2\u00e4\u00e5\7g\2\2\u00e5\36\3")
        buf.write("\2\2\2\u00e6\u00e7\7h\2\2\u00e7\u00e8\7c\2\2\u00e8\u00e9")
        buf.write("\7n\2\2\u00e9\u00ea\7u\2\2\u00ea\u00eb\7g\2\2\u00eb \3")
        buf.write("\2\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee\7w\2\2\u00ee\u00ef")
        buf.write("\7o\2\2\u00ef\u00f0\7d\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2")
        buf.write("\7t\2\2\u00f2\"\3\2\2\2\u00f3\u00f4\7d\2\2\u00f4\u00f5")
        buf.write("\7q\2\2\u00f5\u00f6\7q\2\2\u00f6\u00f7\7n\2\2\u00f7$\3")
        buf.write("\2\2\2\u00f8\u00f9\7u\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb")
        buf.write("\7t\2\2\u00fb\u00fc\7k\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe")
        buf.write("\7i\2\2\u00fe&\3\2\2\2\u00ff\u0100\7t\2\2\u0100\u0101")
        buf.write("\7g\2\2\u0101\u0102\7v\2\2\u0102\u0103\7w\2\2\u0103\u0104")
        buf.write("\7t\2\2\u0104\u0105\7p\2\2\u0105(\3\2\2\2\u0106\u0107")
        buf.write("\7x\2\2\u0107\u0108\7c\2\2\u0108\u0109\7t\2\2\u0109*\3")
        buf.write("\2\2\2\u010a\u010b\7f\2\2\u010b\u010c\7{\2\2\u010c\u010d")
        buf.write("\7p\2\2\u010d\u010e\7c\2\2\u010e\u010f\7o\2\2\u010f\u0110")
        buf.write("\7k\2\2\u0110\u0111\7e\2\2\u0111,\3\2\2\2\u0112\u0113")
        buf.write("\7h\2\2\u0113\u0114\7w\2\2\u0114\u0115\7p\2\2\u0115\u0116")
        buf.write("\7e\2\2\u0116.\3\2\2\2\u0117\u0118\7h\2\2\u0118\u0119")
        buf.write("\7q\2\2\u0119\u011a\7t\2\2\u011a\60\3\2\2\2\u011b\u011c")
        buf.write("\7w\2\2\u011c\u011d\7p\2\2\u011d\u011e\7v\2\2\u011e\u011f")
        buf.write("\7k\2\2\u011f\u0120\7n\2\2\u0120\62\3\2\2\2\u0121\u0122")
        buf.write("\7d\2\2\u0122\u0123\7{\2\2\u0123\64\3\2\2\2\u0124\u0125")
        buf.write("\7d\2\2\u0125\u0126\7t\2\2\u0126\u0127\7g\2\2\u0127\u0128")
        buf.write("\7c\2\2\u0128\u0129\7m\2\2\u0129\66\3\2\2\2\u012a\u012b")
        buf.write("\7e\2\2\u012b\u012c\7q\2\2\u012c\u012d\7p\2\2\u012d\u012e")
        buf.write("\7v\2\2\u012e\u012f\7k\2\2\u012f\u0130\7p\2\2\u0130\u0131")
        buf.write("\7w\2\2\u0131\u0132\7g\2\2\u01328\3\2\2\2\u0133\u0134")
        buf.write("\7k\2\2\u0134\u0135\7h\2\2\u0135:\3\2\2\2\u0136\u0137")
        buf.write("\7g\2\2\u0137\u0138\7n\2\2\u0138\u0139\7k\2\2\u0139\u013a")
        buf.write("\7h\2\2\u013a<\3\2\2\2\u013b\u013c\7g\2\2\u013c\u013d")
        buf.write("\7n\2\2\u013d\u013e\7u\2\2\u013e\u013f\7g\2\2\u013f>\3")
        buf.write("\2\2\2\u0140\u0141\7d\2\2\u0141\u0142\7g\2\2\u0142\u0143")
        buf.write("\7i\2\2\u0143\u0144\7k\2\2\u0144\u0145\7p\2\2\u0145@\3")
        buf.write("\2\2\2\u0146\u0147\7g\2\2\u0147\u0148\7p\2\2\u0148\u0149")
        buf.write("\7f\2\2\u0149B\3\2\2\2\u014a\u014b\7o\2\2\u014b\u014c")
        buf.write("\7c\2\2\u014c\u014d\7k\2\2\u014d\u014e\7p\2\2\u014eD\3")
        buf.write("\2\2\2\u014f\u0150\7-\2\2\u0150F\3\2\2\2\u0151\u0152\7")
        buf.write("/\2\2\u0152H\3\2\2\2\u0153\u0154\7,\2\2\u0154J\3\2\2\2")
        buf.write("\u0155\u0156\7\61\2\2\u0156L\3\2\2\2\u0157\u0158\7\'\2")
        buf.write("\2\u0158N\3\2\2\2\u0159\u015a\7p\2\2\u015a\u015b\7q\2")
        buf.write("\2\u015b\u015c\7v\2\2\u015cP\3\2\2\2\u015d\u015e\7c\2")
        buf.write("\2\u015e\u015f\7p\2\2\u015f\u0160\7f\2\2\u0160R\3\2\2")
        buf.write("\2\u0161\u0162\7q\2\2\u0162\u0163\7t\2\2\u0163T\3\2\2")
        buf.write("\2\u0164\u0165\7?\2\2\u0165V\3\2\2\2\u0166\u0167\7>\2")
        buf.write("\2\u0167\u0168\7/\2\2\u0168X\3\2\2\2\u0169\u016a\7#\2")
        buf.write("\2\u016a\u016b\7?\2\2\u016bZ\3\2\2\2\u016c\u016d\7>\2")
        buf.write("\2\u016d\\\3\2\2\2\u016e\u016f\7>\2\2\u016f\u0170\7?\2")
        buf.write("\2\u0170^\3\2\2\2\u0171\u0172\7@\2\2\u0172`\3\2\2\2\u0173")
        buf.write("\u0174\7@\2\2\u0174\u0175\7?\2\2\u0175b\3\2\2\2\u0176")
        buf.write("\u0177\7\60\2\2\u0177\u0178\7\60\2\2\u0178\u0179\7\60")
        buf.write("\2\2\u0179d\3\2\2\2\u017a\u017b\7?\2\2\u017b\u017c\7?")
        buf.write("\2\2\u017cf\3\2\2\2\u017d\u017e\7*\2\2\u017eh\3\2\2\2")
        buf.write("\u017f\u0180\7+\2\2\u0180j\3\2\2\2\u0181\u0182\7}\2\2")
        buf.write("\u0182l\3\2\2\2\u0183\u0184\7\177\2\2\u0184n\3\2\2\2\u0185")
        buf.write("\u0186\7]\2\2\u0186p\3\2\2\2\u0187\u0188\7_\2\2\u0188")
        buf.write("r\3\2\2\2\u0189\u018a\7.\2\2\u018at\3\2\2\2\u018b\u018c")
        buf.write("\7%\2\2\u018c\u0190\7%\2\2\u018d\u018f\13\2\2\2\u018e")
        buf.write("\u018d\3\2\2\2\u018f\u0192\3\2\2\2\u0190\u0191\3\2\2\2")
        buf.write("\u0190\u018e\3\2\2\2\u0191\u0194\3\2\2\2\u0192\u0190\3")
        buf.write("\2\2\2\u0193\u0195\t\6\2\2\u0194\u0193\3\2\2\2\u0195v")
        buf.write("\3\2\2\2\u0196\u0198\t\7\2\2\u0197\u0196\3\2\2\2\u0198")
        buf.write("\u019c\3\2\2\2\u0199\u019b\t\b\2\2\u019a\u0199\3\2\2\2")
        buf.write("\u019b\u019e\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019d\3")
        buf.write("\2\2\2\u019dx\3\2\2\2\u019e\u019c\3\2\2\2\u019f\u01a1")
        buf.write("\t\t\2\2\u01a0\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2")
        buf.write("\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a4\3\2\2\2")
        buf.write("\u01a4\u01a5\b=\3\2\u01a5z\3\2\2\2\u01a6\u01a7\13\2\2")
        buf.write("\2\u01a7\u01a8\b>\4\2\u01a8|\3\2\2\2\u01a9\u01af\7$\2")
        buf.write("\2\u01aa\u01ae\n\n\2\2\u01ab\u01ac\7)\2\2\u01ac\u01ae")
        buf.write("\7$\2\2\u01ad\u01aa\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ae")
        buf.write("\u01b1\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2")
        buf.write("\u01b0\u01b2\3\2\2\2\u01b1\u01af\3\2\2\2\u01b2\u01b3\7")
        buf.write("\2\2\3\u01b3\u01b4\b?\5\2\u01b4~\3\2\2\2\u01b5\u01b9\7")
        buf.write("$\2\2\u01b6\u01b8\13\2\2\2\u01b7\u01b6\3\2\2\2\u01b8\u01bb")
        buf.write("\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba")
        buf.write("\u01bc\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bc\u01c0\5\u0081")
        buf.write("A\2\u01bd\u01bf\13\2\2\2\u01be\u01bd\3\2\2\2\u01bf\u01c2")
        buf.write("\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1")
        buf.write("\u01c4\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c3\u01c5\t\13\2")
        buf.write("\2\u01c4\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c7")
        buf.write("\b@\6\2\u01c7\u0080\3\2\2\2\u01c8\u01c9\7^\2\2\u01c9\u01ca")
        buf.write("\n\f\2\2\u01ca\u0082\3\2\2\2\37\2\u0089\u008d\u0093\u0097")
        buf.write("\u009f\u00a7\u00b0\u00b2\u00ba\u00bf\u00c1\u00c4\u00c9")
        buf.write("\u00d0\u00d5\u00da\u00df\u0190\u0194\u0197\u019a\u019c")
        buf.write("\u01a2\u01ad\u01af\u01b9\u01c0\u01c4\7\3\t\2\b\2\2\3>")
        buf.write("\3\3?\4\3@\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    TYPE = 2
    IMPLIKEYS = 3
    NUMOP = 4
    LOGICOPBIN = 5
    NUMRELAOPS = 6
    STRINGLIT = 7
    NUMLIT = 8
    BOOLIT = 9
    TRUE = 10
    FALSE = 11
    NUMBER = 12
    BOOL = 13
    STRING = 14
    RETURN = 15
    VAR = 16
    DYNAMIC = 17
    FUNC = 18
    FOR = 19
    UNTIL = 20
    BY = 21
    BREAK = 22
    CONTINUE = 23
    IF = 24
    ELIF = 25
    ELSE = 26
    BEGIN = 27
    END = 28
    MAIN = 29
    PLUS = 30
    MINUS = 31
    STAR = 32
    SLASH = 33
    PERCENT = 34
    NOT = 35
    AND = 36
    OR = 37
    EQUAL = 38
    ASSIGN = 39
    INEQUAL = 40
    LESSTHAN = 41
    LESSEQUAL = 42
    MORETHAN = 43
    MOREEQUAL = 44
    ELLIPSIS = 45
    EQUALITY = 46
    LB = 47
    RB = 48
    LC = 49
    RC = 50
    LS = 51
    RS = 52
    COMMA = 53
    COMMENT = 54
    ID = 55
    WS = 56
    ERROR_CHAR = 57
    UNCLOSE_STRING = 58
    ILLEGAL_ESCAPE = 59
    ES = 60

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\r'", "'true'", "'false'", "'number'", "'bool'", "'string'", 
            "'return'", "'var'", "'dynamic'", "'func'", "'for'", "'until'", 
            "'by'", "'break'", "'continue'", "'if'", "'elif'", "'else'", 
            "'begin'", "'end'", "'main'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'not'", "'and'", "'or'", "'='", "'<-'", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'...'", "'=='", "'('", "')'", "'{'", "'}'", 
            "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "TYPE", "IMPLIKEYS", "NUMOP", "LOGICOPBIN", "NUMRELAOPS", "STRINGLIT", 
            "NUMLIT", "BOOLIT", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
            "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
            "CONTINUE", "IF", "ELIF", "ELSE", "BEGIN", "END", "MAIN", "PLUS", 
            "MINUS", "STAR", "SLASH", "PERCENT", "NOT", "AND", "OR", "EQUAL", 
            "ASSIGN", "INEQUAL", "LESSTHAN", "LESSEQUAL", "MORETHAN", "MOREEQUAL", 
            "ELLIPSIS", "EQUALITY", "LB", "RB", "LC", "RC", "LS", "RS", 
            "COMMA", "COMMENT", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ES" ]

    ruleNames = [ "T__0", "TYPE", "IMPLIKEYS", "NUMOP", "LOGICOPBIN", "NUMRELAOPS", 
                  "SUBSTR", "STRINGLIT", "NUMLIT", "INTERGER", "DECIMAL", 
                  "EXPONENT", "BOOLIT", "TRUE", "FALSE", "NUMBER", "BOOL", 
                  "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                  "BY", "BREAK", "CONTINUE", "IF", "ELIF", "ELSE", "BEGIN", 
                  "END", "MAIN", "PLUS", "MINUS", "STAR", "SLASH", "PERCENT", 
                  "NOT", "AND", "OR", "EQUAL", "ASSIGN", "INEQUAL", "LESSTHAN", 
                  "LESSEQUAL", "MORETHAN", "MOREEQUAL", "ELLIPSIS", "EQUALITY", 
                  "LB", "RB", "LC", "RC", "LS", "RS", "COMMA", "COMMENT", 
                  "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ES" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[7] = self.STRINGLIT_action 
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
     


