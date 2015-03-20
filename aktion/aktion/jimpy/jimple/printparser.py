from jimpy.jimple.baseparser import BaseParser

class PrintParser(BaseParser):
    def expr_binop_parse_action(self, s, loc, toks):
        print "[EXPR][BINOP]: ", toks

    def expr_cast_parse_action(self, s, loc, toks):
        print "[EXPR][CAST]: ", toks

    def expr_instanceof_parse_action(self, s, loc, toks):
        print "[EXPR][INSTANCEOF]: ", toks
        
    def expr_invoke_parse_action(self, s, loc, toks):
        print "[EXPR][INVOKE]: ", toks

    def expr_new_parse_action(self, s, loc, toks):
        print "[EXPR][NEW]: ", toks
    
    def expr_newarray_parse_action(self, s, loc, toks):
        print "[EXPR][NEWARRAY]: ", toks

    def expr_lengthof_parse_action(self, s, loc, toks):
        print "[EXPR][LENGTHOF]: ", toks

    def expr_neg_parse_action(self, s, loc, toks):
        print "[EXPR][NEG]: ", toks

    def expr_newmultiarray_parse_action(self, s, loc, toks):
        print "[EXPR][NEWMULTIARRAY]: " + toks
            
    def stmt_decl_parse_action(self, s, loc, toks):
        print "[STMT][LOCAL_DECL]: ", toks 
        
    def stmt_assign_parse_action(self, s, loc, toks):
        print "[STMT][ASSIGN]: ", toks
    
    def stmt_identity_parse_action(self, s, loc, toks):
        print "[STMT][IDENTITY]: ", toks

    def stmt_goto_parse_action(self, s, loc, toks):
        print "[STMT][GOTO]: ", toks

    def stmt_if_parse_action(self, s, loc, toks):
        print "[STMT][IF]: ", toks

    def stmt_invoke_parse_action(self, s, loc, toks):
        print "[STMT][INVOKE]: ", toks

    def stmt_switch_parse_action(self, s, loc, toks):
        print "[STMT][SWITCH]: ", toks
    
    def stmt_enter_monitor_parse_action(self, s, loc, toks):
        print "[STMT][ENTER_MONITOR]: ", toks
    
    def stmt_exit_monitor_parse_action(self, s, loc, toks):
        print "[STMT][EXIT_MONITOR]: ", toks

    def stmt_return_parse_action(self, s, loc, toks):
        print "[STMT][RETURN]: ", toks

    def stmt_throw_parse_action(self, s, loc, toks):
        print "[STMT][THROW]: ", toks

    def stmt_catch_parse_action(self, s, loc, toks):
        print "[STMT][CATCH]: ", toks
    
    def stmt_breakpoint_parse_action(self, s, loc, toks):
        print "[STMT][BREAKPOINT]: ", toks
        
    def stmt_nop_parse_action(self, s, loc, toks):
        print "[STMT][NOP]: ", toks
        
    def field_decl_parse_action(self, s, loc, toks):
        print "[FIELD]: ", toks
    
    def class_decl_parse_action(self, s, loc, toks):
        print "[CLASS]: ", toks
    
    def method_decl_parse_action(self, s, loc, toks):
        print "[METHOD]: ", toks
    
    def label_parse_action(self, s, loc, toks):
        print "[LABEL]", toks
    
    def expr_imm_parse_action(self, s, loc, toks):
        print "[EXPR][IMMEDIATE]: ", toks
        
infile = "C:\\Users\\wsnav_000\\Desktop\\test.txt"
jp = PrintParser()
jp.parse_file(infile)