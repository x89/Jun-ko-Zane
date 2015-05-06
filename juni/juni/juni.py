class Juni:
    def __init__(self, ids):
        assert isinstance(ids, tuple), "We expected a list, we got %s" % type(ids)
        assert len(ids) == 2, "Wanted 2 ID values, got %i" % len(ids)
        self.ids. = ids
