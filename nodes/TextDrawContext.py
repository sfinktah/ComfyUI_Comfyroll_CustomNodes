class TextDrawContext:
    def __init__(self, draw, font, text_lines, max_text_width, max_text_height,
                 image_width, image_height, margins, line_spacing,
                 position_x, position_y, align, justify, rotation_angle, rotation_options):
        self.draw = draw
        self.font = font
        self.text_lines = text_lines
        self.max_text_width = max_text_width
        self.max_text_height = max_text_height
        self.image_width = image_width
        self.image_height = image_height
        self.margins = margins
        self.line_spacing = line_spacing
        self.position_x = position_x
        self.position_y = position_y
        self.align = align
        self.justify = justify
        self.rotation_angle = rotation_angle
        self.rotation_options = rotation_options
