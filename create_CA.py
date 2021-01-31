import matplotlib.pyplot as plt
import matplotlib
import numpy as np
# matplotlib.use('Agg')


def init_array(n):
    arr = np.zeros(n, dtype=np.int)
    arr[n//2] = 1
    arr = np.reshape(arr, (1, -1))
    return arr


def create_binary_ruleset(ruleset):

    ruleset = bin(ruleset)
    ruleset = ruleset[2:]
    ruleset = [int(i) for i in ruleset]

    count = 0
    if len(ruleset) < 8:
        count = 8-len(ruleset)

    while count:
        ruleset = [0]+ruleset
        count -= 1

    return ruleset


def rules_simplified(l, c, r, ruleset):
    bin_rep = str(l)+str(c)+str(r)
    return ruleset[7-int(bin_rep, 2)]


def rules(l, c, r, ruleset):  # using ruleset n

    if l == 1 and c == 1 and r == 1:
        return ruleset[0]  # msb

    if l == 1 and c == 1 and r == 0:
        return ruleset[1]

    if l == 1 and c == 0 and r == 1:
        return ruleset[2]

    if l == 1 and c == 0 and r == 0:
        return ruleset[3]

    if l == 0 and c == 1 and r == 1:
        return ruleset[4]

    if l == 0 and c == 1 and r == 0:
        return ruleset[5]

    if l == 0 and c == 0 and r == 1:
        return ruleset[6]

    if l == 0 and c == 0 and r == 0:
        return ruleset[7]

    return 0


def compute_next_gen(grid_cell, time, rule_applied):

    # we will create a matrix where each row will represent a generation
    rows, cols = grid_cell.shape
    mat = np.zeros((time, cols), dtype=grid_cell.dtype)
    mat[0] = grid_cell

    for t in range(1, time):  # rows
        curr_gen = mat[t-1]

        for col in range(1, cols-1):
            left = curr_gen[col-1]
            right = curr_gen[col+1]
            curr = curr_gen[col]

            # mat[t][col] = rules(left, curr, right, rule_applied)
            mat[t][col] = rules_simplified(left, curr, right, rule_applied)

    return mat


cmap = plt.get_cmap('Greys')
plt.axis('off')
figure = plt.gcf()  # get current figure
figure.set_size_inches(16, 8)


def save_plot(ca, title="", path=""):
    plt.title("Ruleset " + title)
    plt.axis('off')
    plt.imshow(ca, interpolation='none', cmap=cmap)
    # when saving, specify the DPI
    # plt.savefig("myplot.png", dpi = 100)
    print(f"\nsaving file in file_path: {path}")
    plt.savefig(path, dpi=100, bbox_inches='tight')
    plt.cla()
    # plt.show()


def plot(ca, title=''):
    cmap = plt.get_cmap('Greys')
    plt.title("Ruleset " + title)
    plt.imshow(ca, interpolation='none', cmap=cmap)
    plt.show()


if __name__ == "__main__":
    ruleset = 193
    which_ruleset = create_binary_ruleset(ruleset)
    mat = compute_next_gen(init_array(200), 80, which_ruleset)
    # plot(mat, str(ruleset))
    save_plot(ca=mat, title=str(ruleset),
              path=str(ruleset)+'.png')
