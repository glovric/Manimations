from manim import *

class IntegralTopBottom(Scene):

    def __init__(self, f, F, axes_params, **kwargs):
        super().__init__(**kwargs)
        self.f = f
        self.F = F
        self.axes_params = axes_params

    def construct(self):

        ax1_x_range = self.axes_params["ax1_x_range"]
        ax1_y_range = self.axes_params["ax1_y_range"]
        ax2_x_range = self.axes_params["ax2_x_range"]
        ax2_y_range = self.axes_params["ax2_y_range"]
        graph1_x_range = self.axes_params["graph1_x_range"]

        # f(x)
        ax1 = Axes(
            x_range=ax1_x_range,
            y_range=ax1_y_range,
            #x_length=6,
            #y_length=2.5,
            axis_config={"color": BLUE}
        ).shift(UP * 1.8).scale(0.5)

        # F(x)
        ax2 = Axes(
            x_range=ax2_x_range,
            y_range=ax2_y_range,
            #x_length=6,
            #y_length=2.5,
            axis_config={"color": GRAY_C}
        ).shift(DOWN * 2.2).scale(0.5)

        # Align both axes horizontally (same x-position)
        ax2.align_to(ax1, LEFT)

        # Graphs
        graph1 = ax1.plot(self.f, x_range=graph1_x_range, color=YELLOW)

        # Tracker
        tracker = ValueTracker(0.0)

        # Point on first graph (top)
        point1 = Dot(color=WHITE).add_updater(
            lambda m: m.move_to(ax1.c2p(tracker.get_value(), self.f(tracker.get_value())))
        )

        # Point on derivative graph (bottom)
        point2 = Dot(color=WHITE).add_updater(
            lambda m: m.move_to(ax2.c2p(tracker.get_value(), self.F(tracker.get_value())))
        )

        area = always_redraw(
            lambda: ax1.get_area(
                graph1,
                x_range=[0, tracker.get_value()],
                color=TEAL_B,
                stroke_color=BLUE,
                opacity=0.4,
            )
        )

        # Traced path for derivative - this will be drawn progressively
        trace = TracedPath(
            lambda: ax2.c2p(tracker.get_value(), self.F(tracker.get_value())),
            stroke_color=TEAL_B,
            stroke_width=3
        )

        # Vertical connecting line between the two points
        connecting_line = always_redraw(lambda:
            DashedLine(
                ax1.c2p(tracker.get_value(), self.f(tracker.get_value())),
                ax2.c2p(tracker.get_value(), self.F(tracker.get_value())),
                color=WHITE,
                stroke_width=2,
                stroke_opacity=0.7
            )
        )

        # Add axis labels
        ax1_x_label = MathTex("x", font_size=30).next_to(ax1.x_axis, RIGHT)
        ax1_y_label = MathTex("f(x)", font_size=30).next_to(ax1.y_axis, UP)
        ax1_labels = VGroup(ax1_x_label, ax1_y_label)

        ax2_x_label = MathTex("x", font_size=30).next_to(ax2.x_axis, RIGHT)
        ax2_y_label = MathTex("F(x)", font_size=30).next_to(ax2.y_axis, UP)
        ax2_labels = VGroup(ax2_x_label, ax2_y_label)

        # Slope display
        slope_tex = always_redraw(
            lambda: MathTex(
                rf"""
                \begin{{aligned}}
                \text{{Area }} &= F({tracker.get_value():.3f}) \\ 
                                &= {self.F(tracker.get_value()):.3f}
                \end{{aligned}}
                """,
                font_size=28
            ).to_corner(LEFT, buff=0.3)
        )

        # Title
        title = Text("Function and Its Primitive", font_size=42)
        title.center()

        # Show top graph first
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        self.play(Create(ax1), Write(ax1_labels))
        self.play(Create(graph1))
        self.play(FadeIn(point1))

        self.wait(0.5)

        # Now show bottom axes but NOT the derivative graph yet
        self.play(Create(ax2), Write(ax2_labels))

        self.wait(0.5)

        # Add the connecting line, derivative point and trace
        self.play(Create(connecting_line))
        self.play(FadeIn(point2), FadeIn(trace))
        self.play(Write(slope_tex))

        self.play(Create(area))

        self.wait(0.5)

        # Animate - as tracker moves, the trace draws the derivative graph
        self.play(tracker.animate.set_value(5), run_time=9)

        self.wait(3)

class IntegralLinear(IntegralTopBottom):

    def __init__(self, **kwargs):
        f = lambda x: 2*x
        F = lambda x: x**2
        axes_params = {
            "ax1_x_range": [0, 5.5],
            "ax1_y_range": [-1, 26],
            "ax2_x_range": [0, 5.5],
            "ax2_y_range": [-1, 26],
            "graph1_x_range": [0, 5]
        }
        super().__init__(f, F, axes_params, **kwargs)

class IntegralConstant(IntegralTopBottom):

    def __init__(self, **kwargs):
        f = lambda x: 1
        F = lambda x: x
        axes_params = {
            "ax1_x_range": [0, 5.5],
            "ax1_y_range": [-1, 5.5],
            "ax2_x_range": [0, 5.5],
            "ax2_y_range": [-1, 5.5],
            "graph1_x_range": [0, 5]
        }
        super().__init__(f, F, axes_params, **kwargs)

class RiemannSums(Scene):

    def construct(self):

        def f(x):
            return x**2

        def make_rects(n):
            dx = (b - a) / n
            rects = VGroup()
            approx = 0.0
            for i in range(n):
                xi = a + (i + 1) * dx  # right endpoint
                h = f(xi)
                approx += h * dx
                rect = Rectangle(
                    width=axes.x_length / (3.8) * dx,
                    height=axes.c2p(0, h)[1] - axes.c2p(0, 0)[1],
                    fill_color=TEAL,
                    fill_opacity=0.45,
                    stroke_color=BLUE,
                    stroke_width=1.2,
                )
                # position: bottom-left corner of rect
                bl = axes.c2p(a + i * dx, 0)
                rect.move_to(
                    [bl[0] + rect.width / 2,
                     bl[1] + rect.height / 2,
                     0]
                )
                rects.add(rect)
            return rects, approx

        self.camera.background_color = "#1a1a2e"

        a, b = 0.0, 3.0

        title = (
            Text("Riemann Sums → Definite Integral", font_size=36, color=WHITE)
            .to_edge(UP, buff=0.25)
        )

        axes = (
            Axes(
                x_range=[-0.2, 3.6, 1],
                y_range=[-0.2, 9.5, 2],
                x_length=6.5,
                y_length=5.0,
                axis_config={"color": GREY_B, "stroke_width": 1},
                tips=True,
            )
            .shift(LEFT * 1.8 + DOWN * 0.45)
        )

        ax_labels = axes.get_axis_labels(
            x_label=MathTex("x", font_size=26),
            y_label=MathTex("y", font_size=26),
        )

        curve = axes.plot(f, x_range=[0, 3.05], color=BLUE_B, stroke_width=3)
        f_label = (
            MathTex("f(x)=x^2", font_size=26, color=BLUE_B)
            .move_to(axes.c2p(2.5, 10))
        )

        riemann_formula = (
            MathTex(
                r"\sum_{i=1}^{n} f(x_i)\,\Delta x \approx",
                font_size=40, 
                color=WHITE,
            )
            .to_edge(RIGHT)
            .shift(2 * LEFT)
        )

        rects, val = make_rects(4)
        n_label = (
            MathTex("n = 4", font_size=40, color=TEAL_B)
            .next_to(riemann_formula, UP)
        )

        value = (
            DecimalNumber(
                val,
                num_decimal_places=3,
                font_size=40,
                color=TEAL_B,
            )
            .next_to(riemann_formula, RIGHT, buff=0.1)
            .shift(0.04*UP)
        )

        formula_group = VGroup(
            riemann_formula,
            value
        )

        shaded = axes.get_area(curve, x_range=[0, 3], color=[TEAL, BLUE], opacity=0.35)

        int_formula = MathTex(
            r"\int_0^3 f(x)\,dx = {{9}}",
            font_size=40,
            color=WHITE,
        ).move_to(formula_group)
        int_formula.get_part_by_tex("9").set_color(TEAL_B)

        highlight = SurroundingRectangle(
            int_formula,
            color=YELLOW,
            buff=0.1,
        )

        # ------ Animation start ----- #

        self.play(Write(title))

        self.play(Create(axes), Write(ax_labels))

        self.play(Create(curve), Write(f_label))
        self.wait(0.4)

        self.play(
            Create(rects), 
            Write(n_label), 
            Write(formula_group)
        )
        self.wait(1.5)

        for n in [8, 16, 32, 64, 128, 256, 512]:
            rects_new, val_new = make_rects(n)
            new_n_lbl = MathTex(f"n = {n}", font_size=40, color=TEAL_B).next_to(riemann_formula, UP)

            self.play(
                Transform(rects, rects_new),
                Transform(n_label, new_n_lbl),
                value.animate.set_value(val_new),
                run_time=2,
            )
            self.wait(1.5)

        new_n_lbl = MathTex(r"n \rightarrow \infty", font_size=40, color=TEAL_B).next_to(riemann_formula, UP)

        self.play(FadeIn(shaded), FadeOut(rects), Transform(n_label, new_n_lbl))

        self.play(
            ReplacementTransform(formula_group, int_formula),
            run_time=1.2,
            rate_func=smooth,
        )

        self.play(
            ShowPassingFlash(
                highlight,
                time_width=1,
            ),
            run_time=1,
        )

        self.wait(3)