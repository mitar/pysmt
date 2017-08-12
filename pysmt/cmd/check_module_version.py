import sys

if __name__ == "__main__":
    assert len(sys.argv) == 2
    module = sys.argv[1]

    try:
        if module == "z3":
            import z3
            (major, minor, ver, _) = z3.get_version()
            version = "%d.%d.%d" % (major, minor, ver)
            print(version)
            sys.stderr.write("version\n")
        else:
            print("ERROR")
    except ImportError:
        print("ERROR")
