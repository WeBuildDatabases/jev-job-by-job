"""Runs the round-3 remedy tests (R01, R11) into the same results files. Usage: python run_stress.py [R01 ...]"""
import hashlib, json, sys
import run_all, t_remedy

lock = run_all.OUT / 'PREREGISTERED-ROUND3.json'
if not lock.exists():
    lock.write_text(json.dumps({p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                                for p in sorted(run_all.HERE.glob('*.py'))}, indent=2))
run_all.TESTS = t_remedy.TESTS
run_all.main(set(a.upper() for a in sys.argv[1:]))
