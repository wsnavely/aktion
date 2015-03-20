from jimpy.jimple.baseparser import BaseParser
from jimpy.jimple.entity import *
import logging

class SimpleBodyParser(BaseParser):
    def __init__(self):
        self.expr_stack = []
        self.NULL = NullConst
        self.cur_method_body = []
        self.methods = []
        self.classes = []
        self.interfaces = []
        super(SimpleBodyParser, self).__init__()
    
    def expr_numeric_const_parse_action(self, s, loc, toks):
        self.expr_stack.append(NumericConst(toks[0]))
   
    def expr_str_const_parse_action(self, s, loc, toks):
        self.expr_stack.append(StrConst(toks[0]))
    
    def expr_null_parse_action(self, s, loc, toks):
        self.expr_stack.append(self.NULL)
     
    def expr_local_parse_action(self, s, loc, toks):
        self.expr_stack.append(Local(toks[0]))
    
    def expr_field_ref_parse_action(self, s, loc, toks):
        field = self.expr_stack.pop()
        local = None
        if len(toks[0]) != 0:
            local = self.expr_stack.pop()
        self.expr_stack.append(FieldRef(local, field))
        
    def expr_array_ref_parse_action(self, s, loc, toks):
        index = self.expr_stack.pop()
        local = self.expr_stack.pop()
        self.expr_stack.append(ArrayRef(local, index))
    
    def field_specifier_parse_action(self, s, loc, toks):
        self.expr_stack.append(FieldSpecifier(toks[0], toks[1], toks[2]))
 
    def expr_binop_parse_action(self, s, loc, toks):
        right = self.expr_stack.pop()
        left = self.expr_stack.pop()
        op = toks[1]
        self.expr_stack.append(BinopExpr(left, op, right))

    def expr_cast_parse_action(self, s, loc, toks):
        #print "[EXPR][CAST]: ", toks
        operand = self.expr_stack.pop()
        type_name = toks[0]
        self.expr_stack.append(CastExpr(type_name, operand))

    def expr_instanceof_parse_action(self, s, loc, toks):
        #operand = self.expr_stack.pop()
        self.expr_stack.append(InstanceofExpr("test", "test"))

    def expr_new_parse_action(self, s, loc, toks):
        self.expr_stack.append(NewExpr(toks[0]))
    
    def expr_newarray_parse_action(self, s, loc, toks):
        self.expr_stack.append(NewArrayExpr())

    def expr_lengthof_parse_action(self, s, loc, toks):
        self.expr_stack.append(LengthofExpr())

    def expr_neg_parse_action(self, s, loc, toks):
        self.expr_stack.append(NegExpr())

    def expr_newmultiarray_parse_action(self, s, loc, toks):
        self.expr_stack.append(NewMultiarrayExpr())

    def handle_invoke(self, toks):
        invoke_type = toks[0]
        invoke_arg_toks = []
        is_static = False
        if invoke_type == "staticinvoke":
            invoke_arg_toks = toks[5]
            is_static = True
        else:
            invoke_arg_toks = toks[6]
            
        argc = len(invoke_arg_toks)
        invoke_args = []
        for _ in xrange(argc):
            invoke_args.append(self.expr_stack.pop())
        invoke_args.reverse()
        
        caller = None
        if not is_static:
            caller = self.expr_stack.pop()
            class_name = toks[2]
            ret_type = toks[3]
            method_name = toks[4]
        else:
            class_name = toks[1]
            ret_type = toks[2]
            method_name = toks[3]
 
        return InvokeExpr(
                caller, 
                class_name, 
                ret_type, 
                method_name, 
                invoke_args, 
                is_static)
        
    def expr_invoke_parse_action(self, s, loc, toks):
        invoke = self.handle_invoke(toks)
        self.expr_stack.append(invoke)
            
    def expr_cond_parse_action(self, s, loc, toks):
        right = self.expr_stack.pop()
        left = self.expr_stack.pop()
        op = toks[1]
        self.expr_stack.append(CondExpr(left, op, right))

    def stmt_invoke_parse_action(self, s, loc, toks):
        invoke = self.expr_stack.pop()
        self.cur_method_body.append(InvokeStmt(invoke))
        pass
        
    def stmt_decl_parse_action(self, s, loc, toks):
        pass
    
    def stmt_assign_parse_action(self, s, loc, toks):
        expr = self.expr_stack.pop()
        dest = self.expr_stack.pop()
        self.cur_method_body.append(AssignStmt(dest, expr))
        
    def stmt_identity_parse_action(self, s, loc, toks):
        expr = self.expr_stack.pop()
        dest = self.expr_stack.pop()
        self.cur_method_body.append(IdentityStmt(dest, expr))
            
    def stmt_goto_parse_action(self, s, loc, toks):
        self.cur_method_body.append(GotoStmt(toks[0]))
        pass

    def stmt_if_parse_action(self, s, loc, toks):
        cond_expr = self.expr_stack.pop()
        label = toks[3]
        self.cur_method_body.append(IfStmt(cond_expr, label))
        
    def stmt_switch_parse_action(self, s, loc, toks):
        pass
    
    def stmt_enter_monitor_parse_action(self, s, loc, toks):
        self.cur_method_body.append(EnterMonitorStmt())    
    
    def stmt_exit_monitor_parse_action(self, s, loc, toks):
        self.cur_method_body.append(ExitMonitorStmt())    
    
    def stmt_return_parse_action(self, s, loc, toks):
        operand = None
        if len(toks) > 0:
            operand = self.expr_stack.pop()
        self.cur_method_body.append(ReturnStmt(operand))

    def stmt_throw_parse_action(self, s, loc, toks):
        self.cur_method_body.append(ThrowStmt())    

    def stmt_catch_parse_action(self, s, loc, toks):
        self.cur_method_body.append(CatchStmt())    
    
    def stmt_breakpoint_parse_action(self, s, loc, toks):
        self.cur_method_body.append(BreakpointStmt())    

    def stmt_nop_parse_action(self, s, loc, toks):
        self.cur_method_body.append(NopStmt())    
            
    def field_decl_parse_action(self, s, loc, toks):
        pass
    
    def class_defn_parse_action(self, s, loc, toks):
        toks = toks[0]
        jimple_class = JimpleClass(toks[0], toks[1] , self.methods)
        self.classes.append(jimple_class)
        
    def method_defn_parse_action(self, s, loc, toks):
        toks = toks[0]
        method = JimpleMethod(toks[0], toks[2], toks[1], toks[3], self.cur_method_body)
        self.methods.append(method)
        self.cur_method_body = []
        
    def stmt_parse_action(self, s, loc, toks):
        logging.info(str(toks))

    def label_parse_action(self, s, loc, toks):
        self.cur_method_body.append(Label(toks[0]))