from manim import *
import math

def f(x):
    return x**2

class Secant(Scene):

    @staticmethod
    def get_secant_line(axes, tracker, x0, y0):

        x_current = tracker.get_value()
        dx = x_current - x0
        dy = f(x_current) - y0
        constant = 0.75 / dx

        secant = Line(
            axes.c2p(x0 - constant * dx, y0 - constant * dy),
            axes.c2p(x_current + constant * dx, f(x_current) + constant * dy),
            color=BLUE,
            stroke_width=2
        )

        return secant

    @staticmethod
    def get_slope_tex(tracker, x0, y0):

        x_current = tracker.get_value()
        y_current = f(tracker.get_value())

        slope = (y_current - y0) / (x_current - x0)
        h = f"{x_current - x0:.2f}"

        slope_tex = MathTex(
            rf"""
            \begin{{aligned}}
                \text{{Slope}} &= \frac{{f({x0}+{h})-f({x0})}}{{{h}}} \\
                               &= {slope:.3f}
            \end{{aligned}}
            """,
            font_size=30
        ).to_edge(LEFT)

        return slope_tex

    def construct(self):

        # -------------------------
        # Title
        # -------------------------
        title = Text(
            "Understanding Derivatives",
            font_size=48
        ).center()

        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # -------------------------
        # Axes
        # -------------------------
        x_range = [-1, 4]
        y_range = [0, f(4)]
        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            axis_config={"color": BLUE},
            tips=True,
        ).shift(RIGHT*2).scale(0.7)

        axes_labels = axes.get_axis_labels(
            x_label="x",
            y_label="f(x)"
        )

        self.play(
            Create(axes),
            Write(axes_labels)
        )

        graph = axes.plot(
            f,
            color=YELLOW,
            stroke_width=3,
        )

        graph_label = MathTex(
            r"f(x) = x^2"
        ).to_corner(UR)

        self.play(
            Create(graph),
            Write(graph_label)
        )

        self.wait(1)

        # -------------------------
        # Point of interest
        # -------------------------
        x0 = 2
        y0 = f(x0)

        point_x0 = Dot(
            axes.c2p(x0, y0),
            color=RED,
            radius=0.08,
        )

        point_x0_label = MathTex(
            rf"P({x0}, {y0:g})"
        ).next_to(
            point_x0,
            RIGHT
        )

        self.play(
            Create(point_x0),
            Write(point_x0_label)
        )

        self.wait(0.5)

        # -------------------------
        # Secant lines
        # -------------------------
        tracker = ValueTracker(4)

        moving_dot = always_redraw(
            lambda: Dot(
                axes.c2p(
                    tracker.get_value(),
                    f(tracker.get_value())
                ),
                color=RED,
                radius=0.08
            )
        )

        secant = always_redraw(
            lambda: self.get_secant_line(axes, tracker, x0, y0)
        )

        self.play(
            FadeIn(secant),
            FadeIn(moving_dot),
            run_time=0.7,
        )

        slope_text = self.get_slope_tex(tracker, x0, y0)
        self.play(Write(slope_text))
        self.wait(0.5)

        for h in [1, 0.5, 0.25, 0.1, 0.01]:

            self.play(
                tracker.animate.set_value(x0+h),
                run_time=1.5
            )

            new_slope_text = self.get_slope_tex(tracker, x0, y0)
            self.play(
                slope_text.animate.become(new_slope_text),
                run_time=0.5
            )
            
            self.wait(1)

        self.play(
            *[FadeOut(mobj) for mobj in self.mobjects]
        )

        definition = VGroup(
            MathTex(
                r"\text{The derivative of } f \text{ at } x_0:"
            ),
            MathTex(
                r"f'(x_0)"
                r"="
                r"\lim_{h\to0}"
                r"\frac{f(x_0+h)-f(x_0)}{h}"
            ),
            MathTex(
                r"\text{Geometrically: slope of the tangent line}"
            ),
        ).arrange(
            DOWN,
            buff=0.5
        )

        self.play(Write(definition))
        self.wait(2)

        # -------------------------
        # Final summary
        # -------------------------
        self.play(
            *[FadeOut(mobj) for mobj in self.mobjects]
        )

        summary = Text(
            "Derivative = Instantaneous Rate of Change",
            font_size=36,
        )

        self.play(Write(summary))
        self.wait(2)
