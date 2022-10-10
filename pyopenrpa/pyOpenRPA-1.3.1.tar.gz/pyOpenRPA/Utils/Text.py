import difflib

def SimilarityNoCase(in1Str, in2Str):
  normalized1 = in1Str.lower()
  normalized2 = in2Str.lower()
  matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
  return matcher.ratio()