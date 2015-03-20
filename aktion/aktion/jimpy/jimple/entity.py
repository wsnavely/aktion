class JimpleClass:
    def __init__(self, mods, name, methods):
        self.modifiers = mods
        self.name = name
        self.methods = methods

    def __str__(self):
        result = ""
        result += \
                " ".join(self.modifiers) + " " + self.name + " {\n" \
            +   "".join([method.__str__(indent=1) + "\n\n" for method in self.methods]) \
            +   "}"
        return result
    
class JimpleMethod:
    def __init__(self, mods, name, rettype, params, stmts):
        self.modifiers = mods
        self.name = name
        self.return_type = rettype
        self.params = params
        self.stmts = stmts
    
    def __str__(self, indent=0):
        result = ""
        istr = "\t"*indent
        result += \
                istr + " ".join(self.modifiers) + " " + self.name \
            +   "(" + ",".join(self.params) + ")" + " {\n" \
            +   "".join([istr + "\t" + str(stmt) + "\n" for stmt in self.stmts]) \
            +   istr + "}"
        return result
    
class FieldSpecifier:
    def __init__(self, class_name, type_name, field_name):
        self.class_name = class_name
        self.type_name = type_name
        self.field_name = field_name
    
    def __str__(self):
        return self.type_name + " " + str(self.class_name) + "::" + self.field_name
    
class AssignStmt:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.left) + " = " + str(self.right) + ";" 

class IdentityStmt:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.left) + " := " + str(self.right) + ";" 

class GotoStmt:
    def __init__(self, lbl):
        self.label = lbl

    def __str__(self):
        return  "goto " + str(self.label) + ";" 

class BreakpointStmt:
    def __init__(self):
        pass

    def __str__(self):
        return  "breakpoint;" 
        
class InvokeStmt:
    def __init__(self, invoke_expr):
        self.invoke_expr = invoke_expr
    
    def __str__(self):
        return str(self.invoke_expr) + ";"

class ReturnStmt:
    def __init__(self, operand):
        self.operand = operand
    
    def __str__(self):
        if self.operand == None:
            return "return;"
        else:
            return "return " + str(self.operand) + ";"
    
class IfStmt:
    def __init__(self, cond, label):
        self.cond = cond
        self.label = label

    def __str__(self):
        return "if(" + str(self.cond) + ") goto " + str(self.label)
    
class SwitchStmt:
    def __init__(self):
        pass

    def __str__(self):
        return "SWITCH"

class EnterMonitorStmt:
    def __init__(self):
        pass
    
    def __str__(self):
        return "ENTER MONITOR"

class ExitMonitorStmt:
    def __init__(self):
        pass

class ThrowStmt:
    def __init__(self):
        pass

    def __str__(self):
        return "EXIT MONITOR"

class CatchStmt:
    def __init__(self):
        pass

    def __str__(self):
        return "CATCH"

class NopStmt:
    def __init__(self):
        pass

    def __str__(self):
        return "NOP"

class JimpleExpr:
    def __init__(self):
        pass

class Label:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name + ":"

class Local:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

class FieldRef:
    def __init__(self, local, field):
        self.local = local
        self.field = field
    
    def __str__(self):
        if self.local != None:
            return str(self.local) + "." + str(self.field.field_name)
        else:
            return str(self.field.class_name) + "." + str(self.field.field_name)
    
class InvokeExpr:
    def __init__(self, caller, class_name, return_type, method_name, args, is_static):
        self.caller = caller
        self.class_name = class_name
        self.return_type = return_type
        self.method_name = method_name
        self.args = args
        self.is_static = is_static
    
    def __str__(self):
        result = ""
        if self.caller != None:
            result += str(self.caller) + "."
        else:
            result += str(self.class_name) + "."
        arg_str = ",".join([str(a) for a in self.args])
        result += str(self.method_name) + "(" + arg_str + ")"
        return result

class ArrayRef:
    def __init__(self, local, index):
        self.local = local
        self.index = index
    
    def __str__(self):
        return str(self.local) + "[" + str(self.index) + "]"
        
class StrConst:
    def __init__(self, token):
        self.value = token
    
    def __str__(self):
        return '"' + self.value + '"'

class NumericConst:
    def __init__(self, token):
        token = token.strip("L").strip("F")
        if token == "#Infinity":
            self.value = float("Inf")
        elif token == "#-Infinity":
            self.value = float("-Inf")
        elif token == "#NaN":
            self.value = float("NaN")
        else:
            self.value = eval(token)

    def __str__(self):
        return str(self.value)

class NullConst:
    def __init__(self):
        self.value = None
    
    def __str__(self):
        return "null"

class ClassExpr:
    def __init__(self, class_name):
        self.class_name = class_name
    
    def __str__(self):
        return self.class_name + ".class"

class CondExpr:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
        
    def __str__(self):
        return str(self.left) + str(self.op) + str(self.right)
        
class BinopExpr:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        return str(self.left) + str(self.op) + str(self.right)

class CastExpr:
    def __init__(self, type_name, imm):
        self.type_name = type_name
        self.imm = imm
    
    def __str__(self):
        return "(" + str(self.type_name) + ")" + str(self.imm)
        
class InstanceofExpr:
    def __init__(self, type_name, imm):
        self.type_name = type_name
        self.imm = imm

    def __str__(self):
        return str(self.imm) + " instanceof " + str(self.type_name) 
    
class NewExpr:
    def __init__(self, type_name):
        self.type_name = type_name

    def __str__(self):
        return "new " + str(self.type_name) + "()" 

class NewArrayExpr:
    def __init__(self):
        pass
    
    def __str__(self):
        return "NEWARRAY"

class NewMultiarrayExpr:
    def __init__(self):
        pass

    def __str__(self):
        return "NEWMULTIARRAY"

class LengthofExpr:
    def __init__(self):
        pass
    
    def __str__(self):
        return "LENGTHOF"

class NegExpr:
    def __init__(self):
        pass

    def __str__(self):
        return "NEG"
    