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
        buf.write("\u01cd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2")
        buf.write("\5\2\u0087\n\2\3\3\3\3\5\3\u008b\n\3\3\4\3\4\3\4\3\4\5")
        buf.write("\4\u0091\n\4\3\5\3\5\5\5\u0095\n\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\5\6\u009d\n\6\3\7\3\7\3\7\3\7\7\7\u00a3\n\7\f\7\16")
        buf.write("\7\u00a6\13\7\3\7\3\7\3\7\3\b\3\b\3\b\7\b\u00ae\n\b\f")
        buf.write("\b\16\b\u00b1\13\b\3\b\3\b\3\b\3\t\3\t\5\t\u00b8\n\t\3")
        buf.write("\t\3\t\3\t\5\t\u00bd\n\t\5\t\u00bf\n\t\3\n\5\n\u00c2\n")
        buf.write("\n\3\n\7\n\u00c5\n\n\f\n\16\n\u00c8\13\n\3\13\3\13\7\13")
        buf.write("\u00cc\n\13\f\13\16\13\u00cf\13\13\3\f\3\f\5\f\u00d3\n")
        buf.write("\f\3\f\7\f\u00d6\n\f\f\f\16\f\u00d9\13\f\3\r\3\r\5\r\u00dd")
        buf.write("\n\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3#")
        buf.write("\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3)\3")
        buf.write(")\3)\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3.\3/\3/\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3")
        buf.write(":\3:\3:\7:\u018c\n:\f:\16:\u018f\13:\3:\5:\u0192\n:\3")
        buf.write(";\5;\u0195\n;\3;\7;\u0198\n;\f;\16;\u019b\13;\3<\5<\u019e")
        buf.write("\n<\3<\3<\3=\6=\u01a3\n=\r=\16=\u01a4\3=\3=\3>\3>\3>\3")
        buf.write("?\3?\3?\3?\7?\u01b0\n?\f?\16?\u01b3\13?\3?\3?\3?\3@\3")
        buf.write("@\7@\u01ba\n@\f@\16@\u01bd\13@\3@\3@\7@\u01c1\n@\f@\16")
        buf.write("@\u01c4\13@\3@\5@\u01c7\n@\3@\3@\3A\3A\3A\5\u00a4\u00af")
        buf.write("\u018d\2B\3\3\5\4\7\5\t\6\13\7\r\2\17\b\21\t\23\2\25\2")
        buf.write("\27\2\31\n\33\13\35\f\37\r!\16#\17%\20\'\21)\22+\23-\24")
        buf.write("/\25\61\26\63\27\65\30\67\319\32;\33=\34?\35A\36C\37E")
        buf.write(" G!I\"K#M$O%Q&S\'U(W)Y*[+],_-a.c/e\60g\61i\62k\63m\64")
        buf.write("o\65q\66s\67u8w9y:{;}<\177=\u0081>\3\2\r\4\2$$))\3\2\62")
        buf.write(";\4\2GGgg\4\2--//\3\3\17\17\5\2C\\aac|\6\2\62;C\\aac|")
        buf.write("\4\2\13\13\"\"\3\2$$\3\3$$\t\2))^^ddhhppttvv\2\u01e7\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\3\u0086")
        buf.write("\3\2\2\2\5\u008a\3\2\2\2\7\u0090\3\2\2\2\t\u0094\3\2\2")
        buf.write("\2\13\u009c\3\2\2\2\r\u009e\3\2\2\2\17\u00aa\3\2\2\2\21")
        buf.write("\u00be\3\2\2\2\23\u00c1\3\2\2\2\25\u00c9\3\2\2\2\27\u00d0")
        buf.write("\3\2\2\2\31\u00dc\3\2\2\2\33\u00de\3\2\2\2\35\u00e3\3")
        buf.write("\2\2\2\37\u00e9\3\2\2\2!\u00f0\3\2\2\2#\u00f5\3\2\2\2")
        buf.write("%\u00fc\3\2\2\2\'\u0103\3\2\2\2)\u0107\3\2\2\2+\u010f")
        buf.write("\3\2\2\2-\u0114\3\2\2\2/\u0118\3\2\2\2\61\u011e\3\2\2")
        buf.write("\2\63\u0121\3\2\2\2\65\u0127\3\2\2\2\67\u0130\3\2\2\2")
        buf.write("9\u0133\3\2\2\2;\u0138\3\2\2\2=\u013d\3\2\2\2?\u0143\3")
        buf.write("\2\2\2A\u0147\3\2\2\2C\u014c\3\2\2\2E\u014e\3\2\2\2G\u0150")
        buf.write("\3\2\2\2I\u0152\3\2\2\2K\u0154\3\2\2\2M\u0156\3\2\2\2")
        buf.write("O\u015a\3\2\2\2Q\u015e\3\2\2\2S\u0161\3\2\2\2U\u0163\3")
        buf.write("\2\2\2W\u0166\3\2\2\2Y\u0169\3\2\2\2[\u016b\3\2\2\2]\u016e")
        buf.write("\3\2\2\2_\u0170\3\2\2\2a\u0173\3\2\2\2c\u0177\3\2\2\2")
        buf.write("e\u017a\3\2\2\2g\u017c\3\2\2\2i\u017e\3\2\2\2k\u0180\3")
        buf.write("\2\2\2m\u0182\3\2\2\2o\u0184\3\2\2\2q\u0186\3\2\2\2s\u0188")
        buf.write("\3\2\2\2u\u0194\3\2\2\2w\u019d\3\2\2\2y\u01a2\3\2\2\2")
        buf.write("{\u01a8\3\2\2\2}\u01ab\3\2\2\2\177\u01b7\3\2\2\2\u0081")
        buf.write("\u01ca\3\2\2\2\u0083\u0087\5\37\20\2\u0084\u0087\5#\22")
        buf.write("\2\u0085\u0087\5!\21\2\u0086\u0083\3\2\2\2\u0086\u0084")
        buf.write("\3\2\2\2\u0086\u0085\3\2\2\2\u0087\4\3\2\2\2\u0088\u008b")
        buf.write("\5\'\24\2\u0089\u008b\5)\25\2\u008a\u0088\3\2\2\2\u008a")
        buf.write("\u0089\3\2\2\2\u008b\6\3\2\2\2\u008c\u0091\5C\"\2\u008d")
        buf.write("\u0091\5G$\2\u008e\u0091\5K&\2\u008f\u0091\5E#\2\u0090")
        buf.write("\u008c\3\2\2\2\u0090\u008d\3\2\2\2\u0090\u008e\3\2\2\2")
        buf.write("\u0090\u008f\3\2\2\2\u0091\b\3\2\2\2\u0092\u0095\5O(\2")
        buf.write("\u0093\u0095\5Q)\2\u0094\u0092\3\2\2\2\u0094\u0093\3\2")
        buf.write("\2\2\u0095\n\3\2\2\2\u0096\u009d\5S*\2\u0097\u009d\5W")
        buf.write(",\2\u0098\u009d\5Y-\2\u0099\u009d\5[.\2\u009a\u009d\5")
        buf.write("_\60\2\u009b\u009d\5]/\2\u009c\u0096\3\2\2\2\u009c\u0097")
        buf.write("\3\2\2\2\u009c\u0098\3\2\2\2\u009c\u0099\3\2\2\2\u009c")
        buf.write("\u009a\3\2\2\2\u009c\u009b\3\2\2\2\u009d\f\3\2\2\2\u009e")
        buf.write("\u009f\7)\2\2\u009f\u00a0\7$\2\2\u00a0\u00a4\3\2\2\2\u00a1")
        buf.write("\u00a3\13\2\2\2\u00a2\u00a1\3\2\2\2\u00a3\u00a6\3\2\2")
        buf.write("\2\u00a4\u00a5\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00a7")
        buf.write("\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a7\u00a8\7)\2\2\u00a8")
        buf.write("\u00a9\7$\2\2\u00a9\16\3\2\2\2\u00aa\u00af\7$\2\2\u00ab")
        buf.write("\u00ae\n\2\2\2\u00ac\u00ae\5\r\7\2\u00ad\u00ab\3\2\2\2")
        buf.write("\u00ad\u00ac\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00b0\3")
        buf.write("\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00b2\3\2\2\2\u00b1\u00af")
        buf.write("\3\2\2\2\u00b2\u00b3\7$\2\2\u00b3\u00b4\b\b\2\2\u00b4")
        buf.write("\20\3\2\2\2\u00b5\u00b7\5\23\n\2\u00b6\u00b8\5\27\f\2")
        buf.write("\u00b7\u00b6\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00bf\3")
        buf.write("\2\2\2\u00b9\u00ba\5\23\n\2\u00ba\u00bc\5\25\13\2\u00bb")
        buf.write("\u00bd\5\27\f\2\u00bc\u00bb\3\2\2\2\u00bc\u00bd\3\2\2")
        buf.write("\2\u00bd\u00bf\3\2\2\2\u00be\u00b5\3\2\2\2\u00be\u00b9")
        buf.write("\3\2\2\2\u00bf\22\3\2\2\2\u00c0\u00c2\4\62;\2\u00c1\u00c0")
        buf.write("\3\2\2\2\u00c2\u00c6\3\2\2\2\u00c3\u00c5\t\3\2\2\u00c4")
        buf.write("\u00c3\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2")
        buf.write("\u00c6\u00c7\3\2\2\2\u00c7\24\3\2\2\2\u00c8\u00c6\3\2")
        buf.write("\2\2\u00c9\u00cd\7\60\2\2\u00ca\u00cc\t\3\2\2\u00cb\u00ca")
        buf.write("\3\2\2\2\u00cc\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd")
        buf.write("\u00ce\3\2\2\2\u00ce\26\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0")
        buf.write("\u00d2\t\4\2\2\u00d1\u00d3\t\5\2\2\u00d2\u00d1\3\2\2\2")
        buf.write("\u00d2\u00d3\3\2\2\2\u00d3\u00d7\3\2\2\2\u00d4\u00d6\t")
        buf.write("\3\2\2\u00d5\u00d4\3\2\2\2\u00d6\u00d9\3\2\2\2\u00d7\u00d5")
        buf.write("\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\30\3\2\2\2\u00d9\u00d7")
        buf.write("\3\2\2\2\u00da\u00dd\5\33\16\2\u00db\u00dd\5\35\17\2\u00dc")
        buf.write("\u00da\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd\32\3\2\2\2\u00de")
        buf.write("\u00df\7v\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1\7w\2\2\u00e1")
        buf.write("\u00e2\7g\2\2\u00e2\34\3\2\2\2\u00e3\u00e4\7h\2\2\u00e4")
        buf.write("\u00e5\7c\2\2\u00e5\u00e6\7n\2\2\u00e6\u00e7\7u\2\2\u00e7")
        buf.write("\u00e8\7g\2\2\u00e8\36\3\2\2\2\u00e9\u00ea\7p\2\2\u00ea")
        buf.write("\u00eb\7w\2\2\u00eb\u00ec\7o\2\2\u00ec\u00ed\7d\2\2\u00ed")
        buf.write("\u00ee\7g\2\2\u00ee\u00ef\7t\2\2\u00ef \3\2\2\2\u00f0")
        buf.write("\u00f1\7d\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3\7q\2\2\u00f3")
        buf.write("\u00f4\7n\2\2\u00f4\"\3\2\2\2\u00f5\u00f6\7u\2\2\u00f6")
        buf.write("\u00f7\7v\2\2\u00f7\u00f8\7t\2\2\u00f8\u00f9\7k\2\2\u00f9")
        buf.write("\u00fa\7p\2\2\u00fa\u00fb\7i\2\2\u00fb$\3\2\2\2\u00fc")
        buf.write("\u00fd\7t\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff\7v\2\2\u00ff")
        buf.write("\u0100\7w\2\2\u0100\u0101\7t\2\2\u0101\u0102\7p\2\2\u0102")
        buf.write("&\3\2\2\2\u0103\u0104\7x\2\2\u0104\u0105\7c\2\2\u0105")
        buf.write("\u0106\7t\2\2\u0106(\3\2\2\2\u0107\u0108\7f\2\2\u0108")
        buf.write("\u0109\7{\2\2\u0109\u010a\7p\2\2\u010a\u010b\7c\2\2\u010b")
        buf.write("\u010c\7o\2\2\u010c\u010d\7k\2\2\u010d\u010e\7e\2\2\u010e")
        buf.write("*\3\2\2\2\u010f\u0110\7h\2\2\u0110\u0111\7w\2\2\u0111")
        buf.write("\u0112\7p\2\2\u0112\u0113\7e\2\2\u0113,\3\2\2\2\u0114")
        buf.write("\u0115\7h\2\2\u0115\u0116\7q\2\2\u0116\u0117\7t\2\2\u0117")
        buf.write(".\3\2\2\2\u0118\u0119\7w\2\2\u0119\u011a\7p\2\2\u011a")
        buf.write("\u011b\7v\2\2\u011b\u011c\7k\2\2\u011c\u011d\7n\2\2\u011d")
        buf.write("\60\3\2\2\2\u011e\u011f\7d\2\2\u011f\u0120\7{\2\2\u0120")
        buf.write("\62\3\2\2\2\u0121\u0122\7d\2\2\u0122\u0123\7t\2\2\u0123")
        buf.write("\u0124\7g\2\2\u0124\u0125\7c\2\2\u0125\u0126\7m\2\2\u0126")
        buf.write("\64\3\2\2\2\u0127\u0128\7e\2\2\u0128\u0129\7q\2\2\u0129")
        buf.write("\u012a\7p\2\2\u012a\u012b\7v\2\2\u012b\u012c\7k\2\2\u012c")
        buf.write("\u012d\7p\2\2\u012d\u012e\7w\2\2\u012e\u012f\7g\2\2\u012f")
        buf.write("\66\3\2\2\2\u0130\u0131\7k\2\2\u0131\u0132\7h\2\2\u0132")
        buf.write("8\3\2\2\2\u0133\u0134\7g\2\2\u0134\u0135\7n\2\2\u0135")
        buf.write("\u0136\7k\2\2\u0136\u0137\7h\2\2\u0137:\3\2\2\2\u0138")
        buf.write("\u0139\7g\2\2\u0139\u013a\7n\2\2\u013a\u013b\7u\2\2\u013b")
        buf.write("\u013c\7g\2\2\u013c<\3\2\2\2\u013d\u013e\7d\2\2\u013e")
        buf.write("\u013f\7g\2\2\u013f\u0140\7i\2\2\u0140\u0141\7k\2\2\u0141")
        buf.write("\u0142\7p\2\2\u0142>\3\2\2\2\u0143\u0144\7g\2\2\u0144")
        buf.write("\u0145\7p\2\2\u0145\u0146\7f\2\2\u0146@\3\2\2\2\u0147")
        buf.write("\u0148\7o\2\2\u0148\u0149\7c\2\2\u0149\u014a\7k\2\2\u014a")
        buf.write("\u014b\7p\2\2\u014bB\3\2\2\2\u014c\u014d\7-\2\2\u014d")
        buf.write("D\3\2\2\2\u014e\u014f\7/\2\2\u014fF\3\2\2\2\u0150\u0151")
        buf.write("\7,\2\2\u0151H\3\2\2\2\u0152\u0153\7\61\2\2\u0153J\3\2")
        buf.write("\2\2\u0154\u0155\7\'\2\2\u0155L\3\2\2\2\u0156\u0157\7")
        buf.write("p\2\2\u0157\u0158\7q\2\2\u0158\u0159\7v\2\2\u0159N\3\2")
        buf.write("\2\2\u015a\u015b\7c\2\2\u015b\u015c\7p\2\2\u015c\u015d")
        buf.write("\7f\2\2\u015dP\3\2\2\2\u015e\u015f\7q\2\2\u015f\u0160")
        buf.write("\7t\2\2\u0160R\3\2\2\2\u0161\u0162\7?\2\2\u0162T\3\2\2")
        buf.write("\2\u0163\u0164\7>\2\2\u0164\u0165\7/\2\2\u0165V\3\2\2")
        buf.write("\2\u0166\u0167\7#\2\2\u0167\u0168\7?\2\2\u0168X\3\2\2")
        buf.write("\2\u0169\u016a\7>\2\2\u016aZ\3\2\2\2\u016b\u016c\7>\2")
        buf.write("\2\u016c\u016d\7?\2\2\u016d\\\3\2\2\2\u016e\u016f\7@\2")
        buf.write("\2\u016f^\3\2\2\2\u0170\u0171\7@\2\2\u0171\u0172\7?\2")
        buf.write("\2\u0172`\3\2\2\2\u0173\u0174\7\60\2\2\u0174\u0175\7\60")
        buf.write("\2\2\u0175\u0176\7\60\2\2\u0176b\3\2\2\2\u0177\u0178\7")
        buf.write("?\2\2\u0178\u0179\7?\2\2\u0179d\3\2\2\2\u017a\u017b\7")
        buf.write("*\2\2\u017bf\3\2\2\2\u017c\u017d\7+\2\2\u017dh\3\2\2\2")
        buf.write("\u017e\u017f\7}\2\2\u017fj\3\2\2\2\u0180\u0181\7\177\2")
        buf.write("\2\u0181l\3\2\2\2\u0182\u0183\7]\2\2\u0183n\3\2\2\2\u0184")
        buf.write("\u0185\7_\2\2\u0185p\3\2\2\2\u0186\u0187\7.\2\2\u0187")
        buf.write("r\3\2\2\2\u0188\u0189\7%\2\2\u0189\u018d\7%\2\2\u018a")
        buf.write("\u018c\13\2\2\2\u018b\u018a\3\2\2\2\u018c\u018f\3\2\2")
        buf.write("\2\u018d\u018e\3\2\2\2\u018d\u018b\3\2\2\2\u018e\u0191")
        buf.write("\3\2\2\2\u018f\u018d\3\2\2\2\u0190\u0192\t\6\2\2\u0191")
        buf.write("\u0190\3\2\2\2\u0192t\3\2\2\2\u0193\u0195\t\7\2\2\u0194")
        buf.write("\u0193\3\2\2\2\u0195\u0199\3\2\2\2\u0196\u0198\t\b\2\2")
        buf.write("\u0197\u0196\3\2\2\2\u0198\u019b\3\2\2\2\u0199\u0197\3")
        buf.write("\2\2\2\u0199\u019a\3\2\2\2\u019av\3\2\2\2\u019b\u0199")
        buf.write("\3\2\2\2\u019c\u019e\7\17\2\2\u019d\u019c\3\2\2\2\u019d")
        buf.write("\u019e\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a0\7\f\2\2")
        buf.write("\u01a0x\3\2\2\2\u01a1\u01a3\t\t\2\2\u01a2\u01a1\3\2\2")
        buf.write("\2\u01a3\u01a4\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5")
        buf.write("\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a7\b=\3\2\u01a7")
        buf.write("z\3\2\2\2\u01a8\u01a9\13\2\2\2\u01a9\u01aa\b>\4\2\u01aa")
        buf.write("|\3\2\2\2\u01ab\u01b1\7$\2\2\u01ac\u01b0\n\n\2\2\u01ad")
        buf.write("\u01ae\7)\2\2\u01ae\u01b0\7$\2\2\u01af\u01ac\3\2\2\2\u01af")
        buf.write("\u01ad\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2")
        buf.write("\u01b1\u01b2\3\2\2\2\u01b2\u01b4\3\2\2\2\u01b3\u01b1\3")
        buf.write("\2\2\2\u01b4\u01b5\7\2\2\3\u01b5\u01b6\b?\5\2\u01b6~\3")
        buf.write("\2\2\2\u01b7\u01bb\7$\2\2\u01b8\u01ba\13\2\2\2\u01b9\u01b8")
        buf.write("\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb")
        buf.write("\u01bc\3\2\2\2\u01bc\u01be\3\2\2\2\u01bd\u01bb\3\2\2\2")
        buf.write("\u01be\u01c2\5\u0081A\2\u01bf\u01c1\13\2\2\2\u01c0\u01bf")
        buf.write("\3\2\2\2\u01c1\u01c4\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2")
        buf.write("\u01c3\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4\u01c2\3\2\2\2")
        buf.write("\u01c5\u01c7\t\13\2\2\u01c6\u01c5\3\2\2\2\u01c7\u01c8")
        buf.write("\3\2\2\2\u01c8\u01c9\b@\6\2\u01c9\u0080\3\2\2\2\u01ca")
        buf.write("\u01cb\7^\2\2\u01cb\u01cc\n\f\2\2\u01cc\u0082\3\2\2\2")
        buf.write(" \2\u0086\u008a\u0090\u0094\u009c\u00a4\u00ad\u00af\u00b7")
        buf.write("\u00bc\u00be\u00c1\u00c6\u00cd\u00d2\u00d7\u00dc\u018d")
        buf.write("\u0191\u0194\u0197\u0199\u019d\u01a4\u01af\u01b1\u01bb")
        buf.write("\u01c2\u01c6\7\3\b\2\b\2\2\3>\3\3?\4\3@\5")
        return buf.getvalue()


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
        self.checkVersion("4.9.2")
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
     


