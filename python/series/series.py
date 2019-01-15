def slices(series, length):
    series_len = len(series)
    if series_len == 0:
        raise ValueError("input series is null")
    if length <= 0:
        raise ValueError("input length is invalid")
    if series_len < length:
        raise ValueError("slice length is large than series length")
        
    return [series[i:i+length] for i in range(0,series_len-length+1)]

