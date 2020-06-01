commentToken = "// "
ignoreList = ""

# TODO: feature: remove duplicate rules from result (use Sets?)

for file in ["ignore.list", "customIgnore.list"]:
    with open(file, "r") as f:
        for line in f:
            if not line.startswith(commentToken) and line.startswith('"'):
                if commentToken in line:
                    ignoreList += f"\n{line.split(commentToken)[0].strip()}"
                else:
                    ignoreList += f"\n{line.strip()}"

ignored = ""
lines = ""

for file in ["user.js", "custom.js"]:
    with open(file, "r") as f:
        for line in f:
            if line.startswith('user_pref("'):
                if (
                    '"{}"'.format(line.split('user_pref("')[1].split('"')[0])
                    not in ignoreList
                ):
                    if commentToken in line:
                        lines += f"\n\n{line.split(commentToken)[0].strip()}"
                    else:
                        lines += f"\n\n{line.strip()}"
                else:
                    ignored += f"\n\n{line.strip()}"


with open("CustomUser.js", "w") as f:
    f.write(lines)

with open("IgnoredUser.js", "w") as f:
    f.write(ignored)

