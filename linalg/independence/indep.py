from manim import *

class LinearIndependence(Scene):

    def construct(self):

        # ============================================================
        # 1. TITLE
        # ============================================================

        title = Text(
            "Linear Independence of 2D Vectors",
            font_size=40
        ).to_edge(UP)

        self.play(Write(title))
        self.wait(1)

        # ============================================================
        # 2. COORDINATE SYSTEM
        # ============================================================

        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 4, 1],
            x_length=8,
            y_length=6,
            axis_config={
                "color": GREY_B,
                "include_numbers": True,
            },
        )

        self.play(Create(axes))

        # ============================================================
        # 3. TWO INDEPENDENT VECTORS
        # ============================================================

        u = np.array([3, 1])
        v = np.array([1, 2])

        origin = axes.c2p(0, 0)

        u_end = axes.c2p(*u)
        v_end = axes.c2p(*v)

        u_vec = Arrow(
            origin,
            u_end,
            buff=0,
            color=BLUE,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15,
        )

        v_vec = Arrow(
            origin,
            v_end,
            buff=0,
            color=YELLOW,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15,
        )

        u_label = (
            MathTex(r"\mathbf{u}", color=BLUE)
            .next_to(u_vec, DOWN)
            .shift(UP * 0.6)
        )

        v_label = (
            MathTex(r"\mathbf{v}", color=YELLOW)
            .next_to(v_vec, LEFT, buff=0.1)
            .shift(UP * 0.08)
            .shift(RIGHT * 0.7)
        )

        self.play(
            GrowArrow(u_vec),
            GrowArrow(v_vec),
        )

        self.play(
            Write(u_label),
            Write(v_label),
        )

        self.wait(1)

        # ============================================================
        # 4. PARALLELOGRAM
        # ============================================================

        p1 = axes.c2p(0, 0)
        p2 = axes.c2p(3, 1)
        p3 = axes.c2p(4, 3)
        p4 = axes.c2p(1, 2)

        parallelogram = Polygon(
            p1,
            p2,
            p3,
            p4,
            fill_color=GREEN,
            fill_opacity=0.25,
            stroke_color=GREEN,
            stroke_width=3,
        )

        # Copies of vectors forming the parallelogram
        u_copy = Arrow(
            p4,
            p3,
            buff=0,
            color=BLUE,
            stroke_width=4,
        )

        v_copy = Arrow(
            p2,
            p3,
            buff=0,
            color=YELLOW,
            stroke_width=4,
        )

        self.play(
            Create(parallelogram),
            GrowArrow(u_copy),
            GrowArrow(v_copy),
        )

        self.wait(1)

        # ============================================================
        # 5. DETERMINANT / AREA
        # ============================================================

        determinant = MathTex(
            r"""
            \begin{aligned}
            \text{Area} &= \det(\mathbf{u},\mathbf{v}) \\
            &= 
                \begin{vmatrix}
                3 & 1 \\
                1 & 2
                \end{vmatrix} \\
            &= 5
            \end{aligned}
            """
        ).scale(0.7).to_edge(LEFT)

        self.play(
            Write(determinant)
        )
        self.wait(2)

        # ============================================================
        # 6. INDEPENDENT
        # ============================================================

        independent = Text(
            "LINEARLY INDEPENDENT",
            color=GREEN,
            font_size=34
        ).to_edge(DOWN)

        self.play(
            Write(independent)
        )

        self.wait(2)

        # ============================================================
        # 7. EXPLAIN THE ZERO COMBINATION
        # ============================================================

        zero_equation = MathTex(
            r"a\mathbf{u}+b\mathbf{v}=\mathbf{0}"
        ).scale(0.7).to_edge(RIGHT)

        only_solution = MathTex(
            r"\Longrightarrow\quad a=b=0",
            color=GREEN
        ).scale(0.7).next_to(zero_equation,DOWN)

        self.play(
            Write(zero_equation),
            Write(only_solution),
        )

        self.wait(2)

        # ============================================================
        # 8. REMOVE EXPLANATION
        # ============================================================

        self.play(
            FadeOut(
                VGroup(
                    determinant,
                    independent,
                    zero_equation,
                    only_solution,
                )
            )
        )

        # ============================================================
        # 9. MOVE v UNTIL IT BECOMES PARALLEL TO u
        # ============================================================

        dependent_label = Text(
            "Now make the vectors parallel...",
            font_size=30
        ).to_edge(DOWN)

        self.play(
            Write(dependent_label)
        )

        self.wait(1)

        # A parallel vector that remains on screen:
        target_v = np.array([2.5, 5 / 6])

        new_v_end = axes.c2p(*target_v)

        new_v_vec = Arrow(
            origin,
            new_v_end,
            buff=0,
            color=YELLOW,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15,
        )

        new_v_label = (
            MathTex(r"\mathbf{v}", color=YELLOW)
            .next_to(new_v_vec, UP, buff=0.1)
            .shift(DOWN * 0.6)
        )

        # New parallelogram
        new_p1 = axes.c2p(0, 0)
        new_p2 = axes.c2p(3, 1)
        new_p3 = axes.c2p(
            3 + target_v[0],
            1 + target_v[1]
        )
        new_p4 = new_v_end

        collapsed_parallelogram = Polygon(
            new_p1,
            new_p2,
            new_p3,
            new_p4,
            fill_color=RED,
            fill_opacity=0.25,
            stroke_color=RED,
            stroke_width=3,
        )

        self.play(
            FadeOut(u_copy),
            FadeOut(v_copy),
            FadeOut(dependent_label),
        )

        self.play(
            Transform(v_vec, new_v_vec),
            Transform(
                parallelogram,
                collapsed_parallelogram
            ),
            Transform(v_label, new_v_label),
            run_time=3,
        )

        self.wait(1)

        # ============================================================
        # 10. SHOW ZERO AREA
        # ============================================================

        zero_area = MathTex(
            r"\text{Area}=0",
            color=RED,
            font_size=40
        ).scale(0.7).to_edge(LEFT)

        dependent = Text(
            "LINEARLY DEPENDENT",
            color=RED,
            font_size=34
        ).to_edge(DOWN)

        self.play(
            Write(zero_area),
            Write(dependent),
        )

        self.wait(2)

        # ============================================================
        # 11. SHOW THE DEPENDENCY EXPLICITLY
        # ============================================================

        dependency = MathTex(
            r"\mathbf{v}=c\mathbf{u}"
        ).scale(0.7).to_edge(RIGHT)

        dependency_example = MathTex(
            r"a\mathbf{u}+b\mathbf{v}=\mathbf{0}"
        ).scale(0.7).next_to(dependency,DOWN)

        self.play(
            Write(dependency),
            Write(dependency_example),
        )

        self.wait(2)

        # ============================================================
        # 12. FINAL SUMMARY
        # ============================================================

        self.play(
            FadeOut(
                VGroup(
                    axes,
                    u_vec,
                    v_vec,
                    u_label,
                    v_label,
                    parallelogram,
                    zero_area,
                    dependent,
                    dependency,
                    dependency_example,
                )
            )
        )

        summary = VGroup(
            Text(
                "Linear Independence",
                color=GREEN,
                font_size=36
            ),
            MathTex(
                r"\det(\mathbf{u},\mathbf{v})\neq0"
            ),
            MathTex(
                r"\Longleftrightarrow"
            ),
            Text(
                "Nonzero parallelogram area",
                font_size=28
            ),
        ).arrange(DOWN, buff=0.4)

        self.play(
            Write(summary)
        )

        self.wait(2)
