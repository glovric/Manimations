from manim import *
from manim.scene.vector_space_scene import X_COLOR, Y_COLOR
import numpy as np

class MatrixTransformation(LinearTransformationScene):

    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False,
        )

    def construct(self):

        matrix = np.array([
            [2, 1],
            [1, 2]
        ])

        unit_vectors = [
            (np.array([1, 0]),  X_COLOR),
            (np.array([1, 1]) / np.sqrt(2), ORANGE),
            (np.array([0, 1]),   Y_COLOR),
            (np.array([-1, 1]) / np.sqrt(2), ORANGE),
            (np.array([-1, 0]),  X_COLOR),
            (np.array([-1, -1]) / np.sqrt(2), ORANGE),
            (np.array([0, -1]),   Y_COLOR),
            (np.array([1, -1]) / np.sqrt(2), ORANGE),
        ]

        vectors = [Vector(vec, color=color) for vec, color in unit_vectors]

        i_label = MathTex(
            r"\hat{i}",
            color=WHITE
        ).next_to(
            vectors[0].get_end(),
            DOWN,
            buff=0.15
        )

        matrix_tex = (
            MathTex( r"A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}")
            .scale(0.9)
            .to_corner(UL)
            .shift(DOWN)
        )

        title = (
            Text("Matrix Transforming a Vector Space", font_size=36)
            .to_edge(UP)
        )

        self.play(Write(title))
        self.wait(0.5)

        self.play(
            LaggedStart(
                *[GrowArrow(v) for v in vectors],
                lag_ratio=0.15,
            ),
            run_time=2,
        )

        self.play(Write(i_label))

        for v in vectors:
            self.add_vector(v)

        self.play(Write(matrix_tex))
        self.wait(1)

        self.apply_matrix(matrix)
        self.wait(1)
        # ---------------------------------------------------------
        # Add explanation
        # ---------------------------------------------------------
        explanation = VGroup(
            Text(
                "The matrix A:",
                font_size=24
            ),
            Text(
                "• Transforms the entire coordinate grid",
                font_size=20,
                color=YELLOW
            ),
            Text(
                "• Preserves linearity and origin",
                font_size=20,
                color=YELLOW
            )
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.3
        )

        explanation.to_corner(DR)

        self.play(
            Write(explanation)
        )

        self.wait(3)
