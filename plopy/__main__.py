import plopy
if __name__ == '__main__':
    import sys
    for filename in sys.argv:
        if filename.endswith("__.py"):
            continue
        plopy.add_file(filename)
    plopy.start()
