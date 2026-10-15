"""Draw constituency parse trees as PNG files with matplotlib (no graphviz needed)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from nltk import Tree

LEAF_W = 1.35   # horizontal space per leaf
LEVEL_H = 1.0   # vertical space per level

def layout(t, x0=0.0):
    """Return (node_positions, width) for tree t. Leaves are spaced evenly; parents sit above the middle of their children."""
    if isinstance(t, str):
        return [(t, x0 + LEAF_W / 2, 0, True)], LEAF_W
    nodes, width = [], 0.0
    child_x = []
    for child in t:
        sub, w = layout(child, x0 + width)
        nodes += sub
        child_x.append(sub[0][1])
        width += w
    depth = max(n[2] for n in nodes) + 1
    x = (child_x[0] + child_x[-1]) / 2 if len(child_x) > 1 else child_x[0]
    return [(t.label(), x, depth, False)] + nodes, width

def draw(bracketed, path, title):
    t = Tree.fromstring(bracketed)
    nodes, width = layout(t)
    # positions by object identity: rebuild with parent links
    fig_w = max(4, width * 1.05)
    fig_h = max(3, (t.height() + 0.5) * 0.95)
    fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=160)
    ax.set_xlim(0, width); ax.set_ylim(-0.6, t.height() - 0.4); ax.axis("off")
    # draw recursively so edges connect the right nodes
    def rec(sub, x0):
        if isinstance(sub, str):
            x = x0 + LEAF_W / 2
            ax.text(x, 0, sub, ha="center", va="center", fontsize=12, style="italic",
                    bbox=dict(boxstyle="round,pad=0.25", fc="#f3efe6", ec="#9a8c6f", lw=0.8))
            return x, 0, LEAF_W
        xs, ys, w = [], [], 0.0
        for c in sub:
            cx, cy, cw = rec(c, x0 + w); xs.append(cx); ys.append(cy); w += cw
        y = max(ys) + 1
        x = (xs[0] + xs[-1]) / 2
        for cx, cy in zip(xs, ys):
            ax.plot([x, cx], [y - 0.18, cy + 0.22], color="#6b6b6b", lw=1.1, zorder=1)
        ax.text(x, y, sub.label(), ha="center", va="center", fontsize=12, weight="bold", color="#1f3a3d", zorder=2,
                bbox=dict(boxstyle="round,pad=0.22", fc="white", ec="#1f3a3d", lw=0.9))
        return x, y, w
    rec(t, 0.0)
    ax.set_title(title, fontsize=11, loc="left", color="#333333", pad=8)
    fig.tight_layout()
    fig.savefig(path, facecolor="white")
    plt.close(fig)
    return t

TREES = {
 "tree1_government_raised_interest_rates.png": (
    "(S (NP (Det The) (N government)) (VP (V raised) (NP (N interest) (N rates))))",
    "1. The government raised interest rates."),
 "tree2_internet_gives_everyone_a_voice.png": (
    "(S (NP (Det The) (N internet)) (VP (V gives) (NP (N everyone)) (NP (Det a) (N voice))))",
    "2. The internet gives everyone a voice."),
 "tree3a_man_saw_dog_with_telescope_VP_attachment.png": (
    "(S (NP (Det The) (N man)) (VP (V saw) (NP (Det the) (N dog)) (PP (P with) (NP (Det the) (N telescope)))))",
    "3a. The man saw the dog with the telescope. (PP attached to VP: the man used the telescope)"),
 "tree3b_man_saw_dog_with_telescope_NP_attachment.png": (
    "(S (NP (Det The) (N man)) (VP (V saw) (NP (Det the) (N dog) (PP (P with) (NP (Det the) (N telescope))))))",
    "3b. The man saw the dog with the telescope. (PP attached to NP: the dog has the telescope)"),
}
if __name__ == "__main__":
    for fn, (br, title) in TREES.items():
        t = draw(br, fn, title)
        print(fn, "leaves:", " ".join(t.leaves()))
