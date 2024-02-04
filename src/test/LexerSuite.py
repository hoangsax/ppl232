import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_001(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
        
    def test_002(self):
        self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))
        
    def test_003(self):
        self.assertTrue(TestLexer.test("aAsVN3","aAsVN3,<EOF>",103))
        
    def test_004(self):
        """test integers"""
        self.assertTrue(TestLexer.test("123a123","123,a123,<EOF>",104))
        
    def test_005(self):
        """test identifiers:01"""
        self.assertTrue(TestLexer.test("__init___","__init___,<EOF>",105))
        
    def test_006(self):
        """test identifiers:02"""
        self.assertTrue(TestLexer.test("__init2___","__init2___,<EOF>",106))
        
    def test_007(self):
        """test float num:01"""
        self.assertTrue(TestLexer.test("0.1","0.1,<EOF>",107))
        
    def test_008(self):
        """test float num:02"""
        self.assertTrue(TestLexer.test("1_2E+10","1,_2E,+,10,<EOF>",108))
        
    def test_009(self):
        """test float num:03"""
        self.assertTrue(TestLexer.test("Return x;","Return,x,Error Token ;",109))
        
    def test_010(self):
        self.assertTrue(TestLexer.test("Int main() {};","Int,main,(,),{,},Error Token ;",110))
        
    def test_011(self):
        self.assertTrue(TestLexer.test("Int main () {putintLn(4);}","Int,main,(,),{,putintLn,(,4,),Error Token ;",111))
        
    def test_012(self):
        """test float num:02"""
        self.assertTrue(TestLexer.test("12_3","12,_3,<EOF>",112))
        
    def test_013(self):
        """test float num:02"""
        self.assertTrue(TestLexer.test("main","main,<EOF>",113))
        
    def test_014(self):
        self.assertTrue(TestLexer.test(""" "abc def  """, "Unclosed String: abc def  ",114))
        
    def test_015(self):
        self.assertTrue(TestLexer.test("ab?svn", "ab,Error Token ?", 115))
        
    def test_016(self):
        self.assertTrue(TestLexer.test(""" "abc\\h def"  """, "Illegal Escape In String: abc\h", 116))
        
    def test_017(self):
        self.assertTrue(TestLexer.test(""" "1.0"  """, "1.0,<EOF>", 117))
        
    def test_018(self):
        self.assertTrue(TestLexer.test(""" "abc\\n ytf"  """, "abc\\n ytf,<EOF>", 118))
        
    def test_019(self):
        self.assertTrue(TestLexer.test("0_1234", "0,_1234,<EOF>", 119))
        
    def test_020(self):
        self.assertTrue(TestLexer.test("1_234E+10", "1,_234E,+,10,<EOF>", 120))
        
    def test_021(self):
        self.assertTrue(TestLexer.test("0.2e-1_34", "0.2e-1,_34,<EOF>", 121))
        
    def test_022(self):
        self.assertTrue(TestLexer.test("0b1001", "0,b1001,<EOF>", 122))
        
    def test_023(self):
        self.assertTrue(TestLexer.test("0x10_AF", "0,x10_AF,<EOF>", 123))
        
    def test_024(self):
        self.assertTrue(TestLexer.test("0X10_ABFe", "0,X10_ABFe,<EOF>", 124))
        
    def test_025(self):
        self.assertTrue(TestLexer.test("10e-20", "10e-20,<EOF>", 125))
    
    def test_026(self):
        self.assertTrue(TestLexer.test("01237", "01237,<EOF>", 126))
        
    def test_027(self):
        self.assertTrue(TestLexer.test("01238", "01238,<EOF>", 127))
    
    def test_028(self):
        self.assertTrue(TestLexer.test(""" "This is a string with \\n" """, "This is a string with \\n,<EOF>", 128))
        
    def test_029(self):
        self.assertTrue(TestLexer.test(""" "main foo()" """, "main foo(),<EOF>", 129))
        
    def test_030(self):
        self.assertTrue(TestLexer.test("self","self,<EOF>",130))
        
    def test_031(self):
        self.assertTrue(TestLexer.test("\"self\" + 3","self,+,3,<EOF>",131))
        
    def test_032(self):
        self.assertTrue(TestLexer.test(""" "yasuo ""","Unclosed String: yasuo ",132))
        
    def test_033(self):
        self.assertTrue(TestLexer.test("1.23-10","1.23,-,10,<EOF>",133))
        
    def test_034(self):
        self.assertTrue(TestLexer.test("1.e-10","1.e-10,<EOF>",134))
        
    def test_035(self):
        self.assertTrue(TestLexer.test("0.e-0.1","0.e-0,Error Token .",135))
        
    def test_036(self):
        self.assertTrue(TestLexer.test("_","_,<EOF>",136))
        
    def test_037(self):
        self.assertTrue(TestLexer.test("1_34_6.12","1,_34_6,Error Token .",137))
        
    def test_038(self):
        self.assertTrue(TestLexer.test(""" "Tim ve qua khu co xoa di \\n doan tinh trong mo" ""","Tim ve qua khu co xoa di \\n doan tinh trong mo,<EOF>",138))
        
    def test_039(self):
        self.assertTrue(TestLexer.test("Return x = 1_0.2 + 5;","Return,x,=,1,_0,Error Token .",139))
        
    def test_040(self):
        self.assertTrue(TestLexer.test("$foo(x, y);","Error Token $",140))
        
    def test_041(self):
        self.assertTrue(TestLexer.test("$ _123gg__","Error Token $",141))
        
    def test_042(self):
        self.assertTrue(TestLexer.test("$_123gg__","Error Token $",142))
        
    def test_043(self):
        self.assertTrue(TestLexer.test("!abc","Error Token !",143))
        
    def test_044(self):
        self.assertTrue(TestLexer.test(""" "he said \'\"Hello!\'\"" """, "he said \'\"Hello!\'\",<EOF>",144))
        
    def test_045(self):
        self.assertTrue(TestLexer.test(""" "Error Token ?" ""","Error Token ?,<EOF>", 145))
        
    def test_046(self):
        self.assertTrue(TestLexer.test(""" "break" """, "break,<EOF>", 146))
        
    def test_047(self):
        self.assertTrue(TestLexer.test(""" "Random quotes on Youtube" """, "Random quotes on Youtube,<EOF>", 147))
        
    def test_048(self):
        self.assertTrue(TestLexer.test("""  "\'\"Are you OK?\'\" \'\"Yesn't\'\""  """, "\'\"Are you OK?\'\" \'\"Yesn\'t\'\",<EOF>", 148))
        
    def test_049(self):
        self.assertTrue(TestLexer.test("12 * 100 - (50/2)", "12,*,100,-,(,50,/,2,),<EOF>", 149))
        
    def test_050(self):
        self.assertTrue(TestLexer.test("1234E+10 + 1.e-32", "1234E+10,+,1.e-32,<EOF>", 150))
        
    def test_051(self):
        self.assertTrue(TestLexer.test("(0.2e-1_34/15)+(3%2)", "(,0.2e-1,_34,/,15,),+,(,3,%,2,),<EOF>", 151))
        
    def test_052(self):
        self.assertTrue(TestLexer.test("1001 + 13FD0E", "1001,+,13,FD0E,<EOF>", 152))
        
    def test_053(self):
        self.assertTrue(TestLexer.test(""" "Error Token a" """, "Error Token a,<EOF>", 153))
        
    def test_054(self):
        self.assertTrue(TestLexer.test("0X10_ABFe", "0,X10_ABFe,<EOF>", 154))
        
    def test_055(self):
        self.assertTrue(TestLexer.test(""" "Yodayo! """, "Unclosed String: Yodayo! ", 155))
    
    def test_056(self):
        self.assertTrue(TestLexer.test(""" "Emotional Damage!" """, "Emotional Damage!,<EOF>", 156))
        
    def test_057(self):
        self.assertTrue(TestLexer.test("'123'", "Error Token '", 157))
    
    def test_058(self):
        self.assertTrue(TestLexer.test("for(Int i = 1?)", "for,(,Int,i,=,1,Error Token ?", 158))
        
    def test_059(self):
        self.assertTrue(TestLexer.test(""" "Don't forget to put your quote symbol after finishing a string""", "Unclosed String: Don't forget to put your quote symbol after finishing a string", 159))
        
    def test_060(self):
        self.assertTrue(TestLexer.test(""" "Here we go another string with \\a" """, "Illegal Escape In String: Here we go another string with \\a", 160))
        
    def test_061(self):
        self.assertTrue(TestLexer.test("abcEFG?","abcEFG,Error Token ?",161))
        
    def test_062(self):
        self.assertTrue(TestLexer.test(""" "EOF" ""","EOF,<EOF>",162))
        
    def test_063(self):
        self.assertTrue(TestLexer.test("ab_123.23","ab_123,Error Token .",163))
        
    def test_064(self):
        self.assertTrue(TestLexer.test("_._","_,Error Token .",164))
        
    def test_065(self):
        self.assertTrue(TestLexer.test(""" "This is an identifier: "myID""","This is an identifier: ,myID,<EOF>",165))
        
    def test_066(self):
        self.assertTrue(TestLexer.test("12'33","12,Error Token '",166))
        
    def test_067(self):
        self.assertTrue(TestLexer.test("0.000001","0.000001,<EOF>",167))
        
    def test_068(self):
        self.assertTrue(TestLexer.test("1_2E+/2","1,_2E,+,/,2,<EOF>",168))
        
    def test_069(self):
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 169))
        
    def test_070(self):
        self.assertTrue(TestLexer.test("abcd", "abcd,<EOF>", 170))
        
    def test_071(self):
        self.assertTrue(TestLexer.test("ab_cd", "ab_cd,<EOF>", 171))
        
    def test_072(self):
        self.assertTrue(TestLexer.test("abd1", "abd1,<EOF>", 172))
        
    def test_073(self):
        self.assertTrue(TestLexer.test("\"aa\"", "aa,<EOF>", 173))
        
    def test_074(self):
        self.assertTrue(TestLexer.test("\"aa", "Unclosed String: aa", 174))
        
    def test_075(self):
        self.assertTrue(TestLexer.test("\"He said: \'\"OK!\'\"\"", "He said: \'\"OK!\'\",<EOF>", 175))
        
    def test_076(self):
        self.assertTrue(TestLexer.test("123", "123,<EOF>", 176))
        
    def test_077(self):
        self.assertTrue(TestLexer.test("1_2.33", "1,_2,Error Token .", 177))
        
    def test_078(self):
        self.assertTrue(TestLexer.test("123_4", "123,_4,<EOF>", 178))
        
    def test_079(self):
        self.assertTrue(TestLexer.test("0.12e3", "0.12e3,<EOF>", 179))
        
    def test_080(self):
        self.assertTrue(TestLexer.test(" \"Thuong cho tam than co han\" ", "Thuong cho tam than co han,<EOF>", 180))
    
    def test_081(self):
        self.assertTrue(TestLexer.test("\"Gomen Yui\\t\"", "Gomen Yui\\t,<EOF>", 181))
        
    def test_082(self):
        self.assertTrue(TestLexer.test("12/x + 30/y = 5", "12,/,x,+,30,/,y,=,5,<EOF>", 182))
        
    def test_083(self):
        self.assertTrue(TestLexer.test("1e-13.2", "1e-13,Error Token .", 183))
        
    def test_084(self):
        self.assertTrue(TestLexer.test("_in_+3", "_in_,+,3,<EOF>", 184))
        
    def test_085(self):
        self.assertTrue(TestLexer.test("1e?13.2", "1e,Error Token ?", 185))
        
    def test_086(self):
        self.assertTrue(TestLexer.test("\"Unclosed String: aa\"", "Unclosed String: aa,<EOF>", 186))
        
    def test_087(self):
        self.assertTrue(TestLexer.test("\"123 + 5 = 9\"", "123 + 5 = 9,<EOF>", 187))
        
        
    def test_088(self):
        self.assertTrue(TestLexer.test("1/2", "1,/,2,<EOF>", 188))
        
        
    def test_089(self):
        self.assertTrue(TestLexer.test("\"123 + 5 = 009\"", "123 + 5 = 009,<EOF>", 189))
        
    def test_090(self):
        self.assertTrue(TestLexer.test("?323", "Error Token ?", 190))

    def test_091(self):
        self.assertTrue(TestLexer.test("\"Em oi dung khoc\"", "Em oi dung khoc,<EOF>", 191))

    def test_092(self):
        self.assertTrue(TestLexer.test("\"Bong toi truoc mat \\t\"", "Bong toi truoc mat \\t,<EOF>", 192))

    def test_093(self):
        self.assertTrue(TestLexer.test("\"Se bat em di\"", "Se bat em di,<EOF>", 193))

    def test_094(self):
        self.assertTrue(TestLexer.test("\t", "<EOF>", 194))

    def test_095(self):
        self.assertTrue(TestLexer.test(""" "Hmu hmu" """, "Hmu hmu,<EOF>", 195))
        
    def test_096(self):
        self.assertTrue(TestLexer.test("\"Hmu hmu ", "Unclosed String: Hmu hmu ", 196))
        
    def test_097(self):
        self.assertTrue(TestLexer.test("a = \"hmu hmu\"", "a,=,hmu hmu,<EOF>", 197))
        
    def test_098(self):
        self.assertTrue(TestLexer.test("\"hmu hmu\" + \"ha ha\"", "hmu hmu,+,ha ha,<EOF>", 198))
        
    def test_099(self):
        self.assertTrue(TestLexer.test("\"We are almost here\"", "We are almost here,<EOF>", 199))
        
    def test_100(self):
        self.assertTrue(TestLexer.test("\"Done!\"", "Done!,<EOF>", 200))
