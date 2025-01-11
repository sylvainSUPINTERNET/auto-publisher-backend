import re

def timestr_to_ms(timestr):
    """
    Convert format srt "H:MM:SS.ssssss" in ms (int).
    Ex : "0:00:33.639000" -> 33639
    """
    pattern = r"^(?P<h>\d+):(?P<m>\d+):(?P<s>\d+(?:\.\d+)?)$"
    match = re.match(pattern, timestr)
    if not match:
        raise ValueError(f"Format invalid : '{timestr}'")

    h = int(match.group("h"))
    m = int(match.group("m"))
    s = float(match.group("s"))

    total_seconds = h * 3600 + m * 60 + s
    total_ms = int(total_seconds * 1000)
    return total_ms