"""Runs the round-2 stress tests (S01-S21) into the same results files. Usage: python run_stress.py [S05 ...]"""
import hashlib, json, sys
import run_all, t_stress

lock = run_all.OUT / 'PREREGISTERED-ROUND2.json'
if not lock.exists():
    lock.write_text(json.dumps({p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                                for p in sorted(run_all.HERE.glob('*.py'))}, indent=2))
run_all.TESTS = t_stress.TESTS
run_all.main(set(a.upper() for a in sys.argv[1:]))
