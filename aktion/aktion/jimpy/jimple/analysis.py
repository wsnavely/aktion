'''
Created on Mar 18, 2015

@author: wsnav_000
'''
import logging
import os

from jimpy.jimple.entity import AssignStmt, InvokeExpr
from jimpy.jimple.simplebodyparser import SimpleBodyParser

def is_assign(stmt):
    return isinstance(stmt, AssignStmt)

def process_method(method):
    for stmt in method.stmts:
        if isinstance(stmt, AssignStmt):
            expr = stmt.right
            if isinstance(expr, InvokeExpr):
                if expr.class_name == "android.content.Intent":
                    print stmt

#logging.basicConfig(level="INFO")
indir = "C:\\jimple\\alexcrusher.just6weeks.apk"
#single = indir + "\\" + "com.flurry.org.codehaus.jackson.map.deser.std.StdDeserializer.jimple"
jp = SimpleBodyParser()
#jp.parse_file(single) 
#exit()

for infile in os.listdir(indir):
    try:
        jp.parse_file(indir + "\\" + infile)
    except:
        print infile
        print "whoops!"
        continue
    #for jc in jp.classes:
    #    for method in jc.methods:
    #        process_method(method)