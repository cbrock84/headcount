#!/usr/bin/env python3
"""Enforce US English spelling across the repository.

The author writes in US English, so the catalogue does too. This is a house style rule rather than
a correctness one, but it is the kind that decays without enforcement: a single skill written in
British spelling reads as though it came from somewhere else, which is exactly the impression a
repository of original work should not give.

  python3 scripts/check-us-english.py          report British spellings (CI)
  python3 scripts/check-us-english.py --fix    rewrite them in place

Only exact word forms are listed. Stems are a trap here: "analysis", "analyst", "specialist" and
"realistic" are correct US English and must never be rewritten, so `analyse` is listed and `analys`
is not.

One inflection is deliberately absent, per D33: the third-person form of the British verb is
spelled the same as the plural of "analysis", which is ordinary US English. Listing it flagged
correct prose, and `--fix` rewrote the noun into a verb — corrupting text rather than merely
reporting it. The British verb form is rare in this register; the noun plural is common.
"""
import os
import re
import sys

# British -> American. Exact forms only, matched on word boundaries.
PAIRS = {
    "programme": "program", "programmes": "programs",
    "licence": "license", "licences": "licenses", "licenced": "licensed",
    "behaviour": "behavior", "behaviours": "behaviors", "behavioural": "behavioral",
    "favour": "favor", "favours": "favors", "favoured": "favored",
    "favourable": "favorable", "favourite": "favorite",
    "colour": "color", "colours": "colors", "coloured": "colored",
    "honour": "honor", "honours": "honors", "labour": "labor",
    "analyse": "analyze", "analysed": "analyzed",
    "analysing": "analyzing",
    "organise": "organize", "organised": "organized", "organising": "organizing",
    "organisation": "organization", "organisations": "organizations",
    "organisational": "organizational",
    "prioritise": "prioritize", "prioritised": "prioritized",
    "prioritising": "prioritizing", "prioritisation": "prioritization",
    "optimise": "optimize", "optimised": "optimized", "optimising": "optimizing",
    "optimisation": "optimization",
    "recognise": "recognize", "recognised": "recognized", "recognising": "recognizing",
    "recognisable": "recognizable",
    "realise": "realize", "realised": "realized", "realising": "realizing",
    "realisation": "realization",
    "minimise": "minimize", "minimised": "minimized", "minimising": "minimizing",
    "minimisation": "minimization",
    "maximise": "maximize", "maximised": "maximized", "maximising": "maximizing",
    "standardise": "standardize", "standardised": "standardized",
    "standardising": "standardizing",
    "specialise": "specialize", "specialised": "specialized", "specialising": "specializing",
    "summarise": "summarize", "summarised": "summarized", "summarising": "summarizing",
    "authorise": "authorize", "authorised": "authorized", "authorising": "authorizing",
    "authorisation": "authorization",
    "customise": "customize", "customised": "customized",
    "utilise": "utilize", "utilised": "utilized", "utilising": "utilizing",
    "capitalise": "capitalize", "capitalised": "capitalized",
    "amortise": "amortize", "amortised": "amortized", "amortisation": "amortization",
    "pseudonymise": "pseudonymize", "pseudonymised": "pseudonymized",
    "pseudonymisation": "pseudonymization",
    "synthesise": "synthesize", "synthesised": "synthesized",
    "catalogue": "catalog", "catalogues": "catalogs", "catalogued": "cataloged",
    "artefact": "artifact", "artefacts": "artifacts",
    "judgement": "judgment", "judgements": "judgments",
    "acknowledgement": "acknowledgment", "acknowledgements": "acknowledgments",
    "ageing": "aging", "grey": "gray",
    "sceptic": "skeptic", "sceptical": "skeptical", "scepticism": "skepticism",
    "defence": "defense", "defences": "defenses",
    "offence": "offense", "offences": "offenses",
    "practise": "practice", "practised": "practiced", "practising": "practicing",
    "fulfilment": "fulfillment", "enrolment": "enrollment",
    "instalment": "installment", "instalments": "installments",
    "modelling": "modeling", "modelled": "modeled",
    "labelling": "labeling", "labelled": "labeled",
    "signalling": "signaling", "signalled": "signaled",
    "cancelling": "canceling", "cancelled": "canceled",
    "travelling": "traveling", "travelled": "traveled",
    "centre": "center", "centres": "centers", "centred": "centered",
    "whilst": "while", "amongst": "among",
    "learnt": "learned", "spelt": "spelled", "burnt": "burned",
    "manoeuvre": "maneuver", "cheque": "check",
}
WORD = re.compile(r"\b(" + "|".join(sorted(PAIRS, key=len, reverse=True)) + r")\b", re.I)

SKIP_DIRS = {".git", "node_modules", "__pycache__"}
# LICENSE is the canonical MIT text and is never rewritten. This file lists British spellings by
# definition, so it excludes itself the way check-provenance.py does.
SKIP_FILES = {"LICENSE", os.path.basename(__file__)}
TEXT_EXT = {".md", ".py", ".sh", ".json", ".yml", ".yaml", ".html", ".txt", ".mjs", ".js"}


def match_case(british, american):
    if british.isupper():
        return american.upper()
    if british[0].isupper():
        return american[0].upper() + american[1:]
    return american


def files():
    for root, dirs, names in os.walk("."):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for n in names:
            if n in SKIP_FILES or os.path.splitext(n)[1] not in TEXT_EXT:
                continue
            yield os.path.join(root, n)


def main():
    fix = "--fix" in sys.argv
    problems, changed = [], 0

    for path in sorted(files()):
        try:
            text = open(path, encoding="utf-8").read()
        except (UnicodeDecodeError, OSError):
            continue
        if not WORD.search(text):
            continue

        if fix:
            new = WORD.sub(lambda m: match_case(m.group(1), PAIRS[m.group(1).lower()]), text)
            if new != text:
                open(path, "w", encoding="utf-8").write(new)
                changed += 1
        else:
            for n, line in enumerate(text.splitlines(), 1):
                for m in WORD.finditer(line):
                    b = m.group(1)
                    problems.append(f"{path}:{n}: '{b}' -> '{match_case(b, PAIRS[b.lower()])}'")

    if fix:
        print(f"US English: rewrote {changed} file(s)")
        return 0
    for p in problems[:40]:
        print(f"  {p}")
    if len(problems) > 40:
        print(f"  … and {len(problems) - 40} more")
    print(f"US English: {len(problems)} British spelling(s)"
          + ("" if not problems else " — run: python3 scripts/check-us-english.py --fix"))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
