from manim import *
from manim.scene.vector_space_scene import X_COLOR, Y_COLOR
import numpy as np

class Eigenvectors(LinearTransformationScene):

    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False,
            leave_ghost_vectors=True
        )

    def construct(self):

        matrix = np.array([
            [3, 1],
            [1, 3]
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

        matrix_tex = (
            MathTex( r"A = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}")
            .scale(0.9)
            .to_corner(UL)
            .shift(DOWN)
        )

        title = (
            Text("Eigenvectors", font_size=36)
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


        for v in vectors:
            self.add_vector(v)

        self.play(Write(matrix_tex))
        self.wait(1)

        self.apply_matrix(
            matrix
        )

        eigenvectors_start = [
            Vector(unit_vectors[1][0], color=BLUE),
            Vector(unit_vectors[3][0], color=BLUE)
        ]

        eigenvectors_end = [
            Vector(matrix @ unit_vectors[1][0], color=BLUE),
            Vector(matrix @ unit_vectors[3][0], color=BLUE)
        ]

        self.play(
            LaggedStart(
                *[GrowArrow(v) for v in eigenvectors_start],
                lag_ratio=0.15,
            ),
            run_time=2,
        )

        self.play(*[Transform(v1, v2) for v1, v2 in zip(eigenvectors_start, eigenvectors_end)])

        self.wait(1)

        note = Text(
            "Most vectors change direction AND length",
            font_size=24,
            color=YELLOW
        )
        note.to_edge(DOWN)

        self.play(
            Write(note),
            run_time=1
        )

        self.wait(2)

        eigen_note = Text(
            "Eigenvectors only stretch — they keep their direction!",
            font_size=24,
            color=YELLOW,
            t2c={"Eigenvectors": BLUE}
        )
        eigen_note.to_edge(DOWN)

        self.play(
            Transform(
                note,
                eigen_note
            ),
            run_time=1
        )

        self.wait(3)