"""
A mish-mash of chalky, rich & fontawesome.
"""


# console
# err_console.print("Here is something written to standard error")
# total = 0
# table = Table("Name", "Item")
# table.add_row("Rick", "Portal Gun")
# table.add_row("Morty", "Plumbus")
# console.print(table)

# spinner, txt prog
# with Progress(
#     SpinnerColumn(),
#     TextColumn("[progress.description]{task.description}"),
#     transient=True,
# ) as progress:
#     progress.add_task(description="Processing...", total=None)
#     progress.add_task(description="Preparing...", total=None)
#     time.sleep(5)

# # loading
# for value in track(range(100), description="Processing..."):
#     # Fake processing time
#     time.sleep(0.01)
#     total += 1
# print(f"Processed {total} things.")

import fontawesome as fai
from chalky import Chalk, bg, fg, hex
from chalky.color import Color
from chalky.style import Style

# Too much custom
ghost = hex("#f8f8ff", background=False)
gray65 = hex("#a6a6a6", background=False)
gray09 = hex("#171717")

# Composition
fg = {
    "w": gray65,  # Chalk(foreground=Color.WHITE),
    "g": Chalk(foreground=Color.BRIGHT_GREEN),
    "r": Chalk(foreground=Color.RED),
    "b": Chalk(foreground=Color.BLUE),
}

bg = {"g9": gray09}

weight = {
    "it": Chalk(style={Style.ITALIC}),
    "b": Chalk(style={Style.BOLD}),
    "s": Chalk(style={Style.STRIKETHROUGH}),
    "t": Chalk(style={Style.SLOW_BLINK}),
}

# print(custom_rgb | "Potential link text")
# print(custom_hex | "Black on green text")

# Exports
get_andlog_fmt = lambda: fg["b"] & weight["b"]
get_orlog_fmt = lambda: fg["g"] + weight["b"] + bg["g9"]
