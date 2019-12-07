# rules_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def knows_pattern_matching(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        engine.get_ke('questionsdoenca', 'discrasiahemorragicapergunta').reset()
        with engine.prove(rule.rule_base.root_name, 'dicrisia', context,
                          ()) \
          as gen_2:
          for x_2 in gen_2:
            assert x_2 is None, \
              "rules.knows_pattern_matching: got unexpected plan from when clause 2"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def dicrisia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'discrasiahemorragicapergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.dicrisia: got unexpected plan from when clause 1"
            engine.get_ke('questionsdoenca', 'coceirapergunta').reset()
            with engine.prove(rule.rule_base.root_name, 'coceira', context,
                              ()) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "rules.dicrisia: got unexpected plan from when clause 3"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def coceira(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'coceirapergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.coceira: got unexpected plan from when clause 1"
            engine.get_ke('questionsdoenca', 'hipertrofiaganglionarpergunta').reset()
            with engine.prove(rule.rule_base.root_name, 'parteintensa', context,
                              ()) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "rules.coceira: got unexpected plan from when clause 3"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def coceira1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'coceirapergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.coceira1: got unexpected plan from when clause 1"
            engine.get_ke('questionsdoenca', 'hipertrofiaganglionarpergunta').reset()
            with engine.prove(rule.rule_base.root_name, 'ganglionar', context,
                              ()) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "rules.coceira1: got unexpected plan from when clause 3"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ganglionar(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'hipertrofiaganglionarpergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.ganglionar: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2, 3):
              print("Paciente nao foi diagnosticado com nenhuma doenca")
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ganglionar1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'hipertrofiaganglionarpergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.ganglionar1: got unexpected plan from when clause 1"
            engine.get_ke('questionsdoenca', 'manchapergunta').reset()
            with engine.prove(rule.rule_base.root_name, 'manchas', context,
                              ()) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "rules.ganglionar1: got unexpected plan from when clause 3"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def parteintensa(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'hipertrofiaganglionarpergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.parteintensa: got unexpected plan from when clause 1"
            print("Diagnosticado com zika")
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def parteintensa1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'hipertrofiaganglionarpergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.parteintensa1: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2, 3):
              engine.get_ke('questionsdoenca', 'manchapergunta').reset()
              with engine.prove(rule.rule_base.root_name, 'manchas', context,
                                ()) \
                as gen_4:
                for x_4 in gen_4:
                  assert x_4 is None, \
                    "rules.parteintensa1: got unexpected plan from when clause 4"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def manchas(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'manchapergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.manchas: got unexpected plan from when clause 1"
            print("Diagnosticado com zika")
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def manchas1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'manchapergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.manchas1: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1, 3):
              print("Paciente nao foi diagnosticado com nenhuma doenca")
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def dicrisia1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'discrasiahemorragicapergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.dicrisia1: got unexpected plan from when clause 1"
            engine.get_ke('questionsdoenca','frequenciadormusculospergunta').reset()
            with engine.prove(rule.rule_base.root_name, 'dormusculosdengue', context,
                              ()) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "rules.dicrisia1: got unexpected plan from when clause 3"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def dormusculosdengue(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'frequenciadormusculospergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.dormusculosdengue: got unexpected plan from when clause 1"
            engine.get_ke('questionsdoenca', 'frequenciadorarticulacaopergunta').reset()
            with engine.prove(rule.rule_base.root_name, 'dorarticulacao', context,
                              ()) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "rules.dormusculosdengue: got unexpected plan from when clause 3"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def dorarticulacao(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'frequenciadorarticulacaopergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.dorarticulacao: got unexpected plan from when clause 1"
            print("Paciente diagnosticado com Dengue")
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def dorarticulacao1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'frequenciadorarticulacaopergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.dorarticulacao1: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1, 2):
              engine.get_ke('questionsdoenca', 'febrepergunta').reset()
              with engine.prove(rule.rule_base.root_name, 'febredengue', context,
                                ()) \
                as gen_4:
                for x_4 in gen_4:
                  assert x_4 is None, \
                    "rules.dorarticulacao1: got unexpected plan from when clause 4"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def febredengue(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'febrepergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.febredengue: got unexpected plan from when clause 1"
            print("Paciente diagnosticado com Dengue")
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def febredengue1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'febredengue', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.febredengue1: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2, 3):
              engine.get_ke('questionsdoenca', 'intensidadedorarticularpergunta').reset()
              with engine.prove(rule.rule_base.root_name, 'intensidadedorarticular', context,
                                ()) \
                as gen_4:
                for x_4 in gen_4:
                  assert x_4 is None, \
                    "rules.febredengue1: got unexpected plan from when clause 4"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def intensidadedorarticular(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'intensidadedorarticularpergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.intensidadedorarticular: got unexpected plan from when clause 1"
            print("Paciente diagnosticado com Dengue")
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def intensidadedorarticular1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'intensidadedorarticularpergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.intensidadedorarticular1: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1, 2):
              print("Paciente diagnosticado com Chinkungunya")
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def dormusculosdengue1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'frequenciadormusculospergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.dormusculosdengue1: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2, 3):
              engine.get_ke('questionsdoenca', 'edemadaarticulacaopergunta').reset()
              with engine.prove(rule.rule_base.root_name, 'edema', context,
                                ()) \
                as gen_4:
                for x_4 in gen_4:
                  assert x_4 is None, \
                    "rules.dormusculosdengue1: got unexpected plan from when clause 4"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def edema(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'edemadaarticulacaopergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.edema: got unexpected plan from when clause 1"
            engine.get_ke('questionsdoenca', 'intensidadedorarticularpergunta')
            with engine.prove(rule.rule_base.root_name, 'partintensidadedorarticulacao', context,
                              ()) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "rules.edema: got unexpected plan from when clause 3"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def edema1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'edemadaarticulacaopergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.edema1: got unexpected plan from when clause 1"
            engine.get_ke('questionsdoenca', 'intensidadedorarticularpergunta')
            with engine.prove(rule.rule_base.root_name, 'intentarticulacao', context,
                              ()) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "rules.edema1: got unexpected plan from when clause 3"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def partintensidadedorarticulacao(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'intensidadedorarticularpergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.partintensidadedorarticulacao: got unexpected plan from when clause 1"
            print("Paciente diagnosticado com Dengue")
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def partintensidadedorarticulacao1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'intensidadedorarticularpergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.partintensidadedorarticulacao1: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1, 2):
              engine.get_ke('questionsdoenca', 'frequenciadorarticulacaopergunta').reset()
              with engine.prove(rule.rule_base.root_name, 'frequencia', context,
                                ()) \
                as gen_4:
                for x_4 in gen_4:
                  assert x_4 is None, \
                    "rules.partintensidadedorarticulacao1: got unexpected plan from when clause 4"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def frequencia(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'frequenciadorarticulacaopergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.frequencia: got unexpected plan from when clause 1"
            print("Paciente diagnosticado com Dengue")
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def frequencia1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'frequenciadorarticulacaopergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.frequencia1: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1, 2):
              print("Paciente diagnosticado com Chinkungunya")
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def intentarticulacao(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'intensidadedorarticularpergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.intentarticulacao: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1, 2):
              print("Paciente diagnosticado com Chinkungunya")
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def intentarticulacao1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'intensidadedorarticularpergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.intentarticulacao1: got unexpected plan from when clause 1"
            engine.get_ke('questionsdoenca', 'frequenciadorarticulacaopergunta').reset()
            with engine.prove(rule.rule_base.root_name, 'frequencia', context,
                              ()) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "rules.intentarticulacao1: got unexpected plan from when clause 3"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def dicrisia2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'discrasiahemorragicapergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.dicrisia2: got unexpected plan from when clause 1"
            engine.get_ke('questionsdoenca', 'intensidadedormusculospergunta').reset()
            with engine.prove(rule.rule_base.root_name, 'intensidadedormusculos', context,
                              ()) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "rules.dicrisia2: got unexpected plan from when clause 3"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def intensidadedormusculos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'intensidadedormusculospergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.intensidadedormusculos: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2, 3):
              engine.get_ke('questionsdoenca', 'edemadaarticulacaopergunta').reset()
              with engine.prove(rule.rule_base.root_name, 'edemas', context,
                                ()) \
                as gen_4:
                for x_4 in gen_4:
                  assert x_4 is None, \
                    "rules.intensidadedormusculos: got unexpected plan from when clause 4"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def edemas(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'edemadaarticulacaopergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.edemas: got unexpected plan from when clause 1"
            print("Paciente diagnosticado com Chinkungunya")
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def edemas1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'edemadaarticulacaopergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.edemas1: got unexpected plan from when clause 1"
            engine.get_ke('questionsdoenca', 'intensidadedorarticularpergunta').reset()
            with engine.prove(rule.rule_base.root_name, 'dorarticular', context,
                              ()) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "rules.edemas1: got unexpected plan from when clause 3"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def dorarticular(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'intensidadedorarticularpergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.dorarticular: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1, 2):
              print("Paciente diagnosticado com Chinkungunya")
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def dorarticular1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'intensidadedorarticularpergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.dorarticular1: got unexpected plan from when clause 1"
            engine.get_ke('questionsdoenca', 'frequenciadorarticulacaopergunta').reset()
            with engine.prove(rule.rule_base.root_name, 'finalfrequenciaarticular', context,
                              ()) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "rules.dorarticular1: got unexpected plan from when clause 3"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def finalfrequenciaarticular(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'frequenciadorarticulacaopergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.finalfrequenciaarticular: got unexpected plan from when clause 1"
            print("Paciente diagnosticado com Dengue")
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def finalfrequenciaarticular1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'frequenciadorarticulacaopergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.finalfrequenciaarticular1: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1, 2):
              print("Paciente Diagnosticado com Chinkungunya")
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def intensidadedormusculos1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'intensidadedormusculospergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.intensidadedormusculos1: got unexpected plan from when clause 1"
            engine.get_ke('questionsdoenca', 'frequenciadorarticulacaopergunta').reset()
            with engine.prove(rule.rule_base.root_name, 'freq', context,
                              ()) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "rules.intensidadedormusculos1: got unexpected plan from when clause 3"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def freq(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'frequenciadorarticulacaopergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.freq: got unexpected plan from when clause 1"
            engine.get_ke('questionsdoenca', 'febrepergunta').reset()
            with engine.prove(rule.rule_base.root_name, 'febrechic', context,
                              ()) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "rules.freq: got unexpected plan from when clause 3"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def febrechic(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'febrepergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.febrechic: got unexpected plan from when clause 1"
            print("Paciente diagnosticado com Dengue")
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def febrechic1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'febrepergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.febrechic1: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2, 3):
              engine.get_ke('questionsdoenca', 'intensidadedorarticularpergunta')
              with engine.prove(rule.rule_base.root_name, 'dorart', context,
                                ()) \
                as gen_4:
                for x_4 in gen_4:
                  assert x_4 is None, \
                    "rules.febrechic1: got unexpected plan from when clause 4"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def freq1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'frequenciadorarticulacaopergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.freq1: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1, 2):
              engine.get_ke('questionsdoenca', 'febrepergunta').reset()
              with engine.prove(rule.rule_base.root_name, 'febree', context,
                                ()) \
                as gen_4:
                for x_4 in gen_4:
                  assert x_4 is None, \
                    "rules.freq1: got unexpected plan from when clause 4"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def febree(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'febrepergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.febree: got unexpected plan from when clause 1"
            print("Paciente diagnosticado com Chinkungunya")
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def febre1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'febrepergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.febre1: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1, 2):
              engine.get_ke('questionsdoenca', 'intensidadedorarticularpergunta')
              with engine.prove(rule.rule_base.root_name, 'dorart', context,
                                ()) \
                as gen_4:
                for x_4 in gen_4:
                  assert x_4 is None, \
                    "rules.febre1: got unexpected plan from when clause 4"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def dorart(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'intensidadedorarticularpergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.dorart: got unexpected plan from when clause 1"
            print("Paciente diagnosticado com Dengue")
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def dorart1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questionsdoenca', 'intensidadedorarticularpergunta', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.dorart1: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1, 2):
              print("Paciente diagnosticado com Chinkungunya")
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('rules')
  
  bc_rule.bc_rule('knows_pattern_matching', This_rule_base, 'knows_pattern_matching',
                  knows_pattern_matching, None,
                  (),
                  (),
                  ())
  
  bc_rule.bc_rule('dicrisia', This_rule_base, 'dicrisia',
                  dicrisia, None,
                  (),
                  (),
                  (pattern.pattern_literal(3),))
  
  bc_rule.bc_rule('coceira', This_rule_base, 'coceira',
                  coceira, None,
                  (),
                  (),
                  (pattern.pattern_literal(1),))
  
  bc_rule.bc_rule('coceira1', This_rule_base, 'coceira',
                  coceira1, None,
                  (),
                  (),
                  (pattern.pattern_literal(2),))
  
  bc_rule.bc_rule('ganglionar', This_rule_base, 'ganglionar',
                  ganglionar, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('ganglionar1', This_rule_base, 'ganglionar',
                  ganglionar1, None,
                  (),
                  (),
                  (pattern.pattern_literal(1),))
  
  bc_rule.bc_rule('parteintensa', This_rule_base, 'parteintensa',
                  parteintensa, None,
                  (),
                  (),
                  (pattern.pattern_literal(1),))
  
  bc_rule.bc_rule('parteintensa1', This_rule_base, 'parteintensa',
                  parteintensa1, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('manchas', This_rule_base, 'manchas',
                  manchas, None,
                  (),
                  (),
                  (pattern.pattern_literal(2),))
  
  bc_rule.bc_rule('manchas1', This_rule_base, 'manchas',
                  manchas1, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('dicrisia1', This_rule_base, 'dicrisia',
                  dicrisia1, None,
                  (),
                  (),
                  (pattern.pattern_literal(1),))
  
  bc_rule.bc_rule('dormusculosdengue', This_rule_base, 'dormusculosdengue',
                  dormusculosdengue, None,
                  (),
                  (),
                  (pattern.pattern_literal(1),))
  
  bc_rule.bc_rule('dorarticulacao', This_rule_base, 'dorarticulacao',
                  dorarticulacao, None,
                  (),
                  (),
                  (pattern.pattern_literal(3),))
  
  bc_rule.bc_rule('dorarticulacao1', This_rule_base, 'dorarticulacao',
                  dorarticulacao1, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('febredengue', This_rule_base, 'febredengue',
                  febredengue, None,
                  (),
                  (),
                  (pattern.pattern_literal(1),))
  
  bc_rule.bc_rule('febredengue1', This_rule_base, 'febredengue',
                  febredengue1, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('intensidadedorarticular', This_rule_base, 'intensidadedorarticular',
                  intensidadedorarticular, None,
                  (),
                  (),
                  (pattern.pattern_literal(3),))
  
  bc_rule.bc_rule('intensidadedorarticular1', This_rule_base, 'intensidadedorarticular',
                  intensidadedorarticular1, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('dormusculosdengue1', This_rule_base, 'dormusculosdengue',
                  dormusculosdengue1, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('edema', This_rule_base, 'edema',
                  edema, None,
                  (),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('edema1', This_rule_base, 'edema',
                  edema1, None,
                  (),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('partintensidadedorarticulacao', This_rule_base, 'partintensidadedorarticulacao',
                  partintensidadedorarticulacao, None,
                  (),
                  (),
                  (pattern.pattern_literal(3),))
  
  bc_rule.bc_rule('partintensidadedorarticulacao1', This_rule_base, 'partintensidadedorarticulacao',
                  partintensidadedorarticulacao1, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('frequencia', This_rule_base, 'frequencia',
                  frequencia, None,
                  (),
                  (),
                  (pattern.pattern_literal(3),))
  
  bc_rule.bc_rule('frequencia1', This_rule_base, 'frequencia',
                  frequencia1, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('intentarticulacao', This_rule_base, 'intentarticulacao',
                  intentarticulacao, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('intentarticulacao1', This_rule_base, 'intentarticulacao',
                  intentarticulacao1, None,
                  (),
                  (),
                  (pattern.pattern_literal(3),))
  
  bc_rule.bc_rule('dicrisia2', This_rule_base, 'dicrisia',
                  dicrisia2, None,
                  (),
                  (),
                  (pattern.pattern_literal(2),))
  
  bc_rule.bc_rule('intensidadedormusculos', This_rule_base, 'intensidadedormusculos',
                  intensidadedormusculos, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('edemas', This_rule_base, 'edemas',
                  edemas, None,
                  (),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('edemas1', This_rule_base, 'edemas',
                  edemas1, None,
                  (),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('dorarticular', This_rule_base, 'dorarticular',
                  dorarticular, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('dorarticular1', This_rule_base, 'dorarticular',
                  dorarticular1, None,
                  (),
                  (),
                  (pattern.pattern_literal(3),))
  
  bc_rule.bc_rule('finalfrequenciaarticular', This_rule_base, 'finalfrequenciaarticular',
                  finalfrequenciaarticular, None,
                  (),
                  (),
                  (pattern.pattern_literal(3),))
  
  bc_rule.bc_rule('finalfrequenciaarticular1', This_rule_base, 'finalfrequenciaarticular',
                  finalfrequenciaarticular1, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('intensidadedormusculos1', This_rule_base, 'intensidadedormusculos',
                  intensidadedormusculos1, None,
                  (),
                  (),
                  (pattern.pattern_literal(1),))
  
  bc_rule.bc_rule('freq', This_rule_base, 'freq',
                  freq, None,
                  (),
                  (),
                  (pattern.pattern_literal(3),))
  
  bc_rule.bc_rule('febrechic', This_rule_base, 'febrechic',
                  febrechic, None,
                  (),
                  (),
                  (pattern.pattern_literal(1),))
  
  bc_rule.bc_rule('febrechic1', This_rule_base, 'febrechic',
                  febrechic1, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('freq1', This_rule_base, 'freq',
                  freq1, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('febree', This_rule_base, 'febree',
                  febree, None,
                  (),
                  (),
                  (pattern.pattern_literal(3),))
  
  bc_rule.bc_rule('febre1', This_rule_base, 'febree',
                  febre1, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('dorart', This_rule_base, 'dorart',
                  dorart, None,
                  (),
                  (),
                  (pattern.pattern_literal(3),))
  
  bc_rule.bc_rule('dorart1', This_rule_base, 'dorart',
                  dorart1, None,
                  (),
                  (),
                  (contexts.variable('ans'),))


Krb_filename = '../rules.krb'
Krb_lineno_map = (
    ((14, 18), (2, 2)),
    ((20, 20), (4, 4)),
    ((21, 26), (5, 5)),
    ((39, 43), (10, 10)),
    ((45, 50), (12, 12)),
    ((51, 51), (13, 13)),
    ((52, 57), (14, 14)),
    ((70, 74), (17, 17)),
    ((76, 81), (19, 19)),
    ((82, 82), (20, 20)),
    ((83, 88), (21, 21)),
    ((101, 105), (24, 24)),
    ((107, 112), (26, 26)),
    ((113, 113), (27, 27)),
    ((114, 119), (28, 28)),
    ((132, 136), (32, 32)),
    ((138, 143), (34, 34)),
    ((144, 144), (35, 35)),
    ((145, 145), (36, 36)),
    ((158, 162), (39, 39)),
    ((164, 169), (41, 41)),
    ((170, 170), (42, 42)),
    ((171, 176), (43, 43)),
    ((189, 193), (47, 47)),
    ((195, 200), (49, 49)),
    ((201, 201), (50, 50)),
    ((214, 218), (53, 53)),
    ((220, 225), (55, 55)),
    ((226, 226), (56, 56)),
    ((227, 227), (57, 57)),
    ((228, 233), (58, 58)),
    ((246, 250), (61, 61)),
    ((252, 257), (63, 63)),
    ((258, 258), (64, 64)),
    ((271, 275), (67, 67)),
    ((277, 282), (69, 69)),
    ((283, 283), (70, 70)),
    ((284, 284), (71, 71)),
    ((297, 301), (78, 78)),
    ((303, 308), (80, 80)),
    ((309, 309), (81, 81)),
    ((310, 315), (82, 82)),
    ((328, 332), (85, 85)),
    ((334, 339), (87, 87)),
    ((340, 340), (88, 88)),
    ((341, 346), (89, 89)),
    ((359, 363), (92, 92)),
    ((365, 370), (94, 94)),
    ((371, 371), (95, 95)),
    ((384, 388), (98, 98)),
    ((390, 395), (100, 100)),
    ((396, 396), (101, 101)),
    ((397, 397), (102, 102)),
    ((398, 403), (103, 103)),
    ((416, 420), (108, 108)),
    ((422, 427), (110, 110)),
    ((428, 428), (111, 111)),
    ((441, 445), (114, 114)),
    ((447, 452), (116, 116)),
    ((453, 453), (117, 117)),
    ((454, 454), (118, 118)),
    ((455, 460), (119, 119)),
    ((473, 477), (122, 122)),
    ((479, 484), (124, 124)),
    ((485, 485), (125, 125)),
    ((498, 502), (128, 128)),
    ((504, 509), (130, 130)),
    ((510, 510), (131, 131)),
    ((511, 511), (132, 132)),
    ((524, 528), (136, 136)),
    ((530, 535), (138, 138)),
    ((536, 536), (139, 139)),
    ((537, 537), (140, 140)),
    ((538, 543), (141, 141)),
    ((556, 560), (144, 144)),
    ((562, 567), (146, 146)),
    ((568, 568), (147, 147)),
    ((569, 574), (148, 148)),
    ((587, 591), (151, 151)),
    ((593, 598), (153, 153)),
    ((599, 599), (154, 154)),
    ((600, 605), (155, 155)),
    ((618, 622), (160, 160)),
    ((624, 629), (162, 162)),
    ((630, 630), (163, 163)),
    ((643, 647), (167, 167)),
    ((649, 654), (169, 169)),
    ((655, 655), (170, 170)),
    ((656, 656), (171, 171)),
    ((657, 662), (172, 172)),
    ((675, 679), (176, 176)),
    ((681, 686), (178, 178)),
    ((687, 687), (179, 179)),
    ((700, 704), (182, 182)),
    ((706, 711), (184, 184)),
    ((712, 712), (185, 185)),
    ((713, 713), (186, 186)),
    ((726, 730), (190, 190)),
    ((732, 737), (192, 192)),
    ((738, 738), (193, 193)),
    ((739, 739), (194, 194)),
    ((752, 756), (198, 198)),
    ((758, 763), (200, 200)),
    ((764, 764), (201, 201)),
    ((765, 770), (202, 202)),
    ((783, 787), (207, 207)),
    ((789, 794), (209, 209)),
    ((795, 795), (210, 210)),
    ((796, 801), (211, 211)),
    ((814, 818), (214, 214)),
    ((820, 825), (216, 216)),
    ((826, 826), (217, 217)),
    ((827, 827), (218, 218)),
    ((828, 833), (219, 219)),
    ((846, 850), (222, 222)),
    ((852, 857), (224, 224)),
    ((858, 858), (225, 225)),
    ((871, 875), (229, 229)),
    ((877, 882), (231, 231)),
    ((883, 883), (232, 232)),
    ((884, 889), (233, 233)),
    ((902, 906), (236, 236)),
    ((908, 913), (238, 238)),
    ((914, 914), (239, 239)),
    ((915, 915), (240, 240)),
    ((928, 932), (243, 243)),
    ((934, 939), (245, 245)),
    ((940, 940), (246, 246)),
    ((941, 946), (247, 247)),
    ((959, 963), (250, 250)),
    ((965, 970), (252, 252)),
    ((971, 971), (253, 253)),
    ((984, 988), (256, 256)),
    ((990, 995), (258, 258)),
    ((996, 996), (259, 259)),
    ((997, 997), (260, 260)),
    ((1010, 1014), (264, 264)),
    ((1016, 1021), (266, 266)),
    ((1022, 1022), (267, 267)),
    ((1023, 1028), (268, 268)),
    ((1041, 1045), (271, 271)),
    ((1047, 1052), (273, 273)),
    ((1053, 1053), (274, 274)),
    ((1054, 1059), (275, 275)),
    ((1072, 1076), (278, 278)),
    ((1078, 1083), (280, 280)),
    ((1084, 1084), (281, 281)),
    ((1097, 1101), (284, 284)),
    ((1103, 1108), (286, 286)),
    ((1109, 1109), (287, 287)),
    ((1110, 1110), (288, 288)),
    ((1111, 1116), (289, 289)),
    ((1129, 1133), (292, 292)),
    ((1135, 1140), (294, 294)),
    ((1141, 1141), (295, 295)),
    ((1142, 1142), (296, 296)),
    ((1143, 1148), (297, 297)),
    ((1161, 1165), (300, 300)),
    ((1167, 1172), (302, 302)),
    ((1173, 1173), (303, 303)),
    ((1186, 1190), (306, 306)),
    ((1192, 1197), (308, 308)),
    ((1198, 1198), (309, 309)),
    ((1199, 1199), (310, 310)),
    ((1200, 1205), (311, 311)),
    ((1218, 1222), (314, 314)),
    ((1224, 1229), (316, 316)),
    ((1230, 1230), (317, 317)),
    ((1243, 1247), (321, 321)),
    ((1249, 1254), (323, 323)),
    ((1255, 1255), (324, 324)),
    ((1256, 1256), (325, 325)),
)
