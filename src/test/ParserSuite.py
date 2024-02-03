import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_101(self):
        input = """func main ()
        return 1"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_102(self):
        input = """func main()
        begin
            putIntLn(4)
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    
    def test_103(self):
        input = """func main()
        begin
            return 42
        end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
        
    def test_104(self):
        input = """func factorial(number n) 
begin
    if (n <= 1 )
        begin
            return 1
        end 
    else 
        begin
            n * factorial(n - 1)
        end
end
func main() return 1"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
        
    def test_105(self):
        input = """func main()
        begin
            string y <- "string"
            foo(x)
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
        
    def test_106(self):
        input = """var x <- foo(3)
        func main()
        begin
            return x
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
        
    def test_107(self):
        input = """main()
        begin
                foo()
        end
        """
        expect = "Error on line 3 col 8: }"
        self.assertTrue(TestParser.test(input,expect,207))
        
    def test_108(self):
        input = """func main()
        begin
            var x = 2
        end
        """
        expect = "Error on line 4 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,208))
    
    def test_109(self):
        input = """func main()
        begin
            var x
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))
        
    def test_110(self):
        input = """func main()
        begin
            bool x
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))
        
    def test_111(self):
        input = """func main()
        begin
            var a <- 10
            if (a > 2) a = a - 1
            return a
        end"""
        expect = "Error on line 4 col 12: }"
        self.assertTrue(TestParser.test(input,expect,211))
        
    def test_112(self):
        input = """func foo(n)
        func main()
        begin
            return 1
        end
        """
        expect = "Error on line 1 col 20: x"
        self.assertTrue(TestParser.test(input,expect,212))
        
    def test_113(self):
        input = """func rando(string x, number y)
        begin
            x[y] <- "a"
        end
    func main()
        begin
            return foo("bbcde", 0)
        end
"""
        expect = "Error on line 5 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,213))
        
    def test_114(self):
        input = """func main()
        begin
            var x <- y[0] * foo(5) / (foo(2) + 10)
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
        
        
    def test_115(self):
        input = """main: function void(){
            for (i = 1, i <= 10, i + 1){
                x = 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))
        
    def test_116(self):
        input = """main: function void(){
            do{
                x = x + 1;
            } while (x < 10)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))
        
    def test_117(self):
        input = """main: function void(){
            do{
                x = x + 1;
            } while (x)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
        
    def test_118(self):
        input = """main: function void(){
            do{
                x = x + 1;
            } while (!x)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
        
    def test_119(self):
        input = """main: function void(){
            do{
                x = x + 1
            } while (x)
        }
        """
        expect = "Error on line 4 col 12: }"
        self.assertTrue(TestParser.test(input,expect,219))
        
    def test_120(self):
        input = """main: function void(){
            do{
                x = x + 1;
            } whiles (x)
        }
        """
        expect = "Error on line 4 col 14: whiles"
        self.assertTrue(TestParser.test(input,expect,220))

    def test_121(self):
        input = """main: function void(){}
        abcd:function (x:integer){
        }
        
        """
        expect = "Error on line 2 col 22: ("
        self.assertTrue(TestParser.test(input,expect,221))

    def test_122(self):
        input = """main: function void(){
            if (x <= b){
                x = x - b;
            }
            else{
                x = x + b;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
        
    def test_123(self):
        input = """main: function void(){
            if (x <= b){
                if (x < b){
                    x = x - b;
                }
                else{
                    x = x - b - 1;
                }
            }
            else{
                x = x + b;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))
        
    def test_124(self):
        input = """main: function void(){
            if (x <= b){
            }
            else{
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))
        
    def test_125(self):
        input = """main: function void(){
            while(x){
                break
            }
        }
        """
        expect = "Error on line 4 col 12: }"
        self.assertTrue(TestParser.test(input,expect,225))

    def test_126(self):
        input = """main: function void(){
            while(x){
                break
            }
        }
        """
        expect = "Error on line 4 col 12: }"
        self.assertTrue(TestParser.test(input,expect,226))

    def test_127(self):
        input = """main: function void(){}
        abcd:function float(out x,y){
            
        }
        """
        expect = "Error on line 2 col 33: ,"
        self.assertTrue(TestParser.test(input,expect,227))

    def test_128(self):
        input = """main: function void(){
            while(x){
                break;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))

    def test_129(self):
        input = """main: function void(){
            a: integer = 10 + 5/2;
            b = a;
            c = foo();
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))

    def test_130(self):
        input = """main: function void(){
            while(x){
                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))

    def test_131(self):
        input = """main: function void(){
            while(x){
                continue
            }
        }
        """
        expect = "Error on line 4 col 12: }"
        self.assertTrue(TestParser.test(input,expect,231))

    def test_132(self):
        input = """main: function void(){
            while(x){
                if (x == 2){
                    x = x - 2;
                }
                else{
                    x = 0;
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))

    def test_133(self):
        input = """main: function void(){
            while(x){
                if (x == 2){
                    x = x - 2;
                }
                else{
                    x == 0;
                }
            }
        }
        """
        expect = "Error on line 7 col 22: =="
        self.assertTrue(TestParser.test(input,expect,233))

    def test_134(self):
        input = """main: function void(){
            x = !y;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))

    def test_135(self):
        input = """main: function void(){
            x = y || z;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))

    def test_136(self):
        input = """main: function void(){
            x = y / z + 3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))

    def test_137(self):
        input = """main: function void(){
            x = y / z || 3;
        }
        """
        expect = "Error on line 2 col 22: ||"
        self.assertTrue(TestParser.test(input,expect,237))

    def test_138(self):
        input = """main: function void(){
            x = (y / z) || 3;
        }
        """
        expect = "Error on line 2 col 24: ||"
        self.assertTrue(TestParser.test(input,expect,238))

    def test_139(self):
        input = """main: function void(){
            x = (y / z) <= 3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))

    def test_140(self):
        input = """main: function void(){
            if (x || y){
            
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))

    def test_141(self):
        input = """main: function void(){
            if (x / y < 3){
            
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))

    def test_142(self):
        input = """main: function void(){
            if (2 < 3){
            
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))

    def test_143(self):
        input = """main: function void(){
            if (2 <= 3 <= 5){
            
            }
        }
        """
        expect = "Error on line 2 col 23: <="
        self.assertTrue(TestParser.test(input,expect,243))

    def test_144(self):
        input = """main: function void(){
            if (x || y || z){
            
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))

    def test_145(self):
        input = """main: function void(){
            if (x || y || z <= 3){
            
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))

    def test_146(self):
        input = """main: function void(){
            if (x || y && z){
            
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))

    def test_147(self):
        input = """main: function void(){
            if ((x || y) && z){
            
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))

    def test_148(self):
        input = """main: function void(){
            if (!(x || y) && z){
            
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))

    def test_149(self):
        input = """main: function void(){
            if (!3){
            
            }
        }
        """
        expect = "Error on line 2 col 17: 3"
        self.assertTrue(TestParser.test(input,expect,249))

    def test_149(self):
        input = """main: function void(){
            if (3 || 4){
            
            }
        }
        """
        expect = "Error on line 2 col 18: ||"
        self.assertTrue(TestParser.test(input,expect,249))

    def test_150(self):
        input = """main: function void(){
            if (3 < 2 || 4 < 5){
            
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))

    def test_151(self):
        input = """main: function void(){
            if (foo(2) <= 3){
            
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))

    def test_152(self):
        input = """main: function void(){
            if (foo(x, y, z) <= 3){
            
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))

    def test_153(self):
        input = """main: function void(){
            if (foo(x, y, z) == foo(a, b, c)){
            
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))

    def test_154(self):
        input = """main: function void(){
            if (x){
                x = foo(y) + 2;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))

    def test_155(self):
        input = """main: function void(){
            if (x){
                x = foo(y + 2;
            }
        }
        """
        expect = "Error on line 3 col 29: ;"
        self.assertTrue(TestParser.test(input,expect,255))

    def test_156(self):
        input = """main: function void(){
            if (x){
                x = foo(y + 2);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))

    def test_157(self):
        input = """main: function void(){
            if (x){
                x = fooy + 2);
            }
        }
        """
        expect = "Error on line 3 col 28: )"
        self.assertTrue(TestParser.test(input,expect,257))

    def test_158(self):
        input = """main: function void(){
            x = 3:2;
        }
        """
        expect = "Error on line 2 col 17: :"
        self.assertTrue(TestParser.test(input,expect,258))

    def test_159(self):
        input = """main: function void(){
            x:integer = foo(1);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))

    def test_160(self):
        input = """main: function void){
            x:integer = foo(1);
        }
        """
        expect = "Error on line 1 col 19: )"
        self.assertTrue(TestParser.test(input,expect,260))

    def test_161(self):
        input = """main: function void()){
            x:integer = foo(1);
        }
        """
        expect = "Error on line 1 col 21: )"
        self.assertTrue(TestParser.test(input,expect,261))

    def test_162(self):
        input = """main: function void(){
            x:boolean = TRUE;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))

    def test_163(self):
        input = """main: function void(){
            x:boolean = FALSE;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))

    def test_164(self):
        input = """main: function void(){
            x:string = "FALSE";
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))

    def test_165(self):
        input = """main: function void(){
            x:string = "FALSE" + " ";
        }
        """
        expect = "Error on line 2 col 31: +"
        self.assertTrue(TestParser.test(input,expect,265))

    def test_166(self):
        input = """main: function void(){
            x:string = "FALSE" :: "TRUE";
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))

    def test_167(self):
        input = """main: function void(){
            x:string = 2 :: "TRUE";
        }
        """
        expect = "Error on line 2 col 25: ::"
        self.assertTrue(TestParser.test(input,expect,267))

    def test_168(self):
        input = """main: function void(){
            x:string = 2 / "TRUE";
        }
        """
        expect = "Error on line 2 col 27: TRUE"
        self.assertTrue(TestParser.test(input,expect,268))

    def test_169(self):
        input = """main: function void(){
            x:string = 2 / "TRUE";
        }
        """
        expect = "Error on line 2 col 27: TRUE"
        self.assertTrue(TestParser.test(input,expect,269))

    def test_170(self):
        input = """main: function void(){
            x:string = 2 : "TRUE";
        }
        """
        expect = "Error on line 2 col 25: :"
        self.assertTrue(TestParser.test(input,expect,270))

    def test_171(self):
        input = """main: function void(){
            x:string = "He said: \\\"Are you ok?\\\"";
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))
        
    def test_172(self):
        input = """main: function void(){
            x:string = "He said: \\\"Are you ok?\\\""::"\\\"Yesn't\\\"";
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))

    def test_173(self):
        input = """main: function void(){
            x:string = "He said: \\\"Are you ok?\\\""::;
        }
        """
        expect = "Error on line 2 col 51: ;"
        self.assertTrue(TestParser.test(input,expect,273))

    def test_174(self):
        input = """main: function void(){
            x:float = 1_1.14;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))

    def test_175(self):
        input = """main: function void(){
            x:float = 11.14;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))

    def test_176(self):
        input = """main: function void(){
            x:float = 11E-3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))

    def test_177(self):
        input = """main: function void(){
            x:float = 11E-3 + 0.123;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))

    def test_178(self):
        input = """main: function void(){
            x:float = 11E-3 / 0.123;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))

    def test_179(self):
        input = """main: function void(){
            x:float = 11E-3 || 0.123;
        }
        """
        expect = "Error on line 2 col 28: ||"
        self.assertTrue(TestParser.test(input,expect,279))

    def test_180(self):
        input = """main: function void(){
            x:float = 11E-3 || 0.123;
        }
        """
        expect = "Error on line 2 col 28: ||"
        self.assertTrue(TestParser.test(input,expect,280))

    def test_181(self):
        input = """main: function void(){
            x:float = 11E-3 :: 0.123;
        }
        """
        expect = "Error on line 2 col 28: ::"
        self.assertTrue(TestParser.test(input,expect,281))

    def test_182(self):
        input = """main: function void(){
            x:float = 11E-3 / 100;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))

    def test_183(self):
        input = """main: function void(){
            x: array [4, 1] of integer;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))

    def test_184(self):
        input = """main: function void(){
            x: array [4, 1] of integer = {1, 2, 3, 4};
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))

    def test_185(self):
        input = """main: function void(){
            x: array [4, 1] of string = {"1", "2", "3", "4"};
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285))

    def test_186(self):
        input = """main: function void(){
            x: array [4, 1] of float = {1.1, 2.1, 3.1, 4.1};
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))

    def test_187(self):
        input = """main: function void(){
            x: array [4, 2] of float = {1.1, 2.1, 3.1, 4.1}, {1.2, 2.2, 3.2, 4.2};
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))

    def test_188(self):
        input = """main: function void(){
            x: array [4, 2] of void = {1.1, 2.1, 3.1, 4.1}, {1.2, 2.2, 3.2, 4.2};
        }
        """
        expect = "Error on line 2 col 31: void"
        self.assertTrue(TestParser.test(input,expect,288))

    def test_189(self):
        input = """main: function void(){
            x: array [4, 2] of float = {1.1, "2.1", 3.1, 4.1}, {1.2, 2.2, 3.2, 4.2};
        }
        """
        expect = "Error on line 2 col 45: 2.1"
        self.assertTrue(TestParser.test(input,expect,289))

    def test_190(self):
        input = """func main() return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))

    def test_191(self):
        input = """func main()
        begin
            va x <- 10
        end
        """
        expect = "Error on line 3 col 15: x"
        self.assertTrue(TestParser.test(input,expect,291))

    def test_192(self):
        input = """func main()
        begin
            va x <- 1
        end
        """
        expect = "Error on line 3 col 15: x"
        self.assertTrue(TestParser.test(input,expect,292))

    def test_193(self):
        input = """func main()
        begin
            var x[5] <- [0, 1, 2, 3,] 
        end
        """
        expect = "Error on line 3 col 36: ]"
        self.assertTrue(TestParser.test(input,expect,293))

    def test_194(self):
        input = """func main()
        begin
            var x[5] <- [0, 1, 2, 3, 4]
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))

    def test_195(self):
        input = """func main()
        begin
            return 0
        end
    func _foo()
        begin
            return 0
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))

    def test_196(self):
        input = """func main(){"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.test(input,expect,296))

    def test_197(self):
        input = """func foo1(string x, y)
        func main()
        begin
            return 0
        end
        """
        expect = "Error on line 1 col 20: y"
        self.assertTrue(TestParser.test(input,expect,297))

    def test_198(self):
        input = """func main()
        begin
            a[0, 1] <- 10
            var x <- 10
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,298))

    def test_199(self):
        input = """dynamic y <- x[a, b, 9]
        func main()
        begin
            return 1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))

    def test_200(self):
        input = """func main()
        begin
            a[0, 1] <- 10
            var x <- 10
            
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,300))