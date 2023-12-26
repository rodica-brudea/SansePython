from pyradios import RadioBrowser


def radio(*args):
    rb = RadioBrowser()
    print(rb.search(name="BBC Radio 1", name_exact=True))
