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
        buf.write("\u0176\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\3\2\7\2P\n\2\f\2\16\2S\13\2\3\2\3\2\7\2W\n\2")
        buf.write("\f\2\16\2Z\13\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\5\4c\n\4\3")
        buf.write("\5\3\5\3\5\3\5\7\5i\n\5\f\5\16\5l\13\5\3\5\3\5\5\5p\n")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5x\n\5\3\6\3\6\3\6\5\6}\n")
        buf.write("\6\3\6\3\6\3\6\5\6\u0082\n\6\3\6\3\6\5\6\u0086\n\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\7\t\u0097\n\t\f\t\16\t\u009a\13\t\3\t\3\t\3\t\5\t\u009f")
        buf.write("\n\t\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00aa")
        buf.write("\n\13\3\f\3\f\7\f\u00ae\n\f\f\f\16\f\u00b1\13\f\3\f\3")
        buf.write("\f\3\f\5\f\u00b6\n\f\3\r\3\r\5\r\u00ba\n\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\7\16\u00c2\n\16\f\16\16\16\u00c5\13\16")
        buf.write("\3\16\5\16\u00c8\n\16\3\17\3\17\3\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\6\23\u00df\n\23\r\23\16\23\u00e0")
        buf.write("\3\23\5\23\u00e4\n\23\5\23\u00e6\n\23\3\23\3\23\5\23\u00ea")
        buf.write("\n\23\3\24\3\24\3\25\3\25\3\25\3\25\7\25\u00f2\n\25\f")
        buf.write("\25\16\25\u00f5\13\25\3\25\3\25\3\26\3\26\3\26\5\26\u00fc")
        buf.write("\n\26\3\26\3\26\3\27\3\27\3\27\7\27\u0103\n\27\f\27\16")
        buf.write("\27\u0106\13\27\3\30\3\30\3\30\7\30\u010b\n\30\f\30\16")
        buf.write("\30\u010e\13\30\3\30\5\30\u0111\n\30\3\31\3\31\3\31\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\7\32\u011c\n\32\f\32\16\32")
        buf.write("\u011f\13\32\3\33\3\33\3\33\3\33\3\33\5\33\u0126\n\33")
        buf.write("\3\34\3\34\3\35\3\35\3\35\5\35\u012d\n\35\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u013a")
        buf.write("\n\37\f\37\16\37\u013d\13\37\3 \3 \3 \5 \u0142\n \3!\3")
        buf.write("!\3!\3!\3!\3!\3!\5!\u014b\n!\3\"\3\"\5\"\u014f\n\"\3#")
        buf.write("\3#\3#\3#\5#\u0155\n#\3#\3#\3#\7#\u015a\n#\f#\16#\u015d")
        buf.write("\13#\3$\3$\3$\5$\u0162\n$\3%\3%\3%\3%\3%\3%\3%\3%\5%\u016c")
        buf.write("\n%\3&\3&\5&\u0170\n&\3\'\3\'\5\'\u0174\n\'\3\'\2\5\62")
        buf.write("<D(\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJL\2\7\4\2\4\4\23\23\3\2\4\5\4\2\n\n")
        buf.write("99\3\2\30\31\3\2\t\13\2\u0184\2Q\3\2\2\2\4]\3\2\2\2\6")
        buf.write("b\3\2\2\2\bw\3\2\2\2\n\u0085\3\2\2\2\f\u0087\3\2\2\2\16")
        buf.write("\u008d\3\2\2\2\20\u009e\3\2\2\2\22\u00a0\3\2\2\2\24\u00a9")
        buf.write("\3\2\2\2\26\u00b5\3\2\2\2\30\u00b9\3\2\2\2\32\u00be\3")
        buf.write("\2\2\2\34\u00c9\3\2\2\2\36\u00ce\3\2\2\2 \u00d1\3\2\2")
        buf.write("\2\"\u00d4\3\2\2\2$\u00e9\3\2\2\2&\u00eb\3\2\2\2(\u00ed")
        buf.write("\3\2\2\2*\u00f8\3\2\2\2,\u00ff\3\2\2\2.\u0110\3\2\2\2")
        buf.write("\60\u0112\3\2\2\2\62\u0115\3\2\2\2\64\u0125\3\2\2\2\66")
        buf.write("\u0127\3\2\2\28\u012c\3\2\2\2:\u012e\3\2\2\2<\u0133\3")
        buf.write("\2\2\2>\u0141\3\2\2\2@\u014a\3\2\2\2B\u014e\3\2\2\2D\u0154")
        buf.write("\3\2\2\2F\u0161\3\2\2\2H\u016b\3\2\2\2J\u016f\3\2\2\2")
        buf.write("L\u0173\3\2\2\2NP\5\6\4\2ON\3\2\2\2PS\3\2\2\2QO\3\2\2")
        buf.write("\2QR\3\2\2\2RT\3\2\2\2SQ\3\2\2\2TX\5\f\7\2UW\5\6\4\2V")
        buf.write("U\3\2\2\2WZ\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y[\3\2\2\2ZX\3")
        buf.write("\2\2\2[\\\7\2\2\3\\\3\3\2\2\2]^\5\f\7\2^\5\3\2\2\2_c\5")
        buf.write("\16\b\2`c\5\n\6\2ac\5\24\13\2b_\3\2\2\2b`\3\2\2\2ba\3")
        buf.write("\2\2\2c\7\3\2\2\2de\7\3\2\2ef\7\35\2\2fj\7\3\2\2gi\5\24")
        buf.write("\13\2hg\3\2\2\2il\3\2\2\2jh\3\2\2\2jk\3\2\2\2ko\3\2\2")
        buf.write("\2lj\3\2\2\2mn\7\21\2\2np\5\62\32\2om\3\2\2\2op\3\2\2")
        buf.write("\2pq\3\2\2\2qr\7\3\2\2rs\7\36\2\2sx\7\3\2\2tu\7\21\2\2")
        buf.write("ux\5\62\32\2vx\3\2\2\2wd\3\2\2\2wt\3\2\2\2wv\3\2\2\2x")
        buf.write("\t\3\2\2\2yz\t\2\2\2z|\79\2\2{}\5(\25\2|{\3\2\2\2|}\3")
        buf.write("\2\2\2}\u0086\3\2\2\2~\177\t\3\2\2\177\u0081\79\2\2\u0080")
        buf.write("\u0082\5(\25\2\u0081\u0080\3\2\2\2\u0081\u0082\3\2\2\2")
        buf.write("\u0082\u0083\3\2\2\2\u0083\u0084\7)\2\2\u0084\u0086\5")
        buf.write("\62\32\2\u0085y\3\2\2\2\u0085~\3\2\2\2\u0086\13\3\2\2")
        buf.write("\2\u0087\u0088\7\24\2\2\u0088\u0089\7\37\2\2\u0089\u008a")
        buf.write("\7\61\2\2\u008a\u008b\7\62\2\2\u008b\u008c\5\20\t\2\u008c")
        buf.write("\r\3\2\2\2\u008d\u008e\7\24\2\2\u008e\u008f\79\2\2\u008f")
        buf.write("\u0090\7\61\2\2\u0090\u0091\5.\30\2\u0091\u0092\7\62\2")
        buf.write("\2\u0092\u0093\5\20\t\2\u0093\17\3\2\2\2\u0094\u0098\7")
        buf.write("\35\2\2\u0095\u0097\5\24\13\2\u0096\u0095\3\2\2\2\u0097")
        buf.write("\u009a\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2")
        buf.write("\u0099\u009b\3\2\2\2\u009a\u0098\3\2\2\2\u009b\u009f\7")
        buf.write("\36\2\2\u009c\u009d\7\21\2\2\u009d\u009f\5\62\32\2\u009e")
        buf.write("\u0094\3\2\2\2\u009e\u009c\3\2\2\2\u009f\21\3\2\2\2\u00a0")
        buf.write("\u00a1\3\2\2\2\u00a1\23\3\2\2\2\u00a2\u00aa\5\n\6\2\u00a3")
        buf.write("\u00aa\5\30\r\2\u00a4\u00aa\5*\26\2\u00a5\u00aa\5\62\32")
        buf.write("\2\u00a6\u00aa\5\32\16\2\u00a7\u00a8\7\21\2\2\u00a8\u00aa")
        buf.write("\5\62\32\2\u00a9\u00a2\3\2\2\2\u00a9\u00a3\3\2\2\2\u00a9")
        buf.write("\u00a4\3\2\2\2\u00a9\u00a5\3\2\2\2\u00a9\u00a6\3\2\2\2")
        buf.write("\u00a9\u00a7\3\2\2\2\u00aa\25\3\2\2\2\u00ab\u00af\7\35")
        buf.write("\2\2\u00ac\u00ae\5\24\13\2\u00ad\u00ac\3\2\2\2\u00ae\u00b1")
        buf.write("\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0")
        buf.write("\u00b2\3\2\2\2\u00b1\u00af\3\2\2\2\u00b2\u00b6\7\36\2")
        buf.write("\2\u00b3\u00b6\5\24\13\2\u00b4\u00b6\3\2\2\2\u00b5\u00ab")
        buf.write("\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6")
        buf.write("\27\3\2\2\2\u00b7\u00ba\79\2\2\u00b8\u00ba\5:\36\2\u00b9")
        buf.write("\u00b7\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2")
        buf.write("\u00bb\u00bc\7)\2\2\u00bc\u00bd\5\62\32\2\u00bd\31\3\2")
        buf.write("\2\2\u00be\u00bf\7\32\2\2\u00bf\u00c3\5\34\17\2\u00c0")
        buf.write("\u00c2\5 \21\2\u00c1\u00c0\3\2\2\2\u00c2\u00c5\3\2\2\2")
        buf.write("\u00c3\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c7\3")
        buf.write("\2\2\2\u00c5\u00c3\3\2\2\2\u00c6\u00c8\5\36\20\2\u00c7")
        buf.write("\u00c6\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\33\3\2\2\2\u00c9")
        buf.write("\u00ca\7\61\2\2\u00ca\u00cb\5\62\32\2\u00cb\u00cc\7\62")
        buf.write("\2\2\u00cc\u00cd\5\26\f\2\u00cd\35\3\2\2\2\u00ce\u00cf")
        buf.write("\7\34\2\2\u00cf\u00d0\5\26\f\2\u00d0\37\3\2\2\2\u00d1")
        buf.write("\u00d2\7\33\2\2\u00d2\u00d3\5\34\17\2\u00d3!\3\2\2\2\u00d4")
        buf.write("\u00d5\7\25\2\2\u00d5\u00d6\t\4\2\2\u00d6\u00d7\7\26\2")
        buf.write("\2\u00d7\u00d8\5D#\2\u00d8\u00d9\7\27\2\2\u00d9\u00da")
        buf.write("\5\62\32\2\u00da\u00db\5$\23\2\u00db#\3\2\2\2\u00dc\u00e5")
        buf.write("\7\35\2\2\u00dd\u00df\5\24\13\2\u00de\u00dd\3\2\2\2\u00df")
        buf.write("\u00e0\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2")
        buf.write("\u00e1\u00e3\3\2\2\2\u00e2\u00e4\5&\24\2\u00e3\u00e2\3")
        buf.write("\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e6\3\2\2\2\u00e5\u00de")
        buf.write("\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7")
        buf.write("\u00ea\7\36\2\2\u00e8\u00ea\5\24\13\2\u00e9\u00dc\3\2")
        buf.write("\2\2\u00e9\u00e8\3\2\2\2\u00ea%\3\2\2\2\u00eb\u00ec\t")
        buf.write("\5\2\2\u00ec\'\3\2\2\2\u00ed\u00ee\7\65\2\2\u00ee\u00f3")
        buf.write("\7\n\2\2\u00ef\u00f0\7\67\2\2\u00f0\u00f2\7\n\2\2\u00f1")
        buf.write("\u00ef\3\2\2\2\u00f2\u00f5\3\2\2\2\u00f3\u00f1\3\2\2\2")
        buf.write("\u00f3\u00f4\3\2\2\2\u00f4\u00f6\3\2\2\2\u00f5\u00f3\3")
        buf.write("\2\2\2\u00f6\u00f7\7\66\2\2\u00f7)\3\2\2\2\u00f8\u00f9")
        buf.write("\79\2\2\u00f9\u00fb\7\61\2\2\u00fa\u00fc\5\62\32\2\u00fb")
        buf.write("\u00fa\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd\3\2\2\2")
        buf.write("\u00fd\u00fe\7\62\2\2\u00fe+\3\2\2\2\u00ff\u0104\5\62")
        buf.write("\32\2\u0100\u0101\7\67\2\2\u0101\u0103\5\62\32\2\u0102")
        buf.write("\u0100\3\2\2\2\u0103\u0106\3\2\2\2\u0104\u0102\3\2\2\2")
        buf.write("\u0104\u0105\3\2\2\2\u0105-\3\2\2\2\u0106\u0104\3\2\2")
        buf.write("\2\u0107\u010c\5\60\31\2\u0108\u0109\7\67\2\2\u0109\u010b")
        buf.write("\5\60\31\2\u010a\u0108\3\2\2\2\u010b\u010e\3\2\2\2\u010c")
        buf.write("\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u0111\3\2\2\2")
        buf.write("\u010e\u010c\3\2\2\2\u010f\u0111\3\2\2\2\u0110\u0107\3")
        buf.write("\2\2\2\u0110\u010f\3\2\2\2\u0111/\3\2\2\2\u0112\u0113")
        buf.write("\7\4\2\2\u0113\u0114\79\2\2\u0114\61\3\2\2\2\u0115\u0116")
        buf.write("\b\32\1\2\u0116\u0117\5\64\33\2\u0117\u011d\3\2\2\2\u0118")
        buf.write("\u0119\f\4\2\2\u0119\u011a\7\6\2\2\u011a\u011c\5\64\33")
        buf.write("\2\u011b\u0118\3\2\2\2\u011c\u011f\3\2\2\2\u011d\u011b")
        buf.write("\3\2\2\2\u011d\u011e\3\2\2\2\u011e\63\3\2\2\2\u011f\u011d")
        buf.write("\3\2\2\2\u0120\u0126\5@!\2\u0121\u0126\5D#\2\u0122\u0126")
        buf.write("\5H%\2\u0123\u0126\58\35\2\u0124\u0126\7\t\2\2\u0125\u0120")
        buf.write("\3\2\2\2\u0125\u0121\3\2\2\2\u0125\u0122\3\2\2\2\u0125")
        buf.write("\u0123\3\2\2\2\u0125\u0124\3\2\2\2\u0126\65\3\2\2\2\u0127")
        buf.write("\u0128\t\6\2\2\u0128\67\3\2\2\2\u0129\u012d\79\2\2\u012a")
        buf.write("\u012d\5:\36\2\u012b\u012d\5*\26\2\u012c\u0129\3\2\2\2")
        buf.write("\u012c\u012a\3\2\2\2\u012c\u012b\3\2\2\2\u012d9\3\2\2")
        buf.write("\2\u012e\u012f\79\2\2\u012f\u0130\7\65\2\2\u0130\u0131")
        buf.write("\5<\37\2\u0131\u0132\7\66\2\2\u0132;\3\2\2\2\u0133\u0134")
        buf.write("\b\37\1\2\u0134\u0135\5> \2\u0135\u013b\3\2\2\2\u0136")
        buf.write("\u0137\f\4\2\2\u0137\u0138\7\6\2\2\u0138\u013a\5> \2\u0139")
        buf.write("\u0136\3\2\2\2\u013a\u013d\3\2\2\2\u013b\u0139\3\2\2\2")
        buf.write("\u013b\u013c\3\2\2\2\u013c=\3\2\2\2\u013d\u013b\3\2\2")
        buf.write("\2\u013e\u0142\7\n\2\2\u013f\u0142\5@!\2\u0140\u0142\5")
        buf.write("8\35\2\u0141\u013e\3\2\2\2\u0141\u013f\3\2\2\2\u0141\u0140")
        buf.write("\3\2\2\2\u0142?\3\2\2\2\u0143\u0144\5B\"\2\u0144\u0145")
        buf.write("\7\6\2\2\u0145\u0146\5@!\2\u0146\u014b\3\2\2\2\u0147\u0148")
        buf.write("\7!\2\2\u0148\u014b\5@!\2\u0149\u014b\5B\"\2\u014a\u0143")
        buf.write("\3\2\2\2\u014a\u0147\3\2\2\2\u014a\u0149\3\2\2\2\u014b")
        buf.write("A\3\2\2\2\u014c\u014f\7\n\2\2\u014d\u014f\58\35\2\u014e")
        buf.write("\u014c\3\2\2\2\u014e\u014d\3\2\2\2\u014fC\3\2\2\2\u0150")
        buf.write("\u0151\b#\1\2\u0151\u0155\5F$\2\u0152\u0153\7%\2\2\u0153")
        buf.write("\u0155\5D#\3\u0154\u0150\3\2\2\2\u0154\u0152\3\2\2\2\u0155")
        buf.write("\u015b\3\2\2\2\u0156\u0157\f\5\2\2\u0157\u0158\7\7\2\2")
        buf.write("\u0158\u015a\5F$\2\u0159\u0156\3\2\2\2\u015a\u015d\3\2")
        buf.write("\2\2\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015cE\3")
        buf.write("\2\2\2\u015d\u015b\3\2\2\2\u015e\u0162\7\13\2\2\u015f")
        buf.write("\u0162\5H%\2\u0160\u0162\58\35\2\u0161\u015e\3\2\2\2\u0161")
        buf.write("\u015f\3\2\2\2\u0161\u0160\3\2\2\2\u0162G\3\2\2\2\u0163")
        buf.write("\u0164\5J&\2\u0164\u0165\7\b\2\2\u0165\u0166\5J&\2\u0166")
        buf.write("\u016c\3\2\2\2\u0167\u0168\5L\'\2\u0168\u0169\7\60\2\2")
        buf.write("\u0169\u016a\5L\'\2\u016a\u016c\3\2\2\2\u016b\u0163\3")
        buf.write("\2\2\2\u016b\u0167\3\2\2\2\u016cI\3\2\2\2\u016d\u0170")
        buf.write("\7\n\2\2\u016e\u0170\58\35\2\u016f\u016d\3\2\2\2\u016f")
        buf.write("\u016e\3\2\2\2\u0170K\3\2\2\2\u0171\u0174\7\t\2\2\u0172")
        buf.write("\u0174\58\35\2\u0173\u0171\3\2\2\2\u0173\u0172\3\2\2\2")
        buf.write("\u0174M\3\2\2\2)QXbjow|\u0081\u0085\u0098\u009e\u00a9")
        buf.write("\u00af\u00b5\u00b9\u00c3\u00c7\u00e0\u00e3\u00e5\u00e9")
        buf.write("\u00f3\u00fb\u0104\u010c\u0110\u011d\u0125\u012c\u013b")
        buf.write("\u0141\u014a\u014e\u0154\u015b\u0161\u016b\u016f\u0173")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\r'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'elif'", "'else'", "'begin'", "'end'", "'main'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'not'", "'and'", 
                     "'or'", "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'...'", "'=='", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "TYPE", "IMPLIKEYS", "NUMOP", 
                      "LOGICOPBIN", "NUMRELAOPS", "STRINGLIT", "NUMLIT", 
                      "BOOLIT", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELIF", "ELSE", "BEGIN", 
                      "END", "MAIN", "PLUS", "MINUS", "STAR", "SLASH", "PERCENT", 
                      "NOT", "AND", "OR", "EQUAL", "ASSIGN", "INEQUAL", 
                      "LESSTHAN", "LESSEQUAL", "MORETHAN", "MOREEQUAL", 
                      "ELLIPSIS", "EQUALITY", "LB", "RB", "LC", "RC", "LS", 
                      "RS", "COMMA", "COMMENT", "ID", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ES" ]

    RULE_program = 0
    RULE_main = 1
    RULE_other = 2
    RULE_mainblock = 3
    RULE_valdecl = 4
    RULE_mainfunc = 5
    RULE_funcdecl = 6
    RULE_funcblock = 7
    RULE_stmts = 8
    RULE_stmt = 9
    RULE_stmtblock = 10
    RULE_assignstmt = 11
    RULE_ifstmt = 12
    RULE_ifblock = 13
    RULE_elseblk = 14
    RULE_elifblk = 15
    RULE_forstmt = 16
    RULE_loopblock = 17
    RULE_loopkey = 18
    RULE_array = 19
    RULE_funcall = 20
    RULE_paramcall = 21
    RULE_paramlist = 22
    RULE_params = 23
    RULE_exp = 24
    RULE_exp_01 = 25
    RULE_exp_00 = 26
    RULE_expall = 27
    RULE_indexp = 28
    RULE_indop = 29
    RULE_indop_1 = 30
    RULE_ariexp = 31
    RULE_ariexp_00 = 32
    RULE_logicexp = 33
    RULE_logicexp_00 = 34
    RULE_relatexp = 35
    RULE_relatexp_00 = 36
    RULE_relatexp_01 = 37

    ruleNames =  [ "program", "main", "other", "mainblock", "valdecl", "mainfunc", 
                   "funcdecl", "funcblock", "stmts", "stmt", "stmtblock", 
                   "assignstmt", "ifstmt", "ifblock", "elseblk", "elifblk", 
                   "forstmt", "loopblock", "loopkey", "array", "funcall", 
                   "paramcall", "paramlist", "params", "exp", "exp_01", 
                   "exp_00", "expall", "indexp", "indop", "indop_1", "ariexp", 
                   "ariexp_00", "logicexp", "logicexp_00", "relatexp", "relatexp_00", 
                   "relatexp_01" ]

    EOF = Token.EOF
    T__0=1
    TYPE=2
    IMPLIKEYS=3
    NUMOP=4
    LOGICOPBIN=5
    NUMRELAOPS=6
    STRINGLIT=7
    NUMLIT=8
    BOOLIT=9
    TRUE=10
    FALSE=11
    NUMBER=12
    BOOL=13
    STRING=14
    RETURN=15
    VAR=16
    DYNAMIC=17
    FUNC=18
    FOR=19
    UNTIL=20
    BY=21
    BREAK=22
    CONTINUE=23
    IF=24
    ELIF=25
    ELSE=26
    BEGIN=27
    END=28
    MAIN=29
    PLUS=30
    MINUS=31
    STAR=32
    SLASH=33
    PERCENT=34
    NOT=35
    AND=36
    OR=37
    EQUAL=38
    ASSIGN=39
    INEQUAL=40
    LESSTHAN=41
    LESSEQUAL=42
    MORETHAN=43
    MOREEQUAL=44
    ELLIPSIS=45
    EQUALITY=46
    LB=47
    RB=48
    LC=49
    RC=50
    LS=51
    RS=52
    COMMA=53
    COMMENT=54
    ID=55
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
            self.state = 79
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 76
                    self.other() 
                self.state = 81
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 82
            self.mainfunc()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TYPE) | (1 << ZCodeParser.IMPLIKEYS) | (1 << ZCodeParser.STRINGLIT) | (1 << ZCodeParser.NUMLIT) | (1 << ZCodeParser.BOOLIT) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FUNC) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ID))) != 0):
                self.state = 83
                self.other()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mainfunc(self):
            return self.getTypedRuleContext(ZCodeParser.MainfuncContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_main

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain" ):
                return visitor.visitMain(self)
            else:
                return visitor.visitChildren(self)




    def main(self):

        localctx = ZCodeParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.mainfunc()
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
        self.enterRule(localctx, 4, self.RULE_other)
        try:
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.funcdecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.valdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainblockContext(ParserRuleContext):
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


        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_mainblock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMainblock" ):
                return visitor.visitMainblock(self)
            else:
                return visitor.visitChildren(self)




    def mainblock(self):

        localctx = ZCodeParser.MainblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_mainblock)
        self._la = 0 # Token type
        try:
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.match(ZCodeParser.T__0)
                self.state = 99
                self.match(ZCodeParser.BEGIN)
                self.state = 100
                self.match(ZCodeParser.T__0)
                self.state = 104
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 101
                        self.stmt() 
                    self.state = 106
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.RETURN:
                    self.state = 107
                    self.match(ZCodeParser.RETURN)
                    self.state = 108
                    self.exp(0)


                self.state = 111
                self.match(ZCodeParser.T__0)
                self.state = 112
                self.match(ZCodeParser.END)
                self.state = 113
                self.match(ZCodeParser.T__0)
                pass
            elif token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.match(ZCodeParser.RETURN)
                self.state = 115
                self.exp(0)
                pass
            elif token in [ZCodeParser.EOF]:
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

        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


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
        self.enterRule(localctx, 8, self.RULE_valdecl)
        self._la = 0 # Token type
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.TYPE or _la==ZCodeParser.DYNAMIC):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 120
                self.match(ZCodeParser.ID)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.LS:
                    self.state = 121
                    self.array()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.TYPE or _la==ZCodeParser.IMPLIKEYS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 125
                self.match(ZCodeParser.ID)
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.LS:
                    self.state = 126
                    self.array()


                self.state = 129
                self.match(ZCodeParser.ASSIGN)
                self.state = 130
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
        self.enterRule(localctx, 10, self.RULE_mainfunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(ZCodeParser.FUNC)
            self.state = 134
            self.match(ZCodeParser.MAIN)
            self.state = 135
            self.match(ZCodeParser.LB)
            self.state = 136
            self.match(ZCodeParser.RB)
            self.state = 137
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
        self.enterRule(localctx, 12, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(ZCodeParser.FUNC)
            self.state = 140
            self.match(ZCodeParser.ID)
            self.state = 141
            self.match(ZCodeParser.LB)
            self.state = 142
            self.paramlist()
            self.state = 143
            self.match(ZCodeParser.RB)
            self.state = 144
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

        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StmtContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StmtContext,i)


        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcblock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncblock" ):
                return visitor.visitFuncblock(self)
            else:
                return visitor.visitChildren(self)




    def funcblock(self):

        localctx = ZCodeParser.FuncblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcblock)
        self._la = 0 # Token type
        try:
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(ZCodeParser.BEGIN)
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TYPE) | (1 << ZCodeParser.IMPLIKEYS) | (1 << ZCodeParser.STRINGLIT) | (1 << ZCodeParser.NUMLIT) | (1 << ZCodeParser.BOOLIT) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ID))) != 0):
                    self.state = 147
                    self.stmt()
                    self.state = 152
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 153
                self.match(ZCodeParser.END)
                pass
            elif token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.match(ZCodeParser.RETURN)
                self.state = 155
                self.exp(0)
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
        self.enterRule(localctx, 16, self.RULE_stmts)
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

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_stmt)
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.valdecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.assignstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 162
                self.funcall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 163
                self.exp(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 164
                self.ifstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 165
                self.match(ZCodeParser.RETURN)
                self.state = 166
                self.exp(0)
                pass


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

        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StmtContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StmtContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtblock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtblock" ):
                return visitor.visitStmtblock(self)
            else:
                return visitor.visitChildren(self)




    def stmtblock(self):

        localctx = ZCodeParser.StmtblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_stmtblock)
        self._la = 0 # Token type
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.match(ZCodeParser.BEGIN)
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TYPE) | (1 << ZCodeParser.IMPLIKEYS) | (1 << ZCodeParser.STRINGLIT) | (1 << ZCodeParser.NUMLIT) | (1 << ZCodeParser.BOOLIT) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ID))) != 0):
                    self.state = 170
                    self.stmt()
                    self.state = 175
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 176
                self.match(ZCodeParser.END)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
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
        self.enterRule(localctx, 22, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 181
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 182
                self.indexp()
                pass


            self.state = 185
            self.match(ZCodeParser.ASSIGN)
            self.state = 186
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


        def elifblk(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ElifblkContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ElifblkContext,i)


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
        self.enterRule(localctx, 24, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(ZCodeParser.IF)
            self.state = 189
            self.ifblock()
            self.state = 193
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 190
                    self.elifblk() 
                self.state = 195
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 196
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
        self.enterRule(localctx, 26, self.RULE_ifblock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(ZCodeParser.LB)
            self.state = 200
            self.exp(0)
            self.state = 201
            self.match(ZCodeParser.RB)
            self.state = 202
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
        self.enterRule(localctx, 28, self.RULE_elseblk)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(ZCodeParser.ELSE)
            self.state = 205
            self.stmtblock()
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

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def ifblock(self):
            return self.getTypedRuleContext(ZCodeParser.IfblockContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifblk

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifblk" ):
                return visitor.visitElifblk(self)
            else:
                return visitor.visitChildren(self)




    def elifblk(self):

        localctx = ZCodeParser.ElifblkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_elifblk)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(ZCodeParser.ELIF)
            self.state = 208
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
            self.state = 210
            self.match(ZCodeParser.FOR)
            self.state = 211
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.NUMLIT or _la==ZCodeParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 212
            self.match(ZCodeParser.UNTIL)
            self.state = 213
            self.logicexp(0)
            self.state = 214
            self.match(ZCodeParser.BY)
            self.state = 215
            self.exp(0)
            self.state = 216
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
            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.match(ZCodeParser.BEGIN)
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TYPE) | (1 << ZCodeParser.IMPLIKEYS) | (1 << ZCodeParser.STRINGLIT) | (1 << ZCodeParser.NUMLIT) | (1 << ZCodeParser.BOOLIT) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ID))) != 0):
                    self.state = 220 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 219
                        self.stmt()
                        self.state = 222 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TYPE) | (1 << ZCodeParser.IMPLIKEYS) | (1 << ZCodeParser.STRINGLIT) | (1 << ZCodeParser.NUMLIT) | (1 << ZCodeParser.BOOLIT) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ID))) != 0)):
                            break

                    self.state = 225
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==ZCodeParser.BREAK or _la==ZCodeParser.CONTINUE:
                        self.state = 224
                        self.loopkey()




                self.state = 229
                self.match(ZCodeParser.END)
                pass
            elif token in [ZCodeParser.TYPE, ZCodeParser.IMPLIKEYS, ZCodeParser.STRINGLIT, ZCodeParser.NUMLIT, ZCodeParser.BOOLIT, ZCodeParser.RETURN, ZCodeParser.DYNAMIC, ZCodeParser.IF, ZCodeParser.MINUS, ZCodeParser.NOT, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
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
            self.state = 233
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


    class ArrayContext(ParserRuleContext):
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
            return ZCodeParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = ZCodeParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(ZCodeParser.LS)
            self.state = 236
            self.match(ZCodeParser.NUMLIT)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.COMMA:
                self.state = 237
                self.match(ZCodeParser.COMMA)
                self.state = 238
                self.match(ZCodeParser.NUMLIT)
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 244
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
            self.state = 246
            self.match(ZCodeParser.ID)
            self.state = 247
            self.match(ZCodeParser.LB)
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.STRINGLIT) | (1 << ZCodeParser.NUMLIT) | (1 << ZCodeParser.BOOLIT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ID))) != 0):
                self.state = 248
                self.exp(0)


            self.state = 251
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
            self.state = 253
            self.exp(0)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.COMMA:
                self.state = 254
                self.match(ZCodeParser.COMMA)

                self.state = 255
                self.exp(0)
                self.state = 260
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
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.params()
                self.state = 266
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.COMMA:
                    self.state = 262
                    self.match(ZCodeParser.COMMA)
                    self.state = 263
                    self.params()
                    self.state = 268
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
            self.state = 272
            self.match(ZCodeParser.TYPE)
            self.state = 273
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
            self.state = 276
            self.exp_01()
            self._ctx.stop = self._input.LT(-1)
            self.state = 283
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.ExpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                    self.state = 278
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 279
                    self.match(ZCodeParser.NUMOP)
                    self.state = 280
                    self.exp_01() 
                self.state = 285
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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


        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

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
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.ariexp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.logicexp(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 288
                self.relatexp()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 289
                self.expall()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 290
                self.match(ZCodeParser.STRINGLIT)
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
            self.state = 293
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
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.indexp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 297
                self.funcall()
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
        self.enterRule(localctx, 56, self.RULE_indexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(ZCodeParser.ID)
            self.state = 301
            self.match(ZCodeParser.LS)
            self.state = 302
            self.indop(0)
            self.state = 303
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

        def indop_1(self):
            return self.getTypedRuleContext(ZCodeParser.Indop_1Context,0)


        def indop(self):
            return self.getTypedRuleContext(ZCodeParser.IndopContext,0)


        def NUMOP(self):
            return self.getToken(ZCodeParser.NUMOP, 0)

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
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_indop, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.indop_1()
            self._ctx.stop = self._input.LT(-1)
            self.state = 313
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.IndopContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_indop)
                    self.state = 308
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 309
                    self.match(ZCodeParser.NUMOP)
                    self.state = 310
                    self.indop_1() 
                self.state = 315
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        self.enterRule(localctx, 60, self.RULE_indop_1)
        try:
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.match(ZCodeParser.NUMLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.ariexp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 318
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
        self.enterRule(localctx, 62, self.RULE_ariexp)
        try:
            self.state = 328
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.ariexp_00()
                self.state = 322
                self.match(ZCodeParser.NUMOP)
                self.state = 323
                self.ariexp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.match(ZCodeParser.MINUS)
                self.state = 326
                self.ariexp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 327
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
        self.enterRule(localctx, 64, self.RULE_ariexp_00)
        try:
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.match(ZCodeParser.NUMLIT)
                pass
            elif token in [ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
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
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_logicexp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.STRINGLIT, ZCodeParser.NUMLIT, ZCodeParser.BOOLIT, ZCodeParser.ID]:
                self.state = 335
                self.logicexp_00()
                pass
            elif token in [ZCodeParser.NOT]:
                self.state = 336
                self.match(ZCodeParser.NOT)
                self.state = 337
                self.logicexp(1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 345
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.LogicexpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicexp)
                    self.state = 340
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 341
                    self.match(ZCodeParser.LOGICOPBIN)
                    self.state = 342
                    self.logicexp_00() 
                self.state = 347
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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
        self.enterRule(localctx, 68, self.RULE_logicexp_00)
        try:
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.match(ZCodeParser.BOOLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.relatexp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 350
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
        self.enterRule(localctx, 70, self.RULE_relatexp)
        try:
            self.state = 361
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.relatexp_00()
                self.state = 354
                self.match(ZCodeParser.NUMRELAOPS)
                self.state = 355
                self.relatexp_00()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.relatexp_01()
                self.state = 358
                self.match(ZCodeParser.EQUALITY)
                self.state = 359
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
        self.enterRule(localctx, 72, self.RULE_relatexp_00)
        try:
            self.state = 365
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.match(ZCodeParser.NUMLIT)
                pass
            elif token in [ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
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
        self.enterRule(localctx, 74, self.RULE_relatexp_01)
        try:
            self.state = 369
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.match(ZCodeParser.STRINGLIT)
                pass
            elif token in [ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
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
        self._predicates[29] = self.indop_sempred
        self._predicates[33] = self.logicexp_sempred
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
         

    def logicexp_sempred(self, localctx:LogicexpContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




