from manim import *
from math import sqrt

def f(x):
    return (x**3 - 4*x) / 2

def f_prime(x):
    return (3*x**2 - 4) / 2

class DerivativeLeftRight(Scene):

    def construct(self):

        ax1 = Axes(
            x_range=[-2.5, 2.5],
            y_range=[-2.5, 5], 
            axis_config={"color": BLUE}
        ).shift(LEFT*3).scale(0.5)
        
        ax2 = Axes(
            x_range=[-2.5, 2.5],
            y_range=[-2.5, 5],
            axis_config={"color": GREEN}
        ).shift(RIGHT*3).scale(0.5)
        
        ax2.next_to(ax1, RIGHT, buff=1)
        ax1.align_to(ax2, DOWN)
        
        graph1 = ax1.plot(f, x_range=[-2.3, 2.3], color=YELLOW)
        
        tracker = ValueTracker(-2)
        
        point1 = Dot().add_updater(
            lambda m: m.move_to(ax1.c2p(tracker.get_value(), f(tracker.get_value())))
        )
        
        tangent = always_redraw(lambda: 
            Line(
                ax1.c2p(tracker.get_value()-0.5, f(tracker.get_value())-0.5*f_prime(tracker.get_value())),
                ax1.c2p(tracker.get_value()+0.5, f(tracker.get_value())+0.5*f_prime(tracker.get_value())),
                color=ORANGE
            )
        )
        
        point2 = Dot(color=WHITE).add_updater(
            lambda m: m.move_to(ax2.c2p(tracker.get_value(), f_prime(tracker.get_value())))
        )
        
        trace = TracedPath(
            lambda: ax2.c2p(tracker.get_value(), f_prime(tracker.get_value())),
            stroke_color=ORANGE,
            stroke_width=3
        )
        
        ax1_y_label = MathTex("f(x)", font_size=30).next_to(ax1.y_axis, UP)
        ax2_y_label = MathTex("f'(x)", font_size=30).next_to(ax2.y_axis, UP)

        slope_tex = always_redraw(
            lambda: MathTex(
                rf"""
                \text{{Slope}} = {f_prime(tracker.get_value()):.3f}
                """,
                font_size=30
            ).next_to(ax1, DOWN)
        )
        
        self.play(Create(ax1), Write(ax1_y_label))
        self.play(Create(graph1))
        self.play(FadeIn(point1), Create(tangent))
        self.play(Write(slope_tex))
        
        self.wait(0.5)
        
        self.play(Create(ax2), Write(ax2_y_label))
        
        self.wait(0.5)
        
        self.play(FadeIn(point2), FadeIn(trace))
        
        self.play(tracker.animate.set_value(2), run_time=9)
        
        self.wait(0.5)
        
        self.play(tracker.animate.set_value(-2), run_time=6)
        
        self.wait(0.5)
        
        self.play(tracker.animate.set_value(2 / sqrt(3)), run_time=4)
        
        self.wait(1)

class DerivativeTopBottom(Scene):

    def construct(self):
        # f(x)
        ax1 = Axes(
            x_range=[-2.5, 2.5],
            y_range=[-2.5, 2.5],
            #x_length=6,
            #y_length=2.5,
            axis_config={"color": BLUE}
        ).shift(UP * 1.8).scale(0.5)

        # f'(x)
        ax2 = Axes(
            x_range=[-2.5, 2.5],
            y_range=[-3, 5],
            #x_length=6,
            #y_length=2.5,
            axis_config={"color": GREEN}
        ).shift(DOWN * 2.2).scale(0.5)

        # Align both axes horizontally (same x-position)
        ax2.align_to(ax1, LEFT)

        # Graphs
        graph1 = ax1.plot(f, x_range=[-2.3, 2.3], color=YELLOW)

        # Tracker
        tracker = ValueTracker(-2)

        # Point on first graph (top)
        point1 = Dot(color=WHITE).add_updater(
            lambda m: m.move_to(ax1.c2p(tracker.get_value(), f(tracker.get_value())))
        )

        # Tangent line on top graph
        tangent = always_redraw(lambda:
            Line(
                ax1.c2p(tracker.get_value() - 0.4, f(tracker.get_value()) - 0.4 * f_prime(tracker.get_value())),
                ax1.c2p(tracker.get_value() + 0.4, f(tracker.get_value()) + 0.4 * f_prime(tracker.get_value())),
                color=ORANGE,
                stroke_width=3
            )
        )

        # Point on derivative graph (bottom)
        point2 = Dot(color=WHITE).add_updater(
            lambda m: m.move_to(ax2.c2p(tracker.get_value(), f_prime(tracker.get_value())))
        )

        # Traced path for derivative - this will be drawn progressively
        trace = TracedPath(
            lambda: ax2.c2p(tracker.get_value(), f_prime(tracker.get_value())),
            stroke_color=ORANGE,
            stroke_width=3
        )

        # Vertical connecting line between the two points
        connecting_line = always_redraw(lambda:
            DashedLine(
                ax1.c2p(tracker.get_value(), f(tracker.get_value())),
                ax2.c2p(tracker.get_value(), f_prime(tracker.get_value())),
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
        ax2_y_label = MathTex("f'(x)", font_size=30).next_to(ax2.y_axis, UP)
        ax2_labels = VGroup(ax2_x_label, ax2_y_label)

        # Slope display
        slope_tex = always_redraw(
            lambda: MathTex(
                rf"""
                \begin{{aligned}}
                \text{{Slope }} &= f'({tracker.get_value():.2f}) \\ 
                                &= {f_prime(tracker.get_value()):.3f}
                \end{{aligned}}
                """,
                font_size=28
            ).to_corner(LEFT, buff=0.3)
        )

        # Title
        title = Text("Function and Its Derivative", font_size=42)
        title.center()

        # Show top graph first
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        self.play(Create(ax1), Write(ax1_labels))
        self.play(Create(graph1))
        self.play(FadeIn(point1), Create(tangent))

        self.wait(0.5)

        # Now show bottom axes but NOT the derivative graph yet
        self.play(Create(ax2), Write(ax2_labels))

        self.wait(0.5)

        # Add the connecting line, derivative point and trace
        self.play(Create(connecting_line))
        self.play(FadeIn(point2), FadeIn(trace))
        self.play(Write(slope_tex))

        self.wait(0.5)

        # Animate - as tracker moves, the trace draws the derivative graph
        self.play(tracker.animate.set_value(2), run_time=9)

        self.wait(0.5)

        # Move back to show it works both ways
        self.play(tracker.animate.set_value(-2), run_time=6)

        self.wait(0.5)

        # Return to center
        self.play(tracker.animate.set_value(2 / sqrt(3)), run_time=4)

        self.wait(1)