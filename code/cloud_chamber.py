from PIL import Image


def support_grid(n):
    """
    Return an n by n grid for the positive-indexed support sequence.

    Entry k = a*b is marked by setting row[k-1] = 1.
    The flattened row is then reshaped row-by-row into an n by n bitmap.
    """
    row = [0] * (n * n)

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            row[a * b - 1] = 1

    return [row[i * n:(i + 1) * n] for i in range(n)]


def save_cloud_chamber(n, filename=None, scale=1, flip_vertical=False):
    """
    Save the square-grid display of the support sequence as a PNG.

    Black pixels mark integers k that occur as products a*b
    with 1 <= a,b <= n.
    """
    if filename is None:
        filename = f"support_n{n}.png"

    grid = support_grid(n)

    if flip_vertical:
        grid = grid[::-1]

    img = Image.new("L", (n, n), 255)
    pixels = img.load()

    for y in range(n):
        for x in range(n):
            if grid[y][x]:
                pixels[x, y] = 0

    if scale != 1:
        img = img.resize((n * scale, n * scale), Image.Resampling.NEAREST)

    img.save(filename)


if __name__ == "__main__":
    save_cloud_chamber(256, "support_n256.png")
