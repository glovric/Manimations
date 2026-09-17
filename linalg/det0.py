from manim import *
import numpy as np


class DeterminantZero(Scene):
    def construct(self):

        # =========================================================
        # TITLE
        # =========================================================

        title = Text(
            "When the Determinant is Zero",
            font_size=36
        )
        title.to_edge(UP)

        self.play(Write(title))
        self.wait(1)

        # =========================================================
        # COORDINATE PLANE
        # =========================================================

        plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            background_line_style={
                "stroke_color": BLUE_C,
                "stroke_width": 2,
                "stroke_opacity": 0.7
            },
            axis_config={
                "stroke_color": WHITE,
                "stroke_width": 2
            },
            faded_line_ratio=0
        )

        self.play(
            Create(plane),
            run_time=2
        )

        # =========================================================
        # MATRIX
        # =========================================================

        matrix = np.array([
            [1, 1],
            [2, 2]
        ])

        matrix_tex = MathTex(
            r"""A =
            \begin{pmatrix}
            1 & 1 \\
            2 & 2
            \end{pmatrix}"""
        )

        matrix_tex.scale(0.9)
        matrix_tex.to_corner(UL)

        self.play(
            Write(matrix_tex)
        )

        self.wait(1)

        # =========================================================
        # ORIGINAL UNIT SQUARE
        # =========================================================

        square = Polygon(
            ORIGIN,
            RIGHT,
            RIGHT + UP,
            UP,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=0.4,
            stroke_width=4
        )

        self.play(
            Create(square)
        )

        # =========================================================
        # AREA LABEL
        # =========================================================

        area_label = MathTex(
            r"\text{Area} = 1"
        )

        area_label.scale(0.7)
        area_label.next_to(
            square,
            RIGHT,
            buff=0.3
        )

        self.play(
            Write(area_label)
        )

        # =========================================================
        # BASIS VECTORS
        # =========================================================

        i_hat = Arrow(
            ORIGIN,
            RIGHT,
            color=RED,
            buff=0
        )

        j_hat = Arrow(
            ORIGIN,
            UP,
            color=GREEN,
            buff=0
        )

        i_label = MathTex(
            r"\hat{i}",
            color=RED
        ).next_to(
            i_hat.get_end(),
            DOWN,
            buff=0.15
        )

        j_label = MathTex(
            r"\hat{j}",
            color=GREEN
        ).next_to(
            j_hat.get_end(),
            LEFT,
            buff=0.15
        )

        self.play(
            Create(i_hat),
            Create(j_hat),
            Write(i_label),
            Write(j_label)
        )

        self.wait(1)

        # =========================================================
        # TRANSFORMATION FUNCTION
        # =========================================================

        def transform_point(point):
            x, y = point[0], point[1]

            new_x = (
                matrix[0, 0] * x +
                matrix[0, 1] * y
            )

            new_y = (
                matrix[1, 0] * x +
                matrix[1, 1] * y
            )

            return np.array([
                new_x,
                new_y,
                0
            ])

        # =========================================================
        # CREATE TRANSFORMED OBJECTS
        # =========================================================

        # Transform the entire grid
        transformed_plane = plane.copy()
        transformed_plane.apply_function(
            transform_point
        )

        # Transform the square
        transformed_square = square.copy()
        transformed_square.apply_function(
            transform_point
        )

        # Transform basis vectors
        i_transformed = matrix @ np.array([1, 0])
        j_transformed = matrix @ np.array([0, 1])

        i_target = Arrow(
            ORIGIN,
            i_transformed[0] * RIGHT +
            i_transformed[1] * UP,
            color=RED,
            buff=0
        )

        j_target = Arrow(
            ORIGIN,
            j_transformed[0] * RIGHT +
            j_transformed[1] * UP,
            color=GREEN,
            buff=0
        )

        # =========================================================
        # REMOVE AREA LABEL
        # =========================================================

        self.play(
            FadeOut(area_label)
        )

        # =========================================================
        # SQUISH THE ENTIRE PLANE
        # =========================================================

        self.play(
            Transform(
                plane,
                transformed_plane
            ),
            Transform(
                square,
                transformed_square
            ),
            Transform(
                i_hat,
                i_target
            ),
            Transform(
                j_hat,
                j_target
            ),
            run_time=4,
            rate_func=smooth
        )

        self.wait(2)

        # =========================================================
        # HIGHLIGHT THE COLLAPSED LINE
        # =========================================================

        collapsed_line = Line(
            -4 * RIGHT - 8 * UP,
            4 * RIGHT + 8 * UP,
            color=YELLOW,
            stroke_width=5
        )

        self.play(
            Create(collapsed_line),
            run_time=1.5
        )

        self.wait(1)

        # =========================================================
        # SHOW THAT BOTH BASIS VECTORS ARE ON SAME LINE
        # =========================================================

        same_direction = MathTex(
            r"A\hat{i} = A\hat{j}"
        )

        same_direction.scale(0.9)
        same_direction.to_edge(DOWN)

        self.play(
            Write(same_direction)
        )

        self.wait(2)

        # =========================================================
        # DETERMINANT CALCULATION
        # =========================================================

        determinant = MathTex(
            r"\det(A)"
            r"="
            r"(1)(2)-(1)(2)"
            r"="
            r"0"
        )

        determinant.scale(1.0)
        determinant.to_edge(DOWN)

        self.play(
            Transform(
                same_direction,
                determinant
            ),
            run_time=2
        )

        self.wait(2)

        # =========================================================
        # AREA = ZERO
        # =========================================================

        zero_area = MathTex(
            r"\boxed{\text{Area} = 0}"
        )

        zero_area.scale(1.1)
        zero_area.set_color(YELLOW)
        zero_area.to_edge(DOWN)

        self.play(
            Transform(
                same_direction,
                zero_area
            ),
            run_time=1.5
        )

        self.wait(2)

        # =========================================================
        # FINAL MESSAGE
        # =========================================================

        final_text = Text(
            "The entire 2D space has been squished onto a line!",
            font_size=25,
            color=YELLOW
        )

        final_text.to_edge(DOWN)

        self.play(
            Transform(
                same_direction,
                final_text
            ),
            run_time=1.5
        )

        self.wait(3)
