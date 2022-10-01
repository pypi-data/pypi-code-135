
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ARRAY BIGINT BOOLEAN CHAR COMMA_SPACE DATE DECIMAL DOUBLE INTEGER JSON LPAREN MAP NAME_PART NUMBER REAL ROW RPAREN SMALLINT SPACE TIME TIMESTAMP TINYINT VARBINARY VARCHAR WITH ZONEtype : ARRAY LPAREN type RPARENtype : MAP LPAREN type COMMA_SPACE type RPARENtype : ROW LPAREN row_field_list RPAREN\n    row_field_list : row_field_list COMMA_SPACE row_field\n                   | row_field\n    \n    row_field : row_field_parts\n    \n    row_field_parts : field_part row_field_parts\n                    | type\n    \n    field_part :  NAME_PART\n                | SPACE\n                | WITH\n                | ZONE\n                | ROW\n                | MAP\n                | type\n                | type_name\n                \n    type : type_name\n    type_name :   BOOLEAN\n                | TINYINT\n                | SMALLINT\n                | INTEGER\n                | BIGINT\n                | REAL\n                | DOUBLE\n                | DECIMAL\n                | VARCHAR\n                | VARCHAR LPAREN NUMBER RPAREN\n                | CHAR\n                | VARBINARY\n                | JSON\n                | DATE\n                | TIME\n                | TIMESTAMP\n                | TIMESTAMP LPAREN NUMBER RPAREN SPACE WITH SPACE TIME SPACE ZONE\n    '
    
_lr_action_items = {'ARRAY':([0,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,32,33,34,35,36,37,38,39,42,43,44,45,47,52,57,],[2,-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,2,2,2,-13,2,-15,-9,-10,-11,-12,-14,-16,-1,2,-3,2,-27,-2,-34,]),'MAP':([0,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,32,33,34,35,36,37,38,39,42,43,44,45,47,52,57,],[3,-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,3,3,38,-13,38,-15,-9,-10,-11,-12,-14,-16,-1,3,-3,38,-27,-2,-34,]),'ROW':([0,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,32,33,34,35,36,37,38,39,42,43,44,45,47,52,57,],[4,-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,4,4,28,-13,28,-15,-9,-10,-11,-12,-14,-16,-1,4,-3,28,-27,-2,-34,]),'BOOLEAN':([0,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,32,33,34,35,36,37,38,39,42,43,44,45,47,52,57,],[6,-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,6,6,6,-13,6,-15,-9,-10,-11,-12,-14,-16,-1,6,-3,6,-27,-2,-34,]),'TINYINT':([0,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,32,33,34,35,36,37,38,39,42,43,44,45,47,52,57,],[7,-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,7,7,7,-13,7,-15,-9,-10,-11,-12,-14,-16,-1,7,-3,7,-27,-2,-34,]),'SMALLINT':([0,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,32,33,34,35,36,37,38,39,42,43,44,45,47,52,57,],[8,-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,8,8,8,-13,8,-15,-9,-10,-11,-12,-14,-16,-1,8,-3,8,-27,-2,-34,]),'INTEGER':([0,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,32,33,34,35,36,37,38,39,42,43,44,45,47,52,57,],[9,-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,9,9,9,-13,9,-15,-9,-10,-11,-12,-14,-16,-1,9,-3,9,-27,-2,-34,]),'BIGINT':([0,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,32,33,34,35,36,37,38,39,42,43,44,45,47,52,57,],[10,-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,10,10,10,-13,10,-15,-9,-10,-11,-12,-14,-16,-1,10,-3,10,-27,-2,-34,]),'REAL':([0,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,32,33,34,35,36,37,38,39,42,43,44,45,47,52,57,],[11,-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,11,11,11,-13,11,-15,-9,-10,-11,-12,-14,-16,-1,11,-3,11,-27,-2,-34,]),'DOUBLE':([0,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,32,33,34,35,36,37,38,39,42,43,44,45,47,52,57,],[12,-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,12,12,12,-13,12,-15,-9,-10,-11,-12,-14,-16,-1,12,-3,12,-27,-2,-34,]),'DECIMAL':([0,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,32,33,34,35,36,37,38,39,42,43,44,45,47,52,57,],[13,-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,13,13,13,-13,13,-15,-9,-10,-11,-12,-14,-16,-1,13,-3,13,-27,-2,-34,]),'VARCHAR':([0,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,32,33,34,35,36,37,38,39,42,43,44,45,47,52,57,],[14,-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,14,14,14,-13,14,-15,-9,-10,-11,-12,-14,-16,-1,14,-3,14,-27,-2,-34,]),'CHAR':([0,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,32,33,34,35,36,37,38,39,42,43,44,45,47,52,57,],[15,-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,15,15,15,-13,15,-15,-9,-10,-11,-12,-14,-16,-1,15,-3,15,-27,-2,-34,]),'VARBINARY':([0,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,32,33,34,35,36,37,38,39,42,43,44,45,47,52,57,],[16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,16,16,16,-13,16,-15,-9,-10,-11,-12,-14,-16,-1,16,-3,16,-27,-2,-34,]),'JSON':([0,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,32,33,34,35,36,37,38,39,42,43,44,45,47,52,57,],[17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,17,17,17,-13,17,-15,-9,-10,-11,-12,-14,-16,-1,17,-3,17,-27,-2,-34,]),'DATE':([0,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,32,33,34,35,36,37,38,39,42,43,44,45,47,52,57,],[18,-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,18,18,18,-13,18,-15,-9,-10,-11,-12,-14,-16,-1,18,-3,18,-27,-2,-34,]),'TIME':([0,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,32,33,34,35,36,37,38,39,42,43,44,45,47,52,54,57,],[19,-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,19,19,19,-13,19,-15,-9,-10,-11,-12,-14,-16,-1,19,-3,19,-27,-2,55,-34,]),'TIMESTAMP':([0,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,32,33,34,35,36,37,38,39,42,43,44,45,47,52,57,],[20,-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,20,20,20,-13,20,-15,-9,-10,-11,-12,-14,-16,-1,20,-3,20,-27,-2,-34,]),'$end':([1,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,42,44,47,52,57,],[0,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,-1,-3,-27,-2,-34,]),'LPAREN':([2,3,4,14,20,28,38,],[21,22,23,24,25,23,22,]),'RPAREN':([5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,26,29,30,31,33,39,40,41,42,44,46,47,49,50,52,57,],[-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,42,44,-5,-6,-8,-17,47,48,-1,-3,-7,-27,52,-4,-2,-34,]),'COMMA_SPACE':([5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,27,29,30,31,33,39,42,44,46,47,50,52,57,],[-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,43,45,-5,-6,-8,-17,-1,-3,-7,-27,-4,-2,-34,]),'NAME_PART':([6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,23,28,32,33,34,35,36,37,38,39,42,44,45,47,52,57,],[-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,34,-13,34,-15,-9,-10,-11,-12,-14,-16,-1,-3,34,-27,-2,-34,]),'SPACE':([6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,23,28,32,33,34,35,36,37,38,39,42,44,45,47,48,52,53,55,57,],[-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,35,-13,35,-15,-9,-10,-11,-12,-14,-16,-1,-3,35,-27,51,-2,54,56,-34,]),'WITH':([6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,23,28,32,33,34,35,36,37,38,39,42,44,45,47,51,52,57,],[-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,36,-13,36,-15,-9,-10,-11,-12,-14,-16,-1,-3,36,-27,53,-2,-34,]),'ZONE':([6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,23,28,32,33,34,35,36,37,38,39,42,44,45,47,52,56,57,],[-18,-19,-20,-21,-22,-23,-24,-25,-26,-28,-29,-30,-31,-32,-33,37,-13,37,-15,-9,-10,-11,-12,-14,-16,-1,-3,37,-27,-2,57,-34,]),'NUMBER':([24,25,],[40,41,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'type':([0,21,22,23,32,43,45,],[1,26,27,33,33,49,33,]),'type_name':([0,21,22,23,32,43,45,],[5,5,5,39,39,5,39,]),'row_field_list':([23,],[29,]),'row_field':([23,45,],[30,50,]),'row_field_parts':([23,32,45,],[31,46,31,]),'field_part':([23,32,45,],[32,32,32,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> type","S'",1,None,None,None),
  ('type -> ARRAY LPAREN type RPAREN','type',4,'p_array','parser.py',99),
  ('type -> MAP LPAREN type COMMA_SPACE type RPAREN','type',6,'p_map','parser.py',104),
  ('type -> ROW LPAREN row_field_list RPAREN','type',4,'p_row','parser.py',109),
  ('row_field_list -> row_field_list COMMA_SPACE row_field','row_field_list',3,'p_row_field_list','parser.py',115),
  ('row_field_list -> row_field','row_field_list',1,'p_row_field_list','parser.py',116),
  ('row_field -> row_field_parts','row_field',1,'p_row_field','parser.py',131),
  ('row_field_parts -> field_part row_field_parts','row_field_parts',2,'p_row_field_parts','parser.py',140),
  ('row_field_parts -> type','row_field_parts',1,'p_row_field_parts','parser.py',141),
  ('field_part -> NAME_PART','field_part',1,'p_field_part','parser.py',165),
  ('field_part -> SPACE','field_part',1,'p_field_part','parser.py',166),
  ('field_part -> WITH','field_part',1,'p_field_part','parser.py',167),
  ('field_part -> ZONE','field_part',1,'p_field_part','parser.py',168),
  ('field_part -> ROW','field_part',1,'p_field_part','parser.py',169),
  ('field_part -> MAP','field_part',1,'p_field_part','parser.py',170),
  ('field_part -> type','field_part',1,'p_field_part','parser.py',171),
  ('field_part -> type_name','field_part',1,'p_field_part','parser.py',172),
  ('type -> type_name','type',1,'p_type','parser.py',179),
  ('type_name -> BOOLEAN','type_name',1,'p_type_name','parser.py',187),
  ('type_name -> TINYINT','type_name',1,'p_type_name','parser.py',188),
  ('type_name -> SMALLINT','type_name',1,'p_type_name','parser.py',189),
  ('type_name -> INTEGER','type_name',1,'p_type_name','parser.py',190),
  ('type_name -> BIGINT','type_name',1,'p_type_name','parser.py',191),
  ('type_name -> REAL','type_name',1,'p_type_name','parser.py',192),
  ('type_name -> DOUBLE','type_name',1,'p_type_name','parser.py',193),
  ('type_name -> DECIMAL','type_name',1,'p_type_name','parser.py',194),
  ('type_name -> VARCHAR','type_name',1,'p_type_name','parser.py',195),
  ('type_name -> VARCHAR LPAREN NUMBER RPAREN','type_name',4,'p_type_name','parser.py',196),
  ('type_name -> CHAR','type_name',1,'p_type_name','parser.py',197),
  ('type_name -> VARBINARY','type_name',1,'p_type_name','parser.py',198),
  ('type_name -> JSON','type_name',1,'p_type_name','parser.py',199),
  ('type_name -> DATE','type_name',1,'p_type_name','parser.py',200),
  ('type_name -> TIME','type_name',1,'p_type_name','parser.py',201),
  ('type_name -> TIMESTAMP','type_name',1,'p_type_name','parser.py',202),
  ('type_name -> TIMESTAMP LPAREN NUMBER RPAREN SPACE WITH SPACE TIME SPACE ZONE','type_name',10,'p_type_name','parser.py',203),
]
