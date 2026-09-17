from manim import *

class LinearIndependence3D(ThreeDScene):

    def construct(self):

        # ============================================================
        # 1. TITLE
        # ============================================================

        title = Text(
            "Linear Independence of 3D Vectors",
            font_size=40
        ).to_edge(UP)

        self.add_fixed_in_frame_mobjects(title)

        self.play(Write(title))
        self.wait(1)

        # ============================================================
        # 2. 3D COORDINATE SYSTEM
        # ============================================================

        axes = ThreeDAxes(
            x_range=[-1, 5, 1],
            y_range=[-1, 4, 1],
            z_range=[-1, 4, 1],
            x_length=8,
            y_length=6,
            z_length=6,
            axis_config={
                "color": GREY_B,
                "include_numbers": True,
            },
        )

        self.play(Create(axes))

        # Camera
        self.set_camera_orientation(
            phi=65 * DEGREES,
            theta=-45 * DEGREES,
        )

        # ============================================================
        # 3. THREE INDEPENDENT VECTORS
        # ============================================================

        u = np.array([3, 1, 0])
        v = np.array([1, 2, 0])
        w = np.array([0, 0, 2])

        origin = axes.c2p(0, 0, 0)

        u_end = axes.c2p(*u)
        v_end = axes.c2p(*v)
        w_end = axes.c2p(*w)

        u_vec = Arrow3D(
            origin,
            u_end,
            color=BLUE,
            thickness=0.03,
            height=0.2,
            base_radius=0.06,
        )

        v_vec = Arrow3D(
            origin,
            v_end,
            color=YELLOW,
            thickness=0.03,
            height=0.2,
            base_radius=0.06,
        )

        w_vec = Arrow3D(
            origin,
            w_end,
            color=RED,
            thickness=0.03,
            height=0.2,
            base_radius=0.06,
        )

        # Labels
        u_label = MathTex(
            r"\mathbf{u}",
            color=BLUE
        ).scale(0.7)

        v_label = MathTex(
            r"\mathbf{v}",
            color=YELLOW
        ).scale(0.7)

        w_label = MathTex(
            r"\mathbf{w}",
            color=RED
        ).scale(0.7)

        # Labels are fixed to camera
        self.add_fixed_orientation_mobjects(
            u_label,
            v_label,
            w_label,
        )

        u_label.next_to(u_vec, DOWN)
        v_label.next_to(v_vec, LEFT)
        w_label.next_to(w_vec, RIGHT)

        self.play(
            Create(u_vec),
            Create(v_vec),
            Create(w_vec),
        )

        self.play(
            Write(u_label),
            Write(v_label),
            Write(w_label),
        )

        self.wait(1)

        # ============================================================
        # 4. PARALLELEPIPED
        # ============================================================

        # Vertices
        p000 = axes.c2p(0, 0, 0)

        p100 = axes.c2p(3, 1, 0)
        p010 = axes.c2p(1, 2, 0)
        p001 = axes.c2p(0, 0, 2)

        p110 = axes.c2p(4, 3, 0)
        p101 = axes.c2p(3, 1, 2)
        p011 = axes.c2p(1, 2, 2)
        p111 = axes.c2p(4, 3, 2)

        # Six faces
        bottom = Polygon(
            p000, p100, p110, p010,
            fill_color=GREEN,
            fill_opacity=0.25,
            stroke_color=GREEN,
            stroke_width=2,
        )

        top = Polygon(
            p001, p101, p111, p011,
            fill_color=GREEN,
            fill_opacity=0.25,
            stroke_color=GREEN,
            stroke_width=2,
        )

        side_u = Polygon(
            p000, p100, p101, p001,
            fill_color=GREEN,
            fill_opacity=0.15,
            stroke_color=GREEN,
            stroke_width=2,
        )

        side_v = Polygon(
            p000, p010, p011, p001,
            fill_color=GREEN,
            fill_opacity=0.15,
            stroke_color=GREEN,
            stroke_width=2,
        )

        far_u = Polygon(
            p010, p110, p111, p011,
            fill_color=GREEN,
            fill_opacity=0.15,
            stroke_color=GREEN,
            stroke_width=2,
        )

        far_v = Polygon(
            p100, p110, p111, p101,
            fill_color=GREEN,
            fill_opacity=0.15,
            stroke_color=GREEN,
            stroke_width=2,
        )

        parallelepiped = VGroup(
            bottom,
            top,
            side_u,
            side_v,
            far_u,
            far_v,
        )

        self.play(
            Create(parallelepiped)
        )

        self.wait(1)

        # ============================================================
        # 5. SCALAR TRIPLE PRODUCT / VOLUME
        # ============================================================

        determinant = MathTex(
            r"""
            \begin{aligned}
            \text{Volume}
            &= \left|\det(\mathbf{u},\mathbf{v},\mathbf{w})\right| \\[2mm]
            &=
            \left|
            \begin{vmatrix}
            3 & 1 & 0 \\
            1 & 2 & 0 \\
            0 & 0 & 2
            \end{vmatrix}
            \right| \\[2mm]
            &= 10
            \end{aligned}
            """
        ).scale(0.55).to_edge(LEFT)

        self.add_fixed_in_frame_mobjects(determinant)

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

        self.add_fixed_in_frame_mobjects(independent)

        self.play(
            Write(independent)
        )

        self.wait(2)

        # ============================================================
        # 7. ZERO COMBINATION
        # ============================================================

        zero_equation = MathTex(
            r"""a\mathbf{u}+b\mathbf{v}+c\mathbf{w}
            =\mathbf{0}"""
        ).scale(0.65).to_edge(RIGHT)

        only_solution = MathTex(
            r"""\Longrightarrow\quad
            a=b=c=0""",
            color=GREEN
        ).scale(0.65).next_to(
            zero_equation,
            DOWN
        )

        self.add_fixed_in_frame_mobjects(
            zero_equation,
            only_solution,
        )

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
        # 9. MAKE w DEPENDENT
        # ============================================================

        dependent_label = Text(
            "Now make the vectors coplanar...",
            font_size=30
        ).to_edge(DOWN)

        self.add_fixed_in_frame_mobjects(
            dependent_label
        )

        self.play(
            Write(dependent_label)
        )

        self.wait(1)

        # New w lies in the uv-plane
        target_w = np.array([2, 1, 0])

        new_w_end = axes.c2p(*target_w)

        new_w_vec = Arrow3D(
            origin,
            new_w_end,
            color=RED,
            thickness=0.03,
            height=0.2,
            base_radius=0.06,
        )

        new_w_label = MathTex(
            r"\mathbf{w}",
            color=RED
        ).scale(0.7)

        self.add_fixed_orientation_mobjects(
            new_w_label
        )

        new_w_label.next_to(
            new_w_vec,
            UP
        )

        # ============================================================
        # 10. COLLAPSED PARALLELEPIPED
        # ============================================================

        # Since w is now in the uv-plane,
        # the 3D volume collapses to zero.

        new_p001 = axes.c2p(*target_w)

        new_p101 = axes.c2p(
            *(target_w + u)
        )

        new_p011 = axes.c2p(
            *(target_w + v)
        )

        new_p111 = axes.c2p(
            *(target_w + u + v)
        )

        collapsed_face = Polygon(
            p000,
            p100,
            p110,
            p010,
            fill_color=RED,
            fill_opacity=0.25,
            stroke_color=RED,
            stroke_width=3,
        )

        self.play(
            FadeOut(dependent_label)
        )

        self.play(
            Transform(w_vec, new_w_vec),
            Transform(
                w_label,
                new_w_label
            ),
            Transform(
                parallelepiped,
                collapsed_face
            ),
            run_time=3,
        )

        self.wait(1)

        # ============================================================
        # 11. SHOW ZERO VOLUME
        # ============================================================

        zero_volume = MathTex(
            r"\text{Volume}=0",
            color=RED,
        ).scale(0.7).to_edge(LEFT)

        dependent = Text(
            "LINEARLY DEPENDENT",
            color=RED,
            font_size=34
        ).to_edge(DOWN)

        self.add_fixed_in_frame_mobjects(
            zero_volume,
            dependent,
        )

        self.play(
            Write(zero_volume),
            Write(dependent),
        )

        self.wait(2)

        # ============================================================
        # 12. SHOW DEPENDENCY
        # ============================================================

        dependency = MathTex(
            r"""\mathbf{w}
            =a\mathbf{u}+b\mathbf{v}"""
        ).scale(0.65).to_edge(RIGHT)

        dependency_example = MathTex(
            r"""\mathbf{w}
            =\frac{1}{3}\mathbf{u}
            +\frac{1}{3}\mathbf{v}"""
        ).scale(0.55).next_to(
            dependency,
            DOWN
        )

        self.add_fixed_in_frame_mobjects(
            dependency,
            dependency_example,
        )

        self.play(
            Write(dependency),
            Write(dependency_example),
        )

        self.wait(2)

        # ============================================================
        # 13. FINAL SUMMARY
        # ============================================================

        self.play(
            FadeOut(
                VGroup(
                    axes,
                    u_vec,
                    v_vec,
                    w_vec,
                    u_label,
                    v_label,
                    w_label,
                    parallelepiped,
                    zero_volume,
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
                r"""
                \det(\mathbf{u},\mathbf{v},\mathbf{w})
                \neq 0
                """
            ),
            MathTex(
                r"\Longleftrightarrow"
            ),
            Text(
                "Nonzero parallelepiped volume",
                font_size=28
            ),
        ).arrange(
            DOWN,
            buff=0.4
        )

        self.add_fixed_in_frame_mobjects(summary)

        self.play(
            Write(summary)
        )

        self.wait(2)
