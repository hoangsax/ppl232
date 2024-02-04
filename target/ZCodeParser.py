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
        buf.write("\u01f6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\3\2\3\2\6\2c\n\2\r\2\16\2d\7\2g\n\2\f\2")
        buf.write("\16\2j\13\2\3\2\7\2m\n\2\f\2\16\2p\13\2\3\2\3\2\7\2t\n")
        buf.write("\2\f\2\16\2w\13\2\3\2\3\2\3\3\3\3\5\3}\n\3\3\4\3\4\3\4")
        buf.write("\5\4\u0082\n\4\3\4\3\4\3\4\5\4\u0087\n\4\3\4\3\4\5\4\u008b")
        buf.write("\n\4\3\5\3\5\3\5\3\5\3\5\7\5\u0092\n\5\f\5\16\5\u0095")
        buf.write("\13\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b")
        buf.write("\7\b\u00a3\n\b\f\b\16\b\u00a6\13\b\3\b\3\b\6\b\u00aa\n")
        buf.write("\b\r\b\16\b\u00ab\3\b\3\b\3\b\6\b\u00b1\n\b\r\b\16\b\u00b2")
        buf.write("\3\b\5\b\u00b6\n\b\3\t\3\t\3\t\6\t\u00bb\n\t\r\t\16\t")
        buf.write("\u00bc\3\n\3\n\5\n\u00c1\n\n\3\13\3\13\3\13\3\13\5\13")
        buf.write("\u00c7\n\13\3\13\6\13\u00ca\n\13\r\13\16\13\u00cb\3\13")
        buf.write("\3\13\5\13\u00d0\n\13\3\f\3\f\3\f\3\f\3\f\5\f\u00d7\n")
        buf.write("\f\3\r\3\r\5\r\u00db\n\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\5\20")
        buf.write("\u00ed\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u00f4\n\21\3")
        buf.write("\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\6\23")
        buf.write("\u0100\n\23\r\23\16\23\u0101\3\23\3\23\3\24\7\24\u0107")
        buf.write("\n\24\f\24\16\24\u010a\13\24\3\24\3\24\6\24\u010e\n\24")
        buf.write("\r\24\16\24\u010f\3\24\3\24\3\24\6\24\u0115\n\24\r\24")
        buf.write("\16\24\u0116\5\24\u0119\n\24\3\24\3\24\6\24\u011d\n\24")
        buf.write("\r\24\16\24\u011e\3\24\3\24\3\24\6\24\u0124\n\24\r\24")
        buf.write("\16\24\u0125\5\24\u0128\n\24\3\25\3\25\3\26\3\26\3\26")
        buf.write("\5\26\u012f\n\26\3\26\3\26\3\27\3\27\3\27\7\27\u0136\n")
        buf.write("\27\f\27\16\27\u0139\13\27\3\30\3\30\3\30\7\30\u013e\n")
        buf.write("\30\f\30\16\30\u0141\13\30\3\30\5\30\u0144\n\30\3\31\3")
        buf.write("\31\3\31\3\32\3\32\3\32\3\32\5\32\u014d\n\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\5\33\u0155\n\33\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\5\34\u015e\n\34\3\35\3\35\3\36\3\36")
        buf.write("\3\36\5\36\u0165\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\5\37\u0171\n\37\3 \3 \3 \5 \u0176\n")
        buf.write(" \3!\3!\3!\3!\3!\5!\u017d\n!\3\"\3\"\3\"\3\"\3\"\5\"\u0184")
        buf.write("\n\"\3#\3#\3#\3#\3#\5#\u018b\n#\3$\3$\3$\3$\3$\3%\3%\3")
        buf.write("%\3%\3%\3%\7%\u0198\n%\f%\16%\u019b\13%\3&\3&\3&\3&\3")
        buf.write("&\3&\7&\u01a3\n&\f&\16&\u01a6\13&\3\'\3\'\3\'\5\'\u01ab")
        buf.write("\n\'\3(\3(\3(\3(\3(\3(\3(\5(\u01b4\n(\3)\3)\3)\3)\3)\3")
        buf.write(")\5)\u01bc\n)\3*\3*\3*\3*\3*\5*\u01c3\n*\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\5+\u01cd\n+\3,\3,\5,\u01d1\n,\3-\3-\3-\3-\5")
        buf.write("-\u01d7\n-\3-\3-\3-\7-\u01dc\n-\f-\16-\u01df\13-\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\5.\u01e9\n.\3/\3/\3/\3/\3/\5/\u01f0")
        buf.write("\n/\3\60\3\60\5\60\u01f4\n\60\3\60\2\5HJX\61\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJLNPRTVXZ\\^\2\6\4\2\3\3\22\22\3\2\3\4\3\2\27\30")
        buf.write("\3\2\b\n\2\u0214\2h\3\2\2\2\4|\3\2\2\2\6\u008a\3\2\2\2")
        buf.write("\b\u008c\3\2\2\2\n\u0098\3\2\2\2\f\u009b\3\2\2\2\16\u00b5")
        buf.write("\3\2\2\2\20\u00b7\3\2\2\2\22\u00c0\3\2\2\2\24\u00cf\3")
        buf.write("\2\2\2\26\u00d6\3\2\2\2\30\u00da\3\2\2\2\32\u00df\3\2")
        buf.write("\2\2\34\u00e4\3\2\2\2\36\u00ec\3\2\2\2 \u00f3\3\2\2\2")
        buf.write("\"\u00f5\3\2\2\2$\u00f8\3\2\2\2&\u0127\3\2\2\2(\u0129")
        buf.write("\3\2\2\2*\u012b\3\2\2\2,\u0132\3\2\2\2.\u0143\3\2\2\2")
        buf.write("\60\u0145\3\2\2\2\62\u014c\3\2\2\2\64\u0154\3\2\2\2\66")
        buf.write("\u015d\3\2\2\28\u015f\3\2\2\2:\u0164\3\2\2\2<\u0170\3")
        buf.write("\2\2\2>\u0175\3\2\2\2@\u017c\3\2\2\2B\u0183\3\2\2\2D\u018a")
        buf.write("\3\2\2\2F\u018c\3\2\2\2H\u0191\3\2\2\2J\u019c\3\2\2\2")
        buf.write("L\u01aa\3\2\2\2N\u01b3\3\2\2\2P\u01bb\3\2\2\2R\u01c2\3")
        buf.write("\2\2\2T\u01cc\3\2\2\2V\u01d0\3\2\2\2X\u01d6\3\2\2\2Z\u01e8")
        buf.write("\3\2\2\2\\\u01ef\3\2\2\2^\u01f3\3\2\2\2`b\5\f\7\2ac\7")
        buf.write("9\2\2ba\3\2\2\2cd\3\2\2\2db\3\2\2\2de\3\2\2\2eg\3\2\2")
        buf.write("\2f`\3\2\2\2gj\3\2\2\2hf\3\2\2\2hi\3\2\2\2in\3\2\2\2j")
        buf.write("h\3\2\2\2km\5\4\3\2lk\3\2\2\2mp\3\2\2\2nl\3\2\2\2no\3")
        buf.write("\2\2\2oq\3\2\2\2pn\3\2\2\2qu\5\b\5\2rt\5\4\3\2sr\3\2\2")
        buf.write("\2tw\3\2\2\2us\3\2\2\2uv\3\2\2\2vx\3\2\2\2wu\3\2\2\2x")
        buf.write("y\7\2\2\3y\3\3\2\2\2z}\5\n\6\2{}\5\24\13\2|z\3\2\2\2|")
        buf.write("{\3\2\2\2}\5\3\2\2\2~\177\t\2\2\2\177\u0081\78\2\2\u0080")
        buf.write("\u0082\5<\37\2\u0081\u0080\3\2\2\2\u0081\u0082\3\2\2\2")
        buf.write("\u0082\u008b\3\2\2\2\u0083\u0084\t\3\2\2\u0084\u0086\7")
        buf.write("8\2\2\u0085\u0087\5<\37\2\u0086\u0085\3\2\2\2\u0086\u0087")
        buf.write("\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089\7(\2\2\u0089")
        buf.write("\u008b\5\62\32\2\u008a~\3\2\2\2\u008a\u0083\3\2\2\2\u008b")
        buf.write("\7\3\2\2\2\u008c\u008d\7\23\2\2\u008d\u008e\7\36\2\2\u008e")
        buf.write("\u008f\7\60\2\2\u008f\u0093\7\61\2\2\u0090\u0092\79\2")
        buf.write("\2\u0091\u0090\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0091")
        buf.write("\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0096\3\2\2\2\u0095")
        buf.write("\u0093\3\2\2\2\u0096\u0097\5\16\b\2\u0097\t\3\2\2\2\u0098")
        buf.write("\u0099\5\f\7\2\u0099\u009a\5\16\b\2\u009a\13\3\2\2\2\u009b")
        buf.write("\u009c\7\23\2\2\u009c\u009d\78\2\2\u009d\u009e\7\60\2")
        buf.write("\2\u009e\u009f\5.\30\2\u009f\u00a0\7\61\2\2\u00a0\r\3")
        buf.write("\2\2\2\u00a1\u00a3\79\2\2\u00a2\u00a1\3\2\2\2\u00a3\u00a6")
        buf.write("\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5")
        buf.write("\u00a7\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a7\u00a9\7\34\2")
        buf.write("\2\u00a8\u00aa\79\2\2\u00a9\u00a8\3\2\2\2\u00aa\u00ab")
        buf.write("\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac")
        buf.write("\u00ad\3\2\2\2\u00ad\u00ae\5\26\f\2\u00ae\u00b0\7\35\2")
        buf.write("\2\u00af\u00b1\79\2\2\u00b0\u00af\3\2\2\2\u00b1\u00b2")
        buf.write("\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3")
        buf.write("\u00b6\3\2\2\2\u00b4\u00b6\5\20\t\2\u00b5\u00a4\3\2\2")
        buf.write("\2\u00b5\u00b4\3\2\2\2\u00b6\17\3\2\2\2\u00b7\u00b8\7")
        buf.write("\20\2\2\u00b8\u00ba\5\62\32\2\u00b9\u00bb\79\2\2\u00ba")
        buf.write("\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00ba\3\2\2\2")
        buf.write("\u00bc\u00bd\3\2\2\2\u00bd\21\3\2\2\2\u00be\u00c1\5\24")
        buf.write("\13\2\u00bf\u00c1\5\20\t\2\u00c0\u00be\3\2\2\2\u00c0\u00bf")
        buf.write("\3\2\2\2\u00c1\23\3\2\2\2\u00c2\u00c7\5\6\4\2\u00c3\u00c7")
        buf.write("\5\30\r\2\u00c4\u00c7\5*\26\2\u00c5\u00c7\5\64\33\2\u00c6")
        buf.write("\u00c2\3\2\2\2\u00c6\u00c3\3\2\2\2\u00c6\u00c4\3\2\2\2")
        buf.write("\u00c6\u00c5\3\2\2\2\u00c7\u00c9\3\2\2\2\u00c8\u00ca\7")
        buf.write("9\2\2\u00c9\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00c9")
        buf.write("\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00d0\3\2\2\2\u00cd")
        buf.write("\u00d0\5\32\16\2\u00ce\u00d0\5$\23\2\u00cf\u00c6\3\2\2")
        buf.write("\2\u00cf\u00cd\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0\25\3")
        buf.write("\2\2\2\u00d1\u00d2\5\22\n\2\u00d2\u00d3\5\26\f\2\u00d3")
        buf.write("\u00d7\3\2\2\2\u00d4\u00d7\5\22\n\2\u00d5\u00d7\3\2\2")
        buf.write("\2\u00d6\u00d1\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d5")
        buf.write("\3\2\2\2\u00d7\27\3\2\2\2\u00d8\u00db\78\2\2\u00d9\u00db")
        buf.write("\5F$\2\u00da\u00d8\3\2\2\2\u00da\u00d9\3\2\2\2\u00db\u00dc")
        buf.write("\3\2\2\2\u00dc\u00dd\7(\2\2\u00dd\u00de\5\62\32\2\u00de")
        buf.write("\31\3\2\2\2\u00df\u00e0\7\31\2\2\u00e0\u00e1\5\34\17\2")
        buf.write("\u00e1\u00e2\5 \21\2\u00e2\u00e3\5\36\20\2\u00e3\33\3")
        buf.write("\2\2\2\u00e4\u00e5\7\60\2\2\u00e5\u00e6\5\62\32\2\u00e6")
        buf.write("\u00e7\7\61\2\2\u00e7\u00e8\5&\24\2\u00e8\35\3\2\2\2\u00e9")
        buf.write("\u00ea\7\33\2\2\u00ea\u00ed\5\16\b\2\u00eb\u00ed\3\2\2")
        buf.write("\2\u00ec\u00e9\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed\37\3")
        buf.write("\2\2\2\u00ee\u00ef\5\"\22\2\u00ef\u00f0\5 \21\2\u00f0")
        buf.write("\u00f4\3\2\2\2\u00f1\u00f4\5\"\22\2\u00f2\u00f4\3\2\2")
        buf.write("\2\u00f3\u00ee\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f2")
        buf.write("\3\2\2\2\u00f4!\3\2\2\2\u00f5\u00f6\7\32\2\2\u00f6\u00f7")
        buf.write("\5\34\17\2\u00f7#\3\2\2\2\u00f8\u00f9\7\24\2\2\u00f9\u00fa")
        buf.write("\78\2\2\u00fa\u00fb\7\25\2\2\u00fb\u00fc\5X-\2\u00fc\u00fd")
        buf.write("\7\26\2\2\u00fd\u00ff\7\t\2\2\u00fe\u0100\79\2\2\u00ff")
        buf.write("\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u00ff\3\2\2\2")
        buf.write("\u0101\u0102\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0104\5")
        buf.write("&\24\2\u0104%\3\2\2\2\u0105\u0107\79\2\2\u0106\u0105\3")
        buf.write("\2\2\2\u0107\u010a\3\2\2\2\u0108\u0106\3\2\2\2\u0108\u0109")
        buf.write("\3\2\2\2\u0109\u010b\3\2\2\2\u010a\u0108\3\2\2\2\u010b")
        buf.write("\u010d\7\34\2\2\u010c\u010e\79\2\2\u010d\u010c\3\2\2\2")
        buf.write("\u010e\u010f\3\2\2\2\u010f\u010d\3\2\2\2\u010f\u0110\3")
        buf.write("\2\2\2\u0110\u0111\3\2\2\2\u0111\u0118\5\26\f\2\u0112")
        buf.write("\u0114\5(\25\2\u0113\u0115\79\2\2\u0114\u0113\3\2\2\2")
        buf.write("\u0115\u0116\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3")
        buf.write("\2\2\2\u0117\u0119\3\2\2\2\u0118\u0112\3\2\2\2\u0118\u0119")
        buf.write("\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u011c\7\35\2\2\u011b")
        buf.write("\u011d\79\2\2\u011c\u011b\3\2\2\2\u011d\u011e\3\2\2\2")
        buf.write("\u011e\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0128\3")
        buf.write("\2\2\2\u0120\u0128\5\22\n\2\u0121\u0123\5(\25\2\u0122")
        buf.write("\u0124\79\2\2\u0123\u0122\3\2\2\2\u0124\u0125\3\2\2\2")
        buf.write("\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0128\3")
        buf.write("\2\2\2\u0127\u0108\3\2\2\2\u0127\u0120\3\2\2\2\u0127\u0121")
        buf.write("\3\2\2\2\u0128\'\3\2\2\2\u0129\u012a\t\4\2\2\u012a)\3")
        buf.write("\2\2\2\u012b\u012c\78\2\2\u012c\u012e\7\60\2\2\u012d\u012f")
        buf.write("\5> \2\u012e\u012d\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0130")
        buf.write("\3\2\2\2\u0130\u0131\7\61\2\2\u0131+\3\2\2\2\u0132\u0137")
        buf.write("\5\64\33\2\u0133\u0134\7\66\2\2\u0134\u0136\5\64\33\2")
        buf.write("\u0135\u0133\3\2\2\2\u0136\u0139\3\2\2\2\u0137\u0135\3")
        buf.write("\2\2\2\u0137\u0138\3\2\2\2\u0138-\3\2\2\2\u0139\u0137")
        buf.write("\3\2\2\2\u013a\u013f\5\60\31\2\u013b\u013c\7\66\2\2\u013c")
        buf.write("\u013e\5\60\31\2\u013d\u013b\3\2\2\2\u013e\u0141\3\2\2")
        buf.write("\2\u013f\u013d\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0144")
        buf.write("\3\2\2\2\u0141\u013f\3\2\2\2\u0142\u0144\3\2\2\2\u0143")
        buf.write("\u013a\3\2\2\2\u0143\u0142\3\2\2\2\u0144/\3\2\2\2\u0145")
        buf.write("\u0146\7\3\2\2\u0146\u0147\78\2\2\u0147\61\3\2\2\2\u0148")
        buf.write("\u014d\5\64\33\2\u0149\u014d\5R*\2\u014a\u014d\5X-\2\u014b")
        buf.write("\u014d\5\\/\2\u014c\u0148\3\2\2\2\u014c\u0149\3\2\2\2")
        buf.write("\u014c\u014a\3\2\2\2\u014c\u014b\3\2\2\2\u014d\63\3\2")
        buf.write("\2\2\u014e\u014f\5\66\34\2\u014f\u0150\7\5\2\2\u0150\u0151")
        buf.write("\5\64\33\2\u0151\u0155\3\2\2\2\u0152\u0155\5\66\34\2\u0153")
        buf.write("\u0155\5<\37\2\u0154\u014e\3\2\2\2\u0154\u0152\3\2\2\2")
        buf.write("\u0154\u0153\3\2\2\2\u0155\65\3\2\2\2\u0156\u015e\5N(")
        buf.write("\2\u0157\u015e\5:\36\2\u0158\u015e\5<\37\2\u0159\u015a")
        buf.write("\7\60\2\2\u015a\u015b\5\64\33\2\u015b\u015c\7\61\2\2\u015c")
        buf.write("\u015e\3\2\2\2\u015d\u0156\3\2\2\2\u015d\u0157\3\2\2\2")
        buf.write("\u015d\u0158\3\2\2\2\u015d\u0159\3\2\2\2\u015e\67\3\2")
        buf.write("\2\2\u015f\u0160\t\5\2\2\u01609\3\2\2\2\u0161\u0165\7")
        buf.write("8\2\2\u0162\u0165\5F$\2\u0163\u0165\5*\26\2\u0164\u0161")
        buf.write("\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0163\3\2\2\2\u0165")
        buf.write(";\3\2\2\2\u0166\u0167\7\64\2\2\u0167\u0168\5> \2\u0168")
        buf.write("\u0169\7\65\2\2\u0169\u016a\7\66\2\2\u016a\u016b\5<\37")
        buf.write("\2\u016b\u0171\3\2\2\2\u016c\u016d\7\64\2\2\u016d\u016e")
        buf.write("\5> \2\u016e\u016f\7\65\2\2\u016f\u0171\3\2\2\2\u0170")
        buf.write("\u0166\3\2\2\2\u0170\u016c\3\2\2\2\u0171=\3\2\2\2\u0172")
        buf.write("\u0176\5@!\2\u0173\u0176\5B\"\2\u0174\u0176\5D#\2\u0175")
        buf.write("\u0172\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0174\3\2\2\2")
        buf.write("\u0176?\3\2\2\2\u0177\u0178\7\t\2\2\u0178\u0179\7\66\2")
        buf.write("\2\u0179\u017d\5@!\2\u017a\u017d\7\t\2\2\u017b\u017d\5")
        buf.write(":\36\2\u017c\u0177\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017b")
        buf.write("\3\2\2\2\u017dA\3\2\2\2\u017e\u017f\7\b\2\2\u017f\u0180")
        buf.write("\7\66\2\2\u0180\u0184\5B\"\2\u0181\u0184\7\b\2\2\u0182")
        buf.write("\u0184\5:\36\2\u0183\u017e\3\2\2\2\u0183\u0181\3\2\2\2")
        buf.write("\u0183\u0182\3\2\2\2\u0184C\3\2\2\2\u0185\u0186\7\n\2")
        buf.write("\2\u0186\u0187\7\66\2\2\u0187\u018b\5D#\2\u0188\u018b")
        buf.write("\7\n\2\2\u0189\u018b\5:\36\2\u018a\u0185\3\2\2\2\u018a")
        buf.write("\u0188\3\2\2\2\u018a\u0189\3\2\2\2\u018bE\3\2\2\2\u018c")
        buf.write("\u018d\78\2\2\u018d\u018e\7\64\2\2\u018e\u018f\5H%\2\u018f")
        buf.write("\u0190\7\65\2\2\u0190G\3\2\2\2\u0191\u0192\b%\1\2\u0192")
        buf.write("\u0193\5J&\2\u0193\u0199\3\2\2\2\u0194\u0195\f\4\2\2\u0195")
        buf.write("\u0196\7\66\2\2\u0196\u0198\5H%\2\u0197\u0194\3\2\2\2")
        buf.write("\u0198\u019b\3\2\2\2\u0199\u0197\3\2\2\2\u0199\u019a\3")
        buf.write("\2\2\2\u019aI\3\2\2\2\u019b\u0199\3\2\2\2\u019c\u019d")
        buf.write("\b&\1\2\u019d\u019e\5L\'\2\u019e\u01a4\3\2\2\2\u019f\u01a0")
        buf.write("\f\4\2\2\u01a0\u01a1\7\5\2\2\u01a1\u01a3\5L\'\2\u01a2")
        buf.write("\u019f\3\2\2\2\u01a3\u01a6\3\2\2\2\u01a4\u01a2\3\2\2\2")
        buf.write("\u01a4\u01a5\3\2\2\2\u01a5K\3\2\2\2\u01a6\u01a4\3\2\2")
        buf.write("\2\u01a7\u01ab\7\t\2\2\u01a8\u01ab\5N(\2\u01a9\u01ab\5")
        buf.write(":\36\2\u01aa\u01a7\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01a9")
        buf.write("\3\2\2\2\u01abM\3\2\2\2\u01ac\u01ad\5P)\2\u01ad\u01ae")
        buf.write("\7\5\2\2\u01ae\u01af\5N(\2\u01af\u01b4\3\2\2\2\u01b0\u01b1")
        buf.write("\7 \2\2\u01b1\u01b4\5N(\2\u01b2\u01b4\5P)\2\u01b3\u01ac")
        buf.write("\3\2\2\2\u01b3\u01b0\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b4")
        buf.write("O\3\2\2\2\u01b5\u01bc\7\t\2\2\u01b6\u01bc\5:\36\2\u01b7")
        buf.write("\u01b8\7\60\2\2\u01b8\u01b9\5N(\2\u01b9\u01ba\7\61\2\2")
        buf.write("\u01ba\u01bc\3\2\2\2\u01bb\u01b5\3\2\2\2\u01bb\u01b6\3")
        buf.write("\2\2\2\u01bb\u01b7\3\2\2\2\u01bcQ\3\2\2\2\u01bd\u01be")
        buf.write("\7\60\2\2\u01be\u01bf\5T+\2\u01bf\u01c0\7\61\2\2\u01c0")
        buf.write("\u01c3\3\2\2\2\u01c1\u01c3\5T+\2\u01c2\u01bd\3\2\2\2\u01c2")
        buf.write("\u01c1\3\2\2\2\u01c3S\3\2\2\2\u01c4\u01c5\5\64\33\2\u01c5")
        buf.write("\u01c6\7\6\2\2\u01c6\u01c7\5\64\33\2\u01c7\u01cd\3\2\2")
        buf.write("\2\u01c8\u01c9\5V,\2\u01c9\u01ca\7/\2\2\u01ca\u01cb\5")
        buf.write("V,\2\u01cb\u01cd\3\2\2\2\u01cc\u01c4\3\2\2\2\u01cc\u01c8")
        buf.write("\3\2\2\2\u01cdU\3\2\2\2\u01ce\u01d1\7\b\2\2\u01cf\u01d1")
        buf.write("\5:\36\2\u01d0\u01ce\3\2\2\2\u01d0\u01cf\3\2\2\2\u01d1")
        buf.write("W\3\2\2\2\u01d2\u01d3\b-\1\2\u01d3\u01d7\5Z.\2\u01d4\u01d5")
        buf.write("\7$\2\2\u01d5\u01d7\5X-\3\u01d6\u01d2\3\2\2\2\u01d6\u01d4")
        buf.write("\3\2\2\2\u01d7\u01dd\3\2\2\2\u01d8\u01d9\f\5\2\2\u01d9")
        buf.write("\u01da\7\7\2\2\u01da\u01dc\5Z.\2\u01db\u01d8\3\2\2\2\u01dc")
        buf.write("\u01df\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de\3\2\2\2")
        buf.write("\u01deY\3\2\2\2\u01df\u01dd\3\2\2\2\u01e0\u01e9\7\n\2")
        buf.write("\2\u01e1\u01e9\5R*\2\u01e2\u01e9\5:\36\2\u01e3\u01e9\5")
        buf.write("\64\33\2\u01e4\u01e5\7\60\2\2\u01e5\u01e6\5X-\2\u01e6")
        buf.write("\u01e7\7\61\2\2\u01e7\u01e9\3\2\2\2\u01e8\u01e0\3\2\2")
        buf.write("\2\u01e8\u01e1\3\2\2\2\u01e8\u01e2\3\2\2\2\u01e8\u01e3")
        buf.write("\3\2\2\2\u01e8\u01e4\3\2\2\2\u01e9[\3\2\2\2\u01ea\u01eb")
        buf.write("\5^\60\2\u01eb\u01ec\7.\2\2\u01ec\u01ed\5^\60\2\u01ed")
        buf.write("\u01f0\3\2\2\2\u01ee\u01f0\5^\60\2\u01ef\u01ea\3\2\2\2")
        buf.write("\u01ef\u01ee\3\2\2\2\u01f0]\3\2\2\2\u01f1\u01f4\7\b\2")
        buf.write("\2\u01f2\u01f4\5:\36\2\u01f3\u01f1\3\2\2\2\u01f3\u01f2")
        buf.write("\3\2\2\2\u01f4_\3\2\2\2:dhnu|\u0081\u0086\u008a\u0093")
        buf.write("\u00a4\u00ab\u00b2\u00b5\u00bc\u00c0\u00c6\u00cb\u00cf")
        buf.write("\u00d6\u00da\u00ec\u00f3\u0101\u0108\u010f\u0116\u0118")
        buf.write("\u011e\u0125\u0127\u012e\u0137\u013f\u0143\u014c\u0154")
        buf.write("\u015d\u0164\u0170\u0175\u017c\u0183\u018a\u0199\u01a4")
        buf.write("\u01aa\u01b3\u01bb\u01c2\u01cc\u01d0\u01d6\u01dd\u01e8")
        buf.write("\u01ef\u01f3")
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

    symbolicNames = [ "<INVALID>", "TYPE", "IMPLIKEYS", "NUMOP", "NUMRELAOPS", 
                      "LOGICOPBIN", "STRINGLIT", "NUMLIT", "BOOLIT", "TRUE", 
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
    RULE_vardecl = 2
    RULE_mainfunc = 3
    RULE_funcdecl = 4
    RULE_funcproto = 5
    RULE_funcblock = 6
    RULE_restmt = 7
    RULE_stmt = 8
    RULE_stmt_00 = 9
    RULE_stmtlist = 10
    RULE_assignstmt = 11
    RULE_ifstmt = 12
    RULE_ifblock = 13
    RULE_elseblk = 14
    RULE_elifblk = 15
    RULE_elifblk_0 = 16
    RULE_forstmt = 17
    RULE_loopblock = 18
    RULE_loopkey = 19
    RULE_funcall = 20
    RULE_paramcall = 21
    RULE_paramlist = 22
    RULE_params = 23
    RULE_allexp = 24
    RULE_exp = 25
    RULE_exp_01 = 26
    RULE_exp_00 = 27
    RULE_expall = 28
    RULE_array = 29
    RULE_explist = 30
    RULE_explist_1 = 31
    RULE_explist_2 = 32
    RULE_explist_3 = 33
    RULE_indexp = 34
    RULE_indop = 35
    RULE_indop_0 = 36
    RULE_indop_1 = 37
    RULE_ariexp = 38
    RULE_ariexp_00 = 39
    RULE_relatexp = 40
    RULE_relatexp_00 = 41
    RULE_relatexp_01 = 42
    RULE_logicexp = 43
    RULE_logicexp_00 = 44
    RULE_stringexp = 45
    RULE_stringexp_00 = 46

    ruleNames =  [ "program", "other", "vardecl", "mainfunc", "funcdecl", 
                   "funcproto", "funcblock", "restmt", "stmt", "stmt_00", 
                   "stmtlist", "assignstmt", "ifstmt", "ifblock", "elseblk", 
                   "elifblk", "elifblk_0", "forstmt", "loopblock", "loopkey", 
                   "funcall", "paramcall", "paramlist", "params", "allexp", 
                   "exp", "exp_01", "exp_00", "expall", "array", "explist", 
                   "explist_1", "explist_2", "explist_3", "indexp", "indop", 
                   "indop_0", "indop_1", "ariexp", "ariexp_00", "relatexp", 
                   "relatexp_00", "relatexp_01", "logicexp", "logicexp_00", 
                   "stringexp", "stringexp_00" ]

    EOF = Token.EOF
    TYPE=1
    IMPLIKEYS=2
    NUMOP=3
    NUMRELAOPS=4
    LOGICOPBIN=5
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

        def funcproto(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.FuncprotoContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.FuncprotoContext,i)


        def other(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.OtherContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.OtherContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

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
            self.state = 102
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 94
                    self.funcproto()
                    self.state = 96 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 95
                        self.match(ZCodeParser.NEWLINE)
                        self.state = 98 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==ZCodeParser.NEWLINE):
                            break
             
                self.state = 104
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 108
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 105
                    self.other() 
                self.state = 110
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 111
            self.mainfunc()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TYPE) | (1 << ZCodeParser.IMPLIKEYS) | (1 << ZCodeParser.NUMLIT) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FUNC) | (1 << ZCodeParser.FOR) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LS) | (1 << ZCodeParser.ID))) != 0):
                self.state = 112
                self.other()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
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


        def stmt_00(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_00Context,0)


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
        try:
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.funcdecl()
                pass
            elif token in [ZCodeParser.TYPE, ZCodeParser.IMPLIKEYS, ZCodeParser.NUMLIT, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.IF, ZCodeParser.MINUS, ZCodeParser.LB, ZCodeParser.LS, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.stmt_00()
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


    class VardeclContext(ParserRuleContext):
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

        def allexp(self):
            return self.getTypedRuleContext(ZCodeParser.AllexpContext,0)


        def IMPLIKEYS(self):
            return self.getToken(ZCodeParser.IMPLIKEYS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.TYPE or _la==ZCodeParser.DYNAMIC):
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


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.TYPE or _la==ZCodeParser.IMPLIKEYS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 130
                self.match(ZCodeParser.ID)
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.LS:
                    self.state = 131
                    self.array()


                self.state = 134
                self.match(ZCodeParser.ASSIGN)
                self.state = 135
                self.allexp()
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


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

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
            self.state = 138
            self.match(ZCodeParser.FUNC)
            self.state = 139
            self.match(ZCodeParser.MAIN)
            self.state = 140
            self.match(ZCodeParser.LB)
            self.state = 141
            self.match(ZCodeParser.RB)
            self.state = 145
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 142
                    self.match(ZCodeParser.NEWLINE) 
                self.state = 147
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 148
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

        def funcproto(self):
            return self.getTypedRuleContext(ZCodeParser.FuncprotoContext,0)


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
            self.state = 150
            self.funcproto()
            self.state = 151
            self.funcblock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncprotoContext(ParserRuleContext):
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

        def getRuleIndex(self):
            return ZCodeParser.RULE_funcproto

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncproto" ):
                return visitor.visitFuncproto(self)
            else:
                return visitor.visitChildren(self)




    def funcproto(self):

        localctx = ZCodeParser.FuncprotoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcproto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(ZCodeParser.FUNC)
            self.state = 154
            self.match(ZCodeParser.ID)
            self.state = 155
            self.match(ZCodeParser.LB)
            self.state = 156
            self.paramlist()
            self.state = 157
            self.match(ZCodeParser.RB)
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

        def restmt(self):
            return self.getTypedRuleContext(ZCodeParser.RestmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcblock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncblock" ):
                return visitor.visitFuncblock(self)
            else:
                return visitor.visitChildren(self)




    def funcblock(self):

        localctx = ZCodeParser.FuncblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcblock)
        self._la = 0 # Token type
        try:
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BEGIN, ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NEWLINE:
                    self.state = 159
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 164
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 165
                self.match(ZCodeParser.BEGIN)
                self.state = 167 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 166
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 169 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NEWLINE):
                        break

                self.state = 171
                self.stmtlist()
                self.state = 172
                self.match(ZCodeParser.END)
                self.state = 174 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 173
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 176 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NEWLINE):
                        break

                pass
            elif token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.restmt()
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


    class RestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def allexp(self):
            return self.getTypedRuleContext(ZCodeParser.AllexpContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_restmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRestmt" ):
                return visitor.visitRestmt(self)
            else:
                return visitor.visitChildren(self)




    def restmt(self):

        localctx = ZCodeParser.RestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_restmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(ZCodeParser.RETURN)
            self.state = 182
            self.allexp()
            self.state = 184 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 183
                self.match(ZCodeParser.NEWLINE)
                self.state = 186 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

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

        def stmt_00(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_00Context,0)


        def restmt(self):
            return self.getTypedRuleContext(ZCodeParser.RestmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_stmt)
        try:
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TYPE, ZCodeParser.IMPLIKEYS, ZCodeParser.NUMLIT, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.IF, ZCodeParser.MINUS, ZCodeParser.LB, ZCodeParser.LS, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.stmt_00()
                pass
            elif token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.restmt()
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


    class Stmt_00Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(ZCodeParser.AssignstmtContext,0)


        def funcall(self):
            return self.getTypedRuleContext(ZCodeParser.FuncallContext,0)


        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def ifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ForstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_00

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_00" ):
                return visitor.visitStmt_00(self)
            else:
                return visitor.visitChildren(self)




    def stmt_00(self):

        localctx = ZCodeParser.Stmt_00Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_stmt_00)
        self._la = 0 # Token type
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TYPE, ZCodeParser.IMPLIKEYS, ZCodeParser.NUMLIT, ZCodeParser.DYNAMIC, ZCodeParser.MINUS, ZCodeParser.LB, ZCodeParser.LS, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 192
                    self.vardecl()
                    pass

                elif la_ == 2:
                    self.state = 193
                    self.assignstmt()
                    pass

                elif la_ == 3:
                    self.state = 194
                    self.funcall()
                    pass

                elif la_ == 4:
                    self.state = 195
                    self.exp()
                    pass


                self.state = 199 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 198
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 201 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NEWLINE):
                        break

                pass
            elif token in [ZCodeParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.ifstmt()
                pass
            elif token in [ZCodeParser.FOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 204
                self.forstmt()
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
        self.enterRule(localctx, 20, self.RULE_stmtlist)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.stmt()
                self.state = 208
                self.stmtlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
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

        def allexp(self):
            return self.getTypedRuleContext(ZCodeParser.AllexpContext,0)


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
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 214
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 215
                self.indexp()
                pass


            self.state = 218
            self.match(ZCodeParser.ASSIGN)
            self.state = 219
            self.allexp()
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
        self.enterRule(localctx, 24, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(ZCodeParser.IF)
            self.state = 222
            self.ifblock()
            self.state = 223
            self.elifblk()
            self.state = 224
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

        def allexp(self):
            return self.getTypedRuleContext(ZCodeParser.AllexpContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def loopblock(self):
            return self.getTypedRuleContext(ZCodeParser.LoopblockContext,0)


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
            self.state = 226
            self.match(ZCodeParser.LB)
            self.state = 227
            self.allexp()
            self.state = 228
            self.match(ZCodeParser.RB)
            self.state = 229
            self.loopblock()
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

        def funcblock(self):
            return self.getTypedRuleContext(ZCodeParser.FuncblockContext,0)


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
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(ZCodeParser.ELSE)
                self.state = 232
                self.funcblock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


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
        self.enterRule(localctx, 30, self.RULE_elifblk)
        try:
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.elifblk_0()
                self.state = 237
                self.elifblk()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
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
        self.enterRule(localctx, 32, self.RULE_elifblk_0)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(ZCodeParser.ELIF)
            self.state = 244
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

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def logicexp(self):
            return self.getTypedRuleContext(ZCodeParser.LogicexpContext,0)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def loopblock(self):
            return self.getTypedRuleContext(ZCodeParser.LoopblockContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = ZCodeParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(ZCodeParser.FOR)
            self.state = 247
            self.match(ZCodeParser.ID)
            self.state = 248
            self.match(ZCodeParser.UNTIL)
            self.state = 249
            self.logicexp(0)
            self.state = 250
            self.match(ZCodeParser.BY)
            self.state = 251
            self.match(ZCodeParser.NUMLIT)
            self.state = 253 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 252
                    self.match(ZCodeParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 255 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 257
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

        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def loopkey(self):
            return self.getTypedRuleContext(ZCodeParser.LoopkeyContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_loopblock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopblock" ):
                return visitor.visitLoopblock(self)
            else:
                return visitor.visitChildren(self)




    def loopblock(self):

        localctx = ZCodeParser.LoopblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_loopblock)
        self._la = 0 # Token type
        try:
            self.state = 293
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BEGIN, ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NEWLINE:
                    self.state = 259
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 264
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 265
                self.match(ZCodeParser.BEGIN)
                self.state = 267 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 266
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 269 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NEWLINE):
                        break

                self.state = 271
                self.stmtlist()
                self.state = 278
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.BREAK or _la==ZCodeParser.CONTINUE:
                    self.state = 272
                    self.loopkey()
                    self.state = 274 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 273
                        self.match(ZCodeParser.NEWLINE)
                        self.state = 276 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==ZCodeParser.NEWLINE):
                            break



                self.state = 280
                self.match(ZCodeParser.END)
                self.state = 282 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 281
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 284 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NEWLINE):
                        break

                pass
            elif token in [ZCodeParser.TYPE, ZCodeParser.IMPLIKEYS, ZCodeParser.NUMLIT, ZCodeParser.RETURN, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.IF, ZCodeParser.MINUS, ZCodeParser.LB, ZCodeParser.LS, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.stmt()
                pass
            elif token in [ZCodeParser.BREAK, ZCodeParser.CONTINUE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 287
                self.loopkey()
                self.state = 289 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 288
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 291 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NEWLINE):
                        break

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
        self.enterRule(localctx, 38, self.RULE_loopkey)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
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

        def explist(self):
            return self.getTypedRuleContext(ZCodeParser.ExplistContext,0)


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
            self.state = 297
            self.match(ZCodeParser.ID)
            self.state = 298
            self.match(ZCodeParser.LB)
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.STRINGLIT) | (1 << ZCodeParser.NUMLIT) | (1 << ZCodeParser.BOOLIT) | (1 << ZCodeParser.ID))) != 0):
                self.state = 299
                self.explist()


            self.state = 302
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
            self.state = 304
            self.exp()
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.COMMA:
                self.state = 305
                self.match(ZCodeParser.COMMA)

                self.state = 306
                self.exp()
                self.state = 311
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
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.params()
                self.state = 317
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.COMMA:
                    self.state = 313
                    self.match(ZCodeParser.COMMA)
                    self.state = 314
                    self.params()
                    self.state = 319
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
            self.state = 323
            self.match(ZCodeParser.TYPE)
            self.state = 324
            self.match(ZCodeParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AllexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def relatexp(self):
            return self.getTypedRuleContext(ZCodeParser.RelatexpContext,0)


        def logicexp(self):
            return self.getTypedRuleContext(ZCodeParser.LogicexpContext,0)


        def stringexp(self):
            return self.getTypedRuleContext(ZCodeParser.StringexpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_allexp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAllexp" ):
                return visitor.visitAllexp(self)
            else:
                return visitor.visitChildren(self)




    def allexp(self):

        localctx = ZCodeParser.AllexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_allexp)
        try:
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self.relatexp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 328
                self.logicexp(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 329
                self.stringexp()
                pass


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


        def NUMOP(self):
            return self.getToken(ZCodeParser.NUMOP, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = ZCodeParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exp)
        try:
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.exp_01()
                self.state = 333
                self.match(ZCodeParser.NUMOP)
                self.state = 334
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.exp_01()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 337
                self.array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_01Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ariexp(self):
            return self.getTypedRuleContext(ZCodeParser.AriexpContext,0)


        def expall(self):
            return self.getTypedRuleContext(ZCodeParser.ExpallContext,0)


        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


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
        self.enterRule(localctx, 52, self.RULE_exp_01)
        try:
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.ariexp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.expall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 342
                self.array()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 343
                self.match(ZCodeParser.LB)
                self.state = 344
                self.exp()
                self.state = 345
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
        self.enterRule(localctx, 54, self.RULE_exp_00)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
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
        self.enterRule(localctx, 56, self.RULE_expall)
        try:
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.indexp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 353
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

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = ZCodeParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_array)
        try:
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.match(ZCodeParser.LS)
                self.state = 357
                self.explist()
                self.state = 358
                self.match(ZCodeParser.RS)
                self.state = 359
                self.match(ZCodeParser.COMMA)
                self.state = 360
                self.array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.match(ZCodeParser.LS)
                self.state = 363
                self.explist()
                self.state = 364
                self.match(ZCodeParser.RS)
                pass


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
        self.enterRule(localctx, 60, self.RULE_explist)
        try:
            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.explist_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self.explist_2()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 370
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
        self.enterRule(localctx, 62, self.RULE_explist_1)
        try:
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.match(ZCodeParser.NUMLIT)
                self.state = 374
                self.match(ZCodeParser.COMMA)
                self.state = 375
                self.explist_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
                self.match(ZCodeParser.NUMLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 377
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
        self.enterRule(localctx, 64, self.RULE_explist_2)
        try:
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.match(ZCodeParser.STRINGLIT)
                self.state = 381
                self.match(ZCodeParser.COMMA)
                self.state = 382
                self.explist_2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
                self.match(ZCodeParser.STRINGLIT)
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
        self.enterRule(localctx, 66, self.RULE_explist_3)
        try:
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.match(ZCodeParser.BOOLIT)
                self.state = 388
                self.match(ZCodeParser.COMMA)
                self.state = 389
                self.explist_3()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 390
                self.match(ZCodeParser.BOOLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 391
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
        self.enterRule(localctx, 68, self.RULE_indexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(ZCodeParser.ID)
            self.state = 395
            self.match(ZCodeParser.LS)
            self.state = 396
            self.indop(0)
            self.state = 397
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
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_indop, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.indop_0(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 407
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.IndopContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_indop)
                    self.state = 402
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 403
                    self.match(ZCodeParser.COMMA)
                    self.state = 404
                    self.indop(0) 
                self.state = 409
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

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
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_indop_0, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.indop_1()
            self._ctx.stop = self._input.LT(-1)
            self.state = 418
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Indop_0Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_indop_0)
                    self.state = 413
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 414
                    self.match(ZCodeParser.NUMOP)
                    self.state = 415
                    self.indop_1() 
                self.state = 420
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

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
        self.enterRule(localctx, 74, self.RULE_indop_1)
        try:
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.match(ZCodeParser.NUMLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
                self.ariexp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 423
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
        self.enterRule(localctx, 76, self.RULE_ariexp)
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.ariexp_00()
                self.state = 427
                self.match(ZCodeParser.NUMOP)
                self.state = 428
                self.ariexp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.match(ZCodeParser.MINUS)
                self.state = 431
                self.ariexp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 432
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


        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def ariexp(self):
            return self.getTypedRuleContext(ZCodeParser.AriexpContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ariexp_00

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAriexp_00" ):
                return visitor.visitAriexp_00(self)
            else:
                return visitor.visitChildren(self)




    def ariexp_00(self):

        localctx = ZCodeParser.Ariexp_00Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_ariexp_00)
        try:
            self.state = 441
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.match(ZCodeParser.NUMLIT)
                pass
            elif token in [ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 436
                self.expall()
                pass
            elif token in [ZCodeParser.LB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 437
                self.match(ZCodeParser.LB)
                self.state = 438
                self.ariexp()
                self.state = 439
                self.match(ZCodeParser.RB)
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


    class RelatexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def relatexp_00(self):
            return self.getTypedRuleContext(ZCodeParser.Relatexp_00Context,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_relatexp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelatexp" ):
                return visitor.visitRelatexp(self)
            else:
                return visitor.visitChildren(self)




    def relatexp(self):

        localctx = ZCodeParser.RelatexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_relatexp)
        try:
            self.state = 448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 443
                self.match(ZCodeParser.LB)
                self.state = 444
                self.relatexp_00()
                self.state = 445
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.relatexp_00()
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

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpContext,i)


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
            return ZCodeParser.RULE_relatexp_00

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelatexp_00" ):
                return visitor.visitRelatexp_00(self)
            else:
                return visitor.visitChildren(self)




    def relatexp_00(self):

        localctx = ZCodeParser.Relatexp_00Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_relatexp_00)
        try:
            self.state = 458
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                self.exp()
                self.state = 451
                self.match(ZCodeParser.NUMRELAOPS)
                self.state = 452
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 454
                self.relatexp_01()
                self.state = 455
                self.match(ZCodeParser.EQUALITY)
                self.state = 456
                self.relatexp_01()
                pass


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
        self.enterRule(localctx, 84, self.RULE_relatexp_01)
        try:
            self.state = 462
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 460
                self.match(ZCodeParser.STRINGLIT)
                pass
            elif token in [ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 461
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
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_logicexp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.STRINGLIT, ZCodeParser.NUMLIT, ZCodeParser.BOOLIT, ZCodeParser.MINUS, ZCodeParser.LB, ZCodeParser.LS, ZCodeParser.ID]:
                self.state = 465
                self.logicexp_00()
                pass
            elif token in [ZCodeParser.NOT]:
                self.state = 466
                self.match(ZCodeParser.NOT)
                self.state = 467
                self.logicexp(1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 475
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.LogicexpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicexp)
                    self.state = 470
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 471
                    self.match(ZCodeParser.LOGICOPBIN)
                    self.state = 472
                    self.logicexp_00() 
                self.state = 477
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

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


        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def logicexp(self):
            return self.getTypedRuleContext(ZCodeParser.LogicexpContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_logicexp_00

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicexp_00" ):
                return visitor.visitLogicexp_00(self)
            else:
                return visitor.visitChildren(self)




    def logicexp_00(self):

        localctx = ZCodeParser.Logicexp_00Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_logicexp_00)
        try:
            self.state = 486
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 478
                self.match(ZCodeParser.BOOLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 479
                self.relatexp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 480
                self.expall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 481
                self.exp()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 482
                self.match(ZCodeParser.LB)
                self.state = 483
                self.logicexp(0)
                self.state = 484
                self.match(ZCodeParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stringexp_00(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Stringexp_00Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Stringexp_00Context,i)


        def ELLIPSIS(self):
            return self.getToken(ZCodeParser.ELLIPSIS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stringexp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringexp" ):
                return visitor.visitStringexp(self)
            else:
                return visitor.visitChildren(self)




    def stringexp(self):

        localctx = ZCodeParser.StringexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_stringexp)
        try:
            self.state = 493
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 488
                self.stringexp_00()
                self.state = 489
                self.match(ZCodeParser.ELLIPSIS)
                self.state = 490
                self.stringexp_00()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 492
                self.stringexp_00()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stringexp_00Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def expall(self):
            return self.getTypedRuleContext(ZCodeParser.ExpallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stringexp_00

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringexp_00" ):
                return visitor.visitStringexp_00(self)
            else:
                return visitor.visitChildren(self)




    def stringexp_00(self):

        localctx = ZCodeParser.Stringexp_00Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_stringexp_00)
        try:
            self.state = 497
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
                self.match(ZCodeParser.STRINGLIT)
                pass
            elif token in [ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 496
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
        self._predicates[35] = self.indop_sempred
        self._predicates[36] = self.indop_0_sempred
        self._predicates[43] = self.logicexp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def indop_sempred(self, localctx:IndopContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def indop_0_sempred(self, localctx:Indop_0Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def logicexp_sempred(self, localctx:LogicexpContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




