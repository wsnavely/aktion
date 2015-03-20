from pyparsing import \
    Word, alphas, alphanums, Combine, \
    Literal, Keyword, nums, ZeroOrMore, \
    Optional, Suppress, OneOrMore, \
    delimitedList, Group, QuotedString


class BaseParser(object):
    def __init__(self):
        self.parser = self.build_jimple_parser()
        
    def expr_numeric_const_parse_action(self, s, loc, toks):
        pass
   
    def expr_str_const_parse_action(self, s, loc, toks):
        pass
    
    def expr_null_parse_action(self, s, loc, toks):
        pass
    
    def expr_class_parse_action(self, s, loc, toks):
        pass
    
    def expr_local_parse_action(self, s, loc, toks):
        pass
    
    def expr_binop_parse_action(self, s, loc, toks):
        pass

    def expr_cast_parse_action(self, s, loc, toks):
        pass

    def expr_array_ref_parse_action(self, s, loc, toks):
        pass
    
    def expr_field_ref_parse_action(self, s, loc, toks):
        pass

    def expr_instanceof_parse_action(self, s, loc, toks):
        pass

    def expr_invoke_parse_action(self, s, loc, toks):
        pass

    def expr_new_parse_action(self, s, loc, toks):
        pass
    
    def expr_newarray_parse_action(self, s, loc, toks):
        pass

    def expr_lengthof_parse_action(self, s, loc, toks):
        pass

    def expr_neg_parse_action(self, s, loc, toks):
        pass

    def expr_newmultiarray_parse_action(self, s, loc, toks):
        pass
    
    def expr_parse_action(self, s, loc, toks):
        pass
    
    def expr_lvalue_parse_action(self, s, loc, toks):
        pass

    def expr_cond_parse_action(self, s, loc, toks):
        pass

    def field_specifier_parse_action(self, s, loc, toks):
        pass
            
    def stmt_decl_parse_action(self, s, loc, toks):
        pass
    
    def stmt_assign_parse_action(self, s, loc, toks):
        pass
    
    def stmt_identity_parse_action(self, s, loc, toks):
        pass

    def stmt_goto_parse_action(self, s, loc, toks):
        pass
    
    def stmt_if_parse_action(self, s, loc, toks):
        pass
    
    def stmt_invoke_parse_action(self, s, loc, toks):
        pass
    
    def stmt_switch_parse_action(self, s, loc, toks):
        pass
    
    def stmt_enter_monitor_parse_action(self, s, loc, toks):
        pass
    
    def stmt_exit_monitor_parse_action(self, s, loc, toks):
        pass

    def stmt_return_parse_action(self, s, loc, toks):
        pass

    def stmt_throw_parse_action(self, s, loc, toks):
        pass

    def stmt_catch_parse_action(self, s, loc, toks):
        pass
    
    def stmt_breakpoint_parse_action(self, s, loc, toks):
        pass
    
    def stmt_nop_parse_action(self, s, loc, toks):
        pass
    
    def stmt_parse_action(self, s, loc, toks):
        pass
    
    def field_decl_parse_action(self, s, loc, toks):
        pass
    
    def class_defn_parse_action(self, s, loc, toks):
        pass
    
    def method_defn_parse_action(self, s, loc, toks):
        pass
    
    def label_parse_action(self, s, loc, toks):
        pass

    def expr_imm_parse_action(self, s, loc, toks):
        pass

    def parse_file(self, infile):
        return self.parser.parseFile(infile)

    def build_jimple_parser(self):
        # Literals
        op_add     =   Literal("+")
        op_sub     =   Literal("-")
        op_mul     =   Literal("*")
        op_div     =   Literal("/")
        op_xor     =   Literal("^")
        op_lt      =   Literal("<")
        op_gt      =   Literal(">")
        op_eq      =   Literal("==")
        op_neq     =   Literal("!=")
        op_lte     =   Literal("<=")
        op_gte     =   Literal(">=")
        op_sls     =   Literal("<<")
        op_srs     =   Literal(">>")
        op_urs     =   Literal(">>>")
        op_mod     =   Literal("%")
        op_rem     =   Literal("rem")
        op_bwa     =   Literal("&")
        op_bwo     =   Literal("|")
        op_cmp     =   Literal("cmp")
        op_cmpg    =   Literal("cmpg")
        op_cmpl    =   Literal("cmpl")
        lit_lcb    =   Literal("{").suppress()
        lit_rcb    =   Literal("}").suppress()
        lit_lp     =   Literal("(").suppress()
        lit_rp     =   Literal(")").suppress()
        lit_dot    =   Literal(".").suppress()
        lit_asgn   =   Literal("=").suppress()
        lit_ident  =   Literal(":=").suppress()
        lit_strm   =   Literal(";").suppress()
        lit_cln    =   Literal(":").suppress()
        lit_lsb    =   Literal("[").suppress()
        lit_rsb    =   Literal("]").suppress()
        
        binop =   op_add ^ op_sub ^ op_mul ^ op_div ^ op_xor \
                ^ op_bwa ^ op_mod ^ op_rem ^ op_urs ^ op_lte \
                ^ op_gte ^ op_sls ^ op_srs ^ op_lt  ^ op_gt  \
                ^ op_eq  ^ op_neq ^ op_bwo ^ op_cmp ^ op_cmpg \
                ^ op_cmpl \
                
        cond_op =  op_gte ^ op_lte ^ op_lt ^ op_gt ^ op_eq ^ op_neq 
        
        # Keywords
        kw_specialinvoke   = Keyword("specialinvoke")
        kw_interfaceinvoke = Keyword("interfaceinvoke")
        kw_virtualinvoke   = Keyword("virtualinvoke")
        kw_staticinvoke    = Keyword("staticinvoke")
        kw_instanceof      = Keyword("instanceof")
        kw_new             = Keyword("new")
        kw_newarray        = Keyword("newarray")
        kw_newmultiarray   = Keyword("newmultiarray")
        kw_length          = Keyword("lengthof")
        kw_neg             = Keyword("neg")
        kw_goto            = Keyword("goto")
        kw_if              = Keyword("if")
        kw_this            = Keyword("@this")
        kw_caughtexception = Keyword("@caughtexception")
        kw_lookupswitch    = Keyword("lookupswitch")
        kw_case            = Keyword("case")
        kw_default         = Keyword("default")
        kw_return          = Keyword("return")
        kw_entermonitor    = Keyword("entermonitor")
        kw_exitmonitor     = Keyword("exitmonitor")
        kw_throw           = Keyword("throw")
        kw_throws          = Keyword("throws")
        kw_catch           = Keyword("catch")
        kw_transient       = Keyword("transient")
        kw_from            = Keyword("from")
        kw_to              = Keyword("to")
        kw_with            = Keyword("with")
        kw_breakpoint      = Keyword("breakpoint")
        kw_nop             = Keyword("nop")
        kw_public          = Keyword("public")
        kw_protected       = Keyword("protected")
        kw_private         = Keyword("private")
        kw_volatile        = Keyword("volatile")
        kw_static          = Keyword("static")
        kw_annotation      = Keyword("annotation")
        kw_final           = Keyword("final")
        kw_class           = Keyword("class")
        kw_enum            = Keyword("enum")
        kw_interface       = Keyword("interface")
        kw_abstract        = Keyword("abstract")
        kw_extends         = Keyword("extends")
        kw_implements      = Keyword("implements")
        kw_null            = Keyword("null")
        
        modifier = \
                kw_public | kw_protected | kw_private \
            |   kw_static | kw_abstract | kw_final \
            |   kw_volatile | kw_enum | kw_transient \
            |   kw_annotation
        
        #Identifiers
        id_local  = Combine(Optional(Literal("$")) + Word(alphas) + Word(nums))
        id_java = Word(alphas + "'$_", alphanums + "'$_")
        id_class_comp = Word(alphas + "_", alphanums + "$_")
        id_type = Combine(id_class_comp + ZeroOrMore(Combine(Literal(".") + (id_class_comp))) + Optional(Word("[]")))
        id_method_name = id_java | Word("<clinit>") | Word("<init>") 
        id_label = Combine(Literal("label") + Word(nums)) 
        id_parameter = Combine(Literal("@parameter") + Word(nums)) 
        
        # Field
        field_specifier = \
                Suppress(Literal("<")) \
            +   id_type + lit_cln + id_type + id_java \
            +   Suppress(Literal(">"))
        field_specifier.setParseAction(self.field_specifier_parse_action)
        
        # Method
        method_param_list = delimitedList(id_type, delim=",")
        id_method = \
                Suppress(Literal("<")) \
            +   id_type + lit_cln + id_type + id_method_name \
            +   lit_lp + Group(Optional(method_param_list)) + lit_rp \
            +   Suppress(Literal(">"))
        
        number_suffix = Optional(Literal("F") | Literal("L"))
        
        # Numeric constant
        expr_number = \
                Combine( 
                    Word("+-" + nums, nums) 
                +   Optional(Literal(".") + Optional(Word(nums))) 
                +   Optional(Literal("E") + Optional(Word("+-")) + Word(nums)) 
                +   number_suffix) \
            |   Combine(Literal("#Infinity") + number_suffix) \
            |   Combine(Literal("#-Infinity") + number_suffix) \
            |   Combine(Literal("#NaN") + number_suffix)
                
        expr_number.setParseAction(self.expr_numeric_const_parse_action)
        expr_str = QuotedString(quoteChar='"', escChar="\\")
        expr_str.setParseAction(self.expr_str_const_parse_action)
        
        # Null constant
        expr_null = kw_null
        expr_null.setParseAction(self.expr_null_parse_action)
       
        # Group all constants
        expr_constant = \
                expr_str \
            ^   expr_number \
            ^   expr_null 

        # A 'class' expression (class + classname)
        expr_class = kw_class + QuotedString(quoteChar='"')
        expr_class.setParseAction(self.expr_class_parse_action)
        
        # A local variable expression
        expr_local = id_local
        expr_local.setParseAction(self.expr_local_parse_action)
       
        # Group together all "immediate" values
        expr_imm =  expr_local ^ expr_constant ^ expr_class 
        expr_imm.setParseAction(self.expr_imm_parse_action)
         
        # Conditional expression
        expr_cond = expr_imm + cond_op + expr_imm
        expr_cond.setParseAction(self.expr_cond_parse_action)
        
        # Array index
        array_idx = lit_lsb + expr_imm + lit_rsb
        empty_array_idx = lit_lsb + lit_rsb
        
        expr_binop = expr_imm + binop + expr_imm
        expr_binop.setParseAction(self.expr_binop_parse_action)
        
        expr_cast = lit_lp + id_type + lit_rp + expr_imm
        expr_cast.setParseAction(self.expr_cast_parse_action)
        
        expr_instanceof = expr_imm + kw_instanceof + id_type
        expr_instanceof.setParseAction(self.expr_instanceof_parse_action)
        
        expr_new = Suppress(kw_new) + id_type
        expr_new.setParseAction(self.expr_new_parse_action)
        
        expr_newarray = kw_newarray + lit_lp + id_type + lit_rp + array_idx
        expr_newarray.setParseAction(self.expr_newarray_parse_action)
                
        expr_newmultiarray = kw_newmultiarray + lit_lp + id_type + lit_rp + OneOrMore(array_idx | empty_array_idx)
        expr_newmultiarray.setParseAction(self.expr_newmultiarray_parse_action)
        
        expr_lengthof = kw_length + expr_imm 
        expr_lengthof.setParseAction(self.expr_lengthof_parse_action)
        
        expr_neg = kw_neg + expr_imm
        expr_neg.setParseAction(self.expr_neg_parse_action)
        
        # Invoke Expressions
        method_arg_list = delimitedList(expr_imm, delim=",")
        expr_invoke = \
                kw_specialinvoke \
                    + id_local + lit_dot + id_method \
                    + lit_lp + Group(Optional(method_arg_list)) + lit_rp \
            |   kw_interfaceinvoke \
                    + id_local + lit_dot + id_method \
                    + lit_lp + Group(Optional(method_arg_list)) + lit_rp \
            |   kw_virtualinvoke \
                    + id_local + lit_dot + id_method \
                    + lit_lp + Group(Optional(method_arg_list)) + lit_rp \
            |   kw_staticinvoke + id_method \
                    + lit_lp + Group(Optional(method_arg_list)) + lit_rp 
        expr_invoke.setParseAction(self.expr_invoke_parse_action)
                    
        expr = \
                expr_binop \
            ^   expr_cast \
            ^   expr_instanceof \
            ^   expr_invoke \
            ^   expr_new \
            ^   expr_newarray \
            ^   expr_newmultiarray \
            ^   expr_lengthof \
            ^   expr_neg 
        expr.setParseAction(self.expr_parse_action)
                    
        # Concrete Reference Expression
        expr_field_ref =  Group(Optional(id_local + lit_dot)) + field_specifier 
        expr_field_ref.setParseAction(self.expr_field_ref_parse_action)
        
        expr_array_ref = id_local + array_idx
        expr_array_ref.setParseAction(self.expr_array_ref_parse_action)
        
        # L and R values
        expr_lvalue = \
                id_local \
            ^   expr_field_ref \
            ^   expr_array_ref
            
        expr_lvalue.setParseAction(self.expr_lvalue_parse_action)
        expr_rvalue = \
                expr \
            ^   expr_field_ref \
            ^   expr_array_ref \
            ^   expr_imm 
        
        # Declaration
        stmt_decl = \
                id_type \
            +   Group(delimitedList(id_local, delim=",")) \
            +   lit_strm
        stmt_decl.setParseAction(self.stmt_decl_parse_action)
        
        # Statements 
        stmt_assign = \
                expr_lvalue + lit_asgn + expr_rvalue + lit_strm
        '''
                id_local + lit_asgn + expr_rvalue + lit_strm \
            ^   field_specifier + lit_asgn + expr_imm + lit_strm \
            ^   id_local + lit_dot + field_specifier + lit_asgn + expr_imm + lit_strm \
            ^   id_local + lit_lsb + expr_imm + lit_rsb + lit_asgn + expr_imm + lit_strm
        '''
        
        stmt_assign.setParseAction(self.stmt_assign_parse_action)
        
        stmt_identity = \
                id_local + lit_ident + kw_this + lit_cln + id_type + lit_strm \
            ^   id_local + lit_ident + id_parameter + lit_cln + id_type + lit_strm \
            ^   id_local + lit_ident + kw_caughtexception + lit_strm
            
        stmt_identity.setParseAction(self.stmt_identity_parse_action)
        
        stmt_goto = kw_goto + id_label + lit_strm
        stmt_goto.setParseAction(self.stmt_goto_parse_action)
        
        stmt_if = Suppress(kw_if) + expr_cond + Suppress(kw_goto) + id_label + lit_strm
        stmt_if.setParseAction(self.stmt_if_parse_action)
        
        stmt_invoke = expr_invoke + lit_strm
        stmt_invoke.setParseAction(self.stmt_invoke_parse_action)
        
        switch_case = kw_case + expr_number + lit_cln + kw_goto + id_label + lit_strm
        switch_default = kw_default + lit_cln + kw_goto + id_label + lit_strm
        switch_body = ZeroOrMore(switch_case) + Optional(switch_default)
        stmt_switch = kw_lookupswitch + lit_lp + expr_imm + lit_rp + lit_lcb + switch_body + lit_rcb + lit_strm
        stmt_switch.setParseAction(self.stmt_switch_parse_action)
        
        stmt_enter_monitor = kw_entermonitor + expr_imm + lit_strm
        stmt_enter_monitor.setParseAction(self.stmt_enter_monitor_parse_action)
        
        stmt_exit_monitor = kw_exitmonitor + expr_imm + lit_strm
        stmt_exit_monitor.setParseAction(self.stmt_exit_monitor_parse_action)
        
        stmt_return = Suppress(kw_return) + expr_imm + lit_strm | Suppress(kw_return) + lit_strm
        stmt_return.setParseAction(self.stmt_return_parse_action)
        
        stmt_throw = kw_throw + expr_imm + lit_strm
        stmt_throw.setParseAction(self.stmt_throw_parse_action)
        
        stmt_catch = kw_catch + id_type \
                +   kw_from + id_label \
                +   kw_to + id_label \
                +   kw_with + id_label + lit_strm
        stmt_catch.setParseAction(self.stmt_catch_parse_action)
        
        stmt_breakpoint = kw_breakpoint + lit_strm
        stmt_breakpoint.setParseAction(self.stmt_breakpoint_parse_action)
        
        stmt_nop = kw_nop + lit_strm
        stmt_nop.setParseAction(self.stmt_nop_parse_action)
        
        jimple_stmt = \
                stmt_decl           \
            ^   stmt_assign         \
            ^   stmt_identity       \
            ^   stmt_goto           \
            ^   stmt_if             \
            ^   stmt_invoke         \
            ^   stmt_switch         \
            ^   stmt_enter_monitor  \
            ^   stmt_exit_monitor   \
            ^   stmt_return         \
            ^   stmt_throw          \
            ^   stmt_catch          \
            ^   stmt_breakpoint     \
            ^   stmt_nop
        jimple_stmt.setParseAction(self.stmt_parse_action)
        
        throws_clause = kw_throws + delimitedList(id_type, delim=",")
        
        method_sig = \
                    Group(ZeroOrMore(modifier)) \
                +   id_type + id_method_name \
                +   lit_lp + Group(Optional(method_param_list)) + lit_rp \
                +   Group(Optional(throws_clause))
        
        method_decl = method_sig + lit_strm
        
        field_decl = ZeroOrMore(modifier) + id_type + id_java + lit_strm
        field_decl.setParseAction(self.field_decl_parse_action)
                    
        class_decl = \
                    Group(ZeroOrMore(modifier)) + Suppress(kw_class) + id_type \
                +   Optional(kw_extends + delimitedList(id_type, delim=",")) \
                +   Optional(kw_implements + delimitedList(id_type, delim=","))

        interface_decl = \
                    Group(ZeroOrMore(modifier)) + Suppress(kw_interface) + id_type \
                +   Optional(kw_extends + delimitedList(id_type, delim=",")) \
                +   Optional(kw_implements + delimitedList(id_type, delim=","))

        
        jimple_method_item = \
                jimple_stmt \
            |   Combine(id_label + lit_cln).setParseAction(self.label_parse_action)
            
        jimple_method_body = ZeroOrMore(jimple_method_item)
        jimple_method = \
                Group(method_sig) + lit_lcb \
            +   Group(jimple_method_body) \
            +   lit_rcb
        jimple_method.setParseAction(self.method_defn_parse_action)

        jimple_class_item = field_decl | method_decl | jimple_method
        jimple_class_body = ZeroOrMore(jimple_class_item)
        jimple_class = Group(class_decl | interface_decl) + lit_lcb + Group(jimple_class_body) + lit_rcb
        jimple_class.setParseAction(self.class_defn_parse_action)
        return jimple_class