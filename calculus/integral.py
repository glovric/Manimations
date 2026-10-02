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
            axis_config={"color": GREEN}
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
                color=TEAL,
                stroke_color=BLUE,
                opacity=0.4,
            )
        )

        # Traced path for derivative - this will be drawn progressively
        trace = TracedPath(
            lambda: ax2.c2p(tracker.get_value(), self.F(tracker.get_value())),
            stroke_color=ORANGE,
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
        self.play(tracker.animate.set_value(5), run_time=6)

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