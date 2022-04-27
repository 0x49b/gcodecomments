import base64

if __name__ == "__main__":
    with open(r'key.gcode', 'r') as f:
        lines = f.readlines()
        lines_filtered = []

        with open(r'key_c.gcode', 'w') as f2:
            for l in lines:
                if not l.startswith(";"):
                    if l != "\n":
                        lines_filtered.append(l)
                        f2.write(l)
            f2.close()
        lines_filtered2 = []

        for l in lines_filtered:
            if ';' in l:
                index = l.index(';')
                l = l[0:index]
                lines_filtered2.append(l[0:index] + '\n')
            else:
                lines_filtered2.append(l)

        with open(r'key_cleaned.gcode', 'w') as f3:
            for l in lines_filtered2:
                f3.write(l)
            f3.close()

        cache = ",".join(str(x) for x in lines_filtered2)
        cache = cache.replace('\n', '')

        with open(r'key_squashed', 'w') as f4:
            f4.write(cache)
            f4.close()

        with open(r'key_base64', 'w') as f5:
            encodedBytes = base64.b64encode(cache.encode("utf-8"))
            encodedStr = str(encodedBytes, "utf-8")
            f5.write(encodedStr)
            f5.close()

        f.close()
        print("Finished")
