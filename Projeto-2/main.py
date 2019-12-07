import sys
from pyke import knowledge_engine, krb_traceback

engine = knowledge_engine.engine(__file__)
engine.reset()
try:
    engine.activate('rules')
    engine.prove_1_goal('rules.knows_pattern_matching()')
except Exception:
    krb_traceback.print_exc()
    sys.exit(1)

