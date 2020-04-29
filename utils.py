import numpy as np
import textwrap

TOOLTIP_TEMPLATE = """
    <div style="width:200px;">
    %{text}
    </div>
    """

COLOR_PALETTE_20 = np.array(["#c76029", "#7366d9", "#8ab938", "#be5ec5", "#4fb956",
                             "#d04c90", "#61c598", "#d5433c", "#47afd1", "#d79a34",
                             "#665aa3", "#b2af51", "#8291da", "#5a8234", "#d24461",
                             "#358562", "#b76d98", "#836b2c", "#be665f", "#d9996b"])

def create_tooltip(cell):
    wrapper = textwrap.TextWrapper(width=70)

    dedented_text = textwrap.dedent(text=str(cell))
    shortened = textwrap.shorten(text=dedented_text, width=280)
    shortened_wrapped = wrapper.fill(text=shortened)

    return shortened_wrapped
