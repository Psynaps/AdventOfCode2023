import math

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]


def count_difference(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count


empty_rows = []
for i, line in enumerate(lines):
    if line == "":
        empty_rows.append(i)
empty_rows.append(len(lines))
sum = 0

for i in range(len(empty_rows)):
    begin_row = 0 if i == 0 else empty_rows[i - 1] + 1
    cols = []
    rows = lines[begin_row : empty_rows[i]]
    for i in range(len(rows[0])):
        cols.append("".join([row[i] for row in rows]))
    # print(rows)
    # print(cols)

    for mirror_row_index in range(1, len(rows)):
        # check if rows before i are the same as the first i rows after i
        # any row that doesn't have a corresponding row in range does not have to be checked
        found_match = True
        sum_row_diff = 0
        for i in range(min(len(rows) - mirror_row_index, mirror_row_index)):
            row_diff = count_difference(
                rows[mirror_row_index - i - 1], rows[i + mirror_row_index]
            )
            sum_row_diff += row_diff
            if sum_row_diff > 1:
                found_match = False
                break
        if found_match and sum_row_diff == 1:
            sum += mirror_row_index * 100
            # print("row match:", mirror_row_index)
            break
        else:
            found_match = False
    if not found_match:
        # print("No row mirror found")
        for mirror_col_index in range(1, len(cols)):
            # check if cols before i are the same as the first i cols after i
            # any col that doesn't have a corresponding col in range does not have to be checked
            sum_col_diff = 0
            found_match = True
            for i in range(min(len(cols) - mirror_col_index, mirror_col_index)):
                col_diff = count_difference(
                    cols[mirror_col_index - i - 1], cols[i + mirror_col_index]
                )
                sum_col_diff += col_diff
                if sum_col_diff > 1:
                    found_match = False
                    break
            if found_match and sum_col_diff == 1:
                sum += mirror_col_index
                # print("row match:", mirror_row_index)
                break

print(sum)
