
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND COMMA COMMENT DIVIDE DO ELIF ELSE EQUALS EQUALSEQUALS FALSE FLOATNUMBER FOR FUNCTION GREATER GREATEREQUALS IF INTNUMBER LBRACE LESS LESSEQUALS LPAREN MINUS MULTIPLICATION NOT NOTEQUALS OR PLUS RBRACE RETURN RPAREN SHOW STRING TRUE VAR WHILEexpression : expression PLUS term\n                  | expression MINUS term\n                  term       : term MULTIPLICATION factor\n                  | term DIVIDE factorfactor : VARfactor : VAR EQUALS expressionfactor : TRUE\n              | FALSEexpression : expression AND expressionexpression : expression OR expressionexpression : NOT expressionexpression : expression EQUALSEQUALS expression\n                  | expression GREATER expression\n                  | expression LESS expression\n                  | expression GREATEREQUALS expression\n                  | expression LESSEQUALS expression\n                  | expression NOTEQUALS expressionexpression : termterm : factorfactor : ANDfactor : ORfactor : NOTfactor : IFfactor : ELIFfactor : ELSEfactor : INTNUMBERfactor : FLOATNUMBERfactor : STRINGfactor : COMMENTfactor : SHOW LPAREN expression RPARENfactor : LPAREN expression RPARENfactor : LBRACE expression RBRACEfactor : MINUS factorif_statement : IF LPAREN expression RPAREN LBRACE expression RBRACE elif_clauses else_clause\n                    | IF LPAREN expression RPAREN LBRACE expression RBRACE elif_clauses\n                    | IF LPAREN expression RPAREN LBRACE expression RBRACE else_clause\n                    | IF LPAREN expression RPAREN LBRACE expression RBRACEelif_clauses : ELIF LPAREN expression RPAREN LBRACE expression RBRACE elif_clauses\n                    | ELIF LPAREN expression RPAREN LBRACE expression RBRACEelse_clause : ELSE LBRACE expression RBRACE\n                   | emptyempty :expression : if_statement\n                  | VAR'
    
_lr_action_items = {'NOT':([0,3,6,11,12,22,23,24,25,26,27,28,29,30,31,32,33,39,40,43,63,72,73,78,],[6,36,6,6,6,36,36,6,6,6,6,6,6,6,6,36,36,6,6,6,6,6,6,6,]),'VAR':([0,3,6,11,12,22,23,24,25,26,27,28,29,30,31,32,33,39,40,43,63,72,73,78,],[8,35,8,8,8,35,35,8,8,8,8,8,8,8,8,35,35,8,8,8,8,8,8,8,]),'IF':([0,3,6,11,12,22,23,24,25,26,27,28,29,30,31,32,33,39,40,43,63,72,73,78,],[10,37,10,10,10,37,37,10,10,10,10,10,10,10,10,37,37,10,10,10,10,10,10,10,]),'TRUE':([0,3,6,11,12,22,23,24,25,26,27,28,29,30,31,32,33,39,40,43,63,72,73,78,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'FALSE':([0,3,6,11,12,22,23,24,25,26,27,28,29,30,31,32,33,39,40,43,63,72,73,78,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'AND':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,64,65,66,67,70,71,72,73,74,75,77,78,79,80,81,],[4,24,-18,4,-20,-21,4,-43,-5,-19,-23,4,4,-7,-8,-24,-25,-26,-27,-28,-29,4,4,4,4,4,4,4,4,4,4,4,4,-33,-5,-22,-23,24,4,4,24,24,4,-1,-2,24,24,24,24,24,24,24,24,-3,-4,24,24,-31,-32,24,-30,4,24,-37,-35,-36,-41,-34,4,4,24,24,-40,4,24,-39,-38,]),'OR':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,64,65,66,67,70,71,72,73,74,75,77,78,79,80,81,],[5,25,-18,5,-20,-21,5,-43,-5,-19,-23,5,5,-7,-8,-24,-25,-26,-27,-28,-29,5,5,5,5,5,5,5,5,5,5,5,5,-33,-5,-22,-23,25,5,5,25,25,5,-1,-2,25,25,25,25,25,25,25,25,-3,-4,25,25,-31,-32,25,-30,5,25,-37,-35,-36,-41,-34,5,5,25,25,-40,5,25,-39,-38,]),'ELIF':([0,3,6,11,12,22,23,24,25,26,27,28,29,30,31,32,33,39,40,43,63,65,72,73,78,80,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,68,15,15,15,68,]),'ELSE':([0,3,6,11,12,22,23,24,25,26,27,28,29,30,31,32,33,39,40,43,63,65,66,72,73,78,80,81,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,69,69,16,16,16,-39,-38,]),'INTNUMBER':([0,3,6,11,12,22,23,24,25,26,27,28,29,30,31,32,33,39,40,43,63,72,73,78,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'FLOATNUMBER':([0,3,6,11,12,22,23,24,25,26,27,28,29,30,31,32,33,39,40,43,63,72,73,78,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'STRING':([0,3,6,11,12,22,23,24,25,26,27,28,29,30,31,32,33,39,40,43,63,72,73,78,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'COMMENT':([0,3,6,11,12,22,23,24,25,26,27,28,29,30,31,32,33,39,40,43,63,72,73,78,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'SHOW':([0,3,6,11,12,22,23,24,25,26,27,28,29,30,31,32,33,39,40,43,63,72,73,78,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'LPAREN':([0,3,6,10,11,12,21,22,23,24,25,26,27,28,29,30,31,32,33,39,40,43,63,68,72,73,78,],[11,11,11,40,11,11,43,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,72,11,11,11,]),'LBRACE':([0,3,6,11,12,22,23,24,25,26,27,28,29,30,31,32,33,39,40,43,61,63,69,72,73,76,78,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,63,12,73,12,12,78,12,]),'MINUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,64,65,66,67,70,71,72,73,74,75,77,78,79,80,81,],[3,23,-18,3,-20,-21,3,-43,-5,-19,-23,3,3,-7,-8,-24,-25,-26,-27,-28,-29,3,3,3,3,3,3,3,3,3,3,3,3,-33,-5,-22,-23,23,3,3,23,23,3,-1,-2,23,23,23,23,23,23,23,23,-3,-4,23,23,-31,-32,23,-30,3,23,-37,-35,-36,-41,-34,3,3,23,23,-40,3,23,-39,-38,]),'$end':([1,2,4,5,6,7,8,9,10,13,14,15,16,17,18,19,20,34,35,36,37,38,44,45,46,47,48,49,50,51,52,53,54,55,56,58,59,62,65,66,67,70,71,77,80,81,],[0,-18,-20,-21,-22,-43,-5,-19,-23,-7,-8,-24,-25,-26,-27,-28,-29,-33,-5,-22,-23,-11,-1,-2,-9,-10,-12,-13,-14,-15,-16,-17,-3,-4,-6,-31,-32,-30,-37,-35,-36,-41,-34,-40,-39,-38,]),'PLUS':([1,2,4,5,6,7,8,9,10,13,14,15,16,17,18,19,20,34,35,36,37,38,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,64,65,66,67,70,71,74,75,77,79,80,81,],[22,-18,-20,-21,-22,-43,-5,-19,-23,-7,-8,-24,-25,-26,-27,-28,-29,-33,-5,-22,-23,22,22,22,-1,-2,22,22,22,22,22,22,22,22,-3,-4,22,22,-31,-32,22,-30,22,-37,-35,-36,-41,-34,22,22,-40,22,-39,-38,]),'EQUALSEQUALS':([1,2,4,5,6,7,8,9,10,13,14,15,16,17,18,19,20,34,35,36,37,38,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,64,65,66,67,70,71,74,75,77,79,80,81,],[26,-18,-20,-21,-22,-43,-5,-19,-23,-7,-8,-24,-25,-26,-27,-28,-29,-33,-5,-22,-23,26,26,26,-1,-2,26,26,26,26,26,26,26,26,-3,-4,26,26,-31,-32,26,-30,26,-37,-35,-36,-41,-34,26,26,-40,26,-39,-38,]),'GREATER':([1,2,4,5,6,7,8,9,10,13,14,15,16,17,18,19,20,34,35,36,37,38,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,64,65,66,67,70,71,74,75,77,79,80,81,],[27,-18,-20,-21,-22,-43,-5,-19,-23,-7,-8,-24,-25,-26,-27,-28,-29,-33,-5,-22,-23,27,27,27,-1,-2,27,27,27,27,27,27,27,27,-3,-4,27,27,-31,-32,27,-30,27,-37,-35,-36,-41,-34,27,27,-40,27,-39,-38,]),'LESS':([1,2,4,5,6,7,8,9,10,13,14,15,16,17,18,19,20,34,35,36,37,38,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,64,65,66,67,70,71,74,75,77,79,80,81,],[28,-18,-20,-21,-22,-43,-5,-19,-23,-7,-8,-24,-25,-26,-27,-28,-29,-33,-5,-22,-23,28,28,28,-1,-2,28,28,28,28,28,28,28,28,-3,-4,28,28,-31,-32,28,-30,28,-37,-35,-36,-41,-34,28,28,-40,28,-39,-38,]),'GREATEREQUALS':([1,2,4,5,6,7,8,9,10,13,14,15,16,17,18,19,20,34,35,36,37,38,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,64,65,66,67,70,71,74,75,77,79,80,81,],[29,-18,-20,-21,-22,-43,-5,-19,-23,-7,-8,-24,-25,-26,-27,-28,-29,-33,-5,-22,-23,29,29,29,-1,-2,29,29,29,29,29,29,29,29,-3,-4,29,29,-31,-32,29,-30,29,-37,-35,-36,-41,-34,29,29,-40,29,-39,-38,]),'LESSEQUALS':([1,2,4,5,6,7,8,9,10,13,14,15,16,17,18,19,20,34,35,36,37,38,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,64,65,66,67,70,71,74,75,77,79,80,81,],[30,-18,-20,-21,-22,-43,-5,-19,-23,-7,-8,-24,-25,-26,-27,-28,-29,-33,-5,-22,-23,30,30,30,-1,-2,30,30,30,30,30,30,30,30,-3,-4,30,30,-31,-32,30,-30,30,-37,-35,-36,-41,-34,30,30,-40,30,-39,-38,]),'NOTEQUALS':([1,2,4,5,6,7,8,9,10,13,14,15,16,17,18,19,20,34,35,36,37,38,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,64,65,66,67,70,71,74,75,77,79,80,81,],[31,-18,-20,-21,-22,-43,-5,-19,-23,-7,-8,-24,-25,-26,-27,-28,-29,-33,-5,-22,-23,31,31,31,-1,-2,31,31,31,31,31,31,31,31,-3,-4,31,31,-31,-32,31,-30,31,-37,-35,-36,-41,-34,31,31,-40,31,-39,-38,]),'MULTIPLICATION':([2,4,5,6,7,8,9,10,13,14,15,16,17,18,19,20,34,35,36,37,38,44,45,46,47,48,49,50,51,52,53,54,55,56,58,59,62,65,66,67,70,71,77,80,81,],[32,-20,-21,-22,-43,-5,-19,-23,-7,-8,-24,-25,-26,-27,-28,-29,-33,-5,-22,-23,-11,32,32,-9,-10,-12,-13,-14,-15,-16,-17,-3,-4,-6,-31,-32,-30,-37,-35,-36,-41,-34,-40,-39,-38,]),'DIVIDE':([2,4,5,6,7,8,9,10,13,14,15,16,17,18,19,20,34,35,36,37,38,44,45,46,47,48,49,50,51,52,53,54,55,56,58,59,62,65,66,67,70,71,77,80,81,],[33,-20,-21,-22,-43,-5,-19,-23,-7,-8,-24,-25,-26,-27,-28,-29,-33,-5,-22,-23,-11,33,33,-9,-10,-12,-13,-14,-15,-16,-17,-3,-4,-6,-31,-32,-30,-37,-35,-36,-41,-34,-40,-39,-38,]),'RPAREN':([2,4,5,6,7,8,9,10,13,14,15,16,17,18,19,20,34,35,36,37,38,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,65,66,67,70,71,74,77,80,81,],[-18,-20,-21,-22,-43,-5,-19,-23,-7,-8,-24,-25,-26,-27,-28,-29,-33,-5,-22,-23,-11,58,-1,-2,-9,-10,-12,-13,-14,-15,-16,-17,-3,-4,-6,61,-31,-32,62,-30,-37,-35,-36,-41,-34,76,-40,-39,-38,]),'RBRACE':([2,4,5,6,7,8,9,10,13,14,15,16,17,18,19,20,34,35,36,37,38,42,44,45,46,47,48,49,50,51,52,53,54,55,56,58,59,62,64,65,66,67,70,71,75,77,79,80,81,],[-18,-20,-21,-22,-43,-5,-19,-23,-7,-8,-24,-25,-26,-27,-28,-29,-33,-5,-22,-23,-11,59,-1,-2,-9,-10,-12,-13,-14,-15,-16,-17,-3,-4,-6,-31,-32,-30,65,-37,-35,-36,-41,-34,77,-40,80,-39,-38,]),'EQUALS':([8,35,],[39,39,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,6,11,12,24,25,26,27,28,29,30,31,39,40,43,63,72,73,78,],[1,38,41,42,46,47,48,49,50,51,52,53,56,57,60,64,74,75,79,]),'term':([0,6,11,12,22,23,24,25,26,27,28,29,30,31,39,40,43,63,72,73,78,],[2,2,2,2,44,45,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'if_statement':([0,6,11,12,24,25,26,27,28,29,30,31,39,40,43,63,72,73,78,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'factor':([0,3,6,11,12,22,23,24,25,26,27,28,29,30,31,32,33,39,40,43,63,72,73,78,],[9,34,9,9,9,9,9,9,9,9,9,9,9,9,9,54,55,9,9,9,9,9,9,9,]),'elif_clauses':([65,80,],[66,81,]),'else_clause':([65,66,],[67,71,]),'empty':([65,66,],[70,70,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS term','expression',3,'p_binary_operators','parse.py',7),
  ('expression -> expression MINUS term','expression',3,'p_binary_operators','parse.py',8),
  ('term -> term MULTIPLICATION factor','term',3,'p_binary_operators','parse.py',9),
  ('term -> term DIVIDE factor','term',3,'p_binary_operators','parse.py',10),
  ('factor -> VAR','factor',1,'p_factor_var','parse.py',42),
  ('factor -> VAR EQUALS expression','factor',3,'p_assignment','parse.py',49),
  ('factor -> TRUE','factor',1,'p_factor_boolean','parse.py',54),
  ('factor -> FALSE','factor',1,'p_factor_boolean','parse.py',55),
  ('expression -> expression AND expression','expression',3,'p_expression_and','parse.py',59),
  ('expression -> expression OR expression','expression',3,'p_expression_or','parse.py',72),
  ('expression -> NOT expression','expression',2,'p_expression_not','parse.py',90),
  ('expression -> expression EQUALSEQUALS expression','expression',3,'p_expression_comparison','parse.py',98),
  ('expression -> expression GREATER expression','expression',3,'p_expression_comparison','parse.py',99),
  ('expression -> expression LESS expression','expression',3,'p_expression_comparison','parse.py',100),
  ('expression -> expression GREATEREQUALS expression','expression',3,'p_expression_comparison','parse.py',101),
  ('expression -> expression LESSEQUALS expression','expression',3,'p_expression_comparison','parse.py',102),
  ('expression -> expression NOTEQUALS expression','expression',3,'p_expression_comparison','parse.py',103),
  ('expression -> term','expression',1,'p_expression_term','parse.py',142),
  ('term -> factor','term',1,'p_term_factor','parse.py',146),
  ('factor -> AND','factor',1,'p_factor_and','parse.py',150),
  ('factor -> OR','factor',1,'p_factor_or','parse.py',154),
  ('factor -> NOT','factor',1,'p_factor_not','parse.py',158),
  ('factor -> IF','factor',1,'p_factor_if','parse.py',162),
  ('factor -> ELIF','factor',1,'p_factor_elif','parse.py',166),
  ('factor -> ELSE','factor',1,'p_factor_else','parse.py',170),
  ('factor -> INTNUMBER','factor',1,'p_factor_intnum','parse.py',174),
  ('factor -> FLOATNUMBER','factor',1,'p_factor_floatnum','parse.py',178),
  ('factor -> STRING','factor',1,'p_factor_string','parse.py',182),
  ('factor -> COMMENT','factor',1,'p_factor_comment','parse.py',186),
  ('factor -> SHOW LPAREN expression RPAREN','factor',4,'p_factor_show','parse.py',190),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','parse.py',194),
  ('factor -> LBRACE expression RBRACE','factor',3,'p_factor_brac','parse.py',198),
  ('factor -> MINUS factor','factor',2,'p_factor_neg','parse.py',202),
  ('if_statement -> IF LPAREN expression RPAREN LBRACE expression RBRACE elif_clauses else_clause','if_statement',9,'p_if_statement','parse.py',207),
  ('if_statement -> IF LPAREN expression RPAREN LBRACE expression RBRACE elif_clauses','if_statement',8,'p_if_statement','parse.py',208),
  ('if_statement -> IF LPAREN expression RPAREN LBRACE expression RBRACE else_clause','if_statement',8,'p_if_statement','parse.py',209),
  ('if_statement -> IF LPAREN expression RPAREN LBRACE expression RBRACE','if_statement',7,'p_if_statement','parse.py',210),
  ('elif_clauses -> ELIF LPAREN expression RPAREN LBRACE expression RBRACE elif_clauses','elif_clauses',8,'p_elif_clauses','parse.py',222),
  ('elif_clauses -> ELIF LPAREN expression RPAREN LBRACE expression RBRACE','elif_clauses',7,'p_elif_clauses','parse.py',223),
  ('else_clause -> ELSE LBRACE expression RBRACE','else_clause',4,'p_else_clause','parse.py',233),
  ('else_clause -> empty','else_clause',1,'p_else_clause','parse.py',234),
  ('empty -> <empty>','empty',0,'p_empty','parse.py',242),
  ('expression -> if_statement','expression',1,'p_expression','parse.py',246),
  ('expression -> VAR','expression',1,'p_expression','parse.py',247),
]
