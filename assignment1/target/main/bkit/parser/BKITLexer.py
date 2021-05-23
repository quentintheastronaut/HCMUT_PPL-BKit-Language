# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2X")
        buf.write("\u0327\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3")
        buf.write("!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3$\3$\3%\3%\3")
        buf.write("&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3")
        buf.write(".\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3")
        buf.write("\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67")
        buf.write("\3\67\38\38\38\39\39\39\3:\3:\3:\3;\3;\3;\3<\3<\3=\3=")
        buf.write("\3>\3>\3>\3>\3?\3?\3?\3?\3@\3@\3@\3A\3A\3A\3B\3B\3B\3")
        buf.write("B\3C\3C\3C\3D\3D\3D\3E\3E\3F\3F\5F\u0231\nF\3G\3G\3G\3")
        buf.write("G\3G\7G\u0238\nG\fG\16G\u023b\13G\3G\3G\3G\3G\3G\3G\3")
        buf.write("G\7G\u0244\nG\fG\16G\u0247\13G\3G\3G\3G\3G\3G\3G\3G\7")
        buf.write("G\u0250\nG\fG\16G\u0253\13G\3G\3G\3G\3G\3G\3G\3G\7G\u025c")
        buf.write("\nG\fG\16G\u025f\13G\3G\3G\5G\u0263\nG\3H\3H\5H\u0267")
        buf.write("\nH\3H\3H\3H\7H\u026c\nH\fH\16H\u026f\13H\3H\3H\3H\3H")
        buf.write("\3H\3H\5H\u0277\nH\3I\3I\7I\u027b\nI\fI\16I\u027e\13I")
        buf.write("\3I\3I\3I\3J\3J\5J\u0285\nJ\3K\6K\u0288\nK\rK\16K\u0289")
        buf.write("\3K\3K\6K\u028e\nK\rK\16K\u028f\3K\5K\u0293\nK\3K\3K\5")
        buf.write("K\u0297\nK\3K\6K\u029a\nK\rK\16K\u029b\5K\u029e\nK\3L")
        buf.write("\3L\3L\7L\u02a3\nL\fL\16L\u02a6\13L\5L\u02a8\nL\3M\3M")
        buf.write("\3M\6M\u02ad\nM\rM\16M\u02ae\3N\3N\3N\6N\u02b4\nN\rN\16")
        buf.write("N\u02b5\3O\3O\3O\5O\u02bb\nO\3P\3P\3Q\3Q\3R\3R\3S\3S\3")
        buf.write("T\3T\3U\3U\3V\3V\7V\u02cb\nV\fV\16V\u02ce\13V\3W\3W\3")
        buf.write("W\3W\7W\u02d4\nW\fW\16W\u02d7\13W\3W\5W\u02da\nW\3W\3")
        buf.write("W\3W\3W\3W\3X\3X\3X\3X\7X\u02e5\nX\fX\16X\u02e8\13X\3")
        buf.write("X\3X\3X\3X\3X\3Y\6Y\u02f0\nY\rY\16Y\u02f1\3Y\3Y\3Z\3Z")
        buf.write("\7Z\u02f8\nZ\fZ\16Z\u02fb\13Z\3Z\5Z\u02fe\nZ\3Z\3Z\3[")
        buf.write("\3[\7[\u0304\n[\f[\16[\u0307\13[\3[\3[\3[\3\\\3\\\5\\")
        buf.write("\u030e\n\\\3]\3]\3]\3]\3]\3]\5]\u0316\n]\3^\3^\3^\5^\u031b")
        buf.write("\n^\3_\3_\3_\3`\3`\3`\3`\5`\u0324\n`\3`\3`\4\u02d5\u02e6")
        buf.write("\2a\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\u0087E\u0089F")
        buf.write("\u008bG\u008dH\u008fI\u0091J\u0093K\u0095L\u0097M\u0099")
        buf.write("N\u009bO\u009dP\u009f\2\u00a1\2\u00a3\2\u00a5\2\u00a7")
        buf.write("\2\u00a9\2\u00abQ\u00adR\u00afS\u00b1T\u00b3U\u00b5V\u00b7")
        buf.write("\2\u00b9\2\u00bb\2\u00bdW\u00bfX\3\2\27\4\2GGgg\3\2\63")
        buf.write(";\4\2ZZzz\4\2\62;CH\4\2QQqq\3\2\629\3\2c|\3\2C\\\4\2C")
        buf.write("\\c|\3\2\62;\4\2--//\5\2\62;C\\c|\5\2\n\f\16\17\"\"\7")
        buf.write("\3\n\f\16\17$$))^^\7\2\n\f\16\17$$))^^\t\2))^^ddhhppt")
        buf.write("tvv\3\2))\3\2$$\3\2^^\n\2$$))^^ddhhppttvv\3\2,,\2\u0343")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
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
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u00ab")
        buf.write("\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2")
        buf.write("\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf")
        buf.write("\3\2\2\2\3\u00c1\3\2\2\2\5\u00ce\3\2\2\2\7\u00db\3\2\2")
        buf.write("\2\t\u00e9\3\2\2\2\13\u00f7\3\2\2\2\r\u0107\3\2\2\2\17")
        buf.write("\u0117\3\2\2\2\21\u0126\3\2\2\2\23\u0135\3\2\2\2\25\u013d")
        buf.write("\3\2\2\2\27\u0143\3\2\2\2\31\u014e\3\2\2\2\33\u0153\3")
        buf.write("\2\2\2\35\u0158\3\2\2\2\37\u015e\3\2\2\2!\u0167\3\2\2")
        buf.write("\2#\u016a\3\2\2\2%\u016f\3\2\2\2\'\u0176\3\2\2\2)\u017e")
        buf.write("\3\2\2\2+\u0184\3\2\2\2-\u018b\3\2\2\2/\u0194\3\2\2\2")
        buf.write("\61\u0198\3\2\2\2\63\u01a1\3\2\2\2\65\u01a4\3\2\2\2\67")
        buf.write("\u01ae\3\2\2\29\u01b5\3\2\2\2;\u01ba\3\2\2\2=\u01be\3")
        buf.write("\2\2\2?\u01c4\3\2\2\2A\u01c9\3\2\2\2C\u01cf\3\2\2\2E\u01d5")
        buf.write("\3\2\2\2G\u01d7\3\2\2\2I\u01d9\3\2\2\2K\u01db\3\2\2\2")
        buf.write("M\u01dd\3\2\2\2O\u01df\3\2\2\2Q\u01e1\3\2\2\2S\u01e3\3")
        buf.write("\2\2\2U\u01e5\3\2\2\2W\u01e7\3\2\2\2Y\u01e9\3\2\2\2[\u01eb")
        buf.write("\3\2\2\2]\u01ed\3\2\2\2_\u01ef\3\2\2\2a\u01f1\3\2\2\2")
        buf.write("c\u01f3\3\2\2\2e\u01f6\3\2\2\2g\u01f8\3\2\2\2i\u01fb\3")
        buf.write("\2\2\2k\u01fe\3\2\2\2m\u0201\3\2\2\2o\u0204\3\2\2\2q\u0207")
        buf.write("\3\2\2\2s\u020a\3\2\2\2u\u020d\3\2\2\2w\u0210\3\2\2\2")
        buf.write("y\u0212\3\2\2\2{\u0214\3\2\2\2}\u0218\3\2\2\2\177\u021c")
        buf.write("\3\2\2\2\u0081\u021f\3\2\2\2\u0083\u0222\3\2\2\2\u0085")
        buf.write("\u0226\3\2\2\2\u0087\u0229\3\2\2\2\u0089\u022c\3\2\2\2")
        buf.write("\u008b\u0230\3\2\2\2\u008d\u0262\3\2\2\2\u008f\u0276\3")
        buf.write("\2\2\2\u0091\u0278\3\2\2\2\u0093\u0284\3\2\2\2\u0095\u0287")
        buf.write("\3\2\2\2\u0097\u02a7\3\2\2\2\u0099\u02a9\3\2\2\2\u009b")
        buf.write("\u02b0\3\2\2\2\u009d\u02ba\3\2\2\2\u009f\u02bc\3\2\2\2")
        buf.write("\u00a1\u02be\3\2\2\2\u00a3\u02c0\3\2\2\2\u00a5\u02c2\3")
        buf.write("\2\2\2\u00a7\u02c4\3\2\2\2\u00a9\u02c6\3\2\2\2\u00ab\u02c8")
        buf.write("\3\2\2\2\u00ad\u02cf\3\2\2\2\u00af\u02e0\3\2\2\2\u00b1")
        buf.write("\u02ef\3\2\2\2\u00b3\u02f5\3\2\2\2\u00b5\u0301\3\2\2\2")
        buf.write("\u00b7\u030d\3\2\2\2\u00b9\u0315\3\2\2\2\u00bb\u031a\3")
        buf.write("\2\2\2\u00bd\u031c\3\2\2\2\u00bf\u031f\3\2\2\2\u00c1\u00c2")
        buf.write("\7k\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4\7v\2\2\u00c4\u00c5")
        buf.write("\7a\2\2\u00c5\u00c6\7q\2\2\u00c6\u00c7\7h\2\2\u00c7\u00c8")
        buf.write("\7a\2\2\u00c8\u00c9\7h\2\2\u00c9\u00ca\7n\2\2\u00ca\u00cb")
        buf.write("\7q\2\2\u00cb\u00cc\7c\2\2\u00cc\u00cd\7v\2\2\u00cd\4")
        buf.write("\3\2\2\2\u00ce\u00cf\7h\2\2\u00cf\u00d0\7n\2\2\u00d0\u00d1")
        buf.write("\7q\2\2\u00d1\u00d2\7c\2\2\u00d2\u00d3\7v\2\2\u00d3\u00d4")
        buf.write("\7a\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6\7h\2\2\u00d6\u00d7")
        buf.write("\7a\2\2\u00d7\u00d8\7k\2\2\u00d8\u00d9\7p\2\2\u00d9\u00da")
        buf.write("\7v\2\2\u00da\6\3\2\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd")
        buf.write("\7p\2\2\u00dd\u00de\7v\2\2\u00de\u00df\7a\2\2\u00df\u00e0")
        buf.write("\7q\2\2\u00e0\u00e1\7h\2\2\u00e1\u00e2\7a\2\2\u00e2\u00e3")
        buf.write("\7u\2\2\u00e3\u00e4\7v\2\2\u00e4\u00e5\7t\2\2\u00e5\u00e6")
        buf.write("\7k\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8\7i\2\2\u00e8\b")
        buf.write("\3\2\2\2\u00e9\u00ea\7u\2\2\u00ea\u00eb\7v\2\2\u00eb\u00ec")
        buf.write("\7t\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef")
        buf.write("\7i\2\2\u00ef\u00f0\7a\2\2\u00f0\u00f1\7q\2\2\u00f1\u00f2")
        buf.write("\7h\2\2\u00f2\u00f3\7a\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5")
        buf.write("\7p\2\2\u00f5\u00f6\7v\2\2\u00f6\n\3\2\2\2\u00f7\u00f8")
        buf.write("\7h\2\2\u00f8\u00f9\7n\2\2\u00f9\u00fa\7q\2\2\u00fa\u00fb")
        buf.write("\7c\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd\7a\2\2\u00fd\u00fe")
        buf.write("\7q\2\2\u00fe\u00ff\7h\2\2\u00ff\u0100\7a\2\2\u0100\u0101")
        buf.write("\7u\2\2\u0101\u0102\7v\2\2\u0102\u0103\7t\2\2\u0103\u0104")
        buf.write("\7k\2\2\u0104\u0105\7p\2\2\u0105\u0106\7i\2\2\u0106\f")
        buf.write("\3\2\2\2\u0107\u0108\7u\2\2\u0108\u0109\7v\2\2\u0109\u010a")
        buf.write("\7t\2\2\u010a\u010b\7k\2\2\u010b\u010c\7p\2\2\u010c\u010d")
        buf.write("\7i\2\2\u010d\u010e\7a\2\2\u010e\u010f\7q\2\2\u010f\u0110")
        buf.write("\7h\2\2\u0110\u0111\7a\2\2\u0111\u0112\7h\2\2\u0112\u0113")
        buf.write("\7n\2\2\u0113\u0114\7q\2\2\u0114\u0115\7c\2\2\u0115\u0116")
        buf.write("\7v\2\2\u0116\16\3\2\2\2\u0117\u0118\7d\2\2\u0118\u0119")
        buf.write("\7q\2\2\u0119\u011a\7q\2\2\u011a\u011b\7n\2\2\u011b\u011c")
        buf.write("\7a\2\2\u011c\u011d\7q\2\2\u011d\u011e\7h\2\2\u011e\u011f")
        buf.write("\7a\2\2\u011f\u0120\7u\2\2\u0120\u0121\7v\2\2\u0121\u0122")
        buf.write("\7t\2\2\u0122\u0123\7k\2\2\u0123\u0124\7p\2\2\u0124\u0125")
        buf.write("\7i\2\2\u0125\20\3\2\2\2\u0126\u0127\7u\2\2\u0127\u0128")
        buf.write("\7v\2\2\u0128\u0129\7t\2\2\u0129\u012a\7k\2\2\u012a\u012b")
        buf.write("\7p\2\2\u012b\u012c\7i\2\2\u012c\u012d\7a\2\2\u012d\u012e")
        buf.write("\7q\2\2\u012e\u012f\7h\2\2\u012f\u0130\7a\2\2\u0130\u0131")
        buf.write("\7d\2\2\u0131\u0132\7q\2\2\u0132\u0133\7q\2\2\u0133\u0134")
        buf.write("\7n\2\2\u0134\22\3\2\2\2\u0135\u0136\7r\2\2\u0136\u0137")
        buf.write("\7t\2\2\u0137\u0138\7k\2\2\u0138\u0139\7p\2\2\u0139\u013a")
        buf.write("\7v\2\2\u013a\u013b\7N\2\2\u013b\u013c\7p\2\2\u013c\24")
        buf.write("\3\2\2\2\u013d\u013e\7r\2\2\u013e\u013f\7t\2\2\u013f\u0140")
        buf.write("\7k\2\2\u0140\u0141\7p\2\2\u0141\u0142\7v\2\2\u0142\26")
        buf.write("\3\2\2\2\u0143\u0144\7r\2\2\u0144\u0145\7t\2\2\u0145\u0146")
        buf.write("\7k\2\2\u0146\u0147\7p\2\2\u0147\u0148\7v\2\2\u0148\u0149")
        buf.write("\7U\2\2\u0149\u014a\7v\2\2\u014a\u014b\7t\2\2\u014b\u014c")
        buf.write("\7N\2\2\u014c\u014d\7p\2\2\u014d\30\3\2\2\2\u014e\u014f")
        buf.write("\7t\2\2\u014f\u0150\7g\2\2\u0150\u0151\7c\2\2\u0151\u0152")
        buf.write("\7f\2\2\u0152\32\3\2\2\2\u0153\u0154\7D\2\2\u0154\u0155")
        buf.write("\7q\2\2\u0155\u0156\7f\2\2\u0156\u0157\7{\2\2\u0157\34")
        buf.write("\3\2\2\2\u0158\u0159\7D\2\2\u0159\u015a\7t\2\2\u015a\u015b")
        buf.write("\7g\2\2\u015b\u015c\7c\2\2\u015c\u015d\7m\2\2\u015d\36")
        buf.write("\3\2\2\2\u015e\u015f\7E\2\2\u015f\u0160\7q\2\2\u0160\u0161")
        buf.write("\7p\2\2\u0161\u0162\7v\2\2\u0162\u0163\7k\2\2\u0163\u0164")
        buf.write("\7p\2\2\u0164\u0165\7w\2\2\u0165\u0166\7g\2\2\u0166 \3")
        buf.write("\2\2\2\u0167\u0168\7F\2\2\u0168\u0169\7q\2\2\u0169\"\3")
        buf.write("\2\2\2\u016a\u016b\7G\2\2\u016b\u016c\7n\2\2\u016c\u016d")
        buf.write("\7u\2\2\u016d\u016e\7g\2\2\u016e$\3\2\2\2\u016f\u0170")
        buf.write("\7G\2\2\u0170\u0171\7n\2\2\u0171\u0172\7u\2\2\u0172\u0173")
        buf.write("\7g\2\2\u0173\u0174\7K\2\2\u0174\u0175\7h\2\2\u0175&\3")
        buf.write("\2\2\2\u0176\u0177\7G\2\2\u0177\u0178\7p\2\2\u0178\u0179")
        buf.write("\7f\2\2\u0179\u017a\7D\2\2\u017a\u017b\7q\2\2\u017b\u017c")
        buf.write("\7f\2\2\u017c\u017d\7{\2\2\u017d(\3\2\2\2\u017e\u017f")
        buf.write("\7G\2\2\u017f\u0180\7p\2\2\u0180\u0181\7f\2\2\u0181\u0182")
        buf.write("\7K\2\2\u0182\u0183\7h\2\2\u0183*\3\2\2\2\u0184\u0185")
        buf.write("\7G\2\2\u0185\u0186\7p\2\2\u0186\u0187\7f\2\2\u0187\u0188")
        buf.write("\7H\2\2\u0188\u0189\7q\2\2\u0189\u018a\7t\2\2\u018a,\3")
        buf.write("\2\2\2\u018b\u018c\7G\2\2\u018c\u018d\7p\2\2\u018d\u018e")
        buf.write("\7f\2\2\u018e\u018f\7Y\2\2\u018f\u0190\7j\2\2\u0190\u0191")
        buf.write("\7k\2\2\u0191\u0192\7n\2\2\u0192\u0193\7g\2\2\u0193.\3")
        buf.write("\2\2\2\u0194\u0195\7H\2\2\u0195\u0196\7q\2\2\u0196\u0197")
        buf.write("\7t\2\2\u0197\60\3\2\2\2\u0198\u0199\7H\2\2\u0199\u019a")
        buf.write("\7w\2\2\u019a\u019b\7p\2\2\u019b\u019c\7e\2\2\u019c\u019d")
        buf.write("\7v\2\2\u019d\u019e\7k\2\2\u019e\u019f\7q\2\2\u019f\u01a0")
        buf.write("\7p\2\2\u01a0\62\3\2\2\2\u01a1\u01a2\7K\2\2\u01a2\u01a3")
        buf.write("\7h\2\2\u01a3\64\3\2\2\2\u01a4\u01a5\7R\2\2\u01a5\u01a6")
        buf.write("\7c\2\2\u01a6\u01a7\7t\2\2\u01a7\u01a8\7c\2\2\u01a8\u01a9")
        buf.write("\7o\2\2\u01a9\u01aa\7g\2\2\u01aa\u01ab\7v\2\2\u01ab\u01ac")
        buf.write("\7g\2\2\u01ac\u01ad\7t\2\2\u01ad\66\3\2\2\2\u01ae\u01af")
        buf.write("\7T\2\2\u01af\u01b0\7g\2\2\u01b0\u01b1\7v\2\2\u01b1\u01b2")
        buf.write("\7w\2\2\u01b2\u01b3\7t\2\2\u01b3\u01b4\7p\2\2\u01b48\3")
        buf.write("\2\2\2\u01b5\u01b6\7V\2\2\u01b6\u01b7\7j\2\2\u01b7\u01b8")
        buf.write("\7g\2\2\u01b8\u01b9\7p\2\2\u01b9:\3\2\2\2\u01ba\u01bb")
        buf.write("\7X\2\2\u01bb\u01bc\7c\2\2\u01bc\u01bd\7t\2\2\u01bd<\3")
        buf.write("\2\2\2\u01be\u01bf\7Y\2\2\u01bf\u01c0\7j\2\2\u01c0\u01c1")
        buf.write("\7k\2\2\u01c1\u01c2\7n\2\2\u01c2\u01c3\7g\2\2\u01c3>\3")
        buf.write("\2\2\2\u01c4\u01c5\7V\2\2\u01c5\u01c6\7t\2\2\u01c6\u01c7")
        buf.write("\7w\2\2\u01c7\u01c8\7g\2\2\u01c8@\3\2\2\2\u01c9\u01ca")
        buf.write("\7H\2\2\u01ca\u01cb\7c\2\2\u01cb\u01cc\7n\2\2\u01cc\u01cd")
        buf.write("\7u\2\2\u01cd\u01ce\7g\2\2\u01ceB\3\2\2\2\u01cf\u01d0")
        buf.write("\7G\2\2\u01d0\u01d1\7p\2\2\u01d1\u01d2\7f\2\2\u01d2\u01d3")
        buf.write("\7F\2\2\u01d3\u01d4\7q\2\2\u01d4D\3\2\2\2\u01d5\u01d6")
        buf.write("\7.\2\2\u01d6F\3\2\2\2\u01d7\u01d8\7*\2\2\u01d8H\3\2\2")
        buf.write("\2\u01d9\u01da\7+\2\2\u01daJ\3\2\2\2\u01db\u01dc\7}\2")
        buf.write("\2\u01dcL\3\2\2\2\u01dd\u01de\7\177\2\2\u01deN\3\2\2\2")
        buf.write("\u01df\u01e0\7]\2\2\u01e0P\3\2\2\2\u01e1\u01e2\7_\2\2")
        buf.write("\u01e2R\3\2\2\2\u01e3\u01e4\7=\2\2\u01e4T\3\2\2\2\u01e5")
        buf.write("\u01e6\7<\2\2\u01e6V\3\2\2\2\u01e7\u01e8\7\60\2\2\u01e8")
        buf.write("X\3\2\2\2\u01e9\u01ea\7-\2\2\u01eaZ\3\2\2\2\u01eb\u01ec")
        buf.write("\7/\2\2\u01ec\\\3\2\2\2\u01ed\u01ee\7,\2\2\u01ee^\3\2")
        buf.write("\2\2\u01ef\u01f0\7^\2\2\u01f0`\3\2\2\2\u01f1\u01f2\7\'")
        buf.write("\2\2\u01f2b\3\2\2\2\u01f3\u01f4\7^\2\2\u01f4\u01f5\7\'")
        buf.write("\2\2\u01f5d\3\2\2\2\u01f6\u01f7\7#\2\2\u01f7f\3\2\2\2")
        buf.write("\u01f8\u01f9\7(\2\2\u01f9\u01fa\7(\2\2\u01fah\3\2\2\2")
        buf.write("\u01fb\u01fc\7~\2\2\u01fc\u01fd\7~\2\2\u01fdj\3\2\2\2")
        buf.write("\u01fe\u01ff\7-\2\2\u01ff\u0200\7\60\2\2\u0200l\3\2\2")
        buf.write("\2\u0201\u0202\7/\2\2\u0202\u0203\7\60\2\2\u0203n\3\2")
        buf.write("\2\2\u0204\u0205\7,\2\2\u0205\u0206\7\60\2\2\u0206p\3")
        buf.write("\2\2\2\u0207\u0208\7^\2\2\u0208\u0209\7\60\2\2\u0209r")
        buf.write("\3\2\2\2\u020a\u020b\7>\2\2\u020b\u020c\7?\2\2\u020ct")
        buf.write("\3\2\2\2\u020d\u020e\7@\2\2\u020e\u020f\7?\2\2\u020fv")
        buf.write("\3\2\2\2\u0210\u0211\7>\2\2\u0211x\3\2\2\2\u0212\u0213")
        buf.write("\7@\2\2\u0213z\3\2\2\2\u0214\u0215\7>\2\2\u0215\u0216")
        buf.write("\7?\2\2\u0216\u0217\7\60\2\2\u0217|\3\2\2\2\u0218\u0219")
        buf.write("\7@\2\2\u0219\u021a\7?\2\2\u021a\u021b\7\60\2\2\u021b")
        buf.write("~\3\2\2\2\u021c\u021d\7>\2\2\u021d\u021e\7\60\2\2\u021e")
        buf.write("\u0080\3\2\2\2\u021f\u0220\7@\2\2\u0220\u0221\7\60\2\2")
        buf.write("\u0221\u0082\3\2\2\2\u0222\u0223\7?\2\2\u0223\u0224\7")
        buf.write("\61\2\2\u0224\u0225\7?\2\2\u0225\u0084\3\2\2\2\u0226\u0227")
        buf.write("\7#\2\2\u0227\u0228\7?\2\2\u0228\u0086\3\2\2\2\u0229\u022a")
        buf.write("\7?\2\2\u022a\u022b\7?\2\2\u022b\u0088\3\2\2\2\u022c\u022d")
        buf.write("\7?\2\2\u022d\u008a\3\2\2\2\u022e\u0231\5\u008dG\2\u022f")
        buf.write("\u0231\5\u008fH\2\u0230\u022e\3\2\2\2\u0230\u022f\3\2")
        buf.write("\2\2\u0231\u008c\3\2\2\2\u0232\u0233\5K&\2\u0233\u0239")
        buf.write("\5\u0095K\2\u0234\u0235\5E#\2\u0235\u0236\5\u0095K\2\u0236")
        buf.write("\u0238\3\2\2\2\u0237\u0234\3\2\2\2\u0238\u023b\3\2\2\2")
        buf.write("\u0239\u0237\3\2\2\2\u0239\u023a\3\2\2\2\u023a\u023c\3")
        buf.write("\2\2\2\u023b\u0239\3\2\2\2\u023c\u023d\5M\'\2\u023d\u0263")
        buf.write("\3\2\2\2\u023e\u023f\5K&\2\u023f\u0245\5\u009dO\2\u0240")
        buf.write("\u0241\5E#\2\u0241\u0242\5\u009dO\2\u0242\u0244\3\2\2")
        buf.write("\2\u0243\u0240\3\2\2\2\u0244\u0247\3\2\2\2\u0245\u0243")
        buf.write("\3\2\2\2\u0245\u0246\3\2\2\2\u0246\u0248\3\2\2\2\u0247")
        buf.write("\u0245\3\2\2\2\u0248\u0249\5M\'\2\u0249\u0263\3\2\2\2")
        buf.write("\u024a\u024b\5K&\2\u024b\u0251\5\u0093J\2\u024c\u024d")
        buf.write("\5E#\2\u024d\u024e\5\u0093J\2\u024e\u0250\3\2\2\2\u024f")
        buf.write("\u024c\3\2\2\2\u0250\u0253\3\2\2\2\u0251\u024f\3\2\2\2")
        buf.write("\u0251\u0252\3\2\2\2\u0252\u0254\3\2\2\2\u0253\u0251\3")
        buf.write("\2\2\2\u0254\u0255\5M\'\2\u0255\u0263\3\2\2\2\u0256\u0257")
        buf.write("\5K&\2\u0257\u025d\5\u0091I\2\u0258\u0259\5E#\2\u0259")
        buf.write("\u025a\5\u0091I\2\u025a\u025c\3\2\2\2\u025b\u0258\3\2")
        buf.write("\2\2\u025c\u025f\3\2\2\2\u025d\u025b\3\2\2\2\u025d\u025e")
        buf.write("\3\2\2\2\u025e\u0260\3\2\2\2\u025f\u025d\3\2\2\2\u0260")
        buf.write("\u0261\5M\'\2\u0261\u0263\3\2\2\2\u0262\u0232\3\2\2\2")
        buf.write("\u0262\u023e\3\2\2\2\u0262\u024a\3\2\2\2\u0262\u0256\3")
        buf.write("\2\2\2\u0263\u008e\3\2\2\2\u0264\u0266\5K&\2\u0265\u0267")
        buf.write("\5\u008dG\2\u0266\u0265\3\2\2\2\u0266\u0267\3\2\2\2\u0267")
        buf.write("\u026d\3\2\2\2\u0268\u0269\5E#\2\u0269\u026a\5\u008dG")
        buf.write("\2\u026a\u026c\3\2\2\2\u026b\u0268\3\2\2\2\u026c\u026f")
        buf.write("\3\2\2\2\u026d\u026b\3\2\2\2\u026d\u026e\3\2\2\2\u026e")
        buf.write("\u0270\3\2\2\2\u026f\u026d\3\2\2\2\u0270\u0271\5M\'\2")
        buf.write("\u0271\u0277\3\2\2\2\u0272\u0273\5K&\2\u0273\u0274\5\u008f")
        buf.write("H\2\u0274\u0275\5M\'\2\u0275\u0277\3\2\2\2\u0276\u0264")
        buf.write("\3\2\2\2\u0276\u0272\3\2\2\2\u0277\u0090\3\2\2\2\u0278")
        buf.write("\u027c\7$\2\2\u0279\u027b\5\u00b7\\\2\u027a\u0279\3\2")
        buf.write("\2\2\u027b\u027e\3\2\2\2\u027c\u027a\3\2\2\2\u027c\u027d")
        buf.write("\3\2\2\2\u027d\u027f\3\2\2\2\u027e\u027c\3\2\2\2\u027f")
        buf.write("\u0280\7$\2\2\u0280\u0281\bI\2\2\u0281\u0092\3\2\2\2\u0282")
        buf.write("\u0285\5? \2\u0283\u0285\5A!\2\u0284\u0282\3\2\2\2\u0284")
        buf.write("\u0283\3\2\2\2\u0285\u0094\3\2\2\2\u0286\u0288\5\u00a7")
        buf.write("T\2\u0287\u0286\3\2\2\2\u0288\u0289\3\2\2\2\u0289\u0287")
        buf.write("\3\2\2\2\u0289\u028a\3\2\2\2\u028a\u0292\3\2\2\2\u028b")
        buf.write("\u028d\7\60\2\2\u028c\u028e\5\u00a7T\2\u028d\u028c\3\2")
        buf.write("\2\2\u028e\u028f\3\2\2\2\u028f\u028d\3\2\2\2\u028f\u0290")
        buf.write("\3\2\2\2\u0290\u0293\3\2\2\2\u0291\u0293\7\60\2\2\u0292")
        buf.write("\u028b\3\2\2\2\u0292\u0291\3\2\2\2\u0292\u0293\3\2\2\2")
        buf.write("\u0293\u029d\3\2\2\2\u0294\u0296\t\2\2\2\u0295\u0297\5")
        buf.write("\u00a9U\2\u0296\u0295\3\2\2\2\u0296\u0297\3\2\2\2\u0297")
        buf.write("\u0299\3\2\2\2\u0298\u029a\5\u00a7T\2\u0299\u0298\3\2")
        buf.write("\2\2\u029a\u029b\3\2\2\2\u029b\u0299\3\2\2\2\u029b\u029c")
        buf.write("\3\2\2\2\u029c\u029e\3\2\2\2\u029d\u0294\3\2\2\2\u029d")
        buf.write("\u029e\3\2\2\2\u029e\u0096\3\2\2\2\u029f\u02a8\7\62\2")
        buf.write("\2\u02a0\u02a4\t\3\2\2\u02a1\u02a3\5\u00a7T\2\u02a2\u02a1")
        buf.write("\3\2\2\2\u02a3\u02a6\3\2\2\2\u02a4\u02a2\3\2\2\2\u02a4")
        buf.write("\u02a5\3\2\2\2\u02a5\u02a8\3\2\2\2\u02a6\u02a4\3\2\2\2")
        buf.write("\u02a7\u029f\3\2\2\2\u02a7\u02a0\3\2\2\2\u02a8\u0098\3")
        buf.write("\2\2\2\u02a9\u02aa\7\62\2\2\u02aa\u02ac\t\4\2\2\u02ab")
        buf.write("\u02ad\t\5\2\2\u02ac\u02ab\3\2\2\2\u02ad\u02ae\3\2\2\2")
        buf.write("\u02ae\u02ac\3\2\2\2\u02ae\u02af\3\2\2\2\u02af\u009a\3")
        buf.write("\2\2\2\u02b0\u02b1\7\62\2\2\u02b1\u02b3\t\6\2\2\u02b2")
        buf.write("\u02b4\t\7\2\2\u02b3\u02b2\3\2\2\2\u02b4\u02b5\3\2\2\2")
        buf.write("\u02b5\u02b3\3\2\2\2\u02b5\u02b6\3\2\2\2\u02b6\u009c\3")
        buf.write("\2\2\2\u02b7\u02bb\5\u0097L\2\u02b8\u02bb\5\u0099M\2\u02b9")
        buf.write("\u02bb\5\u009bN\2\u02ba\u02b7\3\2\2\2\u02ba\u02b8\3\2")
        buf.write("\2\2\u02ba\u02b9\3\2\2\2\u02bb\u009e\3\2\2\2\u02bc\u02bd")
        buf.write("\t\b\2\2\u02bd\u00a0\3\2\2\2\u02be\u02bf\t\t\2\2\u02bf")
        buf.write("\u00a2\3\2\2\2\u02c0\u02c1\t\n\2\2\u02c1\u00a4\3\2\2\2")
        buf.write("\u02c2\u02c3\7a\2\2\u02c3\u00a6\3\2\2\2\u02c4\u02c5\t")
        buf.write("\13\2\2\u02c5\u00a8\3\2\2\2\u02c6\u02c7\t\f\2\2\u02c7")
        buf.write("\u00aa\3\2\2\2\u02c8\u02cc\t\b\2\2\u02c9\u02cb\t\r\2\2")
        buf.write("\u02ca\u02c9\3\2\2\2\u02cb\u02ce\3\2\2\2\u02cc\u02ca\3")
        buf.write("\2\2\2\u02cc\u02cd\3\2\2\2\u02cd\u00ac\3\2\2\2\u02ce\u02cc")
        buf.write("\3\2\2\2\u02cf\u02d0\7,\2\2\u02d0\u02d1\7,\2\2\u02d1\u02d9")
        buf.write("\3\2\2\2\u02d2\u02d4\13\2\2\2\u02d3\u02d2\3\2\2\2\u02d4")
        buf.write("\u02d7\3\2\2\2\u02d5\u02d6\3\2\2\2\u02d5\u02d3\3\2\2\2")
        buf.write("\u02d6\u02da\3\2\2\2\u02d7\u02d5\3\2\2\2\u02d8\u02da\7")
        buf.write(",\2\2\u02d9\u02d5\3\2\2\2\u02d9\u02d8\3\2\2\2\u02da\u02db")
        buf.write("\3\2\2\2\u02db\u02dc\7,\2\2\u02dc\u02dd\7,\2\2\u02dd\u02de")
        buf.write("\3\2\2\2\u02de\u02df\bW\3\2\u02df\u00ae\3\2\2\2\u02e0")
        buf.write("\u02e1\7,\2\2\u02e1\u02e2\7,\2\2\u02e2\u02e6\3\2\2\2\u02e3")
        buf.write("\u02e5\13\2\2\2\u02e4\u02e3\3\2\2\2\u02e5\u02e8\3\2\2")
        buf.write("\2\u02e6\u02e7\3\2\2\2\u02e6\u02e4\3\2\2\2\u02e7\u02e9")
        buf.write("\3\2\2\2\u02e8\u02e6\3\2\2\2\u02e9\u02ea\7,\2\2\u02ea")
        buf.write("\u02eb\7,\2\2\u02eb\u02ec\3\2\2\2\u02ec\u02ed\bX\3\2\u02ed")
        buf.write("\u00b0\3\2\2\2\u02ee\u02f0\t\16\2\2\u02ef\u02ee\3\2\2")
        buf.write("\2\u02f0\u02f1\3\2\2\2\u02f1\u02ef\3\2\2\2\u02f1\u02f2")
        buf.write("\3\2\2\2\u02f2\u02f3\3\2\2\2\u02f3\u02f4\bY\3\2\u02f4")
        buf.write("\u00b2\3\2\2\2\u02f5\u02f9\7$\2\2\u02f6\u02f8\5\u00b7")
        buf.write("\\\2\u02f7\u02f6\3\2\2\2\u02f8\u02fb\3\2\2\2\u02f9\u02f7")
        buf.write("\3\2\2\2\u02f9\u02fa\3\2\2\2\u02fa\u02fd\3\2\2\2\u02fb")
        buf.write("\u02f9\3\2\2\2\u02fc\u02fe\t\17\2\2\u02fd\u02fc\3\2\2")
        buf.write("\2\u02fe\u02ff\3\2\2\2\u02ff\u0300\bZ\4\2\u0300\u00b4")
        buf.write("\3\2\2\2\u0301\u0305\7$\2\2\u0302\u0304\5\u00b7\\\2\u0303")
        buf.write("\u0302\3\2\2\2\u0304\u0307\3\2\2\2\u0305\u0303\3\2\2\2")
        buf.write("\u0305\u0306\3\2\2\2\u0306\u0308\3\2\2\2\u0307\u0305\3")
        buf.write("\2\2\2\u0308\u0309\5\u00bb^\2\u0309\u030a\b[\5\2\u030a")
        buf.write("\u00b6\3\2\2\2\u030b\u030e\n\20\2\2\u030c\u030e\5\u00b9")
        buf.write("]\2\u030d\u030b\3\2\2\2\u030d\u030c\3\2\2\2\u030e\u00b8")
        buf.write("\3\2\2\2\u030f\u0310\7^\2\2\u0310\u0316\t\21\2\2\u0311")
        buf.write("\u0312\t\22\2\2\u0312\u0316\t\23\2\2\u0313\u0314\t\24")
        buf.write("\2\2\u0314\u0316\t\22\2\2\u0315\u030f\3\2\2\2\u0315\u0311")
        buf.write("\3\2\2\2\u0315\u0313\3\2\2\2\u0316\u00ba\3\2\2\2\u0317")
        buf.write("\u0318\7^\2\2\u0318\u031b\n\25\2\2\u0319\u031b\n\24\2")
        buf.write("\2\u031a\u0317\3\2\2\2\u031a\u0319\3\2\2\2\u031b\u00bc")
        buf.write("\3\2\2\2\u031c\u031d\13\2\2\2\u031d\u031e\b_\6\2\u031e")
        buf.write("\u00be\3\2\2\2\u031f\u0320\7,\2\2\u0320\u0321\7,\2\2\u0321")
        buf.write("\u0323\3\2\2\2\u0322\u0324\n\26\2\2\u0323\u0322\3\2\2")
        buf.write("\2\u0323\u0324\3\2\2\2\u0324\u0325\3\2\2\2\u0325\u0326")
        buf.write("\b`\7\2\u0326\u00c0\3\2\2\2&\2\u0230\u0239\u0245\u0251")
        buf.write("\u025d\u0262\u0266\u026d\u0276\u027c\u0284\u0289\u028f")
        buf.write("\u0292\u0296\u029b\u029d\u02a4\u02a7\u02ac\u02ae\u02b5")
        buf.write("\u02ba\u02cc\u02d5\u02d9\u02e6\u02f1\u02f9\u02fd\u0305")
        buf.write("\u030d\u0315\u031a\u0323\b\3I\2\b\2\2\3Z\3\3[\4\3_\5\3")
        buf.write("`\6")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    BODY = 13
    BREAK = 14
    CONTINUE = 15
    DO = 16
    ELSE = 17
    ELSEIF = 18
    ENDBODY = 19
    ENDIF = 20
    ENDFOR = 21
    ENDWHILE = 22
    FOR = 23
    FUNCTION = 24
    IF = 25
    PARAMETER = 26
    RETURN = 27
    THEN = 28
    VAR = 29
    WHILE = 30
    TRUE = 31
    FALSE = 32
    ENDDO = 33
    CM = 34
    LP = 35
    RP = 36
    LB = 37
    RB = 38
    LSB = 39
    RSB = 40
    SM = 41
    COLON = 42
    DOT = 43
    ADD = 44
    SUB = 45
    MUL = 46
    DIV = 47
    MOD = 48
    MOD2 = 49
    NOT = 50
    AND = 51
    OR = 52
    ADDPOINT = 53
    SUBPOINT = 54
    MULPOINT = 55
    DIVPOINT = 56
    LTE = 57
    GTE = 58
    LT = 59
    GT = 60
    LTEPOINT = 61
    GTEPOINT = 62
    LTPOINT = 63
    GTPOINT = 64
    NEQPOINT = 65
    NEQ = 66
    EQ = 67
    ASSIGN = 68
    ARRAYLIT = 69
    ARRAY1DLIT = 70
    ARRAYNDLIT = 71
    STRINGLIT = 72
    BOOLINT = 73
    REAL = 74
    DECIMAL = 75
    HEXADECIMAL = 76
    OCTAL = 77
    INTLIT = 78
    ID = 79
    BLOCK_COMMENT = 80
    LINE_COMMENT = 81
    WS = 82
    UNCLOSE_STRING = 83
    ILLEGAL_ESCAPE = 84
    ERROR_CHAR = 85
    UNTERMINATED_COMMENT = 86

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int_of_float'", "'float_of_int'", "'int_of_string'", "'string_of_int'", 
            "'float_of_string'", "'string_of_float'", "'bool_of_string'", 
            "'string_of_bool'", "'printLn'", "'print'", "'printStrLn'", 
            "'read'", "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
            "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", 
            "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", "'Then'", 
            "'Var'", "'While'", "'True'", "'False'", "'EndDo'", "','", "'('", 
            "')'", "'{'", "'}'", "'['", "']'", "';'", "':'", "'.'", "'+'", 
            "'-'", "'*'", "'\\'", "'%'", "'\\%'", "'!'", "'&&'", "'||'", 
            "'+.'", "'-.'", "'*.'", "'\\.'", "'<='", "'>='", "'<'", "'>'", 
            "'<=.'", "'>=.'", "'<.'", "'>.'", "'=/='", "'!='", "'=='", "'='" ]

    symbolicNames = [ "<INVALID>",
            "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
            "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
            "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", 
            "CM", "LP", "RP", "LB", "RB", "LSB", "RSB", "SM", "COLON", "DOT", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "MOD2", "NOT", "AND", "OR", 
            "ADDPOINT", "SUBPOINT", "MULPOINT", "DIVPOINT", "LTE", "GTE", 
            "LT", "GT", "LTEPOINT", "GTEPOINT", "LTPOINT", "GTPOINT", "NEQPOINT", 
            "NEQ", "EQ", "ASSIGN", "ARRAYLIT", "ARRAY1DLIT", "ARRAYNDLIT", 
            "STRINGLIT", "BOOLINT", "REAL", "DECIMAL", "HEXADECIMAL", "OCTAL", 
            "INTLIT", "ID", "BLOCK_COMMENT", "LINE_COMMENT", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "BODY", "BREAK", 
                  "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", 
                  "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                  "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", 
                  "CM", "LP", "RP", "LB", "RB", "LSB", "RSB", "SM", "COLON", 
                  "DOT", "ADD", "SUB", "MUL", "DIV", "MOD", "MOD2", "NOT", 
                  "AND", "OR", "ADDPOINT", "SUBPOINT", "MULPOINT", "DIVPOINT", 
                  "LTE", "GTE", "LT", "GT", "LTEPOINT", "GTEPOINT", "LTPOINT", 
                  "GTPOINT", "NEQPOINT", "NEQ", "EQ", "ASSIGN", "ARRAYLIT", 
                  "ARRAY1DLIT", "ARRAYNDLIT", "STRINGLIT", "BOOLINT", "REAL", 
                  "DECIMAL", "HEXADECIMAL", "OCTAL", "INTLIT", "LOWER", 
                  "UPPER", "LETTER", "UNDERSCORES", "DIGIT", "SIGN", "ID", 
                  "BLOCK_COMMENT", "LINE_COMMENT", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "CHAR", "ESC_SEQ", "ESC_ILLEGAL", "ERROR_CHAR", 
                  "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[71] = self.STRINGLIT_action 
            actions[88] = self.UNCLOSE_STRING_action 
            actions[89] = self.ILLEGAL_ESCAPE_action 
            actions[93] = self.ERROR_CHAR_action 
            actions[94] = self.UNTERMINATED_COMMENT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    y = str(self.text)
                    self.text = y[1:-1]
                
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    y = str(self.text)
                    possible = ['\b', '\t', '\n', '\f', '\r', '"', '\'', '\\']
                    if y[-1] in possible:
                        raise UncloseString(y[1:-1])
                    else:
                        raise UncloseString(y[1:])
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    y = str(self.text)
                    raise IllegalEscape(y[1:])
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                    raise ErrorToken(self.text)
                
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                    y = str(self.text)
                    raise UnterminatedComment()
                
     


