from manim import *
import numpy as np


class Determinant(Scene):
    def construct(self):

        # =========================================================
        # TITLE
        # =========================================================

        title = Text(
            "What Does the Determinant Mean?",
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
            [2, 1],
            [1, 2]
        ])

        matrix_tex = MathTex(
            r"""A =
            \begin{pmatrix}
            2 & 1 \\
            1 & 2
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
            fill_opacity=0.35,
            stroke_width=4
        )

        square.move_to(
            ORIGIN + RIGHT * 0.5 + UP * 0.5,
            aligned_edge=ORIGIN
        )

        # The move_to above can be avoided by explicitly defining
        # the square from the origin:
        square = Polygon(
            ORIGIN,
            RIGHT,
            RIGHT + UP,
            UP,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=0.35,
            stroke_width=4
        )

        # =========================================================
        # LABEL UNIT SQUARE
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
            Create(square),
            Write(area_label)
        )

        self.wait(1)

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
        # TRANSFORM BASIS VECTORS
        # =========================================================

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

        self.play(
            Transform(i_hat, i_target),
            Transform(j_hat, j_target),
            run_time=2
        )

        # =========================================================
        # TRANSFORM THE SQUARE
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

        transformed_square = square.copy()
        transformed_square.apply_function(
            transform_point
        )

        # Remove old area label temporarily
        self.play(
            FadeOut(area_label)
        )

        # Transform square
        self.play(
            Transform(
                square,
                transformed_square
            ),
            run_time=3
        )

        self.wait(1)

        # =========================================================
        # SHOW NEW AREA
        # =========================================================

        new_area = MathTex(
            r"\text{New Area} = 3"
        )

        new_area.scale(0.8)
        new_area.set_color(YELLOW)
        new_area.to_edge(DOWN)

        self.play(
            Write(new_area)
        )

        self.wait(2)

        # =========================================================
        # DETERMINE AREA FROM MATRIX
        # =========================================================

        determinant_formula = MathTex(
            r"\det(A) = ad - bc"
        )

        determinant_formula.scale(1.0)
        determinant_formula.to_edge(DOWN)

        self.play(
            Transform(
                new_area,
                determinant_formula
            ),
            run_time=1.5
        )

        self.wait(1)

        # =========================================================
        # SUBSTITUTE VALUES
        # =========================================================

        determinant_calculation = MathTex(
            r"\det(A)"
            r"="
            r"(2)(2)-(1)(1)"
            r"="
            r"4-1"
            r"="
            r"\boxed{3}"
        )

        determinant_calculation.scale(0.9)
        determinant_calculation.to_edge(DOWN)

        self.play(
            Transform(
                new_area,
                determinant_calculation
            ),
            run_time=2
        )

        self.wait(2)

        # =========================================================
        # EXPLANATION
        # =========================================================

        explanation = Text(
            "The determinant tells us how area scales.",
            font_size=26,
            color=YELLOW
        )

        explanation.to_edge(DOWN)

        self.play(
            Transform(
                new_area,
                explanation
            ),
            run_time=1.5
        )

        self.wait(3)
