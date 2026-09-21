from manim import *

class LimitIntro(Scene):

    def construct(self):

        # ---------------------------------------------------------
        # 1. Intro text
        # ---------------------------------------------------------

        title = Text("What is a Limit?", font_size=42)
        subtitle = MathTex(
            r"\lim_{x \to 2} x^2 = 4",
            font_size=40
        )

        self.play(Write(title))
        self.wait(1)
        self.play(Transform(title, subtitle))
        self.wait(1)
        self.play(FadeOut(title))

        # ---------------------------------------------------------
        # 2. Create coordinate plane
        # ---------------------------------------------------------

        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 10, 2],
            x_length=7,
            y_length=5,
            axis_config={"include_numbers": True},
            tips=False,
        )

        axes_labels = axes.get_axis_labels(
            MathTex("x"),
            MathTex("f(x)")
        )

        self.play(Create(axes), Write(axes_labels))

        # ---------------------------------------------------------
        # 3. Plot f(x) = x^2
        # ---------------------------------------------------------

        graph = axes.plot(
            lambda x: x**2,
            x_range=[0, 3],
            color=BLUE
        )

        graph_label = MathTex("f(x)=x^2", color=BLUE)
        graph_label.next_to(
            axes.c2p(2.7, 7.5),
            RIGHT
        )

        self.play(Create(graph), Write(graph_label))
        self.wait(1)

        # ---------------------------------------------------------
        # 4. Mark the point x = 2
        # ---------------------------------------------------------

        target_x = 2
        target_y = 4

        vertical_line = DashedLine(
            axes.c2p(target_x, 0),
            axes.c2p(target_x, target_y),
            color=YELLOW
        )

        horizontal_line = DashedLine(
            axes.c2p(0, target_y),
            axes.c2p(target_x, target_y),
            color=YELLOW
        )

        target_point = Dot(
            axes.c2p(target_x, target_y),
            color=YELLOW,
            radius=0.09
        )

        self.play(
            Create(vertical_line),
            Create(horizontal_line),
            FadeIn(target_point)
        )

        # ---------------------------------------------------------
        # 5. Introduce moving point
        # ---------------------------------------------------------

        tracker = ValueTracker(3.0)

        moving_dot = always_redraw(
            lambda: Dot(
                axes.c2p(
                    tracker.get_value(),
                    tracker.get_value() ** 2
                ),
                color=RED,
                radius=0.1
            )
        )

        moving_x_line = always_redraw(
            lambda: DashedLine(
                axes.c2p(tracker.get_value(), 0),
                axes.c2p(
                    tracker.get_value(),
                    tracker.get_value() ** 2
                ),
                color=RED,
                stroke_width=2
            )
        )

        moving_y_line = always_redraw(
            lambda: DashedLine(
                axes.c2p(0, tracker.get_value() ** 2),
                axes.c2p(
                    tracker.get_value(),
                    tracker.get_value() ** 2
                ),
                color=RED,
                stroke_width=2
            )
        )

        x_label = MathTex("x =", font_size=30)
        x_number = DecimalNumber(
            tracker.get_value(),
            num_decimal_places=2,
            font_size=30
        )

        fx_label = MathTex("f(x) =", font_size=30).next_to(x_label, DOWN)
        fx_number = DecimalNumber(
            tracker.get_value() ** 2,
            num_decimal_places=2,
            font_size=30
        )

        x_display = VGroup(x_label, x_number).arrange(RIGHT, buff=0.1)
        fx_display = VGroup(fx_label, fx_number).arrange(RIGHT, buff=0.1)

        x_number.add_updater(
            lambda m: m.set_value(tracker.get_value())
        )
        fx_number.add_updater(
            lambda m: m.set_value(tracker.get_value() ** 2)
        )

        # ---------------------------------------------------------
        # 6. Show x approaching 2 from right
        # ---------------------------------------------------------
        approach_text_right = MathTex(
            r"x \to 2^+",
            color=RED,
            font_size=30
        )

        approach_text_right.to_edge(RIGHT)
        x_display.next_to(approach_text_right, direction=DOWN)
        fx_display.next_to(x_display, DOWN, aligned_edge=LEFT)

        self.play(
            Write(approach_text_right),
            Write(x_display),
            Write(fx_display)
        )

        self.wait(1)

        self.play(
            FadeIn(
                moving_dot,
                moving_x_line,
                moving_y_line
            )
        )

        # Move from the right toward 2
        self.play(
            tracker.animate.set_value(2.5),
            run_time=1.5
        )

        self.play(
            tracker.animate.set_value(2.1),
            run_time=1.5
        )

        self.play(
            tracker.animate.set_value(2.01),
            run_time=1.5
        )

        self.wait(1)

        self.play(
            FadeOut(
                approach_text_right,
                moving_dot,
                moving_x_line,
                moving_y_line,
                x_display,
                fx_display
            )
        )

        # ---------------------------------------------------------
        # 7. Approach from the left
        # ---------------------------------------------------------

        approach_text_left = MathTex(
            r"x \to 2^-",
            color=RED,
            font_size=25
        )

        approach_text_left.to_edge(LEFT)
        x_display.next_to(approach_text_left, direction=DOWN)
        fx_display.next_to(x_display, DOWN, aligned_edge=LEFT)

        tracker.set_value(1.5)
        moving_dot.update()
        moving_x_line.update()
        moving_y_line.update()

        self.play(
            Write(approach_text_left),
            Write(x_display),
            Write(fx_display)
        )

        self.wait(1)

        self.play(
            FadeIn(
                moving_dot,
                moving_x_line,
                moving_y_line
            )
        )

        self.play(
            tracker.animate.set_value(1.7),
            run_time=1.5
        )

        self.play(
            tracker.animate.set_value(1.9),
            run_time=1.5
        )

        self.play(
            tracker.animate.set_value(1.99),
            run_time=1.5
        )

        self.wait(1)

        self.play(
            FadeOut(
                approach_text_left,
                moving_dot,
                moving_x_line,
                moving_y_line,
                x_display,
                fx_display
            )
        )

        # ---------------------------------------------------------
        # 8. Explain the result
        # ---------------------------------------------------------
        result = MathTex(
            r"\lim_{x\to2}x^2=4",
            color=GREEN,
            font_size=44
        )

        result.to_edge(LEFT)

        self.play(Write(result))
        self.wait(2)