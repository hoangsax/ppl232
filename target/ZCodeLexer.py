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
        buf.write("\u01ce\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2")
        buf.write("\5\2\u0087\n\2\3\3\3\3\5\3\u008b\n\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\5\4\u0092\n\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u009a\n\5")
        buf.write("\3\6\3\6\5\6\u009e\n\6\3\7\3\7\3\7\3\7\7\7\u00a4\n\7\f")
        buf.write("\7\16\7\u00a7\13\7\3\7\3\7\3\7\3\b\3\b\3\b\7\b\u00af\n")
        buf.write("\b\f\b\16\b\u00b2\13\b\3\b\3\b\3\b\3\t\3\t\5\t\u00b9\n")
        buf.write("\t\3\t\3\t\3\t\5\t\u00be\n\t\5\t\u00c0\n\t\3\n\5\n\u00c3")
        buf.write("\n\n\3\n\7\n\u00c6\n\n\f\n\16\n\u00c9\13\n\3\13\3\13\7")
        buf.write("\13\u00cd\n\13\f\13\16\13\u00d0\13\13\3\f\3\f\5\f\u00d4")
        buf.write("\n\f\3\f\7\f\u00d7\n\f\f\f\16\f\u00da\13\f\3\r\3\r\5\r")
        buf.write("\u00de\n\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3!\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3")
        buf.write("(\3)\3)\3)\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3.\3/\3")
        buf.write("/\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3")
        buf.write("\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\3")
        buf.write("8\39\39\3:\3:\3:\7:\u018d\n:\f:\16:\u0190\13:\3:\5:\u0193")
        buf.write("\n:\3;\5;\u0196\n;\3;\7;\u0199\n;\f;\16;\u019c\13;\3<")
        buf.write("\5<\u019f\n<\3<\3<\3=\6=\u01a4\n=\r=\16=\u01a5\3=\3=\3")
        buf.write(">\3>\3>\3?\3?\3?\3?\7?\u01b1\n?\f?\16?\u01b4\13?\3?\3")
        buf.write("?\3?\3@\3@\7@\u01bb\n@\f@\16@\u01be\13@\3@\3@\7@\u01c2")
        buf.write("\n@\f@\16@\u01c5\13@\3@\5@\u01c8\n@\3@\3@\3A\3A\3A\5\u00a5")
        buf.write("\u00b0\u018e\2B\3\3\5\4\7\5\t\6\13\7\r\2\17\b\21\t\23")
        buf.write("\2\25\2\27\2\31\n\33\13\35\f\37\r!\16#\17%\20\'\21)\22")
        buf.write("+\23-\24/\25\61\26\63\27\65\30\67\319\32;\33=\34?\35A")
        buf.write("\36C\37E G!I\"K#M$O%Q&S\'U(W)Y*[+],_-a.c/e\60g\61i\62")
        buf.write("k\63m\64o\65q\66s\67u8w9y:{;}<\177=\u0081>\3\2\r\4\2$")
        buf.write("$))\3\2\62;\4\2GGgg\4\2--//\3\3\17\17\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\4\2\13\13\"\"\3\2$$\3\3$$\t\2))^^ddhhppttvv\2")
        buf.write("\u01e9\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2")
        buf.write("y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\3\u0086\3\2\2\2\5\u008a\3\2\2\2\7\u0091\3\2\2")
        buf.write("\2\t\u0099\3\2\2\2\13\u009d\3\2\2\2\r\u009f\3\2\2\2\17")
        buf.write("\u00ab\3\2\2\2\21\u00bf\3\2\2\2\23\u00c2\3\2\2\2\25\u00ca")
        buf.write("\3\2\2\2\27\u00d1\3\2\2\2\31\u00dd\3\2\2\2\33\u00df\3")
        buf.write("\2\2\2\35\u00e4\3\2\2\2\37\u00ea\3\2\2\2!\u00f1\3\2\2")
        buf.write("\2#\u00f6\3\2\2\2%\u00fd\3\2\2\2\'\u0104\3\2\2\2)\u0108")
        buf.write("\3\2\2\2+\u0110\3\2\2\2-\u0115\3\2\2\2/\u0119\3\2\2\2")
        buf.write("\61\u011f\3\2\2\2\63\u0122\3\2\2\2\65\u0128\3\2\2\2\67")
        buf.write("\u0131\3\2\2\29\u0134\3\2\2\2;\u0139\3\2\2\2=\u013e\3")
        buf.write("\2\2\2?\u0144\3\2\2\2A\u0148\3\2\2\2C\u014d\3\2\2\2E\u014f")
        buf.write("\3\2\2\2G\u0151\3\2\2\2I\u0153\3\2\2\2K\u0155\3\2\2\2")
        buf.write("M\u0157\3\2\2\2O\u015b\3\2\2\2Q\u015f\3\2\2\2S\u0162\3")
        buf.write("\2\2\2U\u0164\3\2\2\2W\u0167\3\2\2\2Y\u016a\3\2\2\2[\u016c")
        buf.write("\3\2\2\2]\u016f\3\2\2\2_\u0171\3\2\2\2a\u0174\3\2\2\2")
        buf.write("c\u0178\3\2\2\2e\u017b\3\2\2\2g\u017d\3\2\2\2i\u017f\3")
        buf.write("\2\2\2k\u0181\3\2\2\2m\u0183\3\2\2\2o\u0185\3\2\2\2q\u0187")
        buf.write("\3\2\2\2s\u0189\3\2\2\2u\u0195\3\2\2\2w\u019e\3\2\2\2")
        buf.write("y\u01a3\3\2\2\2{\u01a9\3\2\2\2}\u01ac\3\2\2\2\177\u01b8")
        buf.write("\3\2\2\2\u0081\u01cb\3\2\2\2\u0083\u0087\5\37\20\2\u0084")
        buf.write("\u0087\5#\22\2\u0085\u0087\5!\21\2\u0086\u0083\3\2\2\2")
        buf.write("\u0086\u0084\3\2\2\2\u0086\u0085\3\2\2\2\u0087\4\3\2\2")
        buf.write("\2\u0088\u008b\5\'\24\2\u0089\u008b\5)\25\2\u008a\u0088")
        buf.write("\3\2\2\2\u008a\u0089\3\2\2\2\u008b\6\3\2\2\2\u008c\u0092")
        buf.write("\5C\"\2\u008d\u0092\5G$\2\u008e\u0092\5K&\2\u008f\u0092")
        buf.write("\5E#\2\u0090\u0092\5I%\2\u0091\u008c\3\2\2\2\u0091\u008d")
        buf.write("\3\2\2\2\u0091\u008e\3\2\2\2\u0091\u008f\3\2\2\2\u0091")
        buf.write("\u0090\3\2\2\2\u0092\b\3\2\2\2\u0093\u009a\5S*\2\u0094")
        buf.write("\u009a\5Y-\2\u0095\u009a\5[.\2\u0096\u009a\5_\60\2\u0097")
        buf.write("\u009a\5]/\2\u0098\u009a\5W,\2\u0099\u0093\3\2\2\2\u0099")
        buf.write("\u0094\3\2\2\2\u0099\u0095\3\2\2\2\u0099\u0096\3\2\2\2")
        buf.write("\u0099\u0097\3\2\2\2\u0099\u0098\3\2\2\2\u009a\n\3\2\2")
        buf.write("\2\u009b\u009e\5O(\2\u009c\u009e\5Q)\2\u009d\u009b\3\2")
        buf.write("\2\2\u009d\u009c\3\2\2\2\u009e\f\3\2\2\2\u009f\u00a0\7")
        buf.write(")\2\2\u00a0\u00a1\7$\2\2\u00a1\u00a5\3\2\2\2\u00a2\u00a4")
        buf.write("\13\2\2\2\u00a3\u00a2\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5")
        buf.write("\u00a6\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a8\3\2\2\2")
        buf.write("\u00a7\u00a5\3\2\2\2\u00a8\u00a9\7)\2\2\u00a9\u00aa\7")
        buf.write("$\2\2\u00aa\16\3\2\2\2\u00ab\u00b0\7$\2\2\u00ac\u00af")
        buf.write("\n\2\2\2\u00ad\u00af\5\r\7\2\u00ae\u00ac\3\2\2\2\u00ae")
        buf.write("\u00ad\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0\u00b1\3\2\2\2")
        buf.write("\u00b0\u00ae\3\2\2\2\u00b1\u00b3\3\2\2\2\u00b2\u00b0\3")
        buf.write("\2\2\2\u00b3\u00b4\7$\2\2\u00b4\u00b5\b\b\2\2\u00b5\20")
        buf.write("\3\2\2\2\u00b6\u00b8\5\23\n\2\u00b7\u00b9\5\27\f\2\u00b8")
        buf.write("\u00b7\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00c0\3\2\2\2")
        buf.write("\u00ba\u00bb\5\23\n\2\u00bb\u00bd\5\25\13\2\u00bc\u00be")
        buf.write("\5\27\f\2\u00bd\u00bc\3\2\2\2\u00bd\u00be\3\2\2\2\u00be")
        buf.write("\u00c0\3\2\2\2\u00bf\u00b6\3\2\2\2\u00bf\u00ba\3\2\2\2")
        buf.write("\u00c0\22\3\2\2\2\u00c1\u00c3\4\62;\2\u00c2\u00c1\3\2")
        buf.write("\2\2\u00c3\u00c7\3\2\2\2\u00c4\u00c6\t\3\2\2\u00c5\u00c4")
        buf.write("\3\2\2\2\u00c6\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7")
        buf.write("\u00c8\3\2\2\2\u00c8\24\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca")
        buf.write("\u00ce\7\60\2\2\u00cb\u00cd\t\3\2\2\u00cc\u00cb\3\2\2")
        buf.write("\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf")
        buf.write("\3\2\2\2\u00cf\26\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1\u00d3")
        buf.write("\t\4\2\2\u00d2\u00d4\t\5\2\2\u00d3\u00d2\3\2\2\2\u00d3")
        buf.write("\u00d4\3\2\2\2\u00d4\u00d8\3\2\2\2\u00d5\u00d7\t\3\2\2")
        buf.write("\u00d6\u00d5\3\2\2\2\u00d7\u00da\3\2\2\2\u00d8\u00d6\3")
        buf.write("\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\30\3\2\2\2\u00da\u00d8")
        buf.write("\3\2\2\2\u00db\u00de\5\33\16\2\u00dc\u00de\5\35\17\2\u00dd")
        buf.write("\u00db\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de\32\3\2\2\2\u00df")
        buf.write("\u00e0\7v\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2\7w\2\2\u00e2")
        buf.write("\u00e3\7g\2\2\u00e3\34\3\2\2\2\u00e4\u00e5\7h\2\2\u00e5")
        buf.write("\u00e6\7c\2\2\u00e6\u00e7\7n\2\2\u00e7\u00e8\7u\2\2\u00e8")
        buf.write("\u00e9\7g\2\2\u00e9\36\3\2\2\2\u00ea\u00eb\7p\2\2\u00eb")
        buf.write("\u00ec\7w\2\2\u00ec\u00ed\7o\2\2\u00ed\u00ee\7d\2\2\u00ee")
        buf.write("\u00ef\7g\2\2\u00ef\u00f0\7t\2\2\u00f0 \3\2\2\2\u00f1")
        buf.write("\u00f2\7d\2\2\u00f2\u00f3\7q\2\2\u00f3\u00f4\7q\2\2\u00f4")
        buf.write("\u00f5\7n\2\2\u00f5\"\3\2\2\2\u00f6\u00f7\7u\2\2\u00f7")
        buf.write("\u00f8\7v\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa\7k\2\2\u00fa")
        buf.write("\u00fb\7p\2\2\u00fb\u00fc\7i\2\2\u00fc$\3\2\2\2\u00fd")
        buf.write("\u00fe\7t\2\2\u00fe\u00ff\7g\2\2\u00ff\u0100\7v\2\2\u0100")
        buf.write("\u0101\7w\2\2\u0101\u0102\7t\2\2\u0102\u0103\7p\2\2\u0103")
        buf.write("&\3\2\2\2\u0104\u0105\7x\2\2\u0105\u0106\7c\2\2\u0106")
        buf.write("\u0107\7t\2\2\u0107(\3\2\2\2\u0108\u0109\7f\2\2\u0109")
        buf.write("\u010a\7{\2\2\u010a\u010b\7p\2\2\u010b\u010c\7c\2\2\u010c")
        buf.write("\u010d\7o\2\2\u010d\u010e\7k\2\2\u010e\u010f\7e\2\2\u010f")
        buf.write("*\3\2\2\2\u0110\u0111\7h\2\2\u0111\u0112\7w\2\2\u0112")
        buf.write("\u0113\7p\2\2\u0113\u0114\7e\2\2\u0114,\3\2\2\2\u0115")
        buf.write("\u0116\7h\2\2\u0116\u0117\7q\2\2\u0117\u0118\7t\2\2\u0118")
        buf.write(".\3\2\2\2\u0119\u011a\7w\2\2\u011a\u011b\7p\2\2\u011b")
        buf.write("\u011c\7v\2\2\u011c\u011d\7k\2\2\u011d\u011e\7n\2\2\u011e")
        buf.write("\60\3\2\2\2\u011f\u0120\7d\2\2\u0120\u0121\7{\2\2\u0121")
        buf.write("\62\3\2\2\2\u0122\u0123\7d\2\2\u0123\u0124\7t\2\2\u0124")
        buf.write("\u0125\7g\2\2\u0125\u0126\7c\2\2\u0126\u0127\7m\2\2\u0127")
        buf.write("\64\3\2\2\2\u0128\u0129\7e\2\2\u0129\u012a\7q\2\2\u012a")
        buf.write("\u012b\7p\2\2\u012b\u012c\7v\2\2\u012c\u012d\7k\2\2\u012d")
        buf.write("\u012e\7p\2\2\u012e\u012f\7w\2\2\u012f\u0130\7g\2\2\u0130")
        buf.write("\66\3\2\2\2\u0131\u0132\7k\2\2\u0132\u0133\7h\2\2\u0133")
        buf.write("8\3\2\2\2\u0134\u0135\7g\2\2\u0135\u0136\7n\2\2\u0136")
        buf.write("\u0137\7k\2\2\u0137\u0138\7h\2\2\u0138:\3\2\2\2\u0139")
        buf.write("\u013a\7g\2\2\u013a\u013b\7n\2\2\u013b\u013c\7u\2\2\u013c")
        buf.write("\u013d\7g\2\2\u013d<\3\2\2\2\u013e\u013f\7d\2\2\u013f")
        buf.write("\u0140\7g\2\2\u0140\u0141\7i\2\2\u0141\u0142\7k\2\2\u0142")
        buf.write("\u0143\7p\2\2\u0143>\3\2\2\2\u0144\u0145\7g\2\2\u0145")
        buf.write("\u0146\7p\2\2\u0146\u0147\7f\2\2\u0147@\3\2\2\2\u0148")
        buf.write("\u0149\7o\2\2\u0149\u014a\7c\2\2\u014a\u014b\7k\2\2\u014b")
        buf.write("\u014c\7p\2\2\u014cB\3\2\2\2\u014d\u014e\7-\2\2\u014e")
        buf.write("D\3\2\2\2\u014f\u0150\7/\2\2\u0150F\3\2\2\2\u0151\u0152")
        buf.write("\7,\2\2\u0152H\3\2\2\2\u0153\u0154\7\61\2\2\u0154J\3\2")
        buf.write("\2\2\u0155\u0156\7\'\2\2\u0156L\3\2\2\2\u0157\u0158\7")
        buf.write("p\2\2\u0158\u0159\7q\2\2\u0159\u015a\7v\2\2\u015aN\3\2")
        buf.write("\2\2\u015b\u015c\7c\2\2\u015c\u015d\7p\2\2\u015d\u015e")
        buf.write("\7f\2\2\u015eP\3\2\2\2\u015f\u0160\7q\2\2\u0160\u0161")
        buf.write("\7t\2\2\u0161R\3\2\2\2\u0162\u0163\7?\2\2\u0163T\3\2\2")
        buf.write("\2\u0164\u0165\7>\2\2\u0165\u0166\7/\2\2\u0166V\3\2\2")
        buf.write("\2\u0167\u0168\7#\2\2\u0168\u0169\7?\2\2\u0169X\3\2\2")
        buf.write("\2\u016a\u016b\7>\2\2\u016bZ\3\2\2\2\u016c\u016d\7>\2")
        buf.write("\2\u016d\u016e\7?\2\2\u016e\\\3\2\2\2\u016f\u0170\7@\2")
        buf.write("\2\u0170^\3\2\2\2\u0171\u0172\7@\2\2\u0172\u0173\7?\2")
        buf.write("\2\u0173`\3\2\2\2\u0174\u0175\7\60\2\2\u0175\u0176\7\60")
        buf.write("\2\2\u0176\u0177\7\60\2\2\u0177b\3\2\2\2\u0178\u0179\7")
        buf.write("?\2\2\u0179\u017a\7?\2\2\u017ad\3\2\2\2\u017b\u017c\7")
        buf.write("*\2\2\u017cf\3\2\2\2\u017d\u017e\7+\2\2\u017eh\3\2\2\2")
        buf.write("\u017f\u0180\7}\2\2\u0180j\3\2\2\2\u0181\u0182\7\177\2")
        buf.write("\2\u0182l\3\2\2\2\u0183\u0184\7]\2\2\u0184n\3\2\2\2\u0185")
        buf.write("\u0186\7_\2\2\u0186p\3\2\2\2\u0187\u0188\7.\2\2\u0188")
        buf.write("r\3\2\2\2\u0189\u018a\7%\2\2\u018a\u018e\7%\2\2\u018b")
        buf.write("\u018d\13\2\2\2\u018c\u018b\3\2\2\2\u018d\u0190\3\2\2")
        buf.write("\2\u018e\u018f\3\2\2\2\u018e\u018c\3\2\2\2\u018f\u0192")
        buf.write("\3\2\2\2\u0190\u018e\3\2\2\2\u0191\u0193\t\6\2\2\u0192")
        buf.write("\u0191\3\2\2\2\u0193t\3\2\2\2\u0194\u0196\t\7\2\2\u0195")
        buf.write("\u0194\3\2\2\2\u0196\u019a\3\2\2\2\u0197\u0199\t\b\2\2")
        buf.write("\u0198\u0197\3\2\2\2\u0199\u019c\3\2\2\2\u019a\u0198\3")
        buf.write("\2\2\2\u019a\u019b\3\2\2\2\u019bv\3\2\2\2\u019c\u019a")
        buf.write("\3\2\2\2\u019d\u019f\7\17\2\2\u019e\u019d\3\2\2\2\u019e")
        buf.write("\u019f\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a1\7\f\2\2")
        buf.write("\u01a1x\3\2\2\2\u01a2\u01a4\t\t\2\2\u01a3\u01a2\3\2\2")
        buf.write("\2\u01a4\u01a5\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6")
        buf.write("\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a8\b=\3\2\u01a8")
        buf.write("z\3\2\2\2\u01a9\u01aa\13\2\2\2\u01aa\u01ab\b>\4\2\u01ab")
        buf.write("|\3\2\2\2\u01ac\u01b2\7$\2\2\u01ad\u01b1\n\n\2\2\u01ae")
        buf.write("\u01af\7)\2\2\u01af\u01b1\7$\2\2\u01b0\u01ad\3\2\2\2\u01b0")
        buf.write("\u01ae\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0\3\2\2\2")
        buf.write("\u01b2\u01b3\3\2\2\2\u01b3\u01b5\3\2\2\2\u01b4\u01b2\3")
        buf.write("\2\2\2\u01b5\u01b6\7\2\2\3\u01b6\u01b7\b?\5\2\u01b7~\3")
        buf.write("\2\2\2\u01b8\u01bc\7$\2\2\u01b9\u01bb\13\2\2\2\u01ba\u01b9")
        buf.write("\3\2\2\2\u01bb\u01be\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc")
        buf.write("\u01bd\3\2\2\2\u01bd\u01bf\3\2\2\2\u01be\u01bc\3\2\2\2")
        buf.write("\u01bf\u01c3\5\u0081A\2\u01c0\u01c2\13\2\2\2\u01c1\u01c0")
        buf.write("\3\2\2\2\u01c2\u01c5\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3")
        buf.write("\u01c4\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5\u01c3\3\2\2\2")
        buf.write("\u01c6\u01c8\t\13\2\2\u01c7\u01c6\3\2\2\2\u01c8\u01c9")
        buf.write("\3\2\2\2\u01c9\u01ca\b@\6\2\u01ca\u0080\3\2\2\2\u01cb")
        buf.write("\u01cc\7^\2\2\u01cc\u01cd\n\f\2\2\u01cd\u0082\3\2\2\2")
        buf.write(" \2\u0086\u008a\u0091\u0099\u009d\u00a5\u00ae\u00b0\u00b8")
        buf.write("\u00bd\u00bf\u00c2\u00c7\u00ce\u00d3\u00d8\u00dd\u018e")
        buf.write("\u0192\u0195\u0198\u019a\u019e\u01a5\u01b0\u01b2\u01bc")
        buf.write("\u01c3\u01c7\7\3\b\2\b\2\2\3>\3\3?\4\3@\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TYPE = 1
    IMPLIKEYS = 2
    NUMOP = 3
    NUMRELAOPS = 4
    LOGICOPBIN = 5
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
            "TYPE", "IMPLIKEYS", "NUMOP", "NUMRELAOPS", "LOGICOPBIN", "STRINGLIT", 
            "NUMLIT", "BOOLIT", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
            "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
            "CONTINUE", "IF", "ELIF", "ELSE", "BEGIN", "END", "MAIN", "PLUS", 
            "MINUS", "STAR", "SLASH", "PERCENT", "NOT", "AND", "OR", "EQUAL", 
            "ASSIGN", "INEQUAL", "LESSTHAN", "LESSEQUAL", "MORETHAN", "MOREEQUAL", 
            "ELLIPSIS", "EQUALITY", "LB", "RB", "LC", "RC", "LS", "RS", 
            "COMMA", "COMMENT", "ID", "NEWLINE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ES" ]

    ruleNames = [ "TYPE", "IMPLIKEYS", "NUMOP", "NUMRELAOPS", "LOGICOPBIN", 
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
     


