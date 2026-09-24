from manim import *

class LimitDNE(Scene):

    def construct(self):

        # ---------------------------------------------------------
        # 1. Intro text
        # ---------------------------------------------------------

        title = MathTex(
            r"\lim_{x \to 0} \frac{1}{x}",
            font_size=40
        )

        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # ---------------------------------------------------------
        # 2. Create coordinate plane
        # ---------------------------------------------------------

        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-6, 6, 2],
            x_length=9,
            y_length=6,
            axis_config={
                "include_numbers": True,
                "include_tip": False,
            },
        )

        axes_labels = axes.get_axis_labels(
            MathTex("x"),
            MathTex("f(x)")
        )

        self.play(Create(axes), Write(axes_labels))

        # ---------------------------------------------------------
        # 3. Plot f(x) = 1 / x
        # ---------------------------------------------------------

        left_graph = axes.plot(
            lambda x: 1 / x,
            x_range=[-4, -0.15],
            color=BLUE
        )

        right_graph = axes.plot(
            lambda x: 1 / x,
            x_range=[0.15, 4],
            color=GREEN
        )

        self.play(
            Create(left_graph),
            Create(right_graph),
            run_time=2
        )
        
        self.wait(1)

        # ---------------------------------------------------------
        # 4. Mark the line x = 0
        # ---------------------------------------------------------

        asymptote = DashedLine(
            axes.c2p(0, -6),
            axes.c2p(0, 6),
            color=YELLOW
        )

        asymptote_label = (
            MathTex(r"x=0", color=YELLOW, font_size=30)
            .next_to(asymptote, RIGHT)
            .shift(0.3*DOWN)
            .shift(0.1*LEFT)
        )

        self.play(
            Create(asymptote),
            Write(asymptote_label)
        )

        self.wait(2)

        # ---------------------------------------------------------
        # 5. Introduce left moving point
        # ---------------------------------------------------------

        left_tracker = ValueTracker(-2.5)

        left_dot = always_redraw(
            lambda: Dot(
                axes.c2p(
                    left_tracker.get_value(),
                    1 / left_tracker.get_value()
                ),
                color=RED,
                radius=0.1
            )
        )

        moving_x_line_left = always_redraw(
            lambda: DashedLine(
                axes.c2p(left_tracker.get_value(), 0),
                axes.c2p(
                    left_tracker.get_value(),
                    1 / left_tracker.get_value()
                ),
                color=RED,
                stroke_width=2
            )
        )

        moving_y_line_left = always_redraw(
            lambda: DashedLine(
                axes.c2p(0, 1 / left_tracker.get_value()),
                axes.c2p(
                    left_tracker.get_value(),
                    1 / left_tracker.get_value()
                ),
                color=RED,
                stroke_width=2
            )
        )

        x_label_left = MathTex("x =", font_size=30)
        x_number_left = DecimalNumber(
            left_tracker.get_value(),
            num_decimal_places=2,
            font_size=30
        )

        fx_label_left = MathTex("f(x) =", font_size=30).next_to(x_label_left, DOWN)
        fx_number_left = DecimalNumber(
            1 / left_tracker.get_value(),
            num_decimal_places=2,
            font_size=30
        )

        x_display_left = VGroup(x_label_left, x_number_left).arrange(RIGHT, buff=0.1)
        fx_display_left = VGroup(fx_label_left, fx_number_left).arrange(RIGHT, buff=0.1)

        x_display_left.to_corner(UL)
        fx_display_left.next_to(x_display_left, DOWN, aligned_edge=LEFT)

        x_number_left.add_updater(
            lambda m: m.set_value(left_tracker.get_value())
        )
        fx_number_left.add_updater(
            lambda m: m.set_value(1 / left_tracker.get_value())
        )

        self.play(
            FadeIn(left_dot),
            FadeIn(moving_x_line_left),
            FadeIn(moving_y_line_left),
            Write(x_display_left),
            Write(fx_display_left)
        )

        self.wait(1)

        # Approach zero from the left
        self.play(
            left_tracker.animate.set_value(-0.8),
            run_time=1.5
        )

        self.play(
            left_tracker.animate.set_value(-0.4),
            run_time=1.5
        )

        self.play(
            left_tracker.animate.set_value(-0.16),
            run_time=1.5
        )

        self.wait(2)

        left_text = MathTex(
            r"x\to0^-",
            color=BLUE,
            font_size=40
        )
        left_text.to_corner(DL).shift(2*UP)

        left_limit = MathTex(
            r"\frac1x\to-\infty",
            color=BLUE,
            font_size=40
        )
        left_limit.next_to(left_text, DOWN)

        self.play(
            Write(left_text),
            Write(left_limit)
        )

        self.wait(2)

        # ---------------------------------------------------------
        # 6. Introduce right moving point
        # ---------------------------------------------------------

        right_tracker = ValueTracker(2.5)

        right_dot = always_redraw(
            lambda: Dot(
                axes.c2p(
                    right_tracker.get_value(),
                    1 / right_tracker.get_value()
                ),
                color=RED,
                radius=0.1
            )
        )

        moving_x_line_right = always_redraw(
            lambda: DashedLine(
                axes.c2p(right_tracker.get_value(), 0),
                axes.c2p(
                    right_tracker.get_value(),
                    1 / right_tracker.get_value()
                ),
                color=RED,
                stroke_width=2
            )
        )

        moving_y_line_right = always_redraw(
            lambda: DashedLine(
                axes.c2p(0, 1 / right_tracker.get_value()),
                axes.c2p(
                    right_tracker.get_value(),
                    1 / right_tracker.get_value()
                ),
                color=RED,
                stroke_width=2
            )
        )

        x_label_right = MathTex("x =", font_size=30)
        x_number_right = DecimalNumber(
            right_tracker.get_value(),
            num_decimal_places=2,
            font_size=30
        )

        fx_label_right = MathTex("f(x) =", font_size=30).next_to(x_label_right, DOWN)
        fx_number_right = DecimalNumber(
            1 / right_tracker.get_value(),
            num_decimal_places=2,
            font_size=30
        )

        x_display_right = VGroup(x_label_right, x_number_right).arrange(RIGHT, buff=0.1)
        fx_display_right = VGroup(fx_label_right, fx_number_right).arrange(RIGHT, buff=0.1)

        x_display_right.to_corner(UR)
        fx_display_right.next_to(x_display_right, DOWN, aligned_edge=LEFT)

        x_number_right.add_updater(
            lambda m: m.set_value(right_tracker.get_value())
        )
        fx_number_right.add_updater(
            lambda m: m.set_value(1 / right_tracker.get_value())
        )

        self.play(
            FadeIn(right_dot),
            FadeIn(moving_x_line_right),
            FadeIn(moving_y_line_right),
            Write(x_display_right),
            Write(fx_display_right),
        )

        self.wait(1)

        # Approach zero from the left
        self.play(
            right_tracker.animate.set_value(0.8),
            run_time=1.5
        )

        self.play(
            right_tracker.animate.set_value(0.4),
            run_time=1.5
        )

        self.play(
            right_tracker.animate.set_value(0.16),
            run_time=1.5
        )

        self.wait(2)

        right_text = MathTex(
            r"x\to0^+",
            color=GREEN,
            font_size=40
        )
        right_text.to_corner(DR).shift(2*UP)

        right_limit = MathTex(
            r"\frac1x\to\infty",
            color=GREEN,
            font_size=40
        )
        right_limit.next_to(right_text, DOWN)

        self.play(
            Write(right_text),
            Write(right_limit)
        )

        self.wait(2)

        self.play(
            *[FadeOut(mobj) for mobj in self.mobjects]
        )

        # ---------------------------------------------------------
        # 8. Conclude
        # ---------------------------------------------------------
        conclusion = MathTex(
            r"\boxed{\lim_{x\to0}\frac1x\text{ does not exist}}",
            color=WHITE,
            font_size=44
        )
        conclusion.center()

        self.play(Write(conclusion))
        self.wait(2)