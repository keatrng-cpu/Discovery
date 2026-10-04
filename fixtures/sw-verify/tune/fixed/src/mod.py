def parse_ratio(s):
    """'3:4' -> 0.75"""
    a, b = s.split(":")
    return int(a) / int(b)
