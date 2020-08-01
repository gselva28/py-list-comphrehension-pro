text = [99, 'no data', 95, 94, 'no data']
def foo(text):
    return([i if not isinstance(i, str) else 0 for i in text])